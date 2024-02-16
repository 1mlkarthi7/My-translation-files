import pyttsx3

def generate_voiceover(text, language='en', gender='male'):
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Set voice
    voices = engine.getProperty('voices')
    # You might need to experiment with voice indices based on your system
    if gender == 'male':
        engine.setProperty('voice', voices[1].id)
    elif gender == 'female':
        engine.setProperty('voice', voices[0].id)

    # Convert text to speech
    engine.say(text)

    # Save to an audio file
    voiceover_path = f'voiceover_{language}_{gender}.mp3'
    engine.save_to_file(text, voiceover_path)

    # Wait for the speech to finish
    engine.runAndWait()

    return voiceover_path

# Example usage
translated_text = "नमस्ते, कैसे हो आप?"
voiceover_path = generate_voiceover(translated_text, language='hi', gender='male')
print(f'Voiceover saved at: {voiceover_path}')
