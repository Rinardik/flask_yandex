from flask import Flask, render_template

app = Flask(__name__)

@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        title = "Инженерные тренажеры"
        image = "/static/img/engineering.jpg"
    else:
        title = "Научные симуляторы"
        image = "/static/img/science.jpg"

    return render_template('training.html', title=title, image=image)

if __name__ == '__main__':
    app.run(debug=True)