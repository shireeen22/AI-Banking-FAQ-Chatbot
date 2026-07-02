from groq import Groq
from dotenv import load_dotenv
import os
from image_analyzer import extract_text
from faiss_search import get_answer
from document_classifier import classify_doc
from ocr_cleaner import clean_ocrtext
import streamlit as st




chatbot = Groq(api_key=st.secrets["GROQ_API_KEY"])

def image_rag(image_path):
    #*******Text extract*********
    ocr_text = extract_text(image_path)

    # clean the text....
    ocr_text = clean_ocrtext(ocr_text)

    # find the type of document...
    document_type = classify_doc(ocr_text)
    
    #*********If text is blank*********
    if ocr_text.strip() == "":
        return {
            "ocr_text" : "",
            "answer": "Sorry I could not find any text in the given image☹️",
            "sources": []
        }
    
    #**********Retrieve faqs*******
    retrieval = get_answer(ocr_text)
    top_matches = retrieval["Top Matches"]

    context = ""

    for faq in top_matches:

        context += f"""
Question: {faq["Question"]}
Answer: {faq["Answer"]}
"""
    #**********Prompt****************
    prompt = f"""
You are an AI banking assistant.

The uploaded image has been classified as:

Document Type:
{document_type}

OCR Text:
{ocr_text}

Relevant Banking FAQs:
{context}

Your Tasks are:
1. Explain what this document is.
2. Explain its purpose.
3. List important fields visible in the document.
4. Explain what the customer should do.
5. Mention precautions.
6. Suggest related banking services.

Keep the response professional, concise and easy to understand.
"""
    
    response = chatbot.chat.completions.create(model="llama-3.3-70b-versatile",
                                               messages=[
            {
                "role": "system",
                "content": "You are an expert banking assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2)
    answer = response.choices[0].message.content
    return {
        "document_type": document_type,
        "ocr_text": ocr_text,
        "answer": answer,
        "sources": top_matches
    }