import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* ---------------- Main App ---------------- */

    .stApp{

    background:#FFFFFF !important;

    color:#111827 !important;

    }

    /* ---------------- Sidebar ---------------- */

    section[data-testid="stSidebar"]{

    background:#F8FAFC !important;

    border-right:1px solid #D1D5DB;

    }

    section[data-testid="stSidebar"] *{

    color:#111827 !important;

    }

    /* ---------------- Headings ---------------- */

    h1,h2,h3,h4,h5,h6{

    color:#111827 !important;

    }

    p,label,span,li{

    color:#374151 !important;
    }



    /* ---------------- Buttons ---------------- */

    .stButton > button{

    background:#2563EB !important;

    color:white !important;

    border:none;

    border-radius:10px;

    }

    /* ---------------- Chat Messages ---------------- */

    [data-testid="stChatMessage"]{
        background:#FFFFFF !important;
        border:1px solid #E5E7EB;
        border-radius:12px;
        padding:15px;
        margin-bottom:10px;
    }

    /* ---------------- Chat Input ---------------- */

    [data-testid="stChatInput"]{

    background:#FFFFFF !important;

    border:1px solid #CBD5E1;

    }

    /* ---------------- Text Inputs ---------------- */

    textarea,
    input{

    background:#FFFFFF !important;

    color:#111827 !important;

    border:1px solid #CBD5E1 !important;

    }

    /* ---------------- Selectbox ---------------- */

    .stSelectbox div[data-baseweb="select"]{
        background:white !important;
        color:#111827 !important;
    }

    /* ---------------- File Uploader ---------------- */

    [data-testid="stFileUploader"]{
        background:white;
        border:2px dashed #2563EB;
        border-radius:12px;
    }

    [data-testid="stFileUploader"] *{
        color:#111827 !important;
    }

    /* ---------------- Metrics ---------------- */

    [data-testid="metric-container"]{

    background:#FFFFFF !important;

    border:1px solid #E5E7EB;

    border-radius:12px;

    }

    /* ---------------- Expander ---------------- */

    details{
        background:white;
        border:1px solid #E5E7EB;
        border-radius:10px;
    }

    details *{
        color:#111827 !important;
    }

    /* ---------------- Success ---------------- */

    [data-testid="stSuccess"]{

    background:#DCFCE7 !important;

    }

    [data-testid="stInfo"]{

    background:#DBEAFE !important;

    }

    /* ---------------- Info ---------------- */

    [data-testid="stSuccess"]{

    background:#DCFCE7 !important;

    }

    [data-testid="stInfo"]{

    background:#DBEAFE !important;

    }

    /* ---------------- Warning ---------------- */

    [data-testid="stWarning"]{
        border-radius:10px;
    }

    </style>
    """, unsafe_allow_html=True)

