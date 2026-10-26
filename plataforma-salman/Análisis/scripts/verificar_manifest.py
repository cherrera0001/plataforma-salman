import hashlib, json, os, sys
sys.path.insert(0, "")
raiz, manifest = sys.argv[1], sys.argv[2]
datos = json.load(open(manifest, encoding="utf-8"))
ok = falla = faltan = 0
for f in datos.get("files", []):
    ruta = os.path.join(raiz, f["path"])
    if not os.path.isfile(ruta):
        faltan += 1
        continue
    h = hashlib.sha256(open(ruta, "rb").read()).hexdigest()
    if h == f["sha256"] and os.path.getsize(ruta) == f.get("bytes", os.path.getsize(ruta)):
        ok += 1
    else:
        falla += 1
        print("DIFIERE:", f["path"])
print(f"manifest={os.path.basename(manifest)} entradas={len(datos.get('files', []))} ok={ok} difieren={falla} faltan={faltan}")
