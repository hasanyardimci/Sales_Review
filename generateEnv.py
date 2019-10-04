from faker import Faker
from sales import Store


fake = Faker()


def gen_city():
    return fake.city()


def gen_numbers(max_value_num):
    return fake.pyint(max_value=max_value_num)


def gen_env():
    store_1 = Store(gen_numbers(10000), gen_city)
    store_2 = Store(gen_numbers(10000), gen_city)
    manager_1 = store_1.hired_manager(gen_numbers(10000))
    manager_2 = store_2.hired_manager(gen_numbers(10000))
    salesman_11 = store_1.hired_salesman(gen_numbers(10000))
    salesman_12 = store_1.hired_salesman(gen_numbers(10000))
    salesman_21 = store_2.hired_salesman(gen_numbers(10000))
    salesman_22 = store_2.hired_salesman(gen_numbers(10000))
    return store_1, store_2, manager_1, manager_2, salesman_11, salesman_12, salesman_21, salesman_22