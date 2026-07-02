import re

def classify_doc(ocr_text):
    """
    Classify banking documents Using OCR text.
    Returns the Document type.
    """
    text = ocr_text.lower()

    document_types = {
        "Internet Banking Password Reset Form":[
            'internet banking','onlinesbi','reset profile password',
            'registration form','profile password'
        ],
        "Cheque":[
            'pay','payee','account type','cheque','bearer',
            'ifsc','amount'
        ],
        "Passbook":[
            "passbook",
            "transaction",
            "withdrawal",
            "deposit",
            "opening balance",
            "closing balance"
        ],
        "Bank Statement":[
            "statement",
            "account statement",
            "balance",
            "debit",
            "credit"
        ],
        "ATM Receipt":[
            "atm",
            "cash withdrawal",
            "available balance",
            "transaction successful"
        ],
        "Education Loan Form":[
            "education loan",
            "student loan",
            "course",
            "college",
            "university"
        ],
        "Home Loan Form":[
            "home loan",
            "property",
            "housing loan",
            "emi"
        ],
        "KYC Form":[
            "know your customer",
            "kyc",
            "aadhaar",
            "pan",
            "identity proof"
        ],
        "Credit Card Form":[
            "credit card",
            "cvv",
            "card number",
            "visa",
            "mastercard"
        ],
        "Debit Card Form":[
            "debit card",
            "rupay",
            "visa debit",
            "master debit"
        ]
        }
    for doc_type, keywords in document_types.items():
        for keyword in keywords:
            if keyword in text:
                return doc_type
    return "Unknown Document Type"