import streamlit as st

st.title("❄️ Using Snowflake on Streamlit Community Cloud")

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
df


prompt = st.text_input('What do you want to know?', placeholder='Ask a question')
if st.button("Submit", type='primary'):
  response = conn.query("SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', f'{prompt}') as RESPONSE;")
  response_value = response.loc[0, 'RESPONSE']
  st.markdown(response_value)
