import streamlit as st

st.title("❄️ Using Snowflake on Streamlit Community Cloud")

# Connect to Snowflake
conn = st.connection("snowflake")

# Create tabs
tabs = st.tabs(["🔤 Access database", "🤖 Use Cortex"])

# Code block for expander
code_0 = """
  conn = st.connection("snowflake")
  df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
  df
"""

code_1 = """
  conn = st.connection("snowflake")
  prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
  
  if st.button("Submit", type='primary'):
    response = conn.query(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', '{prompt}') as RESPONSE;")
    response_value = response.loc[0, 'RESPONSE']
    st.markdown(response_value)
"""

# Access Snowflake database
with tabs[0]:
  df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
  df

  with st.expander("Show Code"):
    st.code(code_0)

# Use Snowflake Cortex
with tabs[1]:
  prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
  
  if st.button("Submit", type='primary'):
    response = conn.query(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', '{prompt}') as RESPONSE;")
    response_value = response.loc[0, 'RESPONSE']
    st.markdown(response_value)

  with st.expander("Show Code"):
    st.code(code_1)
