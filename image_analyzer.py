import easyocr

#***********Load OCR model**************
reader = easyocr.Reader(['en','hi'],gpu=False) # image reader...

#****************Function for text extract****************
def extract_text(image_path):
    '''
    Extract text from Hindi  and English Banking images.
    '''

    results = reader.readtext(image_path)
    extracted_text = []

    for (_, text, confidence) in results:
        extracted_text.append(text)

    return " ".join(extracted_text)