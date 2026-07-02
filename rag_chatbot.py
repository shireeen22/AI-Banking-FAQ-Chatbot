from groq import Groq
from dotenv import load_dotenv
from faiss_search import get_answer
import os
import streamlit as st
load_dotenv()

api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

chatbot = Groq(api_key=api_key)

def rag_answer(user_query):
    retrival_result = get_answer(user_query)
    top_matches = retrival_result["Top Matches"]
    
    # Build context
    context = ""

    for faq in top_matches:
        context += f"""
        Question: {faq['Question']}
        Answer: {faq['Answer']}"""
        
    # Prompt
    prompt = f"""
    You are an intelligent banking customer support assistant.

    Use the FAQ context below to answer the user's question.

    If the exact answer is not available, use the most relevant information from the context and provide a helpful response.

    Do NOT invent banking policies, interest rates, or eligibility criteria that are not mentioned in the context.
    Context:
    {context}

    User Question:
    {user_query}

    Provide a professional and concise answer."""

    response = chatbot.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a helpful banking assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )


    answer = response.choices[0].message.content
    return{
        "answer": answer,
        "sources": top_matches
    }
