import unittest

testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

# Prints and Returns a list of only even integers
def getEvens(nums):
    evens = list()

    for num in nums:
        if(num % 2 == 0):
            evens.append(num)
    
    print(evens)
    return evens


class TestEvenOddMethods(unittest.TestCase):
    def test_evens(self):
        self.assertEqual(getEvens(testList), [2, 4, 6, 8, 10])
        self.assertEqual(getOdds(testList), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()