from flask import Flask, url_for, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/load_photo', methods=['POST', 'GET'])
def form_sample():
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'default.jpg')
    if request.method == 'POST':
        if 'photo' in request.files:
            file = request.files['photo']
            if file.filename != '':
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg'))
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg')
    image_url = url_for('static', filename=f"img/{os.path.basename(image_path)}")
    return f'''<!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <title>Загрузка файла</title>
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="page">Загрузка фотографии</h1>
            <h3 class="page">для участия в миссии</h3>
            <form class="login_form" method="post" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="photo" class="form-label">Приложите фотографию</label>
                    <input type="file" class="form-control" id="photo" name="photo" accept="image/*">
                </div>
                <div class="image-preview">
                    <p class="no-file-text">Файл не выбран</p>
                    <img id="preview-image" src="{image_url}" alt="Загруженное изображение" style="display: none;">
                </div>
                <button type="submit" class="btn btn-primary mt-3">Отправить</button>
            </form>
        </div>

        <!-- JavaScript для предварительного просмотра -->
        <script>
            document.getElementById('photo').addEventListener('change', function(event) {{
                const input = event.target;
                const previewImage = document.getElementById('preview-image');
                const noFileText = document.querySelector('.no-file-text');

                if (input.files && input.files[0]) {{
                    // Создаем объект FileReader
                    const reader = new FileReader();

                    reader.onload = function(e) {{
                        // Отображаем изображение
                        previewImage.src = e.target.result;
                        previewImage.style.display = 'block';
                        noFileText.style.display = 'none';
                    }};

                    // Читаем выбранный файл
                    reader.readAsDataURL(input.files[0]);
                }} else {{
                    previewImage.src = '';
                    previewImage.style.display = 'none';
                    noFileText.style.display = 'block';
                }}
            }});
        </script>
    </body>
    </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')