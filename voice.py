import nltk
from nltk.chat.util import Chat, reflections
import speech_recognition as sr
from gtts import gTTS
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define a simple NLTK chat
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'How can I help you?']],
    ['how are you', ['I am a chatbot, so I don\'t have feelings, but thanks for asking!']],
    ['Who are you?', ['I am karthika assistent, how can i help you?']],
    ['what is your name', ['My name is angelsquad!']],
]

chatbot = Chat(pairs, reflections)

# Speech Recognition setup
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print("You: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand your audio.")
            return ""

# Function to speak using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")

# Main loop
while True:
    user_input = recognize_speech()
    
    if 'exit' in user_input:
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot.respond(user_input)
    
    if not response:
        # If the NLTK chat does not have a response, use TF-IDF cosine similarity
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([user_input] + [pair[0] for pair in pairs])
        similarity = cosine_similarity(vectors[0], vectors[1:])
        index = similarity.argmax()
        response = pairs[index - 1][1][0]
    
    print("Chatbot:", response)
    speak(response)