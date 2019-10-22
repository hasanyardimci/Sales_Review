import random
import auger
from sales import Salesman
from sales import Store
from sales import Logging

with auger.magic([Salesman]):
    s = Salesman(1, 101, 2)
    s.sales_dict(sales_id=6377275, sales=11392340, item_no=4739021, city_name='London')
    s.sales_csv(sales_id=6377275, sales=11392340, item_no=4739021, city_name='London')
    s.write_review_dict(6, 827764)
    s.write_review_csv(6, 827764)

with auger.magic([Store]):
    st = Store(1, 'London_Store')
    st.hired_manager(101)
    st.hired_salesman(102)

with auger.magic([Logging]):
    lg = Logging("/Users/hsn/Desktop/MyRepos/Sales_Review/output/", 'sql', 1)
    lg.logging_events()
