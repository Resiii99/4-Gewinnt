# Tests

Bei den Tests wurden die Methoden unserer Spiel-Klasse **VierGewinnt** geprüft.
Im Ersten Bereich wurde eine korrekte Indexierung des Spielfeldes sowie die Ausgabe der Spalten und Reihen überprüft, zur Überprüfung wurden unterschiedlich große Spielfelder herangezogen.

In weiterer Folge wurde mit der Methode *test_spielzug_machen* kontrolliert, ob eine bestimmte Eingabe den gewünschten Spielzug erzeugt. 

Im dritten Bereich testet unser Code, ob die Gewinner-Ermittlung korrekt funktioniert, dazu wird je ein Sieg in einer Reihe in einer Spalte und in einer Diagonale vom Spieler mit dem Stein X bzw. O simuliert. Auch wird geprüft, ob der Return-Wert korrekt funktioniert, wenn noch kein Gewinner vorliegt.

Der letzte Bereich unseres Testcodes beschäftigt sich mit dem Spielausgang unentschieden. Hier wird mit Hilfe des Parameters *gespielte_Steine* manuell eine Auslastung des Spielfelds vorgegeben und falls zutreffend ein Unentschieden erwartet. 

Die Methode *spiel_starten* wurde nicht getestet da sie lediglich den Spielablauf und den Computergegner abdeckt.
