# 4-Gewinnt

Im Spiel "4 gewinnt" wird auf einem senkrecht stehenden und hohlen Spielbrett gespielt, in das Steine der beiden Mitspieler fallen gelassen werden. Das Spielbrett besteht aus 7 Spalten und 6 Reihen. Abwechselnd werfen die Mitspieler ihre Steine in die Spalten des Spielbretts, wo diese den jeweils untersten freien Platz einnehmen. Ziel des Spiels ist es, 4 Steine der eigenen Spielfarbe als erstes in einer waagrechten, senkrechten oder diagonalen Linie anzuordnen. 

In unserer programmierten Variante des Spiels gibt es die Möglichkeit gegen einen anderen Spieler, oder gegen den Computer zu spielen.
Bei zwei Personen spielen die Spieler (Spieler 1 und Spieler 2) gegeneinander, indem sie nacheinander dazu aufgefordert werden, per Input eine Spaltennummer anzugeben.
Spielt man gegen den Computer, startet Spieler 1 (= Mensch) mit der Wahl der Spaltennummer, und der automatisierte Spielzug des Computers folgt danach. Die Spaltennummer ist jene senkrechte Reihe des Spielbretts, in die ihr "Spielstein" (Spieler 1: X, Spieler 2 bzw. Computer: O) eingeworfen wird.

Beim Versuch eines ungültigen Spielzugs wird das Recht auf einen Spielzug verwirkt und der andere Spieler ist wieder an der Reihe. 

Nach jedem Spielzug wird automatisch überprüft, ob es einen Gewinner oder ein Unentschieden gibt. Wenn ja, wird das Spiel beendet und eine Mitteilung eingeblendet. 
Wenn es noch keinen Gewinner gibt, wird das neue Spielfeld nach dem letzten Einwurf eingeblendet und der andere Spieler wird zum nächsten Spielzug aufgefordert. Sollte das Spielfeld mit Steinen gefüllt sein, ohne 4 in einer Reihe zu haben, gibt es ein Unentschieden und das Spiel wird beendet.
