class Salesman:

    def __init__(self, is_manager, e_id, store_id):
        self.is_manager = is_manager
        self.e_id = e_id
        self.store_id = store_id
        self.sales_total = 0

    def sales(self, sales_id, sales, item_no, city_name):
        self.sales_total += sales
        if self.is_manager == 1:
            self.sales_total += round(sales * 1/10)
        return {"sales_id": sales_id,
                "e_id": self.e_id,
                "store_id": self.store_id,
                "sales": sales,
                "item_no": item_no,
                "city_name": city_name}

    def write_review(self, review_score, sales_id):
        return {"store_id": self.store_id,
                "e_id": self.e_id,
                "review_score": review_score,
                "sales_id": sales_id}


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

