# Pruebas

Responsable: Carlos Granda

## Metas (Tarea 2)

| Requisito | Meta |
|---|---|
| RNF6 | El extractor PLN acierta tipo, monto y categoría en al menos 80 de 100 frases |
| RNF8 | Cobertura de pruebas de al menos 70 % en dominio y backend, sin advertencias del linter |
| RNF2 | El 100 % de los accesos a datos de otro usuario devuelven 403 o 404 |
| RNF5 | Piloto con 10 usuarios: gasto por voz en menos de 10 s y SUS de 70 o más |

## Niveles de prueba

| Nivel | Dónde |
|---|---|
| Unitarias del backend | [backend/tests/unit/](../../backend/tests/unit/) |
| Integración del backend | [backend/tests/integration/](../../backend/tests/integration/) |
| Widgets y controladores de la app | [mobile/test/](../../mobile/test/) |
| Banco de frases del PLN | Pendiente (sprint 2: 30 frases; sprint 4: 100 frases) |
