import unittest

from viergewinnt.game_4gewinnt import VierGewinnt

class vierGewinntTest(unittest.TestCase):

    def setUp(self) -> None:
        self.ViergewinntS = VierGewinnt("ViergewinntS",4,5)
        self.ViergewinntM = VierGewinnt("ViergewinntM",6,7)
        self.ViergewinntL = VierGewinnt("ViergewinntL",8,9)

### Hat das Spielfeld die richtige Größe ###


### Wird der Stein richtig gesetzt ###

    def test_spielzug_machen(self):
        """

        Überprüft ob die Steine richtig gesetzt werden.
        Returns
        --------
        Testergebnis
        
        """
        self.ViergewinntM.spielzug_machen("X",1)
        erg1 = ([[" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                ["", "X ", " ", " ", " ", " ", " "]])

        self.assertEqual(erg1)



### Wird der Sieger korrekt ermittelt ###




if __name__ == '__main__':
    unittest.main()
