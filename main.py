from flask import Flask, render_template, request, redirect, url_for
import os
from data.db_session import global_init, create_session
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
base_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(base_dir, 'db')
os.makedirs(db_dir, exist_ok=True)

db_path = os.path.join(db_dir, 'blogs.db')
global_init(db_path)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template(
                'register.html',
                title='Регистрация',
                form=form,
                message="Пароли не совпадают"
            )

        db_sess = create_session()

        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template(
                'register.html',
                title='Регистрация',
                form=form,
                message="Такой пользователь уже существует"
            )

        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect(url_for('success'))
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/success')
def success():
    return "Регистрация успешна!"


if __name__ == '__main__':
    app.run(debug=True)