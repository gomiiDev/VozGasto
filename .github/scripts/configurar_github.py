#!/usr/bin/env python3
"""Configura en GitHub el proceso descrito en docs/proceso/PROCESO.md.

Crea etiquetas, issues del backlog (Tarea 2), el Project con sus campos y la
protección de main. Se puede ejecutar varias veces: lo que ya existe se reutiliza.

Requisitos:
  - GitHub CLI (https://cli.github.com) con sesión iniciada por el dueño del repo:
        gh auth login
        gh auth refresh -s project
  - Python 3.8 o superior.

Uso (desde la raíz del repositorio):
  python3 .github/scripts/configurar_github.py --inicio 2026-11-02
  python3 .github/scripts/configurar_github.py --inicio 2026-11-02 --solo tablero

--inicio es el lunes de la semana 1 del semestre (inicio del sprint 1).
"""

import argparse
import json
import subprocess
import sys
from datetime import date, timedelta

REPO = "gomiiDev/VozGasto"
OWNER = REPO.split("/")[0]
PROJECT_TITLE = "Voz Gasto"

# Usuarios de GitHub de cada integrante; completar para asignar los issues.
GH = {
    "Revilla": "RevillaA",
    "Granda": "cjgranda19",
    "Hernandez": "gomiiDev",
}

LABELS = [
    ("historia", "1D76DB", "Historia de usuario del backlog"),
    ("tarea", "5319E7", "Trabajo técnico o de proceso que no es una historia"),
    ("documentación", "0E8A16", "Cambios en docs/, README o guías"),
    ("defecto", "D73A4A", "No funciona como dicen los criterios de aceptación"),
    ("cambio", "FBCA04", "Cambio de alcance o de plan; lo aprueba la docente"),
    ("bloqueado", "B60205", "El issue no puede avanzar"),
    ("riesgo", "F9D0C4", "Riesgo nuevo o actualizado del registro de riesgos"),
]
DEFAULT_LABELS = ["bug", "documentation", "duplicate", "enhancement", "good first issue",
                  "help wanted", "invalid", "question", "wontfix", "accessibility"]

STATUS = ["Backlog", "Por hacer", "En progreso", "En revisión", "Hecho"]

# (título, etiquetas, prioridad, talla, sprint, responsables, cuerpo)
# El orden importa: en un repositorio sin issues, HU1 será #1 y así sucesivamente.
HU = [
    ("HU1 - Crear cuenta", "Must", "S", 2, ["Revilla", "Hernandez"], "visitante", "crear una cuenta", "guardar mis movimientos de forma privada", "RF1",
     ["**C1:** Dado un correo no registrado y una contraseña de al menos 8 caracteres, cuando envío el formulario, entonces se crea la cuenta y entro a la pantalla principal.",
      "**CR:** Dado un correo ya registrado, cuando intento crear la cuenta, entonces el sistema la rechaza con el mensaje «Este correo ya tiene una cuenta»."], "—"),
    ("HU2 - Iniciar sesión", "Must", "S", 2, ["Revilla", "Hernandez"], "usuario registrado", "iniciar sesión", "que solo yo vea mis finanzas aunque preste el celular", "RF2",
     ["**C1:** Dado un correo y contraseña correctos, cuando inicio sesión, entonces veo mi saldo del mes.",
      "**CR:** Dada una contraseña incorrecta, cuando intento entrar, entonces el sistema muestra «Correo o contraseña incorrectos» sin indicar cuál de los dos falló."], "HU1"),
    ("HU3 - Registrar ingreso manual", "Must", "S", 2, ["Revilla", "Hernandez"], "usuario registrado", "registrar un ingreso con su fuente", "que alimente mi presupuesto del mes", "RF3",
     ["**C1:** Dado un presupuesto de $0, cuando registro $800 con fuente Salario y fecha de hoy, entonces el presupuesto disponible del mes es $800.",
      "**CR:** Dado un monto de $0 o negativo, cuando intento guardar, entonces el sistema lo rechaza con «El monto debe ser mayor que 0» (RN1)."], "HU2"),
    ("HU4 - Registrar gasto manual", "Must", "M", 3, ["Revilla", "Hernandez"], "usuario registrado", "registrar un gasto manualmente en una categoría", "tener el control aunque no pueda hablar", "RF4, RF7",
     ["**C1:** Dado un disponible de $100 en Alimentación, cuando registro $12 en esa categoría, entonces el disponible de Alimentación queda en $88.",
      "**C2:** Dado que abro el formulario, cuando despliego las categorías, entonces veo las 8 predefinidas y mis categorías personalizadas.",
      "**CR:** Dada una fecha futura, cuando intento guardar, entonces el sistema la rechaza con «La fecha no puede ser posterior a hoy»."], "HU2, HU3"),
    ("HU5 - Editar movimiento", "Should", "S", 3, ["Revilla", "Hernandez"], "usuario registrado", "editar un movimiento", "corregir un error sin borrarlo y volver a crearlo", "RF5",
     ["**C1:** Dado un gasto de $15 en Transporte, cuando lo cambio a $5, entonces el disponible de Transporte aumenta en $10.",
      "**C2:** Dado un gasto en Transporte, cuando cambio su categoría a Alimentación, entonces se recalculan los saldos de ambas categorías."], "HU4"),
    ("HU6 - Eliminar movimiento", "Should", "S", 3, ["Revilla", "Hernandez"], "usuario registrado", "eliminar un movimiento", "quitar uno que registré por error", "RF6",
     ["**C1:** Dado un gasto de $20, cuando lo elimino y confirmo, entonces desaparece del historial y el saldo aumenta en $20.",
      "**C2:** Dado el diálogo de confirmación, cuando pulso Cancelar, entonces el movimiento se conserva sin cambios."], "HU4"),
    ("HU7 - Crear categoría personalizada", "Should", "S", 3, ["Revilla", "Hernandez"], "usuario registrado", "crear mis propias categorías", "clasificar gastos que no encajan en las predefinidas", "RF8",
     ["**C1:** Dado que no tengo la categoría Mascotas, cuando la creo, entonces aparece en la lista de categorías.",
      "**CR:** Dado que ya existe Mascotas, cuando intento crear otra con el mismo nombre, entonces el sistema la rechaza con «Ya existe esa categoría»."], "HU2"),
    ("HU8 - Dictar un gasto", "Must", "L", 4, ["Granda", "Hernandez"], "usuario registrado", "dictar un gasto con una frase", "registrarlo en segundos aunque tenga las manos ocupadas", "RF9, RF10",
     ["**C1:** Dado que pulso el micrófono, cuando digo «gasté 12 dólares en comida», entonces la app propone: gasto, $12, Alimentación, hoy.",
      "**C2:** Dada la frase «ayer pagué un dólar cincuenta de bus», cuando termino de hablar, entonces la app propone: gasto, $1,50, Transporte, ayer.",
      "**CR:** Dada una frase sin monto («compré comida»), cuando termino de hablar, entonces la app indica «No entendí el monto» y permite repetir o escribirlo."], "HU4"),
    ("HU9 - Dictar un ingreso", "Should", "S", 6, ["Granda", "Hernandez"], "usuario registrado", "dictar un ingreso", "registrar mi pago apenas lo recibo", "RF9, RF10",
     ["**C1:** Dado que pulso el micrófono, cuando digo «me pagaron 800 de salario», entonces la app propone: ingreso, $800, fuente Salario, hoy.",
      "**CR:** Dado que el servicio de voz no responde en 5 s, cuando espero, entonces se abre el formulario manual con el texto reconocido (RNF7)."], "HU3, HU10"),
    ("HU10 - Confirmar o corregir lo entendido", "Must", "M", 4, ["Granda", "Hernandez"], "usuario registrado", "revisar y corregir lo que la app entendió", "que mi saldo no se dañe con un error de voz", "RF11",
     ["**C1:** Dada una propuesta correcta, cuando pulso Confirmar, entonces el movimiento se guarda y se actualiza el saldo.",
      "**C2:** Dada la propuesta con categoría Otros, cuando la cambio a Salud y confirmo, entonces el gasto se guarda en Salud.",
      "**CR:** Dada una propuesta, cuando pulso Descartar, entonces no se guarda nada y el saldo no cambia (RN3)."], "HU8"),
    ("HU11 - Definir límite por categoría", "Must", "M", 5, ["Revilla", "Hernandez"], "usuario registrado", "definir un límite mensual por categoría", "repartir mi dinero antes de gastarlo", "RF12",
     ["**C1:** Dado un presupuesto de $800, cuando fijo $200 para Alimentación, entonces la categoría muestra límite $200 y disponible $200.",
      "**CR:** Dado un límite de $0 o negativo, cuando intento guardarlo, entonces el sistema lo rechaza con «El límite debe ser mayor que 0»."], "HU3"),
    ("HU12 - Ver saldo total y por categoría", "Must", "M", 5, ["Revilla", "Hernandez"], "usuario registrado", "ver cuánto me queda en total y por categoría", "decidir antes de comprar", "RF13",
     ["**C1:** Dado un disponible total de $500, cuando confirmo un gasto de $25, entonces la pantalla principal muestra $475 sin recargar.",
      "**C2:** Dado un límite de $100 en Transporte con $60 gastados, cuando abro la categoría, entonces veo $40 disponibles y 60 % usado."], "HU4, HU11"),
    ("HU13 - Recibir alerta de límite", "Should", "M", 5, ["Revilla", "Hernandez"], "usuario registrado", "recibir un aviso cuando me acerco al límite", "frenar a tiempo y no a fin de mes", "RF14",
     ["**C1:** Dado un límite de $100 en Entretenimiento con $75 gastados, cuando registro $6, entonces recibo «Usaste el 81 % de Entretenimiento».",
      "**C2:** Dado que ya recibí el aviso del 80 % este mes, cuando registro otro gasto sin superar el límite, entonces no recibo un aviso repetido (RN5)."], "HU12"),
    ("HU14 - Ver gráficos por categoría y mes", "Should", "L", 7, ["Hernandez"], "usuario registrado", "ver gráficos de mis gastos por categoría y por mes", "entender en qué se me va el dinero", "RF15",
     ["**C1:** Dados los gastos en octubre, cuando abro Reportes, entonces veo un gráfico con el porcentaje de cada categoría.",
      "**C2:** Dado un mes sin movimientos, cuando lo selecciono, entonces veo «Sin movimientos en este mes» en lugar de un gráfico vacío."], "HU4"),
    ("HU15 - Filtrar historial", "Could", "M", 7, ["Revilla", "Hernandez"], "usuario registrado", "filtrar mi historial", "encontrar rápido un movimiento", "RF16",
     ["**C1:** Dado un historial con 30 movimientos, cuando filtro por Transporte y octubre, entonces solo veo los gastos de Transporte de octubre.",
      "**CR:** Dado un rango con fecha inicial posterior a la final, cuando aplico el filtro, entonces el sistema lo rechaza con «Rango de fechas no válido»."], "HU4"),
    ("HU16 - Editar perfil", "Could", "S", 8, ["Revilla", "Hernandez"], "usuario registrado", "editar mi nombre de perfil", "que la app se dirija a mí correctamente", "RF17",
     ["**C1:** Dado mi perfil, cuando cambio el nombre y guardo, entonces el saludo de la pantalla principal muestra el nuevo nombre.",
      "**CR:** Dado un nombre vacío, cuando intento guardar, entonces el sistema lo rechaza con «El nombre es obligatorio»."], "HU1"),
    ("HU17 - Conectar cuenta bancaria", "Won't", "L", None, [], "usuario registrado", "conectar mi cuenta bancaria", "que mis gastos se registren solos", "— (fuera del alcance del acta)",
     ["**C1:** Dada una cuenta bancaria vinculada, cuando hago un pago con tarjeta, entonces aparece como gasto sin dictarlo.",
      "**C2:** Dado que revoco el acceso, cuando abro la app, entonces deja de importar movimientos."], "—"),
]

# Tareas: (título, etiquetas, prioridad, talla, sprint, responsables, qué hacer)
TAREAS = [
    ("T1 - Repositorio, protección de main y Project", ["tarea"], "Must", "S", 1, ["Revilla"],
     "Crear el repositorio, proteger `main` (PR con 1 aprobación) y configurar el Project con Status, Prioridad, Talla y Sprint."),
    ("T2 - CI con GitHub Actions (pruebas y linter de Flutter y Python)", ["tarea"], "Must", "M", 2, ["Granda"],
     "Flujo en `.github/workflows/` que ejecute pruebas y linter del backend y de la app en cada PR."),
    ("T3 - docker-compose con FastAPI y PostgreSQL 16", ["tarea"], "Must", "S", 2, ["Revilla"],
     "`docker-compose.yml` que levante la API y la base de datos; README con cómo levantar el entorno."),
    ("T4 - Modelo de datos inicial", ["tarea"], "Must", "S", 2, ["Revilla"],
     "Tablas de usuario, categoría, movimiento y presupuesto, con migración inicial."),
    ("T5 - Verificar compilación en Android e iOS (R8)", ["tarea", "riesgo"], "Should", "S", 2, ["Hernandez"],
     "Compilar la app en un dispositivo o emulador de cada plataforma y anotar el resultado de iOS en el tablero."),
    ("T6 - Pruebas de integración de HU1 y HU2", ["tarea"], "Must", "M", 2, ["Granda"],
     "Pruebas de integración de crear cuenta e iniciar sesión, incluidos los casos de rechazo."),
    ("Documentar el proceso del equipo en PROCESO.md", ["documentación"], "Must", "M", 1, ["Revilla"],
     "Partes A, B, C y E del laboratorio en `docs/proceso/PROCESO.md`: metodología, roles, RACI, rotación, artefactos, definición de terminado y flujo de ramas."),
    ("Actualizar CONTRIBUTING y plantillas con la definición de terminado", ["documentación", "tarea"], "Must", "S", 1, ["Hernandez"],
     "CONTRIBUTING con GitHub Flow y la definición de terminado; plantillas de PR, historia, defecto y tarea; sección «Cómo trabajar» del README."),
    ("Registrar la retrospectiva del sprint 1 y el objetivo del sprint 2", ["documentación"], "Must", "S", 1, ["Granda"],
     "Acta `docs/proceso/retros/sprint-1.md` con 2 o 3 acciones y responsables; objetivo del sprint 2 en el README."),
    ("T7 - Prototipo de voz con 30 frases", ["tarea", "riesgo"], "Must", "M", 2, ["Granda"],
     "Informe del prototipo de voz con 30 frases reales (riesgos R7 y R9)."),
    ("Mover HU1, HU2 y T2–T6 al sprint 2 y HU7 al sprint 3", ["cambio"], "Must", "XS", 2, ["Hernandez"],
     "El sprint 1 no cumplió su objetivo técnico (ver `docs/proceso/retros/sprint-1.md`). HU1, HU2 y T2–T6 pasan al sprint 2. Para no superar la capacidad, HU7 (Should) pasa al sprint 3. Afecta el plan de sprints de la Tarea 2 (tabla 14). Requiere la aprobación de la docente."),
]


def run(args, check=True, capture=True):
    r = subprocess.run(args, text=True, capture_output=capture)
    if check and r.returncode != 0:
        sys.exit(f"Error en: {' '.join(args)}\n{r.stderr}")
    return r


def gh(*args, check=True):
    return run(["gh", *args], check=check)


def gql(query, **variables):
    body = json.dumps({"query": query, "variables": variables})
    r = subprocess.run(["gh", "api", "graphql", "--input", "-"], input=body, text=True, capture_output=True)
    data = json.loads(r.stdout or "{}")
    if r.returncode != 0 or data.get("errors"):
        raise RuntimeError(data.get("errors") or r.stderr)
    return data["data"]


def users(keys):
    return [GH[k] for k in keys if GH.get(k)]


# ---------------------------------------------------------------- repositorio
def configurar_repo():
    print("== Reglas de fusión")
    gh("repo", "edit", REPO, "--enable-squash-merge", "--enable-merge-commit=false",
       "--enable-rebase-merge=false", "--delete-branch-on-merge")


def proteger_main():
    print("== Protección de main")
    regla = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": {"required_approving_review_count": 1},
        "restrictions": None,
        "required_conversation_resolution": True,
        "allow_force_pushes": False,
        "allow_deletions": False,
    }
    r = subprocess.run(["gh", "api", "-X", "PUT", f"repos/{REPO}/branches/main/protection", "--input", "-"],
                       input=json.dumps(regla), text=True, capture_output=True)
    print("   listo" if r.returncode == 0 else f"   no se pudo: {r.stdout or r.stderr}")


# ---------------------------------------------------------------- etiquetas
def etiquetas(borrar_defecto):
    print("== Etiquetas")
    for name, color, desc in LABELS:
        gh("label", "create", name, "--repo", REPO, "--color", color, "--description", desc, "--force")
    if borrar_defecto:
        for name in DEFAULT_LABELS:
            gh("label", "delete", name, "--repo", REPO, "--yes", check=False)


# ---------------------------------------------------------------- issues
def cuerpo_hu(actor, accion, beneficio, rf, criterios, depende, prioridad, talla):
    lineas = [f"**Como** {actor} **quiero** {accion} **para** {beneficio}.", "",
              "### Criterios de aceptación", ""]
    lineas += [f"- [ ] {c}" for c in criterios]
    lineas += ["", "### Prioridad y talla", "", f"{prioridad} · {talla}", "",
               "### Requisitos y casos de uso relacionados", "", rf, "",
               "### Depende de", "", depende, "",
               "Fuente: Tarea 2, tablas 11 y 13."]
    return "\n".join(lineas)


def backlog():
    """Lista ordenada de issues a crear con sus campos de tablero."""
    items = []
    for (titulo, prio, talla, sprint, resp, actor, accion, benef, rf, crit, dep) in HU:
        items.append(dict(titulo=titulo, labels=["historia"], prioridad=prio, talla=talla, sprint=sprint,
                          resp=resp, body=cuerpo_hu(actor, accion, benef, rf, crit, dep, prio, talla)))
    for (titulo, labels, prio, talla, sprint, resp, texto) in TAREAS:
        items.append(dict(titulo=titulo, labels=labels, prioridad=prio, talla=talla, sprint=sprint,
                          resp=resp, body=f"### Qué hay que hacer\n\n{texto}"))
    return items


def existentes():
    r = gh("issue", "list", "--repo", REPO, "--state", "all", "--limit", "500", "--json", "number,title,url")
    return {i["title"]: i for i in json.loads(r.stdout)}


def crear_issues():
    print("== Issues")
    ya = existentes()
    for it in backlog():
        if it["titulo"] in ya:
            print(f"   ya existe #{ya[it['titulo']]['number']} {it['titulo']}")
            continue
        args = ["issue", "create", "--repo", REPO, "--title", it["titulo"], "--body", it["body"]]
        for lb in it["labels"]:
            args += ["--label", lb]
        for u in users(it["resp"]):
            args += ["--assignee", u]
        url = gh(*args).stdout.strip()
        print(f"   {url}  {it['titulo']}")


# ---------------------------------------------------------------- tablero
FIELDS_Q = """query($id: ID!) { node(id: $id) { ... on ProjectV2 {
  fields(first: 50) { nodes {
    ... on ProjectV2FieldCommon { id name dataType }
    ... on ProjectV2SingleSelectField { options { id name } }
    ... on ProjectV2IterationField { configuration { iterations { id title startDate } } }
  } } } } }"""


def proyecto():
    r = gh("project", "list", "--owner", OWNER, "--format", "json", "--limit", "100")
    for p in json.loads(r.stdout)["projects"]:
        if p["title"] == PROJECT_TITLE:
            return p["number"], p["id"]
    p = json.loads(gh("project", "create", "--owner", OWNER, "--title", PROJECT_TITLE, "--format", "json").stdout)
    gh("project", "link", str(p["number"]), "--owner", OWNER, "--repo", REPO, check=False)
    print(f"   Project creado: {p['url']}")
    return p["number"], p["id"]


def campos(pid):
    return {f["name"]: f for f in gql(FIELDS_Q, id=pid)["node"]["fields"]["nodes"] if f}


def tablero(inicio):
    print("== Project")
    num, pid = proyecto()
    f = campos(pid)

    # Status con las cinco columnas del proceso
    st = f.get("Status")
    if st and [o["name"] for o in st["options"]] != STATUS:
        try:
            gql("""mutation($f: ID!, $o: [ProjectV2SingleSelectFieldOptionInput!]) {
                   updateProjectV2Field(input: {fieldId: $f, singleSelectOptions: $o}) { clientMutationId } }""",
                f=st["id"], o=[{"name": n, "color": "GRAY", "description": ""} for n in STATUS])
        except RuntimeError as e:
            print(f"   Renombren a mano las opciones de Status ({', '.join(STATUS)}): {e}")

    for nombre, opciones in (("Prioridad", "Must,Should,Could,Won't"), ("Talla", "XS,S,M,L,XL")):
        if nombre not in f:
            gh("project", "field-create", str(num), "--owner", OWNER, "--name", nombre,
               "--data-type", "SINGLE_SELECT", "--single-select-options", opciones)

    if "Sprint" not in f:
        d0 = date.fromisoformat(inicio)
        its = [{"title": f"Sprint {i + 1}", "startDate": (d0 + timedelta(days=14 * i)).isoformat(), "duration": 14}
               for i in range(8)]
        try:
            gql("""mutation($p: ID!, $c: ProjectV2IterationFieldConfigurationInput!) {
                   createProjectV2Field(input: {projectId: $p, dataType: ITERATION, name: "Sprint",
                   iterationConfiguration: $c}) { clientMutationId } }""",
                p=pid, c={"startDate": inicio, "duration": 14, "iterations": its})
        except RuntimeError as e:
            print("   No se pudo crear el campo Sprint por API. Créenlo a mano: Settings del Project → "
                  f"New field → Iteration, 2 semanas, inicio {inicio}, 8 iteraciones. Luego vuelvan a ejecutar "
                  f"con --solo tablero.\n   ({e})")

    f = campos(pid)
    opt = lambda campo, nombre: next((o["id"] for o in f[campo]["options"] if o["name"] == nombre), None)
    sprints = {}
    if "Sprint" in f:
        for it in f["Sprint"]["configuration"]["iterations"]:
            sprints[it["title"]] = it["id"]

    ya = existentes()
    for it in backlog():
        issue = ya.get(it["titulo"])
        if not issue:
            continue
        item = json.loads(gh("project", "item-add", str(num), "--owner", OWNER, "--url", issue["url"],
                             "--format", "json").stdout)["id"]
        estado = "Por hacer" if it["sprint"] in (1, 2) else "Backlog"
        valores = [("Status", opt("Status", estado)), ("Prioridad", opt("Prioridad", it["prioridad"])),
                   ("Talla", opt("Talla", it["talla"]))]
        for campo, oid in valores:
            if campo in f and oid:
                gh("project", "item-edit", "--id", item, "--project-id", pid, "--field-id", f[campo]["id"],
                   "--single-select-option-id", oid)
        sid = sprints.get(f"Sprint {it['sprint']}") if it["sprint"] else None
        if sid:
            gh("project", "item-edit", "--id", item, "--project-id", pid, "--field-id", f["Sprint"]["id"],
               "--iteration-id", sid)
        print(f"   #{issue['number']} {it['titulo']}: {estado}, {it['prioridad']}, {it['talla']}, sprint {it['sprint']}")

    print("\nPasos que la API no permite y se hacen en la web del Project:")
    print("  - Workflows → Auto-add to project: filtro is:issue,pr para este repositorio.")
    print("  - Workflows → Item closed y Pull request merged: Status = Hecho.")
    print("  - En la descripción del Project, pegar el objetivo del sprint 2 (está en el README).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inicio", required=True, help="Lunes de la semana 1 (AAAA-MM-DD)")
    ap.add_argument("--solo", choices=["repo", "etiquetas", "issues", "tablero", "proteccion"])
    ap.add_argument("--borrar-etiquetas-por-defecto", action="store_true")
    a = ap.parse_args()
    date.fromisoformat(a.inicio)
    pasos = {
        "repo": configurar_repo,
        "etiquetas": lambda: etiquetas(a.borrar_etiquetas_por_defecto),
        "issues": crear_issues,
        "tablero": lambda: tablero(a.inicio),
        "proteccion": proteger_main,
    }
    for nombre, paso in pasos.items():
        if a.solo in (None, nombre):
            paso()


if __name__ == "__main__":
    main()
