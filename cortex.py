# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# session = get_active_session()

# st.title("🤖 Snowflake Cortex")

# response = session.sql("SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', 'What is Python?') as RESPONSE;")
# st.write(response)

#####
import streamlit as st

st.title('🎈 App Name')

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM avalanche_db.public.customer_reviews;")
df

response = conn.query("SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', 'What is Python?') as RESPONSE;")
st.write(response[0])
