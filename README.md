# 4-Gewinnt

Im Spiel "4 gewinnt" wird auf einem senkrecht stehenden und hohlen Spielbrett gespielt, in das Steine der beiden Mitspieler fallen gelassen werden. Das Spielbrett besteht aus 7 Spalten und 6 Reihen. Abwechselnd werfen die Mitspieler die Steine mit ihrer Farbe in die Spalten des Spielbretts, wo die Steine den jeweils untersten freien Platz einnehmen. Ziel des Spiels ist es, 4 Steine der eigenen Spielfarbe als erstes in einer waagrechten, senkrechten oder diagonalen Linie anzuordnen. 

In unserer programmierten Variante des Spiels spielen zwei Spieler (Spieler 1 und Spieler 2) gegeneinander, indem sie nacheinander dazu aufgefordert werden, per Input eine Spaltennummer anzugeben. Die Spaltennummer ist jene senkrechte Reihe des Spielbretts, in die ihr "Spielstein" (Spieler 1: X, Spieler 2: O) eingeworfen wird. 

Nach jedem Spielzug wird automatisch überprüft, ob es einen Gewinn gibt. Wenn ja, wird das Spiel beendet und eine Mitteilung eingeblendet. 
Wenn es noch keinen Gewinn gibt, wird das neue Spielfeld nach dem letzten Einwurf eingeblendet und der andere Spieler wird zum nächsten Spielzug aufgefordert. 
