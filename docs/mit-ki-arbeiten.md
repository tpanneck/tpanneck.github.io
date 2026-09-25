# Mit KI arbeiten

<p class="vorspann">Nicht schneller tippen. Ein System führen und sein Ergebnis abnehmen
können — und wissen, woran die eigene Prüfung schon gescheitert ist.</p>

Seit Februar 2026 arbeite ich durchgehend mit einem KI-System. Was dabei entstanden ist,
steht unter [Arbeiten](projekte.md). Diese Seite handelt nicht davon, **dass** ich das tue,
sondern **wie** — denn das erste ist inzwischen verbreitet und das zweite selten.

## Das Grundproblem

Moderne Modelle erzeugen mühelos Ergebnisse, die *richtig aussehen*. Das ist ihre Stärke
und ihr zentrales Risiko: **Der Prüfaufwand verschiebt sich vom Erzeugen zum Abnehmen.**
Wer KI-Tempo mit klassischer Stichproben-Abnahme kombiniert, produziert schnellen,
ungeprüften Bestand — in einem regulierten Umfeld ist das kein Effizienzgewinn, sondern ein
Risiko.

Daraus folgt der Satz, um den sich meine ganze Arbeitsweise dreht:

> AI-Workflows werden nicht über das Erzeugen gesteuert, sondern über das Prüfen. Jede
> Etappe endet an einem Gate, das maschinell und beweisbar feststellt, ob das Ergebnis
> trägt — Plausibilität genügt nie.

Ein Gate ist dabei wörtlich zu nehmen: eine Schranke. Öffnet sie sich nicht, geht es nicht
weiter. Ein Gate, das nur berichtet, ist kein Gate.

## Woher das Verfahren kommt

Nicht aus der Informatik. **Aus der Linguistik — und aus einem Fehlschlag.**

Die erste Fassung meines Sprachmodells (`meaning-layer` v0.1) prüfte sich selbst, indem sie
altgriechische Modelle ins Deutsche zurückübersetzte und mit dem Original verglich. Das
funktionierte — und war die Falle. Das Verfahren optimierte mit der Zeit heimlich auf eine
Grammatik-Maschine: auf die Oberfläche der Rückübersetzung statt auf die dahinterliegende
Bedeutung. **Das Mass war zum Magneten geworden.**

Das ist Goodharts Gesetz, und es hat mich mehr gelehrt als jedes gelungene Projekt: Sobald
ein Mass zum Ziel wird, verdirbt es als Mass. Für KI-Systeme ist der Effekt katalogisiert
und quantifiziert — Optimierung auf ein unvollkommenes Mass verbessert die wahre Leistung
nur bis zu einem kritischen Punkt, danach verschlechtert sie sie.

Aus dieser Erfahrung sind die Prinzipien entstanden, die ich später verallgemeinert und
aufgeschrieben habe.

## Sechs Prinzipien, siebzehn Gates

Das Diskussionspapier [«Verifikationsgetriebene AI-Workflows»](schreiben.md) hält fest, was
sich in der Praxis gehalten hat:

1. **Gate-Kette statt Vertrauenskette** — jede Etappe endet an einer maschinellen Schranke.
2. **Skripte statt Chat-Schleifen** — was wiederholbar sein soll, wird Code, nicht Dialog.
3. **Verfahrenstreue im Lauf** — das Verfahren ist versioniert und wird nicht unterwegs
   angepasst, damit das Ergebnis vergleichbar bleibt.
4. **Adversariale Prüfung als Standard** — der Prüfer sucht den Fehler, nicht die
   Bestätigung.
5. **Zurechnung und Spur** — jedes Artefakt weiss, woraus es entstanden ist.
6. **Messen, was wirklich trägt** — Ablations-Messung statt Etiketten wie «wichtig».

Dazu ein Katalog von siebzehn Gates, hergeleitet aus einem Korpus tatsächlicher Vorfälle.

## Drei Fehlschläge, an denen es sich zeigt

Ein Verfahren ist nur so glaubwürdig wie die Fehler, über die man Auskunft geben kann.

### Der grüne Prüfbericht, der falsch war

Der erste Rotationslauf des Knotens meldete 852 erfolgreiche Anfragen und null Fehler. Er
prüfte nur lesend, während drei tote Knoten in der Konfiguration standen und kein Quorum
mehr bestand. **Ein Prüfer, der nur liest, gibt genau in diesem Fall falsche Entwarnung.**
Behoben mechanisch, nicht durch Vorsatz, mit Gegenprobe am selben Abend.

### Der Geist in der Oberfläche

Ein Subagent, der nie gestartet war, stand zwölf Minuten lang als «läuft» in der Anzeige.
Der Zählweg öffnete den Eintrag beim Aufruf und schloss ihn nur bei einer Fertigmeldung —
die für einen nie gestarteten Agenten nie kommt. Beide Enden, Zählweg und Oberfläche,
hatten dieselbe Lücke. Deshalb half auch die Nachfrage alle fünf Sekunden nicht:

> Zwei Stellen mit demselben blinden Fleck prüfen einander nicht, sie bestätigen einander.

Die erste Korrektur war zu grob und hätte aus einem Geist eine Leiche gemacht — ein
laufender Agent wäre aus der Anzeige verschwunden. Gefunden hat das nicht mein Nachdenken,
sondern eine Beispieldatei mit vier Fällen. Die musste sich dabei selbst korrigieren: Sie
bildete eine Fertigmeldung so nach, wie ich sie mir vorstellte, nicht wie sie wirklich
aussieht. **Eine Beispieldatei, die anders aussieht als die Wirklichkeit, prüft die
Wirklichkeit nicht.**

### Das Mass, das nicht ans Ergebnis angepasst wurde

Die Selbstmessung der Kita-Studie wies für einen Tag «0 von 10 Korrektur-Commits» aus,
obwohl dieser Tag fast nur aus Korrekturen bestand — kein Commit-Titel passte auf den
Suchausdruck. Die Versuchung war, den Suchausdruck zu weiten, bis die Zahl stimmt. Das wäre
das Anpassen des Masses an das gewünschte Ergebnis gewesen. Stattdessen steht der Fehlgriff
jetzt als Beispiel auf der Seite selbst.

## Was daraus für Organisationen folgt

Das ist der Teil, der mich heute am meisten beschäftigt, und er ist keine technische Frage.

- **Die KI entscheidet nie über Geltung.** Sie extrahiert, schlägt vor, implementiert,
  prüft — ob eine Regel gilt, entscheidet das Fach, als *enges, einzelfallbezogenes und
  protokolliertes* menschliches Gate. Pauschale Pflichten zur «menschlichen Aufsicht»
  werden empirisch regelmässig zur Legitimationsfassade, weil niemand die verlangte
  Dauerkontrolle leisten kann.
- **Der Betrieb solcher Verfahren ist eine Rolle, kein Nebenbei.** Verfahren versionieren,
  Gates pflegen, Läufe fahren, Prüfungen ansetzen — so wie der Betrieb einer
  Fertigungsstrasse ein eigenes Handwerk ist und keine Nebenaufgabe der Konstrukteure.
- **Das menschliche Gate ist der Engpass, nicht die Technik.** Und dieser Engpass hat eine
  Grössenordnung, die man aussprechen muss, sonst rechnet sich das Modell nie.
- **Das Sitzungsarchiv gehört zur Akte.** Wer KI-gestützt arbeitet, erzeugt eine Spur, und
  die ist Teil der Nachvollziehbarkeit.

## Und die offene Frage, die ich als offen führe

Meine ganze Evidenz stammt aus **Ein-Personen-plus-KI-Praxis mit voller Werkzeugfreiheit.**
Das ist eine ehrliche Grenze, und sie steht auch so im Papier. Die erste der dort genannten
offenen Fragen lautet:

> Wie übersetzt sich die Gate-Disziplin in ein arbeitsteiliges Team mit bestehenden
> Prozessen?

Darauf habe ich keine erprobte Antwort. Ich habe eine Position, eine Menge Narben und den
Wunsch, das dort weiterzuarbeiten, wo diese Grenze tatsächlich überschritten wird.

Deshalb ist die Frage, die mich interessiert, auch nicht «welche Werkzeuge setzt ihr ein»,
sondern:

> **Wie wollen wir unsere Arbeit neu zuschneiden, wenn ein Teil des Erzeugens wegfällt und
> dafür das Prüfen zur Hauptarbeit wird — und welche Vorstellung davon gibt es schon?**
