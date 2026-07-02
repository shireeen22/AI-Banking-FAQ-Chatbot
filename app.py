import streamlit as st
from rag_chatbot import rag_answer
from feedback import save_feedback
import plotly.express as px
import matplotlib.pyplot as plt
from analytics import get_analysis
from graphan import graph_feed, quest_graph
from translate_lang import translate_to_eng, translate_to_hindi
from img_rag import image_rag
from PIL import Image
from styles import load_css
import tempfile
import os

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="AI Banking FAQ Assistant",
    page_icon="🏦",
    layout="wide"
)
load_css()

# ================= TITLE =================

st.markdown("""
<div style="
padding:25px 10px 20px 10px;
background-color:#F8FAFC;
border-radius:18px;
box-shadow:0px 3px 12px rgba(0,0,0,0.08);
">

<h1 style="
text-align:center;
font-size:48px;
color:#1E3A8A;
font-weight:800;
margin-bottom:5px;
">

🏦 AI Banking FAQ Chatbot

</h1>

<h4 style="
text-align:center;
color:#475569;
font-weight:500;
margin-top:8px;
margin-bottom:0px;
">

AI-Powered Banking FAQ System • GenAI • FAISS • OCR • Multilingual • Image Processing • Customer Support

</h4>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    border:1px solid #E2E8F0;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
    ">
    <h4 style="color:#1E293B;">🤖 Groq Llama 3.3 70B</h4>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    border:1px solid #E2E8F0;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
    ">
    <h4 style="color:#1E293B;">⚡ FAISS Semantic Search</h4>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    border:1px solid #E2E8F0;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
    ">
    <h4 style="color:#1E293B;">📄 OCR Image Analysis</h4>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    border:1px solid #E2E8F0;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
    ">
    <h4 style="color:#1E293B;">🌍 Hindi + English Support</h4>
    </div>
    """, unsafe_allow_html=True)
#***************************************************************

st.divider()

c1,c2,c3 = st.columns(3)

stats = get_analysis()

with c1:
    st.metric(
        "💬 Total Conversations",
        stats["Total queries"]
    )

with c2:
    st.metric(
        "👍 Helpful Feedback",
        stats["Helpful Feedbacks"]
    )

with c3:
    st.metric(
        "📚 Knowledge Base",
        "1000+ FAQs"
    )

st.divider()

# ================= SESSION STATE =================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = ""

if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""

# ================= SIDEBAR =================

language = st.sidebar.selectbox("Select your Language🔠🕉️",["English","Hindi"])

with st.sidebar:

    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.last_question = ""
        st.session_state.last_answer = ""

        st.rerun()

#*******************Usage Guidance****************
st.sidebar.divider()
guide_title = "ऐप का उपयोग कैसे करें🤔" if language=="Hindi" else "How To use this app🤔"
with st.sidebar.expander(guide_title,expanded=False):
    if language=="English":
        st.markdown("""
### Welcome👋
This AI-powered banking assistant helps you to find answers to banking-related questions and analyze banking documents using AI.
⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐
                    
### First Select Your preferred language from the side option🌟
- English
- Hindi
                    
### HOW TO USE❓
                    
### 1.Chat Assistant Option💬
                    
1. Type your Question in the given **Ask Bank Question** Box👉🏻
2. Press Enter
3. Wait some seconds....🕑
4. You will Get the AI generated Answer🤗
5. Also Explore the Related FQAs, below your answer.
6. Don't forget to Give your Feedback by press **Helpful👍** or **Not Helpful👎** buttons. 
                    
### 2.Banking Document Analyzer📄

1. Upload Your Banking Document or image in the given **upload image** box👉🏻
2. Click **Analyze Document** Button.
3. Wait 1 to 2 minutes....🕑    
4. The AI will:
- ✅ Detect the document type
- ✅ Extract text (OCR)
- ✅ Provide banking guidance
- ✅ Show related FAQs

✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

### Tips💡
- Only upload bank related image✅
- Ask complete question✅
- After each use, clear the chat by click on the **Clear chat**✅
- Don't click unnecessarily while analyzing or generating answer❌ 
                    
💫Supported images include:
- Passbook🔴
- Cheque🔴
- ATM/Debit cards🔴
- Loan Forms🔴
- ATM receipts🔴
- Banking Forms (KYC, Account Opening, Updation etc.)🔴
                    
## I hope this application will be very helpful & useful for you❤️🤗
                
            Thank you for using AI Banking Assistant❤️""")

    else:
        st.markdown("""
### आपका स्वागत है👋
                    
## यह ai बैंकिंग एप आपकी बैंक से जुड़े प्रश्नों के उत्तर देने और बैंक संबंधित इमेज या दस्तावेज़ों का विश्लेषण करने में मदद करता है। 
⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐
                    
### सबसे पहले साइड ऑप्शन से अपनी पसंदीदा भाषा का चयन करें🌟
- इंग्लिश 
- हिन्दी 
                    
### केसे उपयोग करें🤔
                    
### 1.चेट सहायक विकल्प💬
                    
1. दिए गए **अपना बैंक प्रशन पूछें** बॉक्स में अपना सवाल टाइप करें।  
2. enter दबाएं
3. कुछ सेकंड इंतज़ार करें🕑
4. आपको एआई से जेनरेट किया गया जवाब मिल जाएगा।  
5. साथ ही अपने जवाब के नीचे दिये गये सम्बंधित faq भी देख सकते हैं। 
6. अपना फीडबैक देना ना भूलें **उपयोगी लगा👍** या **उपयोगी नहीं लगा👎** बटन दबाकर। 
                    
### 2. बैंकिंग दस्तावेज़ विश्लेषक📄

1. दिये गये **बैंकिंग छवि अपलोड करें** बॉक्स में अपना बैंकिंग डाक्यूमेंट्स या इमेज अपलोड करे।                     
2. Analysis बटन पर क्लिक करें  
3. लगभग 1 से 2 मिनट का इंतज़ार करें🕑
4. ai आपके........ 
                    
- ⭐ डाक्यमेन्ट या इमेज का पता लगाएगा
- ⭐ टेक्स्ट निकलेगा 
- ⭐ बैंकिंग guidence देगा 
- ⭐ संबंधित faqs दिखाएगा
                

✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
                    
### सुझाव💫💡                                        

- केवल बैंक से संबंधित इमेज और दस्तावेज ही अपलोड करें। ✅
- साफ़ और स्पष्ट फोटो अपलोड करें।✅
- प्रश्न हमेशा पूरा पूछे , अधूरे प्रश्न पूछने से ग़लत उत्तर देने की सम्भावना है। ✅  
- प्रतिक्रिया मिलने के बाद साइड में दिखाए गए **क्लीअर चेट** बटन पर क्लिक करके चैट्स clear जरूर करें। ✅ 
- हर प्रश्न का उत्तर मिलने के बाद अपना कीमती फीडबैक अवश्य प्रदान करें। ✅
- जवाब या प्रतिक्रिया बनते समय बिना वजह इधर उधर क्लिक ना करें। ❌
- बैंक से संबंधित दस्तावेज के अलावा और किसी भी प्रकार की इमेज या दस्तावेज अपलोड ना करें। ❌    

⭐समर्थक इमेज या दस्तावेज.... 
                    
- पासबुक🔴
- एटीएम/ डेबिट कार्ड्स 🔴
- किसी भी प्रकार का लोन फोरम🔴
- चैक 🔴
-  एटीएम रसीद 🔴
- खाता खोलने का फॉर्म 🔴 

## उम्मीद करते हैं की यह एप आपके लिए बहुत मददगार और उपयोगी होगा🤗❤️✨

        AI Banking Assistant का उपयोग करने के लिए धन्यवाद! ❤️""")


#============================================================================
# Analytics...
#*******************************************************************************
with st.sidebar:
    st.header("Analytics📉")
    stats = get_analysis()  # function calling...

    st.metric(
        "Total queries", stats["Total queries"]
    )

    st.metric(
        "Helpful Feedbacks", stats["Helpful Feedbacks"]
    )

    st.metric(
        "Not Helpful Feedbacks", stats["Not helpful Feedbacks"]
    )
    #****************Feedbacks Visualization**********************
    st.divider()
    st.subheader("Feedback analysis📉")
    try:
        feedback_count = graph_feed()
        #*********Using pie chart*********
        fig = px.pie(values=feedback_count.values,
                     names=feedback_count.index,
                     title="Feedback Analysis📉")
        st.plotly_chart(fig,width="stretch")
    except:
        st.warning("No feedback data available!☹️❌")

    #************Top asked question Analysis*********
    st.divider()
    st.subheader("Most asked Questions analysis❓")
    try:
        question_count = quest_graph()
        #**********Using Bar plot***********
        fig = px.bar(x=question_count.values,
                     y=question_count.index,
                     orientation="h",
                     title="Most asked Questions❓")
        st.plotly_chart(fig,width="stretch")
    except:
        st.warning("No Top questions available yet!❌☹️")


#========================================================================================
#*********************************************************************************       
# ================= DISPLAY CHAT HISTORY =================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ================= USER INPUT =================

# taking user query...
placeholder = ("अपना बैंक प्रशन पूछें❓" if language=="Hindi" else "Ask Bank Question❓")
query = st.chat_input(placeholder)

#**************Image input*****************
st.divider()
imag_head = "बैंकिंग छवि अपलोड करें📸" if language=="Hindi" else "Upload Banking Image📸"
st.subheader(imag_head)

inp_img = "क्रपया बैंकिंग से जुड़ी इमेज यहाँ अपलोड करें📸👇👇" if language=="Hindi" else "Upload a banking image here📸👇👇"
upload_image = st.file_uploader(inp_img,type=["png","jpg","jpeg"])
if upload_image is not None:
    image = Image.open(upload_image)
    st.image(image,caption='Uploaded Image',width="stretch")
    anal_button = "बैंकिंग दस्तावेज़ का विश्लेषण करें🔍" if language=="Hindi" else "Analyze Banking Document🔍"
    if st.button(anal_button):
        with tempfile.NamedTemporaryFile(delete=False,suffix=".png") as tmp:
            tmp.write(upload_image.getvalue())
            temp_path = tmp.name
        spinn_msg = "डॉक्युमेंट्स विश्लेषण हो रहा है....क्रपया 1 से 2 minute इंतज़ार करें😊" if language=="Hindi" else "Analyzing document...Please!Wait for 1-2 min😊"
        with st.spinner(spinn_msg):
            result = image_rag(temp_path)    
        os.remove(temp_path)
        succ_msg = "विश्लेषण पूरा हुआ🟢😃" if language=="Hindi" else "Analysis completed🟢😃"
        st.success(succ_msg)
        
        #******************DOCUMENT TYPE***********************
        doctype_msg = "दस्तावेज़ का प्रकार📄" if language=="Hindi" else "Document Type📄"
        st.subheader(doctype_msg)
        doc_type = result["document_type"]
        if language=="Hindi":
            doc_type = translate_to_hindi(doc_type)
        st.info(doc_type)
        
        #***********************OCR TEXT***********************
        st.subheader("OCR Text✏️")
        st.text_area(
            "",
            result["ocr_text"],
            height=200
        )
        #**********************AI EXPLANATION********************
        st.subheader("AI Explanation🤖✏️")
        img_answer = result["answer"]
        if language=="Hindi":
            img_answer = translate_to_hindi(img_answer) # Translating answer in Hindi....
        st.success(img_answer)
        
        #************************RELATED FAQS*************************
        msg_faqs = "अकसर पूछे जाने वाले संबंधित प्रशन📚" if language=="Hindi" else "Related FAQs📚"
        st.subheader(msg_faqs)
        for faq in result["sources"]:
            faq_questions = faq["Question"]
            if language=="Hindi":
                faq_questions = translate_to_hindi(faq_questions)
            with st.expander(faq_questions):
                category = faq["Category"]
                if language=="Hindi":
                    category = translate_to_hindi(category)
                st.write("**Category:**", category)
                st.write(
                    "**Similarity:**",
                    f"{faq['Similarity']}%"
                )
                faq_answers = faq["Answer"]
                if language=="Hindi":
                    faq_answers = translate_to_hindi(faq_answers)
                st.write(faq_answers)


#Checking lang..and translate...
if language == "Hindi":
    user_query = translate_to_eng(query)
else:
    user_query = query


# ================= NEW QUESTION =================

if user_query:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_query)

    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })
    #=============================================
    # *************Generate answer***************
    #============================================
    spinner_text = "सोच रहा हूँ..." if language=="Hindi" else "Thinking..."
    with st.spinner(spinner_text):

        result = rag_answer(user_query)

    answer = result["answer"]
    sources = result["sources"]

    #**********Translation**************
    if language == "Hindi":
        answer = translate_to_hindi(answer)

    # Save latest Q&A
    st.session_state.last_question = user_query
    st.session_state.last_answer = answer

    # Show assistant message
    with st.chat_message("assistant"):

        st.markdown(answer)

        st.divider()

        if language == 'Hindi':
            st.subheader("उपयोग किए गए स्त्रोत📚")
        else:
            st.subheader("Sources used📚")

        for source in sources:
            source_question = source["Question"]
            if language == "Hindi":
                source_question = translate_to_hindi(source_question)
            with st.expander(
                f"🔍 {source_question}"
            ):

                st.write(
                    f"**Category:** {source['Category']}"
                )

                st.write(
                    f"**Similarity:** {source['Similarity']}%"
                )
                source_answer = source["Answer"]
                if language == "Hindi":
                    source_answer = translate_to_hindi(source_answer)
                st.write(
                    f"**Answer:** {source_answer}"
                )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# ================= FEEDBACK SECTION =================

if st.session_state.last_answer != "":

    st.divider()

    st.subheader("💬 Was this answer helpful?")

    col1, col2 = st.columns(2)

    with col1:
        feed_butt = "ऊपयोगी लगा👍😃" if language=="Hindi" else "Helpful👍😃"
        if st.button(
            feed_butt,
            key="helpful_btn"
        ):

            save_feedback(
                st.session_state.last_question,
                st.session_state.last_answer,
                "Helpful"
            )
            good_feed = "प्रतिक्रिया देने के लिए आपका धन्यवाद❤️" if language=="Hindi" else "Thank you for your Feedback❤️"
            st.success(good_feed)

    with col2:
        feed_button = "उपयोगी नहीं लगा☹️👎" if language=="Hindi" else "Not Helpful☹️👎"
        if st.button(feed_button,
            key="not_helpful_btn"
        ):

            save_feedback(
                st.session_state.last_question,
                st.session_state.last_answer,
                "Not Helpful"
            )
            bad_feed = "प्रतिक्रिया रिकार्ड कर ली गई है☹️" if language=="Hindi" else "Feedback Recorded☹️"
            st.success(bad_feed)
    
st.divider()

st.markdown("""
<div style='text-align:center;
color:#94A3B8;
padding:20px;'>

Making Banking Simpler🩷| Empowering Smarter Banking with Secure & Instant Support © 2026❤️

Groq • FAISS • Sentence Transformers • EasyOCR • Streamlit

<br><br>

✏️Shireen Khan❤️

</div>
""", unsafe_allow_html=True)