import os
import time
from generateEnv import gen_env, gen_city, gen_numbers
from faker.generator import random

# app_dir = "/var/log/Generate/"
app_dir = 'output/'
random_review = 1

## Todo : env_tuple creation will be conditional

env_tuple = gen_env()

Store1Id = env_tuple[0].store_id
Store1Name = env_tuple[0].store_name
Store1Sales = env_tuple[0].store_sales

Store2Id = env_tuple[1].store_id
Store2Name = env_tuple[1].store_name
Store2Sales = env_tuple[1].store_sales

Salesman1Id = env_tuple[2].e_id
Salesman1IsMan = env_tuple[2].is_manager
Salesman1StoreId = env_tuple[2].store_id
Salesman1SalesTotal = env_tuple[2].sales_total

Salesman2Id = env_tuple[3].e_id
Salesman2IsMan = env_tuple[3].is_manager
Salesman2StoreId = env_tuple[3].store_id
Salesman2SalesTotal = env_tuple[3].sales_total

Salesman3Id = env_tuple[4].e_id
Salesman3IsMan = env_tuple[4].is_manager
Salesman3StoreId = env_tuple[4].store_id
Salesman3SalesTotal = env_tuple[4].sales_total

for _ in range(1):
    f_sales = open('sales.txt', 'w')
    f_review = open('review.txt', 'w')
    for _ in range(4000):
        a = random.choice([env_tuple[2], env_tuple[3], env_tuple[4], env_tuple[5], env_tuple[6], env_tuple[7]])
        sales_id = gen_numbers(10000000)
        print(a.sales(sales_id, gen_numbers(100), gen_numbers(1000), gen_city()), file=f_sales)
        if random_review == random.choice([1, 2, 3, 4, 5, 6]):
            print(a.write_review(gen_numbers(10), sales_id), file=f_review)
    file_name_sales = app_dir + 'sales_' + str(round(time.time())) + '.txt'
    os.rename('sales.txt', file_name_sales)
    file_name_review = app_dir + 'review_' + str(round(time.time())) + '.txt'
    os.rename('review.txt', file_name_review)
    f_review.close()
    f_sales.close()
