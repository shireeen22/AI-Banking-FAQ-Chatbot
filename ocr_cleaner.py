import re

def clean_ocrtext(text):
    """
    Clean OCR Text.
    """
    text = re.sub(r"\s+", " ", text)

    replacemets = {
        "OnlineSBI": "Online SBI",
        "FOROFEICE": "FOR OFFICE",
        "OFEICE": "OFFICE",
        "Applicants": "Applicant",
        "Alc": "A/C",
        "No(s).": "Number",
        "No(s)": "Number",
        "Pass Book": "Passbook",
        "email Address": "Email Address",
        "Telephone No": "Telephone Number",
        "SIGNATURE ERIFIED": "SIGNATURE VERIFIED",
        "१४|": "14",
        "११": "11",
        "१३": "13",
    }

    for wrong, correct in replacemets.items():
        text = text.replace(wrong,correct)
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[|]{2,}", "|", text) # Remove repeated punctuation..
        text = re.sub(r"\.{2,}", ".", text) # Remove multiple dots
        text = re.sub(r",{2,}", ",", text) # Remove multiple commas

    return text.strip()
