import pandas as pd
def read():
    df = pd.read_json('C:\\Users\\ariel\kodkod\\tests\DATA-_TEST\orders_simple.json')
    return df


def exchange(df):
    df['shipping_days'] = df['shipping_days'].astype(int)
    df['total_amount'] = df['total_amount'].str.replace('$', " ")
    df['total_amount'] = df['total_amount'].astype(float)
    df['customer_age'] = df['customer_age'].astype(int)
    df['rating'] = df['rating'].astype(float)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['items_html'] = df['items_html'].astype(str)
    return  df.info()

def html_downloads(df):
    df['items_html'] = df['items_html'].str.replace(('<'), '', regex=True)
    df['items_html'] = df['items_html'].str.replace(('>'), '', regex=True)
    df['items_html'] = df['items_html'].str.replace(('/'), '', regex=True)
    return df
def check_coupon(df):
    df['coupon_used'].str.replace(r"!""!", r"no_coupon", regex=True)
    return df
def date(df):
    df['ordr_month'] = df['order_date'].dt.month
    return df

def high_value_order(df):
    mean_amount = df['total_amount'].mean()
    df['high_value_order'] = [True if x > mean_amount else False for x in df['total_amount']]
    df.sort_values(by='total_amount',ascending=False)

def avg(df):
    df['average'] = df.groupby('country')['rating'].transform('mean')
    return df
def drop(df):
    df.drop(df[df['total_amount'] < 1000].index)
    df.drop(df[df['rating'] < 4.5].index)
    return  df
def delivery_status(df):
    df['delivery_status'] = ['delayed' if x > 7 else 'on_time' for x in df['shipping_days']]
    return df

def save(df):
    clean_orders_207827924= df.to_csv('output.csv', index=False)
    return clean_orders_207827924

