import os
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    #file.filename
    filename='photo.jpg'
    f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)

    return redirect(url_for('uploaded_file', filename=filename))

@app.route('/show/<filename>')
def uploaded_file(filename):
    return render_template('index.html', filename=filename, init=True)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, cache_timeout = 1)


@app.route('/retry', methods=["GET", "POST"])
def retry():
    return render_template('index.html', init=False)
