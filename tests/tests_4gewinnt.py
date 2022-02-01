import unittest

from viergewinnt.game_4gewinnt import Viergewinnt

class vierGewinntTest(unittest.TestCase):

    def setUp(self) -> None:
        self.ViergewinntS = Viergewinnt("ViergewinntS",4,5)
        self.ViergewinntM = Viergewinnt("ViergewinntM",6,7)
        self.ViergewinntL = Viergewinnt("ViergewinntL",8,9)


if __name__ == '__main__':
    unittest.main()
