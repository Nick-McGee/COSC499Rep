import unittest

testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Crate a function that returns a list of only even integers

# Prints and Returns a list of only odd integers
def getOdds(nums):
    odds = list()

    for num in nums:
        if(num % 2 == 1):
            odds.append(num)
    
    print(odds)
    return odds

class TestEvenOddMethods(unittest.TestCase):
    def test_odds(self):
        self.assertEqual(getOdds(testList), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()