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

    def get_spalte(self, index: int):
        """
        Gibt eine Spalte am angegebenen Index aus

        Parameter
        -------------
        index:  int
                Index, welche Spalte ausgegeben wird

        Returns
        -------------
        List: Spalte
        """
        return [i[index] for i in self.spielbrett]

    def get_reihe(self, index: int):
        """
        Gibt eine Reihe am angegebenen Index aus

        Parameter
        -------------
        index:  int
                Index, welche Reihe ausgegeben wird

        Returns
        -------------
        List: Reihe
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

    def spielzug_machen(self, team: str, spl: int):
        """
        Macht einen Spielzug --> Setzt in der angegebenen Spalte ein X oder O an die unterste freie Stelle einer Spalte

        Parameter
        -------------
        team:   str
                X oder O
        spl:    int
                Spalte, die vom Spieler per Input ausgewählt wird

        Returns
        -------------
        List: Spielbrett

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
        Überprüft das Spielbrett nach jedem Spielzug auf eine der beiden Gewinnvarianten.
        4 X oder O in einer Reihe (Reihe, Spalte, Diagonale).
        Wenn kein Gewinn eruiert wird, soll keine Ausgabe erfolgen.
        """
        vier_in_einer_reihe_X = [['X', 'X', 'X', 'X']]
        vier_in_einer_reihe_O = [['O', 'O', 'O', 'O']]

        # Reihencheck:
        for i in range(self.hoehe):
            for j in range(self.breite - 3):
                if self.get_reihe(i)[j:j + 4] in vier_in_einer_reihe_X:
                    return "Spieler 1"

                if self.get_reihe(i)[j:j + 4] in vier_in_einer_reihe_O:
                    return "Spieler 2"

        # Spaltencheck:
        for i in range(self.breite):
            for j in range(self.hoehe - 3):
                if self.get_spalte(i)[j:j + 4] in vier_in_einer_reihe_X:
                    return "Spieler 1"

                if self.get_spalte(i)[j:j + 4] in vier_in_einer_reihe_O:
                    return "Spieler 2"

        # Diagonalencheck:
        for i in self.get_diagonale():
            for j, _ in enumerate(i):
                if i[j:j + 4] in vier_in_einer_reihe_X:
                    return "Spieler 1"

                if i[j:j + 4] in vier_in_einer_reihe_O:
                    return "Spieler 2"

        return None

    def spiel_starten(self):
        """
        Startet ein Spiel. Das Spielfeld wird dargestellt, die Spieler werden nacheinander zum Input aufgefordert und
        ihre Spielzüge werden durchgeführt. Nach jeder Durchführung wird auf Gewinn überprüft. Bei Gewinn eines Spielers
        wird abgebrochen.
        """

        while True:

            for i in self.spielbrett:
                print(i)
            if self.check_gewonnen() is not None:
                break

            spl = int(input(f'Spieler 1 – Bitte Spalte von 1 bis {self.breite} auswählen: ')) - 1
            
            if spl > -1 and spl < self.breite:
                self.spielzug_machen('X', spl)
            else:
                print(f'Bitte geben Sie  in der nächsten Runde eine Zahl zwischen 1 und {self.breite} ein!')

            for i in self.spielbrett:
                print(i)
            if self.check_gewonnen() is not None:
                break

            spl = int(input(f'Spieler 2 – Bitte Spalte von 1 bis {self.breite} auswählen: ')) - 1
            
            if spl > -1 and spl < self.breite:
                self.spielzug_machen('O', spl)
            else:
                print(f'Bitte geben Sie  in der nächsten Runde eine Zahl zwischen 1 und {self.breite} ein!')

        print (f'Gratuliere {self.check_gewonnen()}, du hast gewonnen!')

if __name__ == '__main__':
    meinspiel = VierGewinnt(7,7)
    meinspiel.spiel_starten()
