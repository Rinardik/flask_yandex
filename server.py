from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"

@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" alt="здесь должна была быть картинка, но не нашлась">
                    <b>
                        <div class="alert alert-dark" role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Присоединяйся!
                        </div>
                    </b>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')