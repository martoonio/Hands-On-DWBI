import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('Balaji Fast Food Sales.csv')

st.header("Fast Food Sales Dashboard")
st.subheader("18221011 Farchan Martha Adji Chandra")
st.subheader("Handson Tools")

st.write("The dataset")
st.write(df.head())
st.write("The description of the dataset")
st.write(df.describe())

st.header("Cleaning the dataset")

col1, col2 = st.columns(2)

with col1 :
    st.write("Identified Null Values")
    st.write(df.isnull().sum())
    st.write("There is a column with missing values, which is transaction_type")

with col2 :
    st.write("Drop rows with missing values")
    st.markdown("```df.dropna(inplace=True)```")
    df.dropna(inplace=True)
    st.write("Output :")
    st.write(df.isnull().sum())

st.header("Exploratory Data Analysis")
# Top-selling items
items_sold = df.groupby('item_name')['quantity'].sum().sort_values(ascending=False)
top_items_sold = items_sold

# Most expensive and least expensive items
average_price = df.groupby('item_name')['item_price'].mean()
top_items_price = average_price.sort_values(ascending=False)

# Convert to Plotly Express plots
top_items_sold_fig = px.bar(top_items_sold, x=top_items_sold.index, y=top_items_sold.values,
                            labels={'x': 'Item', 'y': 'Quantity Sold'}, title='Item terlaris')

top_items_price_fig = px.bar(top_items_price, x=top_items_price.index, y=top_items_price.values,
                             labels={'x': 'Item', 'y': 'Average Price'}, title='5 Most Expensive Items')

# Display in Streamlit
cc1, cc2, cc3, cc4 = st.columns(4)
c1, c2= st.columns(2)

st.plotly_chart(top_items_sold_fig)
st.plotly_chart(top_items_price_fig)
with st.expander("View analytics"):
        st.write("Berdasarkan grafik di atas, item yang paling diminati adalah Cold Coffee. Restoran perlu memastikan stok biji kopi yang cukup untuk memenuhi permintaan pelanggan. Sedangkan item yang paling tidak diminati adalah Vadapav meskipun harganya terendah. Restoran perlu mempertimbangkan untuk mengganti menu tersebut dengan menu yang lebih diminati oleh pelanggan atau perlu dilakukan promosi bundling untuk meningkatkan penjualan. Frankie menjadi median dari top selling walaupun harganya menduduki item termahal kedua, sehingga dapat disimpulkan bahwa harga tidak mempengaruhi penjualan.")
