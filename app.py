import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

customers = pd.read_csv("loan_customers_dataset.csv")

st.title("Loan Portfolio Risk Dashboard")

st.write(customers.head())

fig, ax = plt.subplots()

sns.countplot(x="default_flag", data=customers, ax=ax)

st.pyplot(fig)

st.subheader("Dataset Shape")
st.write(customers.shape)

st.subheader("Credit Score Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(customers["credit_score"], bins=20)
st.pyplot(fig2)

st.subheader("Future Risk Analysis")

avg_credit = customers["credit_score"].mean()

if avg_credit < 500:
    st.error("High Risk Portfolio")
else:
    st.success("Moderate Risk Portfolio")
