# Mit KI arbeiten

<p class="vorspann">Wie ich vorgehe, woher das kommt und wo es nicht weitergeht.</p>

Seit Februar 2026 arbeite ich durchgehend mit einem KI-System. Ich entwerfe, das System
setzt um, ich nehme ab. Das ist kein Werkzeugtrick, sondern eine Umstellung, die etwas
kostet — und der Preis liegt woanders, als ich erwartet hatte.

## Was sich verschiebt

Moderne Modelle erzeugen mühelos Ergebnisse, die *richtig aussehen*. Das ist praktisch und
zugleich das Problem: **Der Aufwand wandert vom Erzeugen zum Abnehmen.** Wer das Tempo
mitnimmt und beim Prüfen bleibt wie vorher, sammelt schnell viel Ungeprüftes an.

Die Konsequenz, bei der ich gelandet bin:

> Jede Etappe endet an einem Gate, das maschinell feststellt, ob das Ergebnis trägt.
> Plausibilität genügt nicht.

Ein Gate ist dabei wörtlich gemeint: eine Schranke. Öffnet sie sich nicht, geht es nicht
weiter. Ein Gate, das nur berichtet, ist keins.

## Woher das kommt

Nicht aus der Informatik, sondern aus einem missglückten Versuch mit Sprache.

Die erste Fassung des [meaning-layer](projekte.md#meaning-layer) prüfte sich selbst, indem
sie altgriechische Modelle ins Deutsche zurückübersetzte und mit dem Original verglich.
Das funktionierte — und war die Falle. Mit der Zeit optimierte das Verfahren auf die
Oberfläche der Rückübersetzung statt auf die Bedeutung dahinter. Das Mass war zum Ziel
geworden und taugte damit nicht mehr als Mass.

Das ist Goodharts Gesetz, und für KI-Systeme ist der Effekt gut dokumentiert: Optimierung
auf ein unvollkommenes Mass verbessert die tatsächliche Leistung nur bis zu einem Punkt,
danach verschlechtert sie sie.

## Sechs Prinzipien

Aus dieser und ein paar anderen Erfahrungen ist ein Diskussionspapier entstanden,
**«Verifikationsgetriebene AI-Workflows»** (Juli 2026, rund 6 500 Wörter, extern
begutachtet). Die Prinzipien darin:

1. **Gate-Kette statt Vertrauenskette** — jede Etappe endet an einer maschinellen Schranke.
2. **Skripte statt Chat-Schleifen** — was wiederholbar sein soll, wird Code.
3. **Verfahrenstreue im Lauf** — das Verfahren ist versioniert und wird nicht unterwegs
   angepasst.
4. **Adversariale Prüfung als Standard** — der Prüfer sucht den Fehler, nicht die
   Bestätigung.
5. **Zurechnung und Spur** — jedes Artefakt weiss, woraus es entstanden ist.
6. **Messen, was wirklich trägt** — Ablations-Messung statt Etiketten.

Dazu ein Katalog von siebzehn Gates. Das Papier schicke ich auf Anfrage.

## Drei Sachen, die schiefgingen

### Der grüne Prüfbericht

Der erste Rotationslauf von [lingdeem-node](projekte.md#lingdeem-node) meldete 852
erfolgreiche Anfragen und null Fehler. Er prüfte nur lesend, während drei tote Knoten in
der Konfiguration standen und kein Quorum mehr bestand. Ein Prüfer, der nur liest, gibt
genau in diesem Fall falsche Entwarnung.

### Zwei Stellen mit demselben blinden Fleck

Ein Teilprozess, der nie gestartet war, stand zwölf Minuten als «läuft» in der Anzeige.
Zählweg und Oberfläche hatten dieselbe Lücke; die Nachfrage alle fünf Sekunden bestätigte
den Fehler, statt ihn auszuräumen. Gefunden hat das nicht mein Nachdenken, sondern eine
Beispieldatei — und die musste sich dabei selbst korrigieren, weil sie zuerst so aussah,
wie ich mir die Wirklichkeit vorstellte.

### Das Mass, das nicht angepasst wurde

Eine Selbstmessung wies für einen Tag «0 von 10 Korrektur-Commits» aus, obwohl der Tag fast
nur aus Korrekturen bestand — kein Commit-Titel passte auf den Suchausdruck. Die Versuchung
war, den Suchausdruck zu weiten, bis die Zahl stimmt. Das wäre genau der Fehler von oben
gewesen.

## Was das für Organisationen hiesse

Dazu habe ich eine Meinung, aber keine Erfahrung aus dem Team:

- Die KI entscheidet nicht über Geltung. Sie extrahiert, schlägt vor, prüft — ob etwas gilt,
  entscheidet der Mensch, und zwar eng und protokolliert, nicht als breite Aufsichtspflicht.
- Der Betrieb solcher Verfahren wäre eher eine eigene Rolle als eine Nebenaufgabe.
- Der Engpass ist dann nicht die Technik, sondern das menschliche Urteil.

## Wo es nicht weitergeht

Meine ganze Erfahrung stammt aus **Ein-Personen-Praxis mit voller Werkzeugfreiheit**. Wie
sich das in ein arbeitsteiliges Team mit bestehenden Prozessen übersetzt, weiss ich nicht —
das steht auch so im Papier, unter «Was wir nicht wissen».

Die Frage, die mich deshalb interessiert, ist weniger, welche Werkzeuge jemand einsetzt,
als: **Wie schneidet man Arbeit zu, wenn ein Teil des Erzeugens wegfällt und dafür das
Prüfen zur Hauptarbeit wird?**
