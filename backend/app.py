from flask import Flask, request, render_template
import librosa
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# The main functions i foresee
# - handle file/audio upload -- done
# - audio processing to return wave form
# - image manipulation to superimpose wave form
# - file download/ audiogram export

ALLOWED_EXTENSIONS = {'mp3', 'wav'}
UPLOAD_FOLDER = "C:/Users/Bluechip/audiogram_app/backend/file_db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part found'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file, please select one'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print(f"{UPLOAD_FOLDER}")
        # file.save(UPLOAD_FOLDER)
        return 'File uploaded successfully'

    return 'File type not allowed'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/process', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Load the uploaded audio file using librosa
        audio_data, sample_rate = librosa.load(file)
        # Process the audio data (e.g., extract waveform)
        # Perform additional processing as needed
        return 'Audio processed successfully'

if __name__ == "__main__":
    app.run(debug=True)
