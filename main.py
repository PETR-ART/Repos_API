from flask import Flask, redirect, render_template
from data.jobs import Jobs
from data import db_session
from data.users import User
from forms.login import LoginForm
from forms.job_form import JobsForm
from forms.register import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from get.get_weather import get_weather


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(User).filter(User.login == form.login.data).first()
        if jobs and jobs.check_password(form.password.data):
            login_user(jobs, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
        )

        db_sess.add(job)
        db_sess.commit()
        return redirect('/')

    return render_template('add_job.html', title='Добавить работу', form=form)


@app.route('/')
def start():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        job = db_sess.query(Jobs)
        return render_template('index.html', jobs=job)
    return render_template('index.html')


@app.route('/temperature')
def temperature():
    return render_template('temperature.html', city='Йошкар-Ола', temperature=get_weather())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template('form/register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            login=form.login.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/project.db")
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()