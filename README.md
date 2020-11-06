# Bachelorarbeit
Programm zur Bachelorarbeit "Ein adaptives Verfahren für numerische quadratische Programme" an der Philipps-Universität Marburg

## Inhalt
Das Programm besteht aus diesen drei Dateien. 
- Die Datei "Funktionsklasse" beinhaltet die Klasse Funktion, welche dem Programm zur speicherung der quadratischen Funktionen dient.
- Die Datei "CG" beinhaltet den CG-Algorithmus zur Bestimmung der Abstiegsrichtungen, sowie die dazu nötigen Hilfsfunktionen.
- Die Datei "Quasinewton-Verfahren" umfasst den Hauptteil der Software. In ihr ist der Quasinewton-Algorithmus enthalten wie auch alle zusätzlich benötigten Variablen und die Verwaltung der GUI.

## Hinweise
Alle drei Dateien müssen zusammen bleiben, wobei die Datei "Quasinewton-Verfahren" die Datei ist, welche ausgeführt werden muss.

Nach dem Ausführen des Programms öffnet sich die GUI, welche einem ermöglicht die Dimension der Funktion, sowie deren Anzahl festzulegen. Anschließend stehen drei Möglichkeiten zur Verfügung diese Funktionen zu erzeugen. Zuletzt besteht die Möglichkeit eine eigene Toleranzschwelle festzulegen (ohne Eingabe: Tolleranz = 10^-8) und das Optimierungsverfahren zu starten.

Entwickelt und getestet wurde das Programm mit der Entwicklungsumgebung PyCharm von JetBrains. Ausführen der Datei von der Konsole ist jedoch ebenso möglich.
