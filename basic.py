import streamlit as st

st.title('🎈 App Name')

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
df
