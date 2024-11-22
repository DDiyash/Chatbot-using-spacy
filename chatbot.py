import spacy
import unicodedata
import re
import streamlit as st

# Preprocess the text
def clean_text(text):
    # Normalize Unicode characters
    text = unicodedata.normalize('NFKC', text)

    # Replace non-breaking or zero-width spaces with regular spaces
    text = text.replace('\u200a', ' ').replace('\u00a0', ' ')

    return text

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Load and clean the text file
with open('long-story.txt', encoding='utf-8') as f:
    text = f.read()

cleaned_text = clean_text(text)
doc = nlp(cleaned_text)

# Define the regular expression to match titles and the content between them
pattern = r"\n\n([A-Z\s]+)\n([^\n]+(?:\n[^\n]+)*)"

# Use findall to capture all title-content pairs
sections = re.findall(pattern, cleaned_text)

# Store the sections in a dictionary
sections_dict = {}

# Iterate through the matches and store the content in a dictionary with titles as keys
for title, content in sections:
    # Clean the title and content by stripping unnecessary newlines
    cleaned_title = title.strip().lower()  # Convert the title to lowercase for case-insensitive matching
    cleaned_content = content.strip()
    sections_dict[cleaned_title] = cleaned_content

# Function to retrieve content based on user input (case-insensitive)
def get_section(user_input):
    # Normalize user input to lowercase for matching
    user_input = user_input.lower()
    
    # Iterate through the keys to find a match
    for key in sections_dict:
        if user_input in key:  # If the user's keyword matches part of the title
            return sections_dict[key]
    
    return "No matching section found."

# Streamlit UI
def chatbot_ui():
    st.title("Text-Based Chatbot")

    # Display instructions
    st.write("Ask the chatbot for specific sections from the document by typing keywords like 'productivity', 'life hacks', 'communication skills', 'skill development', 'personal development', 'goal setting' ")

    # Input field for the user
    user_input = st.text_input("Enter a keyword", "")

    # If the user enters a keyword, get the matching section and display it
    if user_input:
        section_content = get_section(user_input)
        st.write(section_content)

# Run the Streamlit app
if __name__ == "__main__":
    chatbot_ui()
