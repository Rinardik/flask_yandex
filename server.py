from flask import Flask, render_template_string, url_for, request, redirect
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/galery')
def index():
    default_images = ['img/mars1.jpg',
        'img/mars2.jpg',
        'img/mars3.jpg']
    uploaded_files = [f'uploads/{f}' for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images = default_images + uploaded_files
    return render_template_string(open('gal.html').read(), images=images)

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('photo')
        if file and file.filename != '':
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template_string(open('ins.html').read(), image_url=url_for('static', filename='css/style.css')[:-len('style.css')] + 'img/placeholder.jpg')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')