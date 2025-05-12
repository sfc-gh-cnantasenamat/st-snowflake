import streamlit as st
import snowflake

st.title('🎈 App Name')

conn = snowflake.connector.connect(
    user=st.secrets['user'],
    password=st.secrets['password'],
    account=st.secrets['account'],
    warehouse=st.secrets['warehouse'],
    database=st.secrets['database'],
    schema=st.secrets['schema']
)

df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews")
df


