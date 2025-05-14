import streamlit as st
from snowflake.cortex import complete

st.title("🤖 Snowflake Cortex")

code = 'complete("claude-3-5-sonnet", "What is Python?")'
st.code(code)

response = complete('claude-3-5-sonnet',"What is Python?")
st.write(response)
