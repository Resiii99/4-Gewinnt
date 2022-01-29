"""
Module Docstring
Spieler 1 hat den Spielstein X
Spieler 2 hat den Spielstein O
"""


class VierGewinnt:
    """
    Klasse erstellt ein Spiel 4gewinnt
    """
    def __init__(self, hoehe=6, breite=7):
        self.hoehe = hoehe
        self.breite = breite
        self.spielbrett = [[' ' for x in range(breite)] for i in range(hoehe)]

    def get_spalte(self, index):
        """
        Gibt eine Spalte am angegebenen Index aus

        :param index: Index, welche Spalte ausgegeben wird
        """
        return [i[index] for i in self.spielbrett]

    def get_reihe(self, index):
        """
        Gibt eine Reihe am angegebenen Index aus

        :param index: Index, welche Reihe ausgegeben wird
        """
        return self.spielbrett[index]

    def get_diagonale(self):
        """
        Gibt alle Diagonalen im Spiel aus
        """
        diagonale = []

        for i in range(self.hoehe + self.breite - 1):
            diagonale.append([])
            for j in range(max(i - self.hoehe + 1, 0), min(i + 1, self.hoehe)):
                diagonale[i].append(self.spielbrett[self.hoehe - i + j - 1][j])

        for i in range(self.hoehe + self.breite - 1):
            diagonale.append([])
            for j in range(max(i - self.hoehe + 1, 0), min(i + 1, self.hoehe)):
                diagonale[i].append(self.spielbrett[i - j][j])

        return diagonale