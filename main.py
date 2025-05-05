from flask import Flask, render_template, redirect, url_for, abort, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.users import User
from data.jobs import Job
from forms.login import LoginForm
from forms.user import RegisterForm
from forms.job import JobForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mars_explorer_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs_list = db_sess.query(Job).all()
    return render_template('index.html', jobs=jobs_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', message='Неверный логин или пароль', form=form)
    return render_template('login.html', title='Вход', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            return render_template('register.html', message='Пароли не совпадают', form=form)

        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', message='Такой пользователь уже существует', form=form)

        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.email = form.email.data
        user.set_password(form.password.data)

        db_sess.add(user)
        db_sess.commit()

        return redirect(url_for('login'))

    return render_template('register.html', title='Регистрация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Job()
        job.job_title = form.job_title.data
        job.team_leader_id = form.team_leader_id.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        db_sess.add(job)
        db_sess.commit()
        return redirect(url_for('index'))
    return render_template('add_job.html', title='Добавить работу', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/jobs/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    db_sess = db_session.create_session()

    job = db_sess.query(Job).get(job_id)
    if not job:
        abort(404)
    if job.team_leader_id != current_user.id and current_user.id != 1:
        abort(403)
    form = JobForm()
    if form.validate_on_submit():
        job.job_title = form.job_title.data
        job.team_leader_id = form.team_leader_id.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        db_sess.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.job_title.data = job.job_title
        form.team_leader_id.data = job.team_leader_id
        form.work_size.data = job.work_size
        form.collaborators.data = job.collaborators
        form.is_finished.data = job.is_finished

    return render_template('add_job.html', title='Редактировать работу', form=form)


@app.route('/jobs/<int:job_id>/delete', methods=['POST'])
@login_required
def delete_job(job_id):
    db_sess = db_session.create_session()

    job = db_sess.query(Job).get(job_id)
    if not job:
        abort(404)
    if job.team_leader_id != current_user.id and current_user.id != 1:
        abort(403)
    db_sess.delete(job)
    db_sess.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db_path = "db/blogs.db"
    db_session.global_init(db_path)
    app.run(port=8080, host='127.0.0.1', debug=True)