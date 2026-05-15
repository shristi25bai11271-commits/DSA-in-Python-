import unittest
from array import array
from Bubble_sort import Bubble_sort as sort_function

class TestBubbleSort(unittest.TestCase):

    def test_array(self):
        test_data=array('i',[7, 3, 9, 12, 11])
        result=array('i',[3, 7, 9, 11, 12])
        sort_function(test_data)
        self.assertEqual(test_data, result)
if __name__ == "__main__":
    unittest.main()
