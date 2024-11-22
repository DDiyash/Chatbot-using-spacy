# Chatbot-using-spacy
Problem statement - Generate Key Insights from Long Story  Analyze a long story discussing various topics like career guidance, productivity, and life hacks. Create a solution to extract specific insights (e.g., generate productivity-related insights when prompted).

File structure:
text_preprocessing.ipynb: This file includes lemmatization, NER, etc using spacy. This file is not used by chatbot , it is written just to show the basic functionalities.
long-story.txt: The document containing the text to be processed. The chatbot extracts and processes sections from this file.
chatbot_app.py: The main Python script that runs the chatbot. 
It includes:
Text cleaning and preprocessing.
Regular expressions to extract titles and their corresponding content.
Streamlit-based UI for user interaction.
