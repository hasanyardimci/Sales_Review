import sales
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
            Store(1, 'London_Store').hired_salesman(employee_id=102),
            sales.Salesman
        )

    def test_sales_csv(self):
        self.assertEqual(
            Salesman(1, 101, 2).sales_csv(sales_id=6377275, sales=12531574, item_no=4739021, city_name='London'),
            (6377275, 101, 2, 12531574, 4739021, 'London')
        )

    def test_sales_dict(self):
        self.assertEqual(
            Salesman(1, 101, 2).sales_dict(sales_id=6377275, sales=12531574, item_no=4739021, city_name='London'),
            {'sales_id': 6377275, 'employee_id': 101, 'store_id': 2, 'sales': 12531574, 'item_no': 4739021, 'city_name': 'London'}
        )

    def test_write_review_csv(self):
        self.assertEqual(
            Salesman(1, 101, 2).write_review_csv(review_score=6, sales_id=827764),
            (2, 101, 6, 827764)
        )

    def test_write_review_dict(self):
        self.assertEqual(
            Salesman(1, 101, 2).write_review_dict(review_score=6, sales_id=827764),
            {'store_id': '2', 'employee_id': '101', 'review_score': '6', 'sales_id': '827764'}
        )


if __name__ == "__main__":
    unittest.main()
