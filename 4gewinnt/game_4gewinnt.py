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


    def spielzug_machen(self, team, spl):
        """
        Macht einen Spielzug --> Setzt in der angegebenen Spalte ein X oder O an die unterste freie Stelle einer Spalte
        :param team: X oder O
        :param spl: Spalte, die vom Spieler per Input ausgewählt wird
        """

        if ' ' not in self.get_spalte(spl):
            return self.spielbrett
        i = self.hoehe - 1
        while self.spielbrett[i][spl] != ' ':
            i -= 1
        self.spielbrett[i][spl] = team
        return self.spielbrett

    def check_gewonnen(self):
        """
        Überprüft das Spielbrett nach jedem Spielzug auf eine der beiden Gewinnvarianten. 4 X oder O in einer Reihe (Reihe, Spalte, Diagonale)
        """
        vier_in_einer_reihe = [['X', 'X', 'X', 'X'], ['O', 'O', 'O', 'O']]

        # Reihencheck:
        for i in range(self.hoehe):
            for j in range(self.breite - 3):
                if self.get_reihe(i)[j:j + 4] in vier_in_einer_reihe:
                    return self.spielbrett[i][j]

        # Spaltencheck:
        for i in range(self.breite):
            for j in range(self.hoehe - 3):
                if self.get_spalte(i)[j:j + 4] in vier_in_einer_reihe:
                    return self.spielbrett[j][i]

        #Diagonalencheck:
        for i in self.get_diagonale():
            for j, _ in enumerate(i):
                if i[j:j + 4] in vier_in_einer_reihe:
                    return i[j]

        return None