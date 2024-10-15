import youtube_dl
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from google.cloud import texttospeech


def download_video(url):
    ydl_opts = {'format': 'best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    return ydl.prepare_filename(url)


def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        return text
    except sr.UnknownValueError:
        return "Não foi possível transcrever a fala"
    

def summarize_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('portuguese'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    summary = ' '.join(filtered_tokens[:50])
    return summary


def read_summary(summary):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=summary)
    voice = texttospeech.VoiceSelectionParams(
        language_code='pt-BR',
        name='pt-BR-Wavenet-A'
    )
    config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=config
    )
    return response.audio_content


def main():
    url = input("Digite a URL do vídeo de YouTube: ")
    video_file = download_video(url)
    audio_file = f"{video_file}.wav"
    text = transcribe_audio(audio_file)
    summary = summarize_text(text)
    audio_content = read_summary(summary)
    with open("summary.mp3", "wb") as f:
        f.write(audio_content)
    print("Resumo gerado com sucesso!")

if __name__ == "__main__":
    main()
