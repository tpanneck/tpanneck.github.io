#!/usr/bin/env python3
"""Setzt feste Anker an die Projektueberschriften.

Ohne feste Anker leitet MkDocs den Sprungpunkt aus dem ganzen Ueberschriftentext
ab — `#lingdeem-node-ein-knoten-der-berechtigungen-lokal-beantwortet`. Der
bricht, sobald jemand die Ueberschrift umformuliert, und die Startseite
verlinkt dann ins Leere. Mit `{ #name }` bleibt der Anker, auch wenn der Text
sich aendert.

Einmalig auszufuehren; das Ergebnis steht danach in der Markdown-Datei.
"""
from pathlib import Path

ZIEL = Path(__file__).parent / "docs" / "projekte.md"

ANKER = {
    "### lingdeem-node — ein Knoten, der Berechtigungen lokal beantwortet": "lingdeem-node",
    "### federation-rt — Container-Laufzeit mit Beweisen": "federation-rt",
    "### cloud-arbeit und infra — Plattform und ihre Grundlage": "cloud-arbeit",
    "### claude-remote — Werkbank für die Zusammenarbeit": "claude-remote",
    "### cybersicherheit — ein deutschsprachiges Feldwerk": "cybersicherheit",
    "### meaning-layer — was unter der Sprache liegt": "meaning-layer",
    "### probanz-werkstatt": "probanz-werkstatt",
    "### kita-studie — was öffentliche Kinderbetreuung kostet": "kita-studie",
}

text = ZIEL.read_text(encoding="utf-8")
for zeile, name in ANKER.items():
    if f"{{ #{name} }}" in text:
        continue
    if zeile not in text:
        raise SystemExit(f"Ueberschrift nicht gefunden: {zeile}")
    text = text.replace(zeile, f"{zeile} {{ #{name} }}")
ZIEL.write_text(text, encoding="utf-8")
print(f"{len(ANKER)} Anker gesetzt in {ZIEL}")
