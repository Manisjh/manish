d = {"name":"kalyani","age":23}
d['phn'] = 46432
print(d)
d['age'] = 23
print(d)
del d['phn']
print(d)
import unittest
from task import Ticket_Pricing

class TestAssignment(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(Ticket_Pricing(5), 10)

    def test_multiple_digits(self):
        self.assertEqual(Ticket_Pricing(25), 20)

    def test_with_zero(self):
        self.assertEqual(Ticket_Pricing(70), 15)

if __name__ == "__main__":
    unittest.main()