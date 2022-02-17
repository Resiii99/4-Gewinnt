import unittest

from viergewinnt.game_4gewinnt import VierGewinnt

class vierGewinntTest(unittest.TestCase):

    def setUp(self) -> None:
        self.ViergewinntS = VierGewinnt(4,5)
        self.ViergewinntM = VierGewinnt(6,7)
        self.ViergewinntL = VierGewinnt(8,9)
        self.ViergewinntQ = VierGewinnt(6,7)
        self.ViergewinntA = VierGewinnt(6, 7)
        self.ViergewinntB = VierGewinnt(6, 7)
        self.ViergewinntC = VierGewinnt(6, 7)
        self.ViergewinntD = VierGewinnt(6, 7)
        self.ViergewinntE = VierGewinnt(6, 7)
        self.ViergewinntF = VierGewinnt(6, 7)
        self.ViergewinntG = VierGewinnt(6, 7)
        self.ViergewinntH = VierGewinnt(6, 7)



### Indexierung des Spielfelds ###

    def test_getspalte(self):
        """
        Überprüft, ob Index der Spaltenbreite mit Parameter übereinstimmt.
        Returns
        --------
        Testergebnis
        """
        erg1spalte = self.ViergewinntS.get_spalte(1)
        self.assertEqual(erg1spalte, [" ", " ", " ", " "])

        erg2spalte = self.ViergewinntM.get_spalte(3)
        self.assertEqual(erg2spalte, [" ", " ", " ", " ", " ", " "])

        erg3spalte = self.ViergewinntL.get_spalte(3)
        self.assertEqual(erg3spalte, [" ", " ", " ", " ", " ", " ", " ", " "])

    def test_getreihe(self):

        erg1reihe = self.ViergewinntS.get_reihe(1)
        self.assertEqual(erg1reihe, [" ", " ", " ", " ", " "])

        erg2reihe = self.ViergewinntM.get_reihe(2)
        self.assertEqual(erg2reihe, [" ", " ", " ", " ", " ", " ", " "])

        erg3reihe = self.ViergewinntL.get_reihe(5)
        self.assertEqual(erg3reihe, [" ", " ", " ", " ", " ", " ", " ", " ", " "])

### Wird der Stein richtig gesetzt ###

    def test_spielzug_machen(self):
        """

        Überprüft ob die Steine richtig gesetzt werden.
        Returns
        --------
        Testergebnis
        
        """
        spielzugA = self.ViergewinntM.spielzug_machen("X", 1)
        ergA = ([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', 'X', ' ', ' ', ' ', ' ', ' ']])

        self.assertEqual(spielzugA, ergA)

        spielzugB = self.ViergewinntM.spielzug_machen("O", 5)
        ergB = ([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', 'X', ' ', ' ', ' ', 'O', ' ']])

        self.assertEqual(spielzugB, ergB)

        spielzugC = self.ViergewinntM.spielzug_machen("X", 5)
        ergC = ([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', 'X', ' '],
                [' ', 'X', ' ', ' ', ' ', 'O', ' ']])

        self.assertEqual(spielzugC, ergC)

        spielzugD = self.ViergewinntM.spielzug_machen("O", 4)
        ergD = ([[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', 'X', ' '],
                [' ', 'X', ' ', ' ', 'O', 'O', ' ']])

        self.assertEqual(spielzugD, ergD)

### Überprüfung ob bereits ein Gewinner vorliegt ###

    def test_check_gewonnen(self):

        ### Sieg in einer Reihe von Spieler mit Stein "O" ###

        self.ViergewinntS.spielzug_machen("O", 0)
        self.ViergewinntS.spielzug_machen("X", 0)
        self.ViergewinntS.spielzug_machen("O", 1)
        self.ViergewinntS.spielzug_machen("X", 1)
        self.ViergewinntS.spielzug_machen("O", 2)
        self.ViergewinntS.spielzug_machen("X", 2)
        self.ViergewinntS.spielzug_machen("O", 3)

        pruefungS = self.ViergewinntS.check_gewonnen()
        self.assertEqual(pruefungS, "Spieler 2")

        ### Sieg in einer Reihe von Spieler mit Stein "X" ###

        self.ViergewinntA.spielzug_machen("X", 0)
        self.ViergewinntA.spielzug_machen("O", 0)
        self.ViergewinntA.spielzug_machen("X", 1)
        self.ViergewinntA.spielzug_machen("O", 1)
        self.ViergewinntA.spielzug_machen("X", 2)
        self.ViergewinntA.spielzug_machen("O", 2)
        self.ViergewinntA.spielzug_machen("X", 3)

        pruefungA = self.ViergewinntA.check_gewonnen()
        self.assertEqual(pruefungA, "Spieler 1")


        ### Sieg in einer Spalte von Spieler mit Stein "O" ###

        self.ViergewinntQ.spielzug_machen("X", 5)
        self.ViergewinntQ.spielzug_machen("O", 4)
        self.ViergewinntQ.spielzug_machen("X", 3)
        self.ViergewinntQ.spielzug_machen("O", 4)
        self.ViergewinntQ.spielzug_machen("X", 2)
        self.ViergewinntQ.spielzug_machen("O", 4)
        self.ViergewinntQ.spielzug_machen("X", 1)
        self.ViergewinntQ.spielzug_machen("O", 4)

        pruefungQ = self.ViergewinntQ.check_gewonnen()
        self.assertEqual(pruefungQ, "Spieler 2")

        ### Sieg in einer Spalte von Spieler mit Stein "X" ###

        self.ViergewinntM.spielzug_machen("X", 4)
        self.ViergewinntM.spielzug_machen("O", 5)
        self.ViergewinntM.spielzug_machen("X", 4)
        self.ViergewinntM.spielzug_machen("O", 3)
        self.ViergewinntM.spielzug_machen("X", 4)
        self.ViergewinntM.spielzug_machen("O", 2)
        self.ViergewinntM.spielzug_machen("X", 4)

        pruefungM = self.ViergewinntM.check_gewonnen()
        self.assertEqual(pruefungM, "Spieler 1")


        ### Kein Gewinner -> Erwartung None ###

        self.ViergewinntB.spielzug_machen("O", 0)
        self.ViergewinntB.spielzug_machen("X", 1)
        self.ViergewinntB.spielzug_machen("O", 2)
        self.ViergewinntB.spielzug_machen("X", 3)

        pruefungB = self.ViergewinntB.check_gewonnen()
        self.assertEqual(pruefungB, None)

        ### Sieg auf Diagonale von Spieler mit Stein X ###

        self.ViergewinntL.spielzug_machen("X", 0)
        self.ViergewinntL.spielzug_machen("O", 1)
        self.ViergewinntL.spielzug_machen("X", 1)
        self.ViergewinntL.spielzug_machen("O", 2)
        self.ViergewinntL.spielzug_machen("O", 2)
        self.ViergewinntL.spielzug_machen("X", 2)
        self.ViergewinntL.spielzug_machen("O", 3)
        self.ViergewinntL.spielzug_machen("O", 3)
        self.ViergewinntL.spielzug_machen("O", 3)
        self.ViergewinntL.spielzug_machen("X", 3)

        pruefungL = self.ViergewinntL.check_gewonnen()
        self.assertEqual(pruefungL, "Spieler 1")

        ### Sieg auf Diagonale von Spieler mit Stein O ###

        self.ViergewinntC.spielzug_machen("X", 1)
        self.ViergewinntC.spielzug_machen("X", 2)
        self.ViergewinntC.spielzug_machen("X", 2)
        self.ViergewinntC.spielzug_machen("X", 3)
        self.ViergewinntC.spielzug_machen("X", 3)
        self.ViergewinntC.spielzug_machen("X", 3)
        self.ViergewinntC.spielzug_machen("O", 0)
        self.ViergewinntC.spielzug_machen("O", 1)
        self.ViergewinntC.spielzug_machen("O", 2)
        self.ViergewinntC.spielzug_machen("O", 3)

        pruefungC = self.ViergewinntC.check_gewonnen()
        self.assertEqual(pruefungC, "Spieler 2")

    def test_check_unentschieden(self):
        self.ViergewinntA.gespielte_Steine = 42
        self.assertEqual(self.ViergewinntA.check_unentschieden(), True)

        self.ViergewinntB.gespielte_Steine = 41
        self.assertEqual(self.ViergewinntB.check_unentschieden(), None)

        self.ViergewinntC.gespielte_Steine = 12
        self.assertEqual(self.ViergewinntC.check_unentschieden(), None)

        self.ViergewinntD.gespielte_Steine = 48
        self.assertEqual(self.ViergewinntD.check_unentschieden(), True)

    #def test_spiel_starten(self):
        #self.ViergewinntA.spiel_starten()

if __name__ == '__main__':
    unittest.main()
