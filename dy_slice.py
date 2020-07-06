import os	
from flask import Flask ,render_template , url_for,flash, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['xml'])
upload_dir=os.path.join(app.instance_path, 'uploads')
os.makedirs(upload_dir, exist_ok=True)


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")

@app.route("/home")
def home():
	return render_template

@app.route("/Dynamic_slice")
def Dynamic_slice():
	return render_template('Dynamic_slice.html', title='Dynamic Slice')

@app.route('/upload', methods=['GET', 'POST'])

def upload():
	if request.method=='POST' :
		file=request.files['file']
		if file and allowed_file(file.filename):
			filename=secure_filename(file.filename)
			file.save(os.path.join(upload_dir, filename))
		return render_template('upload.html')
	





