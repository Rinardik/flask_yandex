from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Настройка пути для статических файлов
STATIC_FOLDER = 'static'
app.config['STATIC_FOLDER'] = STATIC_FOLDER

@app.route('/')
def index():
    # Список путей к изображениям
    images = [
        'img/mars1.jpg',
        'img/mars2.jpg',
        'img/mars3.jpg'
    ]

    # HTML-шаблон с каруселью
    html_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}" />
        <title>Пейзажи Марса</title>
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="text-center">Пейзажи Марса</h1>
            <div id="marsCarousel" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-indicators">
                    {% for i in range(images|length) %}
                        <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="{{ i }}"
                                {% if i == 0 %}class="active"{% endif %} aria-current="true" aria-label="Slide {{ i + 1 }}"></button>
                    {% endfor %}
                </div>
                <div class="carousel-inner">
                    {% for image in images %}
                        <div class="carousel-item {% if loop.first %}active{% endif %}">
                            <img src="{{ url_for('static', filename=image) }}" class="d-block w-100" alt="Марсианский пейзаж">
                        </div>
                    {% endfor %}
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#marsCarousel" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#marsCarousel" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
                crossorigin="anonymous"></script>
    </body>
    </html>
    '''

    return render_template_string(html_template, images=images)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')