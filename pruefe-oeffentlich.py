#!/usr/bin/env python3
"""Gate vor dem Veroeffentlichen: Was darf auf einer oeffentlichen Seite nicht stehen?

Die Seite geht unter eigenem Namen ins offene Netz. Was hier einmal steht, ist
zitierbar, indexiert und auch nach dem Loeschen noch im Cache. Deshalb laeuft
vor jedem Deploy eine Schranke, die maschinell prueft — nicht die Erinnerung.

Geprueft wird der GEBAUTE Bestand (site/), nicht die Quelle: Was im HTML steht,
ist das, was ausgeliefert wird.

Aufruf:  python3 pruefe-oeffentlich.py
Beendet mit 1, wenn etwas gefunden wurde.
"""
import re
import sys
from pathlib import Path

SITE = Path(__file__).parent / "site"

# (Name, Muster, Begruendung)
VERBOTEN = [
    ("Telefonnummer", r"\+41[\s.]?\d{2}[\s.]?\d{3}[\s.]?\d{2}[\s.]?\d{2}|\+41 \d{2} \d{3} \d{2} \d{2}",
     "Nicht auf eine oeffentliche Seite — Kontakt laeuft ueber E-Mail."),
    ("Wohnadresse", r"Zulligerstrasse|CH-3063|3063 Ittigen",
     "Ortsangabe ja, Hausadresse nein."),
    ("Lohnklasse", r"\bLK ?\d{2}\b|Lohnklasse",
     "Gehoert in kein oeffentliches Dokument."),
    ("Referenz-Nr. einer Ausschreibung", r"\b\d{3}-\d{4,5}\b",
     "Verraet, auf welche Stellen gerade beworben wird."),
    ("Austrittslage", r"Aufloesungsvereinbarung|Auflösungsvereinbarung|"
                      r"gegenseitigem Einvernehmen|organisatorische Neuausrichtung|"
                      r"Probezeit|Kuendigung|Kündigung",
     "Die eigene Vertragslage ist Sache des Gespraechs, nicht der Startseite."),
    ("Amt namentlich", r"\bSECO\b|EasyGov|Staatssekretariat für Wirtschaft",
     "Die aktuelle Stelle steht als «Bundesverwaltung», ohne Amt."),
    ("Namen von Ansprechpersonen", r"Hänggi|Haenggi|Ducrey|Nussbaumer|Micic|"
                                   r"Plattner|Felber|Zemp|Bigler|Drews|Thomi|Hoffmann",
     "Keine Namen aus laufenden Verfahren."),
    ("Interne Pfade", r"/home/ubuntu|/tmp/claude|lingdeem\.ch/belege",
     "Pfade dieser Maschine gehoeren nicht ins Netz."),
    ("Zugangsdaten", r"(?i)\b(token|passwort|password|api[_-]?key|secret)\b\s*[:=]",
     "Offensichtlich."),
    ("E-Mail-Adresse", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|mailto:",
     "Ausdruecklich nicht auf diese Seite. Die Adresse geben wir selbst weiter."),
    ("Verfuegbarkeit", r"(?i)\bverf(ü|ue)gbar\b|ab Januar 20\d\d|"
                       r"\b\d{2}\s?(bis|–|-)\s?\d{2}\s?Prozent\b|\b\d{2}–\d{3}\s?%",
     "Kein Datum, kein Pensum — das gehoert ins Gespraech, nicht ins Netz."),
]

# Was ausdruecklich erlaubt ist, obwohl ein Muster greifen koennte.
AUSNAHMEN = [
    r"99,995",          # Abrechnungsgenauigkeit, keine Referenznummer
    r"200-1 bis 200-4",  # BSI-Standards
]


def bereinigen(text):
    for a in AUSNAHMEN:
        text = re.sub(a, " ", text)
    return text


def main():
    if not SITE.is_dir():
        print("site/ fehlt — zuerst `python3 -m mkdocs build --strict`")
        return 2

    dateien = sorted(SITE.rglob("*.html"))
    funde = 0
    for name, muster, warum in VERBOTEN:
        treffer = []
        for f in dateien:
            if "/assets/" in str(f):
                continue
            text = bereinigen(f.read_text(encoding="utf-8", errors="replace"))
            for m in re.finditer(muster, text):
                umgebung = text[max(0, m.start() - 45):m.end() + 45].replace("\n", " ")
                treffer.append(f"{f.relative_to(SITE)}: …{umgebung}…")
        if treffer:
            funde += len(treffer)
            print(f"FUND  {name} — {warum}")
            for t in treffer[:4]:
                print(f"        {t}")
        else:
            print(f"  ok  {name}")

    print(f"\n{len(dateien)} Seiten geprueft, {funde} Funde")
    return 1 if funde else 0


if __name__ == "__main__":
    sys.exit(main())
