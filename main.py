import pandas as pd
from  utils import *
df=read()
exchange(df)
html_downloads(df)
check_coupon(df)
date(df)
high_value_order(df)
avg(df)
drop(df)
delivery_status(df)
save(df)

