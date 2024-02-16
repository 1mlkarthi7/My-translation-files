import streamlit as st
import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spacy
 
# Load a pre-trained word embedding model (e.g., spaCy's en_core_web_md)
import en_core_web_sm

nlp = en_core_web_sm.load()
# nlp = spacy.load("en_core_web_md")
 
# Function to extract audio from video
def extract_audio(video_path, audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()
 
# Function to convert speech to text
def speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return text
 
# Function to translate text
def translate_text(text, target_language='te'):  # Change 'hi' to the desired language code
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
#Again translated telugu to english text
def translate_text2(translated_text, target_language1='en'):  # Change 'hi' to the desired language code
    translator2 = Translator()
    translated_text2 = translator2.translate(translated_text, dest=target_language1)
    return translated_text2.text

 
# Function to generate voiceover
def generate_voiceover(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    return tts
# Function to calculate cosine similarity
def calculate_cosine_similarity(original_text, translated_text2):
    original_embedding = nlp(original_text).vector
    translated_embedding = nlp(translated_text2).vector
    original_embedding = original_embedding.reshape(1, -1)
    translated_embedding = translated_embedding.reshape(1, -1)
    similarity = cosine_similarity(original_embedding, translated_embedding)[0][0]
    return similarity
# Function to create translated video
def create_translated_video(video_path, translated_language, output_path, voiceover_path):
    extract_audio(video_path, 'temp_audio.wav')
    original_text = speech_to_text('temp_audio.wav')
    translated_text = translate_text(original_text, target_language=translated_language)
    voiceover = generate_voiceover(translated_text, language=translated_language)
    voiceover.save(voiceover_path)
 
    video_clip = mp.VideoFileClip(video_path)
    voiceover_clip = mp.AudioFileClip(voiceover_path)
    video_clip = video_clip.set_audio(voiceover_clip)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    voiceover_clip.close()
 
    similarity = calculate_cosine_similarity(original_text, translated_text)
    return similarity
# Streamlit app
def main():
    st.title("Video Translation App")
 
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4"])
 
    if uploaded_file is not None:
        st.video(uploaded_file)
 
        translated_language = st.selectbox("Select target language", ["te", "hi","bho","ta","ml","kn","gu","mr","bn","sa","as"])  # Add more languages as needed
 
        if st.button("Translate Video"):
            with st.spinner("Translating..."):
                video_bytes = uploaded_file.read()
                video_path = 'temp_video.mp4'
                output_path = 'output_video.mp4'
                voiceover_path = 'temp_voiceover.mp3'
 
                with open(video_path, 'wb') as video_file:
                    video_file.write(video_bytes)
 
                similarity = create_translated_video(video_path, translated_language, output_path, voiceover_path)
 
                st.success(f"Translation complete! Here is the translated video. Similarity: {similarity:.2%}")
                st.write(f"Cosine Similarity: {similarity:.2%}")
                st.video(output_path)
                
# Function to create translated video
def create_translated_video(video_path, translated_language, output_path, voiceover_path):
    extract_audio(video_path, 'temp_audio.wav')
    original_text = speech_to_text('temp_audio.wav')
    translated_text = translate_text(original_text, target_language=translated_language)
    voiceover = generate_voiceover(translated_text, language=translated_language)
    voiceover.save(voiceover_path)
 
    video_clip = mp.VideoFileClip(video_path)
    voiceover_clip = mp.AudioFileClip(voiceover_path)
    video_clip = video_clip.set_audio(voiceover_clip)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    voiceover_clip.close()
 
    similarity = calculate_cosine_similarity(original_text, translated_text)
    return similarity
 
# Streamlit app
def main():
    st.title("Video Translation App")
 
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4"])
 
    if uploaded_file is not None:
        st.video(uploaded_file)
 
        translated_language = st.selectbox("Select target language", ["te", "hi","bho","ta","ml","kn","gu","mr","bn","sa","as"])  # Add more languages as needed
 
        if st.button("Translate Video"):
            with st.spinner("Translating..."):
                video_bytes = uploaded_file.read()
                video_path = 'temp_video.mp4'
                output_path = 'output_video.mp4'
                voiceover_path = 'temp_voiceover.mp3'
 
                with open(video_path, 'wb') as video_file:
                    video_file.write(video_bytes)
 
                similarity = create_translated_video(video_path, translated_language, output_path, voiceover_path)
 
                st.success(f"Translation complete! Here is the translated video. Similarity: {similarity:.2%}")
                st.write(f"Cosine Similarity: {similarity:.2%}")
                st.video(output_path)
 
if __name__ == "__main__":
    main()

 
