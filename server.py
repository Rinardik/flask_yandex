from flask import Flask, render_template_string

app = Flask(__name__)

planets_info = {
    "Марс": [
        "Эта планета близка к Земле;",
        "На ней много необходимых ресурсов;",
        "На ней есть вода и атмосфера;",
        "На ней есть небольшое магнитное поле;",
        "Наконец, она просто красивая!"
    ],
    "Венера": [
        "Очень горячая планета;",
        "Имеет толстую атмосферу;",
        "Богата углеродом и серой;",
        "Потенциально может быть преобразована;"
    ],
    "Юпитер": [
        "Самая большая планета Солнечной системы;",
        "Имеет множество спутников;",
        "Обладает мощным магнитным полем;",
        "Текущие технологии не позволяют освоить ее;"
    ]
}

html_tem = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Выбор планеты</title>
    <!-- Подключение Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>Мое предложение: {{ planet_name }}</h1>
        {% for info in planet_info %}
            {% set color_classes = ['alert-success', 'alert-warning', 'alert-danger', 'alert-info'] %}
            <div class="alert {{ color_classes[loop.index0 % color_classes|length] }}" role="alert">{{ info }}</div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/choice/<planet_name>')
def choice(planet_name):
    if planet_name in planets_info:
        planet_info = planets_info[planet_name]
        return render_template_string(html_tem, planet_name=planet_name, planet_info=planet_info)
    else:
        return "Планета не найдена", 404

if __name__ == '__main__':
    app.run(debug=True)