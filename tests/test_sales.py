import _bootlocale
from codecs import IncrementalEncoder
from mock import patch
from random import Random
import sales
from sales import Logging
from sales import Salesman
from sales import Store
import unittest


class SalesTest(unittest.TestCase):
    def test_hired_manager(self):
        self.assertIsInstance(
            Store(1, 'London_Store').hired_manager(employee_id=101),
            sales.Salesman
        )

    def test_hired_salesman(self):
        self.assertIsInstance(
            Store(1, 'London_Store').hired_salesman(employee_id=103),
            sales.Salesman
        )

    @patch.object(_bootlocale, 'getpreferredencoding')
    @patch.object(IncrementalEncoder, '__init__')
    @patch.object(Random, 'randint')
    @patch.object(Random, 'choice')
    def test_logging_events(self, mock_choice, mock_randint, mock___init__, mock_getpreferredencoding):
        mock_choice.return_value = 'Ealing'
        mock_randint.return_value = 3050914
        mock___init__.return_value = None
        mock_getpreferredencoding.return_value = 'UTF-8'
        self.assertEqual(
            Logging("/Users/hsn/Desktop/MyRepos/Sales_Review/output/", 'sql', 1).logging_events(),
            None
        )

    def test_sales_csv(self):
        self.assertEqual(
            Salesman(1, 101, 1).sales_csv(sales_id=2479830, sales=7, item_no=270, city_name='Barnet'),
            (2479830, 101, 1, 8, 270, 'Barnet')
        )

    def test_sales_dict(self):
        self.assertEqual(
            Salesman(1, 101, 2).sales_dict(sales_id=6377275,sales=11392340,item_no=4739021,city_name='London'),
            {'sales_id': 6377275, 'employee_id': 101, 'store_id': 2, 'sales': 12531574, 'item_no': 4739021, 'city_name': 'London'}
        )

    def test_write_review_csv(self):
        self.assertEqual(
            Salesman(1, 101, 1).write_review_csv(review_score=9, sales_id=8802694),
            (1, 101, 9, 8802694)
        )

    def test_write_review_dict(self):
        self.assertEqual(
            Salesman(1, 101, 2).write_review_dict(review_score=6, sales_id=827764),
            {'store_id': '2', 'employee_id': '101', 'review_score': '6', 'sales_id': '827764'}
        )


if __name__ == "__main__":
    unittest.main()
