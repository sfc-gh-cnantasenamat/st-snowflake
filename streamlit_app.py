import streamlit as st

conn = st.connection("my_example_connection")
df = conn.query("SELECT * FROM customer_reviews")
df

st.title('🎈 App Name')

