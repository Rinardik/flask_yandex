from flask import Flask

app = Flask(__name__)
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def two_params(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результат отбора</title>
                  </head>
                  <body>
                    <h2>Результаты отбора</h2>
                    <div>Претендента на участие в мисии {nickname}</div>
                    <div class="alert alert-success" role="alert">Поздравляем ваш рейтинг после {level} этапа отбора</div>
                    <div>состовляет {rating}</div>
                    <div class="alert alert-warning" role="alert">Желаем удачи</div>
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(debug=True)