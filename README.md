# 🏦 AI Banking FAQ Assistant

An AI-powered Banking FAQ Assistant built using **Retrieval-Augmented Generation (RAG)** that answers banking-related questions, analyzes banking documents, and supports multilingual interactions.

---

## 🚀 Features

- 💬 AI-powered Banking FAQ Chatbot
- 🔍 Semantic Search using Sentence Transformers
- 📚 FAISS Vector Database for fast retrieval
- 🤖 Groq LLM (Llama 3.3 70B) for answer generation
- 📄 Banking Document Analysis
- 🖼 OCR-based Text Extraction (English + Hindi)
- 🌍 Multilingual Support (English & Hindi)
- 📊 Analytics Dashboard
- 👍 User Feedback System
- 📖 Related FAQs with Similarity Scores
- 📱 Interactive Streamlit UI

---

## 🛠 Technologies Used

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Groq API
- EasyOCR
- Pandas
- Plotly
- Pillow

---

## 📂 Project Structure

```text
app.py
rag_chatbot.py
img_rag.py
image_analyzer.py
faiss_search.py
semantic_search.py
feedback.py
analytics.py
graphan.py
processed_data.csv
bank_faq.index
requirements.txt
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Banking-FAQ-Assistant.git
```

### Move into the project

```bash
cd AI-Banking-FAQ-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add your Groq API Key

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Questions

- How do I open a savings account?
- How can I reset my net banking password?
- How do I apply for a home loan?
- What documents are required for KYC?
- How do I get an education loan?

---

## 📸 Features

### 💬 AI Banking Chatbot

- Answers banking-related questions using RAG.
- Provides source FAQs.

### 📄 Banking Document Analyzer

Upload:

- Passbooks
- Cheques
- Loan Forms
- KYC Documents
- Account Opening Forms
- Bank Notices

The assistant:

- Detects document type
- Extracts text
- Explains the document
- Provides banking guidance
- Suggests related FAQs

---

## 📊 Analytics

- Total Queries
- Helpful Feedback
- Feedback Visualization
- Most Asked Questions

---

## 🌍 Multilingual Support

Supported Languages:

- 🇬🇧 English
- 🇮🇳 Hindi

---

## 📷 Screenshots

_Add screenshots of your application here._

Example:

- Home Page
- Chat Interface
- Document Analysis
- Analytics Dashboard

---

## 🌐 Live Demo

Coming Soon

---

## 👩‍💻 Developed By

**Shireen Khan**

LinkedIn: *(https://www.linkedin.com/in/shireen-khan-b9134a360/)*

GitHub: *(https://github.com/shireeen22)*

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub!
