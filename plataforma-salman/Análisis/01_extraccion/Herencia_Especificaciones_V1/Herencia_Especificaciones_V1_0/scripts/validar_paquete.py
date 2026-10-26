from pathlib import Path
import csv,json,re,hashlib,sys,collections
ROOT=Path(__file__).resolve().parents[1] if Path(__file__).resolve().parent.name=='scripts' else Path('/mnt/data/Herencia_Especificaciones_V1_0')
CHECKS=[]
def check(name,condition,detail=''):
 CHECKS.append({'check':name,'result':'PASS' if condition else 'FAIL','detail':detail})
def rows(rel):
 with (ROOT/rel).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def load(rel):return json.loads((ROOT/rel).read_text())
def walk(obj):
 if isinstance(obj,dict):
  yield obj
  for x in obj.values():yield from walk(x)
 elif isinstance(obj,list):
  for x in obj:yield from walk(x)
def resolve(doc,ref):
 cur=doc
 for p in ref[2:].split('/'):
  cur=cur[p.replace('~1','/').replace('~0','~')]
 return cur
r=rows('registros/requisitos_originales_preservados.csv');ids={x['ID'] for x in r}
t=rows('registros/trazabilidad.csv');ts=rows('registros/tareas.csv');cas=rows('pruebas/casos_aceptacion.csv');e2e=rows('pruebas/escenarios_criticos.csv');ds=rows('registros/decisiones.csv')

check('Preservacion exacta de campos originales',r==rows('fuentes/requisitos_baseline_V0_3.csv'))
check('Constitucion nativa y vista iguales',(ROOT/'sdd/constitucion.md').read_bytes()==(ROOT/'.specify/memory/constitution.md').read_bytes())
check('153 requisitos originales unicos',len(r)==len(ids)==153)
check('24 capitulos desarrollados',len(list((ROOT/'maestro').glob('M*.md')))==24)
check('23 paquetes con spec plan tasks',len(list((ROOT/'specs').glob('*/spec.md')))==23 and all((p.parent/'plan.md').exists() and (p.parent/'tasks.md').exists() for p in (ROOT/'specs').glob('*/spec.md')))
check('Trazabilidad completa y unica',{x['requisito'] for x in t}==ids and len(t)==153)
check('Requisitos con detalle propio',all(len(x.get('detail',''))>70 and x['positive_fixture'] and x['negative_expected'] for x in load('registros/requisitos_detallados.json')['requirements']))
check('505 tareas unicas',len(ts)==len({x['id'] for x in ts})==505)
check('306 casos por requisito',len(cas)==306 and all(sum(x['requisito']==i for x in cas)==2 for i in ids))
check('48 escenarios criticos desarrollados',len(e2e)==48 and all(x['Requisitos vinculados']!='POR_MAPEAR_EN_ESPECIFICACION' and x['Resultado esperado detallado']!='POR_DESARROLLAR' for x in e2e))
check('Ninguna prueba de aplicacion falsamente ejecutada',all(x['estado']=='NO_EJECUTADA' for x in cas) and all(x['Estado']=='NO_EJECUTADA' for x in e2e))
check('45 decisiones pendientes identificadas',len(ds)==45 and len({x['ID'] for x in ds})==45)
check('22 acoplamientos clasificados',len(rows('registros/acoplamientos_resueltos.csv'))==22 and all(x['Tipo resuelto'] for x in rows('registros/acoplamientos_resueltos.csv')))
# Task graph.
graph={x['id']:[d for d in x['depends_on'].split(';') if d] for x in ts};unknown=[(i,d) for i,deps in graph.items() for d in deps if d not in graph]
check('Tareas sin referencias inexistentes',not unknown,str(unknown))
state={};cycle=[]
def dfs(i,trail):
 if state.get(i)==1:cycle.append(trail+[i]);return
 if state.get(i)==2:return
 state[i]=1
 for d in graph[i]:
  if d in graph:dfs(d,trail+[i])
 state[i]=2
for i in graph:dfs(i,[])
check('Grafo de implementacion aciclico',not cycle,str(cycle[:2]))
for row in t:
 check('Referencias '+row['requisito'],(ROOT/row['spec']).exists() and all(x in graph for x in row['tareas'].split(';')) and all(x in {c['id'] for c in cas} for x in row['pruebas'].split(';')))
model=load('modelos/diccionario_datos.json');ent={x['name']:x for x in model['entities']};fields=[f for e in ent.values() for f in e['fields']]
check('109 entidades y1409 campos',len(ent)==109 and len(fields)==1409)
check('Claves foraneas existentes',all(not f['fk'] or f['fk'] in ent for f in fields))
check('Cada entidad tiene id y version',all({'id','version'}.issubset({f['field'] for f in e['fields']}) for e in ent.values()))
trans=rows('reglas/transiciones.csv');bad=[]
for tr in trans:
 f=next((f for f in ent[tr['entidad']]['fields'] if f['field']==tr['campo_estado']),None)
 if not f or tr['origen'] not in f['enum'] or tr['destino'] not in f['enum']:bad.append(tr['id'])
check('Transiciones concuerdan con enums',not bad,str(bad))
api=load('contratos/openapi.json');badrefs=[]
for ob in walk(api):
 if '$ref' in ob:
  try:resolve(api,ob['$ref'])
  except Exception:badrefs.append(ob['$ref'])
check('API sin referencias rotas',not badrefs,str(set(badrefs)))
operations=[v for methods in api['paths'].values() for k,v in methods.items() if k in ['get','post','patch','delete','put']]
check('OperationIds API unicos',len({v['operationId'] for v in operations})==len(operations),str(len(operations)))
check('Rutas tienen parametros completos',all(set(re.findall(r'\{(.*?)\}',p))=={q['name'] for q in op.get('parameters',[]) if q['in']=='path'} for p,methods in api['paths'].items() for op in methods.values()))
check('API se declara propuesta no servicio real','example.invalid' in api['servers'][0]['url'])
nested=load('modelos/esquemas_json.json');badn=[]
for ob in walk(nested):
 if '$ref' in ob:
  try:resolve(nested,ob['$ref'])
  except Exception:badn.append(ob['$ref'])
check('Esquemas anidados con referencias validas',not badn,str(set(badn)))
check('30 camposJSON mapeados',len(nested['field_schema_map'])==30)
check('53 pantallas y roles definidos',len(rows('ux/pantallas.csv'))==53 and all(x['perfiles'] and x['acciones'] for x in rows('ux/pantallas.csv')))
check('Permisos comandos cubiertos',len(rows('seguridad/permisos.csv'))==88)
check('13 integraciones sin afirmacion de acceso real',len(rows('contratos/integraciones.csv'))==13 and all('NO_PROBADA' in x['estado'] for x in rows('contratos/integraciones.csv')))
check('Datos de ejemplo claramente sinteticos',load('datos_sinteticos/fixture.json')['not_real'] is True)
check('17 habitaciones sinteticas',len(load('datos_sinteticos/fixture.json')['rooms'])==17)
check('Sin planillas privadas originales',not any(p.suffix.lower() in ['.xls','.xlsx'] for p in ROOT.rglob('*')))
check('Calculo ejemplo liquidacion',100000+80000-5400==174600)
check('Calculo ejemplo caja',20000+150000-100000-10000==60000)
check('Calculo ejemplo reparto',3334+3333+3333==10000)
check('Calculo ejemplo desayuno',8*1800+2*1800==18000)
check('Calculo ejemplo incentivo',min(6000,(4+6*0.5)*1000)==6000)
# Check decisions referenced in feature manifests.
check('Decisiones referenciadas existen',all(set(load(str(p.relative_to(ROOT)))['decisions']).issubset({d['ID'] for d in ds}) for p in (ROOT/'specs').glob('*/status.json')))
# Native package validation never implies production or third party access.
report={'scope':'VALIDACION_DOCUMENTAL_Y_CALCULOS_DE_EJEMPLO_NO_TESTS_DE_APLICACION','checks':len(CHECKS),'passed':sum(c['result']=='PASS' for c in CHECKS),'failed':sum(c['result']=='FAIL' for c in CHECKS),'native_spec_kit_executed':False,'application_tests_executed':False,'independent_review':False,'results':CHECKS}
(ROOT/'evidencias_documentales').mkdir(exist_ok=True)
(ROOT/'evidencias_documentales/resultado_validacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='results'},ensure_ascii=False))
for c in CHECKS:
 if c['result']=='FAIL':print(c)
sys.exit(1 if report['failed'] else 0)
