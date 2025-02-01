import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('Proyek Analsis Data :sparkles:')
st.subheader('Diagram Customer berdasarkan City')
orders_customers_df = pd.read_csv("all_data_orders_customers.csv", delimiter=",")
group_df = orders_customers_df.groupby(by="customer_city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
group_df.head()

fig = plt.figure(figsize=(10, 5))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x="customer_city", y="order_id", data=group_df.head(), palette=colors)
plt.title("Diagram Customer berdasarkan City", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()
st.pyplot(fig)


st.subheader('Diagram Customer berdasarkan State')
orders_customers_df = pd.read_csv("all_data_orders_customers.csv", delimiter=",")
group_df = orders_customers_df.groupby(by="customer_state").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
group_df.head()

fig = plt.figure(figsize=(10, 5))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x="customer_state", y="order_id", data=group_df.head(), palette=colors)
plt.title("Diagram Customer berdasarkan State", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()
st.pyplot(fig)
