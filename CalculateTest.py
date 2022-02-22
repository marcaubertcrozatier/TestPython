import unittest
import json
from calculate import compute_invoice


class CalculateTest(unittest.TestCase):

    def test_should_calculate_total_for_ES_single_item(self):
        order_string = '{"prices":[10],"quantities":[1],"country":"ES","reduction":"STANDARD"}'
        order_object = json.loads(order_string)
        order_total = round(compute_invoice(order_object), 2)
        print (order_total)
        self.assertEqual(11.90, order_total)


if __name__ == '__main__':
    unittest.main()