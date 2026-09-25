# tpanneck.github.io

Persönliche Seite von Thorsten Panneck-Conradi — <https://tpanneck.github.io/>

Gebaut mit [MkDocs](https://www.mkdocs.org/) und dem Material-Theme.

## Aufbau

| Ort | Was |
|---|---|
| `docs/` | die Seiten als Markdown |
| `docs/stylesheets/eigenes.css` | die eigene Schicht über dem Theme — Kacheln, Stationen, Farben |
| `mkdocs.yml` | Navigation, Theme, Erweiterungen |

Zwei Zweige: **`master`** trägt die Quellen, **`gh-pages`** die gebaute Seite. Nichts von
Hand in `gh-pages` ändern — der Zweig wird beim Veröffentlichen überschrieben.

## Ansehen und bauen

```bash
python3 -m mkdocs serve          # lokal unter http://127.0.0.1:8000
python3 -m mkdocs build --strict # baut nach site/, bricht bei Warnungen ab
python3 pruefe-oeffentlich.py    # das Gate: elf Muster gegen den gebauten Bestand
```

`pruefe-oeffentlich.py` läuft **vor** jedem Veröffentlichen. Es prüft den gebauten Bestand
unter `site/`, nicht die Quelle — ausgeliefert wird das HTML. Beendet mit 1, wenn etwas
gefunden wurde.

## Veröffentlichen

```bash
python3 -m mkdocs gh-deploy --strict
```

Baut die Seite und schiebt sie nach `gh-pages`. Die Quellen im Zweig `master` werden dabei
nicht angefasst — die committet und pusht man wie gewohnt.

## Hausregeln für den Inhalt

- **Keine Zahl, die sich nicht belegen lässt.** Alle Zahlen sind aus der
  Versionsverwaltung abgelesen, nicht geschätzt. Codezeilen stehen bewusst nirgends, weil
  in einer Auszählung des Bestands erzeugte Dateien mitzählen würden.
- **Keine Arbeitgeber-Interna.** Keine Namen von Ansprechpersonen, keine Lohnklassen, keine
  vertraulichen Projektdetails, nichts aus laufenden Verfahren.
- **Keine Kontaktangaben.** Keine E-Mail-Adresse, keine Telefonnummer, keine Wohnadresse,
  keine Verfügbarkeit und kein Pensum. Die Seite ist ein Nachschlagewerk für Leute, die den
  Weg ohnehin schon haben — kein Formular für Fremde. Wer die Seite bekommt, bekommt sie
  von Thorsten, und damit auch die Adresse.
- **Private Repositorien werden beschrieben, nicht verlinkt.** Tote Links auf private
  Repositorien sehen schlechter aus als eine ehrliche Zeile.
