import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
import os
import pyttsx3

def extract_audio(video_path, audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

def speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return text

def translate_text(text, target_language='hi'): 
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
def generate_voiceover(text, language='hi', gender='female'):
    engine = pyttsx3.init()
    if gender == 'female':
        engine.setProperty('voice', 'english_female')  # Change this to a male voice in your language
    else:
        engine.setProperty('voice', 'english_male')  # Change this to a female voice in your language
    
    engine.save_to_file(text, 'temp_audiop.mp3')
    engine.runAndWait()

def create_translated_video(video_path, translated_text, output_path):
    video_clip = mp.VideoFileClip(video_path)
    txt_clip = mp.TextClip(translated_text, fontsize=24, color='white', bg_color='black')
    txt_clip = txt_clip.set_pos('bottom').set_duration(video_clip.duration)
    video_clip = mp.CompositeVideoClip([video_clip, txt_clip])
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()

def main():
    video_path = r'C:\Users\DELL\OneDrive\Desktop\translate\Prannay Roy 1.mp4'
    audio_path = r'C:\Users\DELL\OneDrive\Desktop\translate\temp_audiop.wav'
    output_path = r'C:\Users\DELL\OneDrive\Desktop\translate\output_videop.mp4'

    extract_audio(video_path, audio_path)
    text = speech_to_text(audio_path)
    translated_text = translate_text(text)
    generate_voiceover(translated_text, language='hi', gender='female')

    create_translated_video(video_path, translated_text, output_path)

    # Optional: Clean up temporary files
    os.remove(audio_path)
    os.remove('temp_audiop.wav')

if __name__=="__main__":
    main()
