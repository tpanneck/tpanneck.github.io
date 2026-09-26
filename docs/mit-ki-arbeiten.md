# Mit KI arbeiten

<p class="vorspann">Überlegungen aus der Praxis hinter den verlinkten Arbeiten, Stand
September 2026 — samt der Grenze, die diese Praxis hat.</p>

## Die Arbeitsweise

Thorsten Panneck-Conradi entwirft und entscheidet, das KI-System setzt um, er prüft und
nimmt ab. So ist seit Februar 2026 alles entstanden, was unter
[Die Seiten](index.md#die-seiten) verlinkt ist.

## Was sich dabei verschiebt

Der Aufwand wandert vom Erzeugen zum Prüfen. Das klingt harmlos und ist es nicht: Die
Ergebnisse sehen mühelos richtig aus, und eine Sichtprüfung erkennt den Unterschied nicht
zuverlässig. Wer das Tempo mitnimmt und beim Prüfen bleibt wie vorher, sammelt schnell
viel Ungeprüftes an.

Die Konsequenz daraus: Jede Etappe endet an einer maschinellen Prüfung, die entweder
durchlässt oder abbricht. Eine Prüfung, die nur berichtet, nützt nichts — die Meldung geht
unterwegs verloren oder wird gewohnheitsmässig überlesen.

## Drei Beobachtungen

**Eine Prüfung, die nur liest, übersieht ganze Fehlerklassen.** Ein Prüflauf meldete 852
erfolgreiche Anfragen und null Fehler, während drei tote Knoten in der Konfiguration
standen und kein Quorum mehr bestand — Lesen lief ja weiter. Gegenmassnahme: Jede Prüfung
enthält einen Fall, der fehlschlagen *muss*, sonst sagt «grün» nichts.

**Zwei Stellen, die aus derselben Quelle ableiten, prüfen einander nicht.** Eine Anzeige
und ihr Zählweg hatten dieselbe Lücke; häufigeres Nachfragen bestätigte den Fehler, statt
ihn auszuräumen. Gegenmassnahme: Eine Kontrolle braucht eine unabhängige Quelle, sonst ist
sie Dekoration.

**Ein Mass, das zum Ziel wird, taugt nicht mehr als Mass.** Die erste Fassung des
Sprachmodells prüfte sich selbst durch Rückübersetzung ins Deutsche und optimierte mit der
Zeit auf die Oberfläche dieser Rückübersetzung statt auf die Bedeutung. Das ist Goodharts
Gesetz; für KI-Systeme ist der Effekt belegt: Optimierung auf ein unvollkommenes Mass
verbessert die tatsächliche Leistung nur bis zu einem Punkt, danach verschlechtert sie sie.

## Die offene Frage

Die Werkzeugfrage scheint die kleinere zu sein. Die grössere ist, wie man Arbeit
zuschneidet, wenn ein Teil des Erzeugens wegfällt und das Prüfen zur Hauptarbeit wird: Wer
nimmt ab, wie eng ist dieses Urteil gefasst, und ist der Betrieb solcher Verfahren eine
eigene Aufgabe oder etwas nebenher.

Eine belastbare Antwort gibt es hier nicht. Die Praxis hinter diesen Seiten ist
Ein-Personen-Praxis mit voller Werkzeugfreiheit; wie sich das in ein Team mit bestehenden
Prozessen überträgt, ist offen.

Ausführlicher steht das in einem Diskussionspapier von Juli 2026,
«Verifikationsgetriebene AI-Workflows» — sechs Prinzipien und ein Katalog von siebzehn
Prüfschranken, hergeleitet aus Vorfällen aus der eigenen Arbeit. Es ist noch nicht
veröffentlicht.
