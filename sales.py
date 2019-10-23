import time
import random
import logging
import os
import boto3
from botocore.exceptions import ClientError
from boto3.exceptions import S3UploadFailedError
from minio import Minio
from minio.error import (ResponseError, InvalidEndpointError, NoSuchBucket)


# "AWS S3 Operation Upload File Method"
def upload_file_aws(aws_file_name, bucket, object_name=None):

    if object_name is None:
        object_name = aws_file_name

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(aws_file_name, bucket, object_name)
    except ClientError as client_error:
        logging.error(client_error)
        return False
    return True


# "Minio S3 Operation Upload File Method"
def upload_file_minio(endpoint, access_key, secret_key, minio_bucket_name, minio_file_name):
    minio_client = Minio(endpoint, access_key, secret_key, secure=False)
    try:
        minio_client.fput_object(minio_bucket_name, minio_file_name, minio_file_name)
        return True
    except ResponseError as err:
        print(err)
        return False

class Salesman:

    def __init__(self, is_manager, employee_id, store_id):
        self.is_manager = is_manager
        self.employee_id = employee_id
        self.store_id = store_id
        self.sales_total = 0

    def write_sales_dict(self, sales_id, sales, item_no, city_name):
        self.sales_total += sales
        if self.is_manager == 1:
            self.sales_total += round(sales * 1 / 10)
        return {"sales_id": sales_id,
                "employee_id": self.employee_id,
                "store_id": self.store_id,
                "sales": self.sales_total,
                "item_no": item_no,
                "city_name": city_name}

    def write_sales(self, sales_id, sales, item_no, city_name):
        self.sales_total += sales
        if self.is_manager == 1:
            self.sales_total += round(sales * 1 / 10)
        return sales_id, self.employee_id, self.store_id, self.sales_total, item_no, city_name

    def write_review_dict(self, review_score, sales_id):
        return {"store_id": str(self.store_id),
                "employee_id": str(self.employee_id),
                "review_score": str(review_score),
                "sales_id": str(sales_id)}

    def write_review(self, review_score, sales_id):
        return self.store_id, self.employee_id, review_score, sales_id


class Store:

    def __init__(self, store_id, store_name):
        self.store_id = store_id
        self.store_name = store_name
        self.store_sales = 0

    def hired_salesman(self, employee_id):
        salesman = Salesman(0, employee_id, self.store_id)
        return salesman

    def hired_manager(self, employee_id):
        manager = Salesman(1, employee_id, self.store_id)
        return manager


class Logging:

    def __init__(self, app_dir, file_extension, random_review):
        self.random_review = random_review
        self.app_dir = app_dir
        self.file_extension = file_extension
        self.file_name_sales = app_dir + 'sales_' + str(round(time.time())) + '.' + file_extension
        self.file_name_review = app_dir + 'review_' + str(round(time.time())) + '.' + file_extension
        self.store_1 = Store(1, random.choice(['Richmond', 'Ealing', 'Barnet', 'Hounslow', 'Merton', 'Westmister']))
        self.store_2 = Store(2, random.choice(['Richmond', 'Ealing', 'Barnet', 'Hounslow', 'Merton', 'Westmister']))
        self.manager_1 = self.store_1.hired_manager(101)
        self.manager_2 = self.store_2.hired_manager(201)
        self.salesman_11 = self.store_1.hired_salesman(102)
        self.salesman_12 = self.store_1.hired_salesman(103)
        self.salesman_21 = self.store_2.hired_salesman(202)
        self.salesman_22 = self.store_2.hired_salesman(203)

    def logging_events(self):
        for _ in range(1):
            f_sales = open(self.file_name_sales, 'w')
            f_review = open(self.file_name_review, 'w')
            for _ in range(1000):
                random_salesman = random.choice([self.salesman_11, self.salesman_12,
                                                 self.salesman_21, self.salesman_22,
                                                 self.manager_2, self.manager_1])
                invoice_id = random.randint(1, 10000000)
                print("insert into sales.sales_detail values ", file=f_sales)
                print(random_salesman.write_sales(invoice_id,
                                                random.randint(1, 40),
                                                random.randint(1, 1000),
                                                random.choice(
                                                    ['Richmond', 'Ealing', 'Barnet', 'Hounslow', 'Merton', 'Westmister']
                                                )), file=f_sales, end=";\n")
                if self.random_review == random.choice([1, 2, 3, 4, 5, 6]):
                    print("insert into sales.review_detail values ", file=f_review)
                    print(random_salesman.write_review(random.randint(1, 10), invoice_id), file=f_review, end=";\n")
            f_sales.close()
            f_review.close()


if __name__ == "__main__":

    # "App related variables.."
    sales_app_dir = "/Users/hsn/Desktop/MyRepos/Sales_Review/output/"
    bucket_name = "salesreviewbucket"
    app_post_dir = "processed/"  # Do not forget to put "/" at the end of the directory
    endpoint = "127.0.0.1:9000"
    endpoint_type = 1  # 0=AWS 1=Minio
    access_key = "HDGURRIIEODNN7"
    secret_key = "jdkjUYRJFNXSQsggseIK7MDENGbPxRf"

    # "Sales and Reviews files are generated"
    try:
        logging_start = Logging(sales_app_dir, 'sql', 1)
        logging_start.logging_events()
    except FileNotFoundError as file_not_found_error:
        print("File Not Found Error occurred. Detailed error is:\n", file_not_found_error)

    if endpoint_type == 0:
        # "AWS S3 upload operation is performed."
        # "Uploaded files are going to move to app_post_dir"
        try:
            for file_name in os.listdir(sales_app_dir):
                if "sales" in file_name or "review" in file_name:
                    os.chdir(sales_app_dir)
                    if upload_file_aws(file_name, bucket_name) is True:
                        os.rename(file_name, app_post_dir + file_name)
        except S3UploadFailedError as s3_upload_failed_error:
            print("S3 Upload Failed Error error with AWS S3:\n ", s3_upload_failed_error)
        except FileNotFoundError as file_not_found_error:
            print("File Not Found Error occurred. Detailed error is:\n", file_not_found_error)
    else:
        # "Minio S3 upload operation is performed."
        # "Uploaded files are going to move to app_post_dir"
        try:
            for file_name in os.listdir(sales_app_dir):
                if "sales" in file_name or "review" in file_name:
                    os.chdir(sales_app_dir)
                    if upload_file_minio(endpoint, access_key, secret_key, bucket_name, file_name) is True:
                        os.rename(file_name, app_post_dir + file_name)
        except InvalidEndpointError as invalid_endpoint_error:
            print("Invalid Endpoint Error for Minio:\n ", invalid_endpoint_error)
        except ResponseError as response_error:
            print("S3 Upload Failed Error error with AWS S3:\n ", response_error)
        except NoSuchBucket as no_such_bucket:
            print ("No Such Bucket Name. Please check bucket name:\n", no_such_bucket)
