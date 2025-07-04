# Data_dashboard_Q-A
Using Open source tool to Integrate data with (Year ,Quarter, Month and day ) insights and analytics dashboards and data visualization with q&a AI models


# Smart CSV Dashboard with AI-Powered Q&A

This project is developed as the app allows users to **upload CSV files**, **visualize time-based insights**, and **interact with the data through natural language questions** using a **locally deployed LLM (FLAN-T5)**.

---

## 🔍 Features

✅ Upload any structured CSV file  
✅ Auto-detect and parse date columns  
✅ Extract time-based features: **Year**, **Quarter**, **Month**, **Day**  
✅ Generate interactive **line charts** using Plotly  
✅ Ask questions about trends using **AI-powered text generation**  
✅ Lightweight and runs offline using **open-source FLAN-T5 model**

---

## 🧠 Tech Stack

| Component        | Tool/Library                    |
|------------------|---------------------------------|
| Language         | Python                          |
| Framework        | Streamlit                       |
| Visualization    | Plotly                          |
| AI/LLM           | HuggingFace Transformers (FLAN-T5) |
| Embeddings       | SentenceTransformers            |

---

## 📁 Project Structure

SmartCSV_QA/
│
├── app.py # Streamlit app code
├── requirements.txt # Python dependencies
├── README.md # Project overview and usage
├── report.pdf # Short report for submission
├── sample_csv/ # Sample CSVs for testing
│ └── sample_sales.csv
├── screenshots/ # Output screenshots
│ └── dashboard_output.png


---

## 🚀 How to Run Locally

### ✅ Step 1: Install Dependencies
### ✅ Step 2: Launch the App
    ```bash
    pip install -r requirements.txt

### ✅ Step 3: Interact with the App
    ```bash
    streamlit run app.py


