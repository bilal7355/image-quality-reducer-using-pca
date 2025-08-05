from flask import Flask, render_template, request, send_from_directory
import matplotlib.pyplot as plt
import os
import uuid
from image_reducer import reducer

app = Flask(__name__)
UPLOAD_FOLDER = 'static/compressed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded."

        file = request.files['image']
        if file.filename == '':
            return "No file selected."

        quality = int(request.form.get('quality', 50))
        if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            x = plt.imread(file)

            # If alpha channel exists (RGBA), drop it
            if x.shape[-1] == 4:
                x = x[:, :, :3]

            filename = f"{uuid.uuid4().hex}.jpg"
            save_path = os.path.join(UPLOAD_FOLDER, filename)

            reducer(x, quality, save_path)

            return render_template('index.html', download_link=filename)

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
