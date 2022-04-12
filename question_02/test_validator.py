import unittest
from validator import valida_cdvpy

TEST_CASES = (
        ["123456",  True],
        ["551234",  True],
        ["",        False],
        ["1235",    False],
        ["12B456",  False],
        ["a23456",  False],
        ["695552",  False], #tecnicaly 55 appears 2 times
        ["027432",  False],
        ["441344",  False],
        ["957213",  True]
        )


class Test_validator(unittest.TestCase):
    def test_validator(self):
        self.assertEqual(valida_cdvpy(test_case[0]), test_case[1])


if __name__ == "__main__":
    for test_case in TEST_CASES:
        unittest.main(exit=False)
