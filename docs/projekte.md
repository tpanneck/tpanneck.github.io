# Projekte

<p class="vorspann">Nebenher entstanden, seit Februar 2026, alle mit einem KI-System
gebaut. Versuche, keine Produkte.</p>

!!! note "Zu den Zahlen"
    Wo Commits und Tage stehen, sind sie aus der Versionsverwaltung abgelesen. Codezeilen
    stehen nirgends: In einer Auszählung des Bestands zählen erzeugte Dateien und
    Bauartefakte mit, das gäbe Zahlen, die nichts bedeuten.

## claude-remote — eine Werkbank { #claude-remote }

**152 Commits, August bis September 2026. Clojure und Babashka.**

Broker, Connector und eine Weboberfläche, um von überall mit dem KI-System zu arbeiten und
zu sehen, was gerade läuft. Entstanden aus einem praktischen Bedürfnis: Wer unterwegs eine
Frage hat, möchte nicht erst einen Rechner aufklappen.

Enthält die Regressionsproben zu einem Fehler, den ich lange nicht gesehen habe: Ein
Teilprozess, der nie gestartet war, stand zwölf Minuten lang als «läuft» in der Anzeige.
Zählweg und Oberfläche hatten dieselbe Lücke, deshalb half auch die Nachfrage alle fünf
Sekunden nichts — zwei Stellen mit demselben blinden Fleck prüfen einander nicht.

## lingdeem-node — Berechtigungen lokal beantworten { #lingdeem-node }

**458 Commits, 30. August bis 21. September 2026. OCaml.**

Ein Cloud-Knoten, der die Steuerungsebene repliziert mitträgt und Berechtigungsfragen
lokal beantwortet, ohne Netzaufruf. Im Abbild steckt kein Geheimnis, nur der öffentliche
Vertrauensanker; Identität und Rolle kommen beim Start von aussen.

Gemessen gegen einen Bestand aus 43 Prinzipalen, 25 Rechten, 12 Rollen und 34 Bindungen:

| | |
|:--|:--|
| Entscheidungen gegen die zentrale Referenz | 712 von 712 identisch |
| Lokale Autorisierung | rund 2 ms |
| Entzogenes Recht überall sichtbar | 87–111 ms |
| Vierter Knoten tritt im Betrieb bei | auskunftsfähig nach 1,5–3,2 s |
| Quorum verloren (3 von 4 tot) | Lesen läuft weiter, Schreiben verweigert |

Wichtiger als die Tabelle ist, was daneben passiert ist: Der erste Rotationslauf meldete
852 erfolgreiche Anfragen und null Fehler — und war falsch. Der Prüfer las nur, während
drei tote Knoten in der Konfiguration standen und kein Quorum mehr bestand.

## cybersicherheit — eine Sammlung auf Deutsch { #cybersicherheit }

**176 Seiten, 72 Commits, September 2026.**

Von der Lage über Technik und Erkennung bis zu Betrieb und Ausbildung. Angefangen, weil
ich beim Suchen nichts gefunden habe, das durchgehend war: Behördenportale sind auf
Zertifizierung zugeschnitten, Vereine auf Aufklärung, Verbände auf ihre Mitglieder,
Fachmedien auf Aktualität. Für das IT-Grundschutz-Kompendium gibt es ein deutschsprachiges
Gegenstück zur NIST-Reihe; für MITRE ATT&CK nicht.

Eine Regel hält das Ganze zusammen:

> Nichts steht hier, weil es interessant ist. Es steht hier, weil jemand daran etwas prüfen
> oder bauen kann.

<p class="privat">Zurzeit nur intern. Ob und in welcher Form etwas davon zeigbar wird, ist
offen.</p>

## meaning-layer — was unter der Sprache liegt { #meaning-layer }

**208 Commits, Juni bis September 2026. Clojure.**

Zwei Schichten: körpernahe **Grundoperationen** als geteiltes Skelett — Bild-Schemata nach
Johnson und Lakoff — und darüber sprachspezifische **Dekoratoren**: *fliehen* statt bloss
*weg-bewegen*. Die Grammatik wohnt im Dekorator, nie im Kern.

Die Bedeutung steckt dabei nicht im Modell, sondern beim Leser: Das Modell ist ein Skelett
mit Anker, kein Behälter. Jeder Text wird zuerst einsprachig modelliert — Homer im
Altgriechischen, mit eigener Übersetzung. Übersetzbarkeit ist dann nicht Voraussetzung,
sondern Ergebnis: Greift die Dekorator-Klasse der Zielsprache, was die der Quellsprache
trägt, oder nicht?

Ob das Modell trägt, weiss ich nicht. Die erste Fassung trug jedenfalls nicht, und warum,
steht unter [Mit KI arbeiten](mit-ki-arbeiten.md).

## federation-rt — eine Laufzeit mit Beweisen { #federation-rt }

**289 Commits in sieben Tagen, März 2026. OCaml und Rocq.**

Eine Laufzeitumgebung für Container, deren Isolationseigenschaften nicht behauptet, sondern
in Rocq bewiesen werden. Ein Versuch, ob sich das im Nebenbei überhaupt machen lässt.

## probanz-werkstatt { #probanz-werkstatt }

**21 Commits, Juni bis September 2026.** Eine kleine Werkstatt zur Frage, wie sich geteilte
Wirklichkeit im Sprachgebrauch messen lässt. Gehört zum meaning-layer.

---

Der Code liegt in privaten Repositorien. Im Gespräch zeige ich gern etwas davon — an einem
Messprotokoll oder an einem Fehler.
