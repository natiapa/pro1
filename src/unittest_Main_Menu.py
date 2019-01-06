import unittest
import Main_Menu

class TestStringMethods(unittest.TestCase):
    
    def test_isPositive(self):
        average=3
        self.assertEqual(Main_Menu.isPositive(average), True, 'isPositive returned False, True expected')
    def test_isBudget(self):
        budget=999
        self.assertEqual(Main_Menu.isBudget(budget), False, 'isBudget returned False, True expected')

if __name__ == '__main__':
    unittest.main()
