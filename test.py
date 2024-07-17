from rulesheet import load_ruler_from_csv
import unittest


class TestExample(unittest.TestCase):
    def test_example(self):
        ruler = load_ruler_from_csv("./example.csv")

        self.assertTrue(ruler.test({"year": 2023}))
        self.assertTrue(ruler.test({"id": "ABC12345"}))
        self.assertTrue(ruler.test({"version": 150}))


if __name__ == "__main__":
    unittest.main()
