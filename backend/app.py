from flask import Flask, request, jsonify, send_file, make_response
import os
from gtts import gTTS
from pydub import AudioSegment
from backend.utils import split_text

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Conversor texto para fala"

@app.route('/convert', methods=['POST'])  # Renomeado a rota para consistência
def convert_text_to_audio():  # Renomeado a função
    if request.method == 'POST':
        text = request.form['texto']  # Mantido 'texto' para corresponder ao HTML
        print(f'Received text: {text}')  # Usar logging em produção

        try:
            text_chunks = split_text(text)  # Renomeado
            audio_files = []

            for i, chunk in enumerate(text_chunks):
                tts = gTTS(text=chunk, lang='pt')
                filename = f"part_{i}.mp3"
                tts.save(filename)
                audio_files.append(filename)

            full_audio = AudioSegment.empty()
            for audio_file in audio_files:
                audio_segment = AudioSegment.from_mp3(audio_file)
                full_audio += audio_segment
                os.remove(audio_file)

            final_audio_file = "final_audio.mp3"
            full_audio.export(final_audio_file, format="mp3")

            return send_file(final_audio_file, mimetype='audio/mpeg', as_attachment=True, download_name='audio_completo.mp3')

        except Exception as e:
            print(f"Error during conversion: {e}")  # Usar logging
            return make_response(jsonify({'error': 'Failed to convert text to audio'}), 500)  # Padronizar resposta JSON

    return make_response(jsonify({'error': 'Method not allowed'}), 405)  # Usar make_response para consistência

if __name__ == '__main__':
    app.run(debug=True)