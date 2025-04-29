from flask import render_template, Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/distribution')
def distribution():
    astronauts = ['Иванов И.И.', 'Петров П.П.', 'Сидоров С.С.', 'Козлов К.К.']
    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')