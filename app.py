from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = './files'  # Ensure this path is correct

@app.route('/')
def index():
    files = [(file, os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], file)))
             for file in os.listdir(app.config['UPLOAD_FOLDER'])]
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'NetskopeMQ123!':  # Set your upload password here
            file = request.files['file']
            if file:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                return redirect(url_for('index'))
        else:
            flash('Invalid password')
    return render_template('upload.html')

@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')