import sys
sys.path.append("/home/herre/.local/lib/python3.12/site-packages")
from docx import Document
from docx.oxml.ns import qn

origen, destino = sys.argv[1], sys.argv[2]
doc = Document(origen)
lineas = []
cuerpo = doc.element.body
for hijo in cuerpo.iterchildren():
    if hijo.tag == qn("w:p"):
        from docx.text.paragraph import Paragraph
        p = Paragraph(hijo, doc)
        texto = p.text.strip()
        if texto:
            estilo = p.style.name if p.style is not None else ""
            prefijo = "# " if estilo.startswith("Heading 1") or estilo == "Título 1" else ("## " if estilo.startswith(("Heading 2", "Heading 3", "Título 2", "Título 3")) else "")
            lineas.append(prefijo + texto)
    elif hijo.tag == qn("w:tbl"):
        from docx.table import Table
        t = Table(hijo, doc)
        lineas.append("[TABLA]")
        for fila in t.rows:
            celdas = []
            vistos = set()
            for c in fila.cells:
                if id(c._tc) in vistos:
                    continue
                vistos.add(id(c._tc))
                celdas.append(c.text.strip().replace("\n", " / "))
            lineas.append("| " + " | ".join(celdas) + " |")
        lineas.append("[/TABLA]")
with open(destino, "w", encoding="utf-8") as f:
    f.write("\n".join(lineas) + "\n")
print("parrafos+tablas:", len(lineas), "lineas; imagenes en documento:", len(doc.inline_shapes))
