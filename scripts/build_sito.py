#!/usr/bin/env python3
"""Costruisce il sito pubblico delle lezioni (cartella sito/).

Per ogni cartella «NN LEZ UNIVERSITA'» legge LEZIONE.md, toglie le sezioni
private (esercizi svolti e dubbi aperti) e la converte in HTML con pandoc.
Uso: python3 scripts/build_sito.py   (dalla radice del repository)
"""
import html
import pathlib
import re
import shutil
import subprocess

RADICE = pathlib.Path(__file__).resolve().parent.parent
SITO = RADICE / "sito"

# Sezioni che restano solo nel repository privato
SEZIONI_PRIVATE = ("esercizi svolti", "dubbi aperti", "esercizi")

PAGINA = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titolo}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="stylesheet" href="{base}style.css">
</head>
<body>
<header class="testata"><a href="{base}index.html">Analisi 1 · Lezioni 2026/27</a></header>
<main>
{corpo}
</main>
<footer>Appunti personali di Pierluigi Ceccon · Analisi Matematica 1, Università di Udine.
Le slide del docente non sono riprodotte qui.</footer>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script>
document.querySelectorAll('.math').forEach(function (el) {{
  try {{
    katex.render(el.textContent, el, {{displayMode: el.classList.contains('display'), throwOnError: false}});
  }} catch (e) {{}}
}});
</script>
</body>
</html>
"""


def togli_sezioni_private(testo: str) -> str:
    """Elimina le sezioni '## ...' private (fino alla sezione successiva)."""
    blocchi = re.split(r"(?m)^(?=## )", testo)
    tenuti = []
    for b in blocchi:
        intestazione = b.splitlines()[0].lower() if b.strip() else ""
        if intestazione.startswith("## ") and any(
            intestazione[3:].strip().startswith(s) for s in SEZIONI_PRIVATE
        ):
            continue
        tenuti.append(b)
    pulito = "".join(tenuti)
    # toglie eventuali separatori '---' rimasti in fondo
    return re.sub(r"(\n-{3,}\s*)+$", "\n", pulito.rstrip()) + "\n"


def md_in_html(md: str) -> str:
    r = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html5", "--katex"],
        input=md, capture_output=True, text=True, check=True,
    )
    return r.stdout


def main() -> None:
    if SITO.exists():
        shutil.rmtree(SITO)
    (SITO / "lezioni").mkdir(parents=True)
    shutil.copy(RADICE / "scripts" / "style.css", SITO / "style.css")

    voci = []
    for cartella in sorted(RADICE.glob("[0-9][0-9] LEZ UNIVERSITA*")):
        f = cartella / "LEZIONE.md"
        if not f.exists():
            continue
        num = cartella.name[:2]
        md = togli_sezioni_private(f.read_text(encoding="utf-8"))
        titolo = md.splitlines()[0].lstrip("# ").strip()
        argomento = titolo.split("–", 1)[-1].strip()
        data = re.search(r"Data della lezione:\*\*\s*([0-9/]+)", md)
        corpo = md_in_html(md)
        (SITO / "lezioni" / f"{num}.html").write_text(
            PAGINA.format(titolo=html.escape(titolo), base="../", corpo=corpo),
            encoding="utf-8",
        )
        voci.append((num, data.group(1) if data else "", argomento))

    righe = "\n".join(
        f'<li><a href="lezioni/{n}.html"><span class="num">{n}</span>'
        f'<span class="arg">{html.escape(a)}</span><span class="data">{d}</span></a></li>'
        for n, d, a in voci
    )
    indice = (
        "<h1>Lezioni di Analisi 1</h1>\n"
        "<p class=\"intro\">I miei appunti delle lezioni di Analisi Matematica 1 "
        "(Università di Udine, a.a. 2026/27), una pagina per lezione.</p>\n"
        f"<ol class=\"elenco\">\n{righe}\n</ol>"
    )
    (SITO / "index.html").write_text(
        PAGINA.format(titolo="Analisi 1 · Lezioni 2026/27", base="", corpo=indice),
        encoding="utf-8",
    )
    print(f"Sito costruito: {len(voci)} lezioni in {SITO}")


if __name__ == "__main__":
    main()
