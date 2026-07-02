from deep_translator import GoogleTranslator

def translate_to_eng(text):
    try:
        return GoogleTranslator(source='auto',target='en').translate(text)
    except:
        return text
    
def translate_to_hindi(text):
    try:
        return GoogleTranslator(source='en',target='hi').translate(text)
    except:
        return text