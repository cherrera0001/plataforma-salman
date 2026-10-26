#!/usr/bin/env python3
"""Smoke/negative checks of the documentary validator, using temporary copies.
Does not install or test Spec Kit, and never tests hotel functionality.
"""
from pathlib import Path
import csv
import json
import shutil
import tempfile
from validar_paquete import validate

root = Path(__file__).resolve().parents[1]
cases = []

def run_case(name, mutation, expected):
    with tempfile.TemporaryDirectory(prefix='herencia-validator-') as tmp:
        dst = Path(tmp) / 'package'
        shutil.copytree(root, dst, ignore=shutil.ignore_patterns('__pycache__'))
        mutation(dst)
        result = validate(dst, verify_manifest=False)
        cases.append({'name': name, 'expected_valid': expected, 'observed_valid': result['ok'], 'passed': result['ok'] == expected})

run_case('valid_documentary_package', lambda p: None, True)
run_case('missing_agents_rejected', lambda p: (p/'AGENTS.md').unlink(), False)

def change_requirement(p):
    f = p/'matrices/01_requisitos_base.csv'
    with f.open(encoding='utf-8-sig', newline='') as h:
        rows = list(csv.DictReader(h))
    rows[0]['Requisito'] = 'ALTERED_WITHOUT_BASELINE_CHANGE'
    with f.open('w',encoding='utf-8-sig',newline='') as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
run_case('silent_requirement_change_rejected', change_requirement, False)

def cycle(p):
    f=p/'config/paquetes_sdd.json';d=json.loads(f.read_text());d['features'][0]['dependencias']='F01';f.write_text(json.dumps(d))
run_case('candidate_dependency_cycle_rejected', cycle, False)

def duplicate(p):
    f=p/'matrices/01_requisitos_base.csv'
    with f.open(encoding='utf-8-sig',newline='') as h: rows=list(csv.DictReader(h))
    rows.append(rows[0])
    with f.open('w',encoding='utf-8-sig',newline='') as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
run_case('duplicate_requirement_rejected', duplicate, False)

def fake_production(p):
    f=p/'config/proyecto.json';d=json.loads(f.read_text());d['production_authorized']=True;f.write_text(json.dumps(d))
run_case('false_initial_production_authorization_rejected', fake_production, False)

result={'scope':'TESTS_OF_DOCUMENTARY_VALIDATOR_ONLY','ok':all(c['passed'] for c in cases),'cases':cases}
print(json.dumps(result,indent=2,ensure_ascii=False))
raise SystemExit(0 if result['ok'] else 1)
