from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = { 'webp', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def processImage(filename,operation):
    print(f"the operation is {operation} and the file is {filename}")   
    pass

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/edit" , methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get('operation')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            processImage(filename,operation)
            return render_template("index.html")
    return render_template("index.html")



app.run(debug=True, port=3000)