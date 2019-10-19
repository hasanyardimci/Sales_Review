import os
import time
import random


class Salesman:

    def __init__(self, is_manager, e_id, store_id):
        self.is_manager = is_manager
        self.e_id = e_id
        self.store_id = store_id
        self.sales_total = 0

    def sales_dict(self, sales_id, sales, item_no, city_name):
        self.sales_total += sales
        if self.is_manager == 1:
            self.sales_total += round(sales * 1/10)
        return {"sales_id": sales_id,
                "e_id": self.e_id,
                "store_id": self.store_id,
                "sales": sales,
                "item_no": item_no,
                "city_name": city_name}

    def sales_csv(self, sales_id, sales, item_no, city_name):
        self.sales_total += sales
        if self.is_manager == 1:
            self.sales_total += round(sales * 1 / 10)
        return sales_id, self.e_id, self.store_id, sales, item_no, city_name

    def write_review_dict(self, review_score, sales_id):
        return {"store_id": str(self.store_id),
                "e_id": str(self.e_id),
                "review_score": str(review_score),
                "sales_id": str(sales_id)}

    def write_review_csv(self, review_score, sales_id):
        return str(self.store_id), str(self.e_id), str(review_score), str(sales_id)


class Store:

    def __init__(self, store_id, store_name):
        self.store_id = store_id
        self.store_name = store_name
        self.store_sales = 0

    def hired_salesman(self, e_id):
        salesman = Salesman(0, e_id, self.store_id)
        return salesman

    def hired_manager(self, e_id):
        manager = Salesman(1, e_id, self.store_id)
        return manager


class Logging:

    def __init__(self, app_dir, file_extension, random_review):
        self.random_review = random_review
        self.app_dir = app_dir
        self.file_extension = file_extension
        self.file_name_sales = app_dir + 'sales_' + str(round(time.time())) + '.' + file_extension
        self.file_name_review = app_dir + 'review_' + str(round(time.time())) + '.' + file_extension
        self.store_1 = Store(random.randint(1, 10000),
                             random.choice(['Richmond', 'Ealing', 'Barnet', 'Hounslow', 'Merton', 'Westmister']))
        self.store_2 = Store(random.randint(1, 10000),
                             random.choice(['Richmond', 'Ealing', 'Barnet', 'Hounslow', 'Merton', 'Westmister']))
        self.manager_1 = self.store_1.hired_manager(random.randint(1, 10000))
        self.manager_2 = self.store_2.hired_manager(random.randint(1, 10000))
        self.salesman_11 = self.store_1.hired_salesman(random.randint(1, 10000))
        self.salesman_12 = self.store_1.hired_salesman(random.randint(1, 10000))
        self.salesman_21 = self.store_2.hired_salesman(random.randint(1, 10000))
        self.salesman_22 = self.store_2.hired_salesman(random.randint(1, 10000))

    def logging_events(self):
        for _ in range(1):
            f_sales = open(self.file_name_sales, 'w')
            f_review = open(self.file_name_review, 'w')
            for _ in range(10000):
                random_salesman = random.choice([self.salesman_11, self.salesman_12,
                                                 self.salesman_21, self.salesman_22,
                                                 self.manager_2, self.manager_1])
                invoice_id = random.randint(1, 10000000)
                print(random_salesman.sales_csv(invoice_id,
                                                random.randint(1, 10000),
                                                random.randint(1, 10000),
                                                random.choice(
                                                    ['Richmond', 'Ealing', 'Barnet', 'Hounslow', 'Merton', 'Westmister']
                                                             )), file=f_sales)
                if self.random_review == random.choice([1, 2, 3, 4, 5, 6]):
                    print(random_salesman.write_review_csv(
                        random.randint(1, 10),
                        invoice_id), file=f_review)
            f_sales.close()
            f_review.close()


if __name__ == "__main__":
    logging_start = Logging('output/', 'cvs', 1)
    logging_start.logging_events()
