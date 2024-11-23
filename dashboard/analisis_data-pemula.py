# -*- coding: utf-8 -*-
"""Proyek_Analisis_Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sCFzflNSohzDDI8-XJJqdM60LAcHURM8

<a href="https://colab.research.google.com/github/Mazwan98/dicoding/blob/main/Proyek_Analisis_Data_E_Commerce.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Proyek Analisis Data: E-Commerce Public Dataset
- Nama: **Rendy Prasetya**
- Email: **rendyprasetya45@gmail.com**
- Id Dicoding: **rendypraas**

## Menentukan Pertanyaan Bisnis

- Apa saja Produk terlaris dan tidak?
- Seberapa banyak budget yang dihabiskan customer dalam beberapa bulan terakhir?
- Seiring berjalannya waktu, Bagaimana performa penjualan pada platform E-Commerce ?
- Bagaimana tingkat kepuasan customer terhadap layanan kami?
- Bagaimana profil demografis customer dan apakah ada perbedaan preferensi pembelian di antara mereka?
- Customer terbanyak berdasarkan letak geografis, dimana saja?

## Menyaipkan semua library yang dibutuhkan
"""

pip install unidecode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import urllib.request
import streamlit as st

"""## Data Wrangling

### Gathering Data
"""

customers_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1mNRnzXF4qoGj_LjFF3RdPLLhxso6tjltl6e-sLGdqvw/export?format=csv')
customers_df.head()

geo_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1eOZHB_7AdN-Lhxh7G1onTvATvllmifGKNyIHDC77X9U/export?format=csv')
geo_df.head()

order_items = pd.read_csv('https://docs.google.com/spreadsheets/d/1WVA7m5D0bMBsx73ZZKO8oBywDUBoNvQbzn8XHAqX18A/export?format=csv')
order_items.head()

order_pay = pd.read_csv('https://docs.google.com/spreadsheets/d/16jeOkpVY2ZW-pDoQdLEpNRrOe8hTeyjE9EzY_IyMFEw/export?format=csv')
order_pay.head()

order_rev = pd.read_csv('https://docs.google.com/spreadsheets/d/1MWFoA52Lw80wiAJ4Bs2Vk25jtyqgiQy5s1cPhhNbQqU/export?format=csv')
order_rev.head()

orders_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1frAvA2DJZIYN92_EPKcArdDrNUlNiA2Lg4-X9IQ3GHw/export?format=csv')
orders_df.head()

product_cat = pd.read_csv('https://docs.google.com/spreadsheets/d/1rSoWuwnDSNiUQ3vmktErrbLVHPRXmPQJS8Nlrcj0pOY/export?format=csv')
product_cat.head()

products_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1djCxcInUkmDgd_a-uJ1PMvX-WkHiFuktSAXffvin8Yc/export?format=csv')
products_df.head()

sellers_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1VkK6SMaSyP_Uh8wWX7YAObxUsiALb_e4qKqwq8Z3cz4/export?format=csv')
sellers_df.head()

"""### Assessing Data
*Menilai Data*
"""

print('\n', customers_df.info())
print('\n', geo_df.info())
print('\n', order_items.info())
print('\n', order_pay.info())
print('\n', order_rev.info())
print('\n', orders_df.info())
print('\n', product_cat.info())
print('\n', products_df.info())
print('\n', sellers_df.info())

"""*apakah ada data null pada setiap DataFrame ?*"""

print('\nInfo data null customers:\n', customers_df.isnull().sum())
print('\nInfo data null geolocation:\n', geo_df.isnull().sum())
print('\nInfo data null order items:\n', order_items.isnull().sum())
print('\nInfo data null order payments:\n', order_pay.isnull().sum())
print('\nInfo data null order reviews:\n', order_rev.isnull().sum())
print('\nInfo data null orders:\n', orders_df.isnull().sum())
print('\nInfo data null product category:\n', product_cat.isnull().sum())
print('\nInfo data null products:\n', products_df.isnull().sum())
print('\nInfo data null sellers:\n', sellers_df.isnull().sum())

"""*ada data duplikat pada setiap DataFrame?*"""

print('Info data duplikat customers:', customers_df.duplicated().sum())
print('Info data duplikat geolocation:', geo_df.duplicated().sum())
print('Info data duplikat order items:', order_items.duplicated().sum())
print('Info data duplikat order payments:', order_pay.duplicated().sum())
print('Info data duplikat order reviews:', order_rev.duplicated().sum())
print('Info data duplikat orders:', orders_df.duplicated().sum())
print('Info data duplikat product category:', product_cat.duplicated().sum())
print('Info data duplikat products:', products_df.duplicated().sum())
print('Info data duplikat sellers:', sellers_df.duplicated().sum())

print('\nData describe customers:\n', customers_df.describe(include='all'))
print('\nData describe geolocation:\n', geo_df.describe(include='all'))
print('\nData describe order items:\n', order_items.describe(include='all'))
print('\nData describe order payments:\n', order_pay.describe(include='all'))
print('\nData describe order reviews:\n', order_rev.describe(include='all'))
print('\nData describe orders:\n', orders_df.describe(include='all'))
print('\nData describe product category:\n', product_cat.describe(include='all'))
print('\nData describe products:\n', products_df.describe(include='all'))
print('\nData describe sellers:\n', sellers_df.describe(include='all'))

geo_df.info()

"""### Cleaning Data

Data duplikat tedapat pada Geolocation dataset, oleh karenanya drop duplikat tidak dilakukan. Mungkin pada kolom *'geolocation_city', 'geolocation_state'* value tertinggi adalah **sao paulo (SP)**
"""

order_rev[order_rev.review_comment_title.isna()]

order_rev.review_comment_title.value_counts()

order_rev[order_rev.review_comment_message.isna()]

order_rev.review_comment_message.value_counts()

order_rev.fillna(value="no comment", inplace=True)

orders_df[orders_df.order_approved_at.isna()]

datetime_oi = ["shipping_limit_date"]

for column in datetime_oi:
  order_items[column] = pd.to_datetime(order_items[column])

datetime_or = ["review_creation_date","review_answer_timestamp"]

for column in datetime_or:
  order_rev[column] = pd.to_datetime(order_rev[column])

datetime_oo = ["order_purchase_timestamp","order_approved_at","order_delivered_carrier_date","order_delivered_customer_date","order_estimated_delivery_date"]

for column in datetime_oo:
  orders_df[column] = pd.to_datetime(orders_df[column])

order_items.info()

order_rev.info()

orders_df.info()

"""## Exploratory Data Analysis (EDA)

### Explore **customers_df**
"""

customers_df.sample(5)

customers_df.describe(include='all')

customers_df.customer_id.is_unique

customers_df.customer_id.duplicated

customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)

customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)

order_pay.sample(5)

order_pay.describe(include='all')

order_pay.groupby(by="payment_type").order_id.nunique().sort_values(ascending=False)

orders_df.sample(5)

delivery_time = orders_df["order_delivered_customer_date"] - orders_df["order_delivered_carrier_date"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders_df["delivery_time"] = round(delivery_time/86400)

orders_df.sample(5)

orders_df.delivery_time.hist()

customer_id_in_orders_df = orders_df.customer_id.values

customers_df["status"] = customers_df["customer_id"].apply(lambda x: "Active" if x in customer_id_in_orders_df else "Non Active")

customers_df.sample(5)

customers_df.groupby(by="status").customer_id.count()

"""Merge customers_df & orders_df

Visualization & Explanatory Analysis
"""

cust_orders_df = pd.merge(
    left=customers_df,
    right=orders_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
cust_orders_df.head()

cust_orders_df.groupby(by="customer_city").order_id.nunique().sort_values(ascending=False).head(10)

cust_orders_df.groupby(by="customer_state").order_id.nunique().sort_values(ascending=False).head(10)

cust_orders_df.groupby(by="customer_zip_code_prefix").order_id.nunique().sort_values(ascending=False).head(10)

cust_orders_df.groupby(by="order_status").order_id.nunique().sort_values(ascending=False).head(10)

"""**Merge order_pay & order_rev**"""

order_payrev_df = pd.merge(
    left=order_pay,
    right=order_rev,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
order_payrev_df.head()

order_payrev_df.groupby(by="payment_type").order_id.nunique().sort_values(ascending=False).head(10)

order_payrev_df.sort_values(by="payment_value", ascending=False)

order_payrev_df.groupby(by="payment_type").agg({
    "order_id": "nunique",
    "payment_value":  ["min", "max"]
})

"""#### Merge cust_orders_df & order_payrev"""

customers_df = pd.merge(
    left=cust_orders_df,
    right=order_payrev_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
customers_df.head()

"""### Explore order_items & sellers_df

#### Merge order_items & sellers_df
"""

item_seller_df = pd.merge(
    left=order_items,
    right=sellers_df,
    how="left",
    left_on="seller_id",
    right_on="seller_id"
)
item_seller_df.head()

item_seller_df.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False).head(10)

"""### Explore products_df & product_cat
#### Merge products_df & product_cat
"""

product_df = pd.merge(
    left=products_df,
    right=product_cat,
    how="left",
    left_on="product_category_name",
    right_on="product_category_name"
)
product_df.head()

product_df.groupby(by="product_category_name").product_id.nunique().sort_values(ascending=False).head(10)

product_df.groupby(by="product_category_name_english").product_id.nunique().sort_values(ascending=False).head(10)

"""#### Merge item_seller_df & product_df"""

sellers_df = pd.merge(
    left=product_df,
    right=item_seller_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)
sellers_df.head()

sellers_df.sort_values(by="price", ascending=False)

sellers_df.groupby(by="product_category_name_english").agg({
    "order_id": "nunique",
    "price":  ["min", "max"]
})

"""### Explore geo_df"""

geo_df.sample(5)

def pretty_string(column):
    column_space = ' '.join(column.split())
    return unidecode.unidecode(column_space.lower())

geo_df['geolocation_city'] = geo_df['geolocation_city'].apply(pretty_string)

geo_df.groupby('geolocation_zip_code_prefix').size().sort_values(ascending=False)

geo_df[geo_df['geolocation_zip_code_prefix'] == 24220].head()

"""### Explore All Data
#### Merge all data

Pada kasus ini saya tidak menggabungkan dataset geolocation, karena menurut saya dataset ini tidak begitu diperlukan.
"""

all_data = pd.merge(
    left=customers_df,
    right=sellers_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
all_data.head()

all_data.info()

all_data.groupby(by=["customer_city", "product_category_name_english"]).agg({
    "price": "sum",
    "freight_value": "sum"
})

all_data.groupby(by=["customer_state", "product_category_name_english"]).agg({
    "price": "sum",
    "freight_value": "sum"
})

all_data.groupby(by="customer_state").agg({
    "order_id": "nunique",
    "payment_value": "sum"
}).sort_values(by="payment_value", ascending=False)

all_data.groupby(by="product_category_name_english").agg({
    "order_id": "nunique",
    "review_score":  ["min", "max"]
})

"""### Convert all_data to .csv"""

all_data.to_csv('all_data.csv', index=False)

"""## Visualization & Explanatory Analysis

### Pertanyaan 1 : Produk apa yang paling banyak & sedikit terjual?
"""

sum_order_items_df = all_data.groupby("product_category_name_english")["product_id"].count().reset_index()
sum_order_items_df = sum_order_items_df.rename(columns={"product_id": "products"})
sum_order_items_df = sum_order_items_df.sort_values(by="products", ascending=False)
sum_order_items_df = sum_order_items_df.head(10)

sum_order_items_df.head()

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="products", y="product_category_name_english", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Produk paling banyak terjual", loc="center", fontsize=18)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="products", y="product_category_name_english", data=sum_order_items_df.sort_values(by="products", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Produk paling sedikit terjual", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("Produk paling banyak dan paling sedikit terjual", fontsize=20)
plt.show()

"""> Terlihat pada grafik diatas, Produk yang paling banya terjual adalah bed_bath_table. dan produk yang paling sedikit terjual adalah auto.

### Pertanyaan 2 : Bagaimana performa penjualan platform E-Commerce kami seiring berjalannya waktu?
"""

monthly_df = all_data.resample(rule='M', on='order_approved_at').agg({
    "order_id": "nunique",
})
monthly_df.index = monthly_df.index.strftime('%B') #mengubah format order_approved_at menjadi Tahun-Bulan
monthly_df = monthly_df.reset_index()
monthly_df.rename(columns={
    "order_id": "order_count",
}, inplace=True)
monthly_df.head()

monthly_df = monthly_df.sort_values('order_count').drop_duplicates('order_approved_at', keep='last')

monthly_df.head()

monthly_df.sort_values(by='order_count')

month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

monthly_df["month_numeric"] = monthly_df["order_approved_at"].map(month_mapping)
monthly_df = monthly_df.sort_values("month_numeric")
monthly_df = monthly_df.drop("month_numeric", axis=1)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_df["order_approved_at"],
    monthly_df["order_count"],
    marker='o',
    linewidth=2,
    color="#068DA9"
)
plt.title("Number of Orders per Month (2018)", loc="center", fontsize=20)
plt.xticks(fontsize=10, rotation=25)
plt.yticks(fontsize=10)
plt.show()

"""Terlihat pada grafik diatas bahwa terjadi penurunan signifikan pada bulan September dan mengalami penaikan yang signifikan pada bulan November.

### Pertanyaan 3 : Berapa banyak uang yang dihabiskan customer dalam beberapa bulan terakhir?
"""

monthly_spend_df = all_data.resample(rule='M', on='order_approved_at').agg({
    "payment_value":"sum"
})
monthly_spend_df.index = monthly_spend_df.index.strftime('%B') #mengubah format order_approved_at menjadi Tahun-Bulan
monthly_spend_df = monthly_spend_df.reset_index()
monthly_spend_df.rename(columns={
    "payment_value":"total_spend"
}, inplace=True)
monthly_spend_df.head()

monthly_spend_df = monthly_spend_df.sort_values('total_spend').drop_duplicates('order_approved_at', keep='last')

monthly_spend_df.head()

monthly_spend_df.sort_values(by='total_spend')

monthly_spend_df["month_numeric"] = monthly_spend_df["order_approved_at"].map(month_mapping)
monthly_spend_df = monthly_spend_df.sort_values("month_numeric")
monthly_spend_df = monthly_spend_df.drop("month_numeric", axis=1)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_spend_df["order_approved_at"],
    monthly_spend_df["total_spend"],
    marker='o',
    linewidth=2,
    color="#068DA9"
)
plt.title("Total customer spend money per Month (2018)", loc="center", fontsize=20)
plt.xticks(fontsize=10, rotation=25)
plt.yticks(fontsize=10)
plt.show()

"""Pada grafik diatas, total uang yang dihabiskan paling banyak pada bilang November dan paling sedikit pada bulan September.

### Pertanyaan 4 : Bagaimana tingkat kepuasan customer terhadap layanan kami?
"""

review_scores = all_data['review_score'].value_counts().sort_values(ascending=False)

most_common_score = review_scores.idxmax()

sns.set(style="darkgrid")

plt.figure(figsize=(10, 5))
sns.barplot(x=review_scores.index,
            y=review_scores.values,
            order=review_scores.index,
            palette=["#068DA9" if score == most_common_score else "#D3D3D3" for score in review_scores.index]
            )

plt.title("Rating by customers for service", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(fontsize=12)
plt.show()

"""Pada grafik diatas menunjukan bahwa customer sangat puas dengan layanan yang disediakan, terbukti dengan data bahwa customer yang memberikan rating 5 memiliki data terbanyak daripada rating yang lainnya.

### Pertanyaan 5 : Bagaimana profil demografis customer kami, dan apakah ada perbedaan preferensi pembelian di antara mereka?

#### Berdasarkan customer_state
"""

bystate_df = all_data.groupby(by="customer_state").customer_id.nunique().reset_index()
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
bystate_df.head()

plt.figure(figsize=(12, 6))

most_common_state = bystate_df.loc[bystate_df['customer_count'].idxmax(), 'customer_state']

bystate_df = bystate_df.sort_values(by='customer_count', ascending=False)

sns.barplot(x='customer_state',
            y='customer_count',
            data=bystate_df,
            palette=["#068DA9" if state == most_common_state else "#D3D3D3" for state in bystate_df['customer_state']]
            )

plt.title("Number customers from State", fontsize=15)
plt.xlabel("State")
plt.ylabel("Number Customers")
plt.xticks(fontsize=10)
plt.show()

"""Pada grafik diatas berdasarkan State, SP memiliki data customer terbanyak."""

bycity_df = all_data['customer_city'].value_counts().head(10)

plt.figure(figsize=(12, 6))

most_common_city = bycity_df.idxmax()

bycity_df = bycity_df.sort_values(ascending=False)

sns.barplot(x=bycity_df.index,
            y=bycity_df.values,
            palette=["#068DA9" if city == most_common_city else "#D3D3D3" for city in bycity_df.index]
            )

plt.title("Number of Customers from Each City", fontsize=15)
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45, fontsize=10)
plt.show()

"""Pada grafik diatas berdasarkan City, sao paulo memiliki data customer terbanyak."""

order_status_counts = all_data['order_status'].value_counts()

plt.figure(figsize=(8, 6))
order_status_counts.plot(kind='bar', color='skyblue')
plt.title('Order Status')
plt.xlabel('Status')
plt.ylabel('Number of Orders')
plt.show()

"""Pada grafik diatas status order paling banyak adalah delivered.

### Pertanyaan 6 : Dimana letak geografis yang memiliki customer terbanyak?
"""

other_state_geolocation = geo_df.groupby(['geolocation_zip_code_prefix'])['geolocation_state'].nunique().reset_index(name='count')
other_state_geolocation[other_state_geolocation['count']>= 2].shape
max_state = geo_df.groupby(['geolocation_zip_code_prefix','geolocation_state']).size().reset_index(name='count').drop_duplicates(subset = 'geolocation_zip_code_prefix').drop('count',axis=1)

geolocation_silver = geo_df.groupby(['geolocation_zip_code_prefix','geolocation_city','geolocation_state','geolocation_lat','geolocation_lng']).median(numeric_only=True).reset_index() # Added numeric_only=True to handle non-numeric values
geolocation_silver = geolocation_silver.merge(max_state,on=['geolocation_zip_code_prefix','geolocation_state'],how='inner')

customers_silver = customers_df.merge(geolocation_silver,left_on='customer_zip_code_prefix',right_on='geolocation_zip_code_prefix',how='inner')

customers_silver.head()

customers_silver.to_csv("geolocation.csv", index=False)

def plot_brazil_map(data):
    brazil = mpimg.imread(urllib.request.urlopen('https://i.pinimg.com/originals/3a/0c/e1/3a0ce18b3c842748c255bc0aa445ad41.jpg'),'jpg')
    ax = data.plot(kind="scatter", x="geolocation_lng", y="geolocation_lat", figsize=(10,10), alpha=0.3,s=0.3,c='maroon')
    plt.axis('off')
    plt.imshow(brazil, extent=[-73.98283055, -33.8,-33.75116944,5.4])
    plt.show()

plot_brazil_map(customers_silver.drop_duplicates(subset='customer_unique_id'))

"""Banyak customer yang berasal negara bagian tenggara dan selatan.

## Conclusion

- Produk apa yang paling banyak & sedikit terjual?
> Hasil visualisasi menunjkkan bahwa customer lebih sering membeli produk bed_bath_table, dan paling tidak banyak dibeli adalah produk auto.
- Seiring berjalannya waktu, Bagaimana performa penjualan pada platform E-Commerce ?
> Performa penjualan E-Commerce memiliki kestabilan pada bulan Januari - Mei,penurunan tidak signifikan pada bulan Juni - Juli,penaikan tidak signifikan pada bulan Agustus,dan penurunan sangat signifikan pada bulan September
lalu terjadi penaikan yang sangat signifikan pada bulan Oktober-November dan kembali menurun pada bulan Desember.
- Seberapa banyak bajet yang dihabiskan customer dalam beberapa bulan terakhir?
> Berdasarkan hasil visualisasi yang sudah ditampilkan, sesuai dengan grafik pada pertanyaan ke 2 total uang yang dihabiskan customer pada bulan Januari - Mei stabil terjadi penurunan pada bulan Juni-September, kenaikan signifikan pada bulan Oktober-November, dan kembali menurun pada bulan Desember.
- Bagaimana tingkat kepuasan customer terhadap layanan kami?
> Kepuasan customer terhadap layanan yang diberikan sangatlah memuaskan dikarenakan pada visualisasi yang sudah ditampilkan memperlihatkan bahwa customer yang memberikan rating 5 sangat banyak, dan rating 4 pada urutan ke-2 terbanyak.
- Bagaimana profil demografis customer dan apakah ada perbedaan preferensi pembelian di antara mereka?
> Negara bagian yang memiliki customer terbanyak adalah SP yang artinya Kota yang memiliki customer terbanyak adalah Sao Paulo dan urutan ke-2 adalah RJ (Rio de janeiro) dan status order item customer paling banyak adalah delivered, yang artinya item yang dipesan oleh customer tidak terjadi sebuah kesalahan sehinggan item terkirim dengan sukses ke customer yang ini juga merujuk pada customer memberikan rating 5 pada pelayanan E-Commerce.
- Customer terbanyak berdasarkan letak geografis, dimana saja?> Sesuai dengan grafik yang sudah dibuat, ada lebih banyak customer di bagian tenggara dan selatan. Informasi lainnya, ada lebih banyak customer di kota-kota yang merupakan ibu kota (São Paulo, Rio de Janeiro, Porto Alegre, dan lainnya).
"""
