import pandas as pd
import streamlit as st
import plotly.express as px
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# --- Title & Description ---
st.title("📊 Smart Data Dashboard with Q&A")
st.write("Upload a CSV with a date column. Visualize trends and ask questions about your data using an open-source LLM.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
        
        # --- Detect and Parse Dates ---
    date_columns = df.columns[df.columns.str.contains("date", case=False)].tolist()
    
    if not date_columns:
        st.warning("No obvious date column found. Please select one manually.")
        date_columns = df.columns.tolist()

    selected_date_col = st.sidebar.selectbox("Select the date column:", date_columns)

    try:
        df[selected_date_col] = pd.to_datetime(df[selected_date_col], errors='coerce')  # use 'coerce' to handle bad values
        df = df.dropna(subset=[selected_date_col])  # drop rows where date parsing failed
        df['Year'] = df[selected_date_col].dt.year
        df['Quarter'] = df[selected_date_col].dt.to_period('Q').astype(str)
        df['Month'] = df[selected_date_col].dt.month
        df['Day'] = df[selected_date_col].dt.day
    except Exception as e:
        st.error(f"❌ Failed to parse date: {e}")


    # --- Show Data ---
    st.subheader("Raw Data")
    st.dataframe(df.head())

    # --- Group & Plot ---
    st.subheader("📅 Time-Based Summary")
    time_group = st.selectbox("Group data by", ['Year', 'Quarter', 'Month', 'Day'])

    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    selected_metric = st.selectbox("Choose numeric column to summarize", numeric_columns)

    agg_df = df.groupby(time_group)[selected_metric].sum().reset_index()
    fig = px.line(agg_df, x=time_group, y=selected_metric, markers=True, title=f"{selected_metric} over {time_group}")
    st.plotly_chart(fig)

    # --- Summary for LLM ---
    summary = agg_df.to_string(index=False)

    # --- Q&A Section ---
    st.subheader("💬 Ask Questions about the Data")

    # Load FLAN-T5 model only once
    @st.cache_resource
    def load_llm():
        return pipeline("text2text-generation", model="google/flan-t5-base")

    llm = load_llm()

    user_question = st.text_input("Ask a question (e.g., 'Which year had highest sales?')")

    if user_question:
        prompt = f"Given the data:\n{summary}\n\nAnswer this question:\n{user_question}"
        response = llm(prompt, max_new_tokens=100)[0]['generated_text']
        st.success(f"🤖 Answer: {response}")

else:
    st.warning("Please upload a CSV file to get started.")
