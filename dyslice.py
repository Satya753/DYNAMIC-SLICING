import os	
from flask import Flask ,render_template , url_for,flash, redirect,request
from werkzeug.utils import secure_filename
from algo import Algorithm
app = Flask(__name__)
UPLOAD_FOLDER = '/home/satya/Documents'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['xml'])
slice=Algorithm()


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route("/input", methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			slice.generate_graph(file)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return render_template('input.html')                      
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)
@app.route("/result", methods=['GET','POST'])
def slicingc():
	if request.method=='POST':
<<<<<<< HEAD
		a=(request.form['inp'])
		slice.change_to_numbering(a)
=======
		a=int(request.form['inp'])
		slice.dfs(a)
>>>>>>> a1fe116de1e6b132b06315a1393b47d76bcdecee
		res=[]
		res=slice.print_result()	
		slice.make_empty()
	return render_template('input.html',res=res)

if __name__ == "__main__":
    app.run(debug = True)