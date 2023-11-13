import unittest
from math_quiz import randInt, randOp, calculation


class TestMathGame(unittest.TestCase):

    #Test cases for random Integer
    def test_randInt(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = randInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    #Test cases for random Operators
    def test_randOp(self):
        ops = {'+', '-', '*'}
        for _ in range(1000):
            random_operator = randOp()
            self.assertIn(random_operator, ops)
        pass

    #Test cases for Calculation
    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (100, 1, '+', '5 + 2', 101),
                (100, 1, '-', '6 - 2', 99),
                (100, 1, '*', '5 * 2', 100),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                with self.subTest(num1=num1, num2=num2, operator=operator, expected_problem=expected_problem,
                    expected_answer=expected_answer):
                    res = calculation(num1, num2, operator)
                    if operator in ['+', '-', '*']:
                        self.assertEqual(res, (expected_problem, expected_answer),
                                        f"Expected: {expected_problem} = {expected_answer}, Got: {res[0]} = {res[1]}")
                    else:
                        self.fail(f"Unsupported operator: {operator} in {expected_problem}")
                pass

if __name__ == "__main__":
    unittest.main()

