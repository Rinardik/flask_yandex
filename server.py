from flask import Flask, request, url_for, redirect, render_template, render_template_string
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import os
import json
import random
from data.db_session import global_init, create_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
CREW_JSON_PATH = os.path.join(app.root_path, 'templates', 'astr.json')
db_path = os.path.join(os.getcwd(), 'db', 'blog.db')
global_init(db_path)

def get_random_crew_member():
    with open(CREW_JSON_PATH, encoding='utf-8') as f:
        crew = json.load(f)
    return random.choice(crew)


class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_kap = StringField('id астронавта', validators=[DataRequired()])
    password_kap = PasswordField('Пароль астронавта', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/member')
def member():
    member_data = get_random_crew_member()
    return render_template('member.html', member=member_data)

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
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/table')
def table():
    gender = request.args.get('gender')
    age_str = request.args.get('age')
    return render_template('training.html', gender=gender, age=int(age_str))

@app.route('/selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
        <html lang="en">
        <html lang="en">
            <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Анкета претендента</title>
            </head>
        <body>
            <div class="container mt-5">
                <h1 class="page">Анкета претендента</h1>
                <h3 class="page">на участие в миссии</h3>
                <form class="login_form" method="post">
                    <div class="mb-3">
                        <input type="password" class="form-control" id="password" placeholder="Введите фамилию" name="password">
                    </div>
                    <div class="mb-3">
                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите имя" name="email">
                    </div>
                    <div class="mb-3">
                        <input type="password" class="form-control" id="password" placeholder="Введите адрес почты" name="password">
                    </div>
                    <div class="mb-3">
                        <label for="education" class="form-label">Какое у Вас образование?</label>
                        <select class="form-select" id="education" name="education" required>
                            <option value="начальное">начальное</option>
                            <option value="среднее">среднее</option>
                            <option value="высшее">высшее</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <p>Какие у Вас есть профессии?</p>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="инженер-исследователь" id="engineer-researcher" name="professions">
                            <label class="form-check-label" for="engineer-researcher">Инженер-исследователь</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="пилот" id="pilot" name="professions">
                            <label class="form-check-label" for="pilot">Пилот</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="строитель" id="builder" name="professions">
                            <label class="form-check-label" for="builder">Строитель</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="экзобиолог" id="exobiologist" name="professions">
                            <label class="form-check-label" for="exobiologist">Экзобиолог</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="врач" id="doctor" name="professions">
                            <label class="form-check-label" for="doctor">Врач</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="инженер по терраформированию" id="terraform-engineer" name="professions">
                            <label class="form-check-label" for="terraform-engineer">Инженер по терраформированию</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="климатолог" id="climatologist" name="professions">
                            <label class="form-check-label" for="climatologist">Климатолог</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="специалист по радиационной защите" id="radiation-specialist" name="professions">
                            <label class="form-check-label" for="radiation-specialist">Специалист по радиационной защите</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="астрогеолог" id="astrogeologist" name="professions">
                            <label class="form-check-label" for="astrogeologist">Астрогеолог</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="гляциолог" id="glaciologist" name="professions">
                            <label class="form-check-label" for="glaciologist">Гляциолог</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="инженер жизнеобеспечения" id="life-support-engineer" name="professions">
                            <label class="form-check-label" for="life-support-engineer">Инженер жизнеобеспечения</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="метеоролог" id="meteorologist" name="professions">
                            <label class="form-check-label" for="meteorologist">Метеоролог</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="оператор марсохода" id="rover-operator" name="professions">
                            <label class="form-check-label" for="rover-operator">Оператор марсохода</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="киберинженер" id="cyber-engineer" name="professions">
                            <label class="form-check-label" for="cyber-engineer">Киберинженер</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="штурман" id="navigator" name="professions">
                            <label class="form-check-label" for="navigator">Штурман</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="пилот дронов" id="drone-pilot" name="professions">
                            <label class="form-check-label" for="drone-pilot">Пилот дронов</label>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="sex" class="form-label">Укажите пол</label>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                            <label class="form-check-label" for="male">
                                Мужской
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                            <label class="form-check-label" for="female">
                                Женский
                            </label>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="motivation" class="form-label">Почему вы хотите принять участие в миссии?</label>
                        <textarea class="form-control" id="motivation" rows="3" name="motivation" required></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="photo" class="form-label">Приложите фотографию</label>
                        <input type="file" class="form-control" id="photo" name="photo">
                    </div>
                    <div class="mb-3 form-check">
                        <input class="form-check-input" type="checkbox" id="stay-on-mars" name="stay_on_mars">
                        <label class="form-check-label" for="stay-on-mars">
                            Готовы остаться на Марсе?
                        </label>
                    </div>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </div>
        </body>
        </html>'''

    elif request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        email = request.form['email']
        education = request.form['education']
        professions = request.form.getlist('professions')
        sex = request.form['sex']
        motivation = request.form['motivation']
        photo = request.files['photo']
        stay_on_mars = 'stay_on_mars' in request.form
    return f'''
            <h1>Данные успешно отправлены!</h1>
            <p><strong>Фамилия:</strong> {surname}</p>
            <p><strong>Имя:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Образование:</strong> {education}</p>
            <p><strong>Профессии:</strong> {', '.join(professions)}</p>
            <p><strong>Пол:</strong> {sex}</p>
            <p><strong>Мотивация:</strong> {motivation}</p>
            <p><strong>Готов остаться на Марсе:</strong> {'Да' if stay_on_mars else 'Нет'}</p>
        '''

@app.route('/jobs')
def jobs_list():
    session = create_session()
    jobs = session.query(Jobs).all()
    return render_template('journal.html', jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
