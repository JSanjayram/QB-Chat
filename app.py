from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_audio_url', methods=['POST'])
def get_audio_url():
    data = request.json
    video_url = data.get('video_url')
    
    ydl_opts = {'format': 'bestaudio/best'}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            audio_url = info_dict['url']
            return jsonify({'audio_url': audio_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
