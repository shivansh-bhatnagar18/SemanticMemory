from textblob import TextBlob

def correct_sentence(sentence):
    blob = TextBlob(sentence)
    corrected_sentence = blob.correct()
    
    return str(corrected_sentence)