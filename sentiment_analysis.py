import spacy
from textblob import TextBlob
import pandas as pd

nlp = spacy.load('en_core_web_sm')
df = pd.read_csv('Amazon_product_reviews.csv') # read amazon file
clean_data = df.dropna(subset=['reviews.text']) # remove rows with no review text 

def sentiment(i):
    review = clean_data['reviews.text'][i].lower().strip()

    # Use spaCy for tokenization and filter out stop words
    doc = nlp(review)
    filtered_words = [token.text for token in doc if not token.is_stop]
    filtered_sentence = ' '.join(filtered_words)

    # Use TextBlob for sentiment analysis.
    text_blob = TextBlob(filtered_sentence)

    # Get the sentiment polarity and subjectivity
    sentiment_review = text_blob.sentiment    
    print(f"The sentiment score is {sentiment_review}")

# Get user to select a review then view the review and compare to the sentiment score
while True:
    try:
        i = int(input("Please enter a number from 0 to 28331: "))
    
        # Check if the entered index is within bounds
        if 0 <= i < len(clean_data['reviews.text']):
            print(clean_data['reviews.text'][i])
            sentiment(i)
            break
        else:
            print("Index is out of bounds.")
    except ValueError:
        print("Please enter an integer between 0 and 28331.")


