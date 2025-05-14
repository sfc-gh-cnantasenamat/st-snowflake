# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# session = get_active_session()

# st.title("🤖 Snowflake Cortex")

# response = session.sql("SELECT SNOWFLAKE.CORTEX.COMPLETE('claude-3-5-sonnet', 'What is Python?') as RESPONSE;")
# st.write(response)

from snowflake.core import Root
from snowflake.snowpark.context import get_active_session

def embed_service():
    # Initialize Snowflake session and root
    session = get_active_session()
    root = Root(session)

    # Send embed_request request and process response
    response = root.cortex_embed_service.embed("e5-base-v2", ['foo', 'bar'])
    print(response)

if __name__ == "__main__":
    embed_service()
