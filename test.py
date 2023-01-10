import unittest
import main
class ToTest(unittest.TestCase):
    def test_main_do_stuff(self):
        num=10
        getnumber=main.do_stuff(num)
        self.assertEqual(getnumber, 15)
if __name__ == '__main__':
 unittest.main()
