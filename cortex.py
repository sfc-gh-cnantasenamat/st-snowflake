import streamlit as st
from snowflake.snowpark.context import get_active_session

session = get_active_session()

st.title("🤖 Snowflake Cortex")

response = session.sql("SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', 'What is Python?') as RESPONSE;")
st.write(response)
