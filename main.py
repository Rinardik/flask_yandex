from flask import Flask, render_template
import os
from data.db_session import global_init, create_session
from data.jobs import Jobs

app = Flask(__name__)

db_path = os.path.join(os.getcwd(), 'db', 'blogs.db')
global_init(db_path)


@app.route('/jobs')
def jobs_list():
    session = create_session()
    jobs = session.query(Jobs).all()
    return render_template('journal.html', jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)