#!/usr/bin/env python3
"""Validate the documentary delivery, not hotel software or Spec Kit runtime.

Standard library only. Read-only except when --output is explicitly supplied.
Run from any directory: python scripts/validar_paquete.py --root <package>.
Exit status: 0 = structural checks passed, 1 = failure, 2 = invocation error.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


def validate(root: Path, verify_manifest: bool = True) -> dict[str, Any]:
    root = root.resolve()
    checks: list[dict[str, Any]] = []
    errors: list[str] = []
    warnings: list[str] = []

    def check(name: str, ok: bool, detail: str = '') -> None:
        checks.append({'check': name, 'passed': bool(ok), 'detail': detail})
        if not ok:
            errors.append(name + (': ' + detail if detail else ''))

    def safe_path(rel: str) -> Path:
        p = (root / rel).resolve()
        if p != root and root not in p.parents:
            raise ValueError('Path escapes package: ' + rel)
        return p

    def read(rel: str) -> str:
        return safe_path(rel).read_text(encoding='utf-8-sig')

    def table(rel: str) -> list[dict[str, str]]:
        with safe_path(rel).open(encoding='utf-8-sig', newline='') as h:
            return list(csv.DictReader(h))

    required = [
        '00_LEEME.md', 'AGENTS.md', 'CHANGELOG.md',
        '01_PROMPT_MAESTRO_SDD_v0_3.md', '01_PROMPT_MAESTRO_SDD_v0_3.txt',
        '02_INICIAR_ESPECIFICACIONES.txt', '03_REANUDAR_ESPECIFICACIONES.txt',
        '04_PREPARAR_CONSTRUCCION_POSTERIOR.txt',
        'config/proyecto.json', 'config/entorno_sdd.json', 'config/estado_inicial.json',
        'config/paquetes_sdd.json',
        'docs/01_INDICE_MAESTRO.md', 'docs/02_VENTAS_REDES.md',
        'docs/03_CONTRATO_SDD.md', 'docs/04_CONSTITUCION_PROPUESTA.md',
        'docs/05_GOBIERNO_ESTADOS_Y_CAMBIOS.md', 'docs/06_COBERTURA_Y_ACEPTACION.md',
        'docs/07_PLAN_DE_GENERACION.md', 'docs/08_INSTALACION_Y_USO_POSTERIOR.md',
        'docs/09_SEGURIDAD_Y_AUTONOMIA.md', 'docs/10_DECISIONES_TECNICAS_Y_COBERTURA.md',
        'matrices/01_requisitos_base.csv', 'matrices/02_decisiones.csv',
        'matrices/03_paquetes_sdd.csv', 'matrices/04_controles_sdd.csv',
        'matrices/05_escenarios_base.csv', 'matrices/06_trazabilidad_por_desarrollar.csv',
        'matrices/07_acoplamientos_a_resolver.csv',
        'plantillas/spec.template.md', 'plantillas/plan.template.md',
        'plantillas/tasks.template.md', 'plantillas/research.template.md',
        'plantillas/data-model.template.md', 'plantillas/contracts.template.md',
        'plantillas/quickstart.template.md', 'plantillas/checklist.template.md',
        'plantillas/acceptance.template.md', 'plantillas/adr.template.md',
        'plantillas/cambio.template.md', 'plantillas/orden_trabajo.template.md',
        'plantillas/work-order.schema.json', 'plantillas/estado.template.json',
        'fuentes/01_FUENTES_SDD.md', 'fuentes/inventario_originales.json',
        'fuentes/antecedentes_v0_2/05_REQUISITOS_AMPLIADOS_v0_2.csv',
        'fuentes/antecedentes_v0_2/06_DECISIONES_AMPLIADAS_v0_2.csv',
        'fuentes/antecedentes_v0_2/01_PROMPT_MAESTRO_HERENCIA_v0_2.txt',
    ]
    missing = [x for x in required if not safe_path(x).is_file()]
    check('required_files', not missing, ', '.join(missing))
    if missing:
        return {'ok': False, 'scope': 'DOCUMENTARY_PACKAGE_ONLY', 'checks': checks,
                'errors': errors, 'warnings': warnings}
    try:
        all_paths = [p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
        check('no_empty_files', all(p.stat().st_size > 0 for p in all_paths))
        json_errors = []
        for p in all_paths:
            if p.suffix == '.json':
                try:
                    json.loads(p.read_text(encoding='utf-8-sig'))
                except (ValueError, UnicodeError) as exc:
                    json_errors.append(f'{p.relative_to(root)}: {exc}')
        check('json_parse', not json_errors, '; '.join(json_errors))
        project = json.loads(read('config/proyecto.json'))
        environment = json.loads(read('config/entorno_sdd.json'))
        features = json.loads(read('config/paquetes_sdd.json'))['features']
        reqs = table('matrices/01_requisitos_base.csv')
        old = table('fuentes/antecedentes_v0_2/05_REQUISITOS_AMPLIADOS_v0_2.csv')
        decisions = table('matrices/02_decisiones.csv')
        old_dec = table('fuentes/antecedentes_v0_2/06_DECISIONES_AMPLIADAS_v0_2.csv')
        tests = table('matrices/05_escenarios_base.csv')
        controls = table('matrices/04_controles_sdd.csv')
        coupling = table('matrices/07_acoplamientos_a_resolver.csv')
        req_ids = [r['ID'] for r in reqs]
        reqmap = {r['ID']: r for r in reqs}
        featmap = {f['id']: f for f in features}
        check('153_requirement_ids_unique', len(req_ids) == 153 and len(set(req_ids)) == 153)
        check('original_requirements_preserved', all(
            row['ID'] in reqmap and all(reqmap[row['ID']].get(k) == v for k, v in row.items())
            for row in old) and len(old) == 153)
        dmap = {r['ID']: r for r in decisions}
        check('36_original_decisions_preserved', len(old_dec) == 36 and all(
            r['ID'] in dmap and all(dmap[r['ID']].get(k) == v for k, v in r.items()) for r in old_dec))
        check('44_decisions_unique', len(decisions) == 44 and len(dmap) == 44)
        check('23_feature_seeds_unique', len(features) == 23 and len(featmap) == 23)
        check('48_scenarios_unique_and_unexecuted', len(tests) == 48 and len({t['ID'] for t in tests}) == 48
              and all(t['Estado'] == 'NO_EJECUTADA' for t in tests))
        check('18_process_controls_unique', len(controls) == 18 and len({r['ID'] for r in controls}) == 18)
        orphan_deps = [(r['ID'], d) for r in reqs for d in re.findall(r'[A-Z]+-[0-9]{3}', r['Dependencias']) if d not in reqmap]
        check('requirement_dependency_references', not orphan_deps, str(orphan_deps))
        check('chapters_in_requirement_rows', all(re.fullmatch(r'M(?:0[1-9]|1[0-9]|2[0-4])', r['Capitulo maestro']) for r in reqs))
        check('every_requirement_assigned_to_feature', all(r['Paquete SDD propuesto'] in featmap for r in reqs))
        owned = [rid for f in features for rid in f['requisitos']]
        check('one_primary_owner_per_requirement', len(owned) == len(set(owned)) == 153 and set(owned) == set(req_ids))
        check('feature_registry_matches_requirement_map', all(
            reqmap[rid]['Paquete SDD propuesto'] == f['id'] for f in features for rid in f['requisitos']))
        check('feature_brief_paths_exist', all(safe_path(f['brief_path']).is_file() for f in features))
        check('feature_csv_matches_registry', {r['ID'] for r in table('matrices/03_paquetes_sdd.csv')} == set(featmap))
        visiting: set[str] = set()
        seen: set[str] = set()
        def visit(fid: str) -> None:
            if fid in visiting:
                raise ValueError('Cycle in candidate ordering: ' + fid)
            if fid in seen:
                return
            if fid not in featmap:
                raise ValueError('Unknown feature: ' + fid)
            visiting.add(fid)
            for dep in filter(None, featmap[fid]['dependencias'].split(';')):
                visit(dep)
            visiting.remove(fid)
            seen.add(fid)
        try:
            for f in features:
                visit(f['id'])
            check('candidate_order_acyclic', True, 'Candidate order only; not an approved execution DAG.')
        except ValueError as exc:
            check('candidate_order_acyclic', False, str(exc))
        check('couplings_are_explicit_valid_references', all(
            r['Requisito'] in reqmap and r['Depende de'] in reqmap and r['Paquete'] in featmap and r['Paquete relacionado'] in featmap
            for r in coupling))
        prompt = read('01_PROMPT_MAESTRO_SDD_v0_3.md')
        check('prompt_txt_md_identical', safe_path('01_PROMPT_MAESTRO_SDD_v0_3.md').read_bytes() == safe_path('01_PROMPT_MAESTRO_SDD_v0_3.txt').read_bytes())
        chapter_ids = re.findall(r'^### (M[0-9]{2})\.', prompt, re.M)
        check('24_master_chapters_retained', len(chapter_ids) == 24 and set(chapter_ids) == {f'M{i:02}' for i in range(1,25)})
        check('48_scenarios_retained_in_prompt', all(f'{i}. ' in prompt for i in range(1,49)))
        checks_text = ['ESPECIFICAR', 'SPECIFY_FEATURE_DIRECTORY', 'OBLIGATORIAS', 'spec.md', 'plan.md', 'tasks.md', 'converge', '153']
        check('mandatory_sdd_instructions', all(t in prompt for t in checks_text))
        check('tests_required_in_local_templates', all('OBLIGATORIAS' in read(p) for p in ['plantillas/spec.template.md','plantillas/tasks.template.md']))
        check('no_application_or_production_claim', project['mode'] == 'ESPECIFICAR' and not project['production_authorized'] and not project['application_implemented'])
        check('runtime_status_honest', environment['installed_version'] is None and environment['external_actions_authorized'] is False)
        check('original_workbooks_not_bundled', not any(p.suffix.lower() in {'.xls','.xlsx'} for p in all_paths))
        # All explicit current-package paths in the prompt must exist. Paths clearly
        # designated as future output/native artefacts are deliberately excluded.
        paths = re.findall(r'`((?:docs|config|matrices|fuentes|plantillas|scripts|backlog)/[^`]+)`', prompt)
        check('explicit_package_references_exist', all(safe_path(p).exists() for p in paths), ', '.join(p for p in paths if not safe_path(p).exists()))
        manifest_path = root / 'MANIFEST.json'
        if verify_manifest and manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
            mismatches = []
            expected = set()
            for item in manifest['files']:
                p = safe_path(item['path'])
                expected.add(item['path'])
                if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
                    mismatches.append(item['path'])
            excluded = set(manifest['excluded_from_hash'])
            actual = {p.relative_to(root).as_posix() for p in all_paths}
            check('manifest_sha256', not mismatches, ', '.join(mismatches))
            check('manifest_inventory', actual - excluded == expected, str(sorted((actual-excluded)^expected)))
        else:
            warnings.append('Manifest integrity not checked (not requested or not present).')
        warnings.extend([
            f'{len(coupling)} inherited dependency relationships require refinement in the master before executable plans.',
            'Feature seeds and templates are not approved specifications.',
            'No Spec Kit runtime, hotel application, external API or production test is validated by this script.',
            'Structural success does not prove semantic completeness, legal compliance or independent audit.'
        ])
        counts = {'requirements': len(reqs), 'decisions': len(decisions), 'feature_seeds': len(features),
                  'process_controls': len(controls), 'scenarios': len(tests), 'chapters': len(chapter_ids),
                  'dependency_relationships_to_refine': len(coupling), 'checks': len(checks)}
    except (OSError, KeyError, TypeError, ValueError, UnicodeError) as exc:
        check('read_and_structure_exception', False, f'{type(exc).__name__}: {exc}')
        counts = {}
    return {'ok': not errors, 'scope': 'DOCUMENTARY_PACKAGE_ONLY', 'counts': counts,
            'checks': checks, 'errors': errors, 'warnings': warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, help='Optional JSON report output; otherwise stdout only.')
    parser.add_argument('--skip-manifest', action='store_true', help='For authoring changes only; skips distribution hashes, not structural checks.')
    args = parser.parse_args()
    report = validate(args.root, verify_manifest=not args.skip_manifest)
    data = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data, encoding='utf-8')
    sys.stdout.write(data)
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
