import csv, hashlib, os, sys
sys.path.insert(0, "")
base, salida = sys.argv[1], sys.argv[2]
filas = []
for dirpath, _, nombres in os.walk(base):
    for n in nombres:
        ruta = os.path.join(dirpath, n)
        rel = os.path.relpath(ruta, base)
        data = open(ruta, "rb").read()
        filas.append([rel, os.path.getsize(ruta), hashlib.sha256(data).hexdigest(), os.path.splitext(n)[1].lower() or "(sin extension)"])
filas.sort()
with open(salida, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["ruta_relativa", "bytes", "sha256", "extension"])
    w.writerows(filas)
print(os.path.basename(salida), "filas:", len(filas))
