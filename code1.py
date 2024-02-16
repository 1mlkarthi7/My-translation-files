import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
 
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
 
def translate_text(text, target_language='hi'):  # Change 'hi' to the desired language code
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
 
def generate_voiceover(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    return tts
 
def create_translated_video(video_path, translated_text, output_path):
    video_clip = mp.VideoFileClip(video_path)
    txt_clip = mp.TextClip(translated_text, fontsize=24, color='white', bg_color='black')
    txt_clip = txt_clip.set_pos('bottom').set_duration(video_clip.duration)
    video_clip = mp.CompositeVideoClip([video_clip, txt_clip])
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
def main():
    video_path = r'C:\Users\DELL\OneDrive\Desktop\translate\english_speaking.mp4'
    audio_path = r'C:\Users\DELL\OneDrive\Desktop\translate\Eng_hin.wav'
    output_path = r'C:\Users\DELL\OneDrive\Desktop\translate\Eng_hin.mp4'
    voiceover_path = 'Eng_hin.mp3'
 
    extract_audio(video_path, audio_path)
    text = speech_to_text(audio_path)
    translated_text = translate_text(text)
    voiceover = generate_voiceover(translated_text, language='hi')  # Change 'hi' to the desired language code
    voiceover.save(voiceover_path)
 
    # Combine video and voiceover using moviepy
    video_clip = mp.VideoFileClip(video_path)
    voiceover_clip = mp.AudioFileClip(voiceover_path)
    video_clip = video_clip.set_audio(voiceover_clip)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video_clip.close()
    voiceover_clip.close()
 
    # Optional: Clean up temporary files
    os.remove(audio_path)
    os.remove(voiceover_path)
 
if __name__ == "__main__":
    main()
