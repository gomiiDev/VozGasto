# Arquitectura de Voz Gasto

Documento: [Taller1_p2_NRC36848_Grupo04_VozGasto.pdf](Taller1_p2_NRC36848_Grupo04_VozGasto.pdf)

| Nivel | Arquitectura | Dónde se aplica |
|---|---|---|
| General | Cliente-servidor de tres niveles | App móvil ↔ API FastAPI ↔ PostgreSQL |
| Frontend | MVC | [mobile/lib/](../../mobile/lib/) |
| Backend | Capas | [backend/app/](../../backend/app/) |

El servidor calcula el saldo, controla las alertas e interpreta las frases. Así la app usa las mismas reglas en Android y en iOS, y se puede mejorar la interpretación de frases sin actualizar la app.

Diagrama (Drawio): https://drive.google.com/file/d/1ZvL8NIA121z2vQ97DggJK3tBm3BVnbpm/view?usp=sharing
