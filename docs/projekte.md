# Arbeiten

<p class="vorspann">Elf Vorhaben seit Februar 2026, in vier Fächern. Alle unter eigener
Führung entstanden, keines allein getippt. Was sie verbindet, ist nicht das Thema, sondern
das Verfahren.</p>

<div class="kacheln" markdown="0">
  <div class="kachel"><span class="zahl">2 155</span><span class="was">Commits seit 23. Februar 2026</span></div>
  <div class="kachel"><span class="zahl">11</span><span class="was">Vorhaben, neben einer vollen Stelle</span></div>
  <div class="kachel"><span class="zahl">4</span><span class="was">Fächer: Software, Sicherheit, Sprache, Finanzen</span></div>
</div>

!!! note "Warum hier keine Codezeilen stehen"
    Sie liessen sich ausweisen und wären beeindruckend. Aber in einer Auszählung des
    Bestands zählen erzeugte Dateien und Bauartefakte mit — bei zwei der Repositorien
    ergäbe das über eine Million «Zeilen». Eine Zahl, die man nicht verteidigen kann,
    entwertet den Rest. Commits und Kalendertage sind prüfbar, Zeilen sind es hier nicht.

## Software und Infrastruktur

### lingdeem-node — ein Knoten, der Berechtigungen lokal beantwortet

**458 Commits, 30. August bis 21. September 2026. OCaml.**

Ein Cloud-Knoten, der die Steuerungsebene repliziert mitträgt und Berechtigungsfragen
lokal beantwortet, ohne Netzaufruf. Im Abbild steckt kein Geheimnis, nur der öffentliche
Vertrauensanker; Identität und Rolle kommen beim Start von aussen. Gemessen gegen einen
echten Bestand aus 43 Prinzipalen, 25 Rechten, 12 Rollen, 31 Ressourcen und 34 Bindungen:

| Messung | Ergebnis |
|:--|:--|
| Entscheidungen gegen die zentrale Referenz | 712 von 712 identisch |
| Lokale Autorisierung | rund 2 ms, ohne Netzaufruf |
| Entzogenes Recht überall sichtbar | 87–111 ms, ohne Cache-Invalidierung |
| Vierter Knoten tritt im Betrieb bei | auskunftsfähig nach 1,5–3,2 s |
| Leader hart getötet | neuer Leader nach 1,7–2,8 s |
| Quorum verloren (3 von 4 tot) | Lesen läuft weiter, Schreiben verweigert korrekt |

**Und der Befund, der mehr wert ist als die Tabelle.** Der erste Rotationslauf meldete 852
erfolgreiche Anfragen und null Fehler — und war falsch. Der Prüfer las nur, während drei
tote Knoten noch in der Konfiguration standen und kein Quorum mehr bestand. Ein Prüfer,
der nur liest, gibt genau in diesem Fall falsche Entwarnung. Behoben nicht durch Disziplin,
sondern mechanisch, mit Gegenprobe am selben Abend.

### federation-rt — Container-Laufzeit mit Beweisen

**289 Commits in sieben Tagen, März 2026. OCaml und Rocq.**

Eine Laufzeitumgebung für Container, deren Isolationseigenschaften nicht behauptet, sondern
in Rocq bewiesen werden.

### cloud-arbeit und infra — Plattform und ihre Grundlage

**446 und 218 Commits, Juni bis September 2026.**

Anforderungen und Dokumentation einer Plattform, dazu deren Infrastruktur als Code:
OpenTofu für die Beschaffung, Ansible für die Einrichtung, mit Zustandstrennung,
Netzsegmentierung und Zugangsregeln als versionierte Artefakte.

### claude-remote — Werkbank für die Zusammenarbeit

**152 Commits, August bis September 2026. Clojure und Babashka.**

Broker, Connector und Weboberfläche, um die eigene KI-Arbeit von überall zu führen und zu
beobachten. Enthält die Regressionsproben, die bei einem Fehler in der Agentenanzeige mehr
gefunden haben als das Nachdenken — siehe [Mit KI arbeiten](mit-ki-arbeiten.md).

<p class="privat">Der Code dieser Vorhaben liegt in privaten Repositorien. Einsicht auf
Anfrage, in einem Gespräch gern im Detail.</p>

## Sicherheit

### cybersicherheit — ein deutschsprachiges Feldwerk

**176 Seiten, rund 234 700 Wörter, 72 Commits — in drei Tagen, 21. bis 23. September 2026.**

Ein Nachschlagewerk, das das Feld als Ganzes bewirtschaftet: von der Lage über Technik und
Erkennung bis zu Betrieb und Befähigung einer Mannschaft. Angefangen, weil eine Durchsicht
von zwölf deutschsprachigen Angeboten ergab, dass keines das leistet — Behördenportale sind
auf Zertifizierung zugeschnitten, Vereine auf Aufklärung, Verbände auf ihre Mitglieder,
Fachmedien auf Aktualität. Für das IT-Grundschutz-Kompendium gibt es ein deutschsprachiges
Gegenstück zur NIST-Reihe; für MITRE ATT&CK gibt es keines.

Die Hausregel:

> Nichts steht hier, weil es interessant ist. Es steht hier, weil jemand daran etwas prüfen
> oder bauen kann.

<p class="privat">Zurzeit als interne Fassung geführt. Eine zeigbare Auswahl ist in
Vorbereitung.</p>

## Sprache

### meaning-layer — was unter der Sprache liegt

**208 Commits, Juni bis September 2026. Clojure.**

Ein Modell mit zwei Schichten: körpernahe **Grundoperationen** als geteiltes Skelett
(Bild-Schemata nach Johnson und Lakoff) und darüber die sprachspezifischen **Dekoratoren** —
*fliehen* statt bloss *weg-bewegen*. Die Grammatik wohnt im Dekorator, nie im Kern.

Die Bedeutung steckt dabei ausdrücklich nicht im Modell, sondern beim Beobachter: Das
Modell ist ein Skelett mit Anker, kein Behälter. Jeder Text wird zuerst einsprachig
modelliert — Homer im Altgriechischen, mit eigener Übersetzung —, und Übersetzbarkeit ist
nicht Voraussetzung, sondern **Befund**: Greift die Dekorator-Klasse der Zielsprache, was
die der Quellsprache trägt, oder nicht? Das Nicht-Greifen ist die Messung.

**Warum das hier steht und nicht unter «Hobbys».** Dieses Vorhaben ist der Ursprung des
Verfahrens, nach dem ich heute alles andere prüfe — gefunden an seinem eigenen Scheitern.
Mehr dazu unter [Mit KI arbeiten](mit-ki-arbeiten.md).

### probanz-werkstatt

**21 Commits, Juni bis September 2026.** Offene Forschungswerkstatt zur Vermessung von
Wirklichkeit im Sprachgebrauch.

## Finanzen und Verwaltung

### kita-studie — was öffentliche Kinderbetreuung kostet

**67 Seiten, rund 211 000 Wörter, 127 Commits — in fünf Tagen, 19. bis 23. September 2026.**

Eine Untersuchung zur Finanzierbarkeit öffentlich getragener Kitas in einer Schweizer
Stadt, ausschliesslich aus öffentlich zugänglichen Quellen. 263 geprüfte Quellenadressen,
6 151 interne Verweise, ein Zahlenregister mit dreissig Selbstprüfungen, die bei jedem Bau
mitlaufen.

Der methodische Kern ist eine Unterscheidung, die sich auf jede Kostendiskussion
übertragen lässt: **Divergenz** ist derselbe Wert unter denselben Prämissen, verschieden
angegeben — ein Fehler. **Lesart** ist derselbe Gegenstand unter verschieden *benennbaren*
Prämissen — beide bleiben stehen, nebeneinander. Die Studie zwingt sich, jede Lesart als
solche auszuweisen, statt eine davon zur Wahrheit zu erklären.

<p class="privat">Interne Fassung.</p>

## Und das Verbindende

Vier Fächer, die fachlich nichts miteinander zu tun haben — Berechtigungssysteme,
Cybersicherheit, altgriechische Semantik, kommunale Finanzen. Was sie verbindet, ist die
Bauweise: eine Behauptung gilt erst, wenn eine Maschine sie prüft; jede Verwandlung
deklariert eine prüfbare Invariante; und wer ein Mass zum Ziel macht, verdirbt es als Mass.

Das ist keine Werkzeugkenntnis. Es ist ein Verfahren, und wo es herkommt, steht auf der
[nächsten Seite](mit-ki-arbeiten.md).
