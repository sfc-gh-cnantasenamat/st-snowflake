import streamlit as st

st.title("❄️ Using Snowflake on Streamlit Community Cloud")

tabs = st.tabs(["🔤 Access database", "🤖 Use Cortex"])

code_0 = """
  conn = st.connection("snowflake")
  df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
  df
"""

code_1 = """
  prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
  
  if st.button("Submit", type='primary'):
    response = conn.query(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', '{prompt}') as RESPONSE;")
    response_value = response.loc[0, 'RESPONSE']
    st.markdown(response_value)
"""

with tabs[0]:
  st.code(code_0)
  
  conn = st.connection("snowflake")
  df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
  df

with tabs[1]:
  st.code(code_1)
  
  prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
  
  if st.button("Submit", type='primary'):
    response = conn.query(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', '{prompt}') as RESPONSE;")
    response_value = response.loc[0, 'RESPONSE']
    st.markdown(response_value)
