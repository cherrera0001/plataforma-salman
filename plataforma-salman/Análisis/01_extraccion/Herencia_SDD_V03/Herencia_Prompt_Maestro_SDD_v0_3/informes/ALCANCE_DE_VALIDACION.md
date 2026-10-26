# Alcance de las comprobaciones

Los informes JSON de esta carpeta se generan al ejecutar los scripts del paquete. Distinguir:
- validación estructural e integridad de los documentos de entrada;
- pruebas positivas/negativas del propio validador;
- pruebas del software hotelero, que NO se ejecutaron porque no forma parte de esta entrega.

La existencia de referencias válidas no garantiza que todos los requisitos sean suficientes. El maestro debe pasar auditoría funcional, técnica y empresarial. Las 22 relaciones de dependencia registradas siguen siendo trabajo de especificación. No se presentaran como errores resueltos por tener IDs válidos.

El informe final se excluye del hash de si mismo junto con MANIFEST.json para evitar una referencia circular. El manifiesto enumera esa exclusión. Los demas archivos entregados quedan identificados por huella. No hay firma digital ni certificacion externa.
