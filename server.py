from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route('/table')
def table():
    gender = request.args.get('gender')
    age_str = request.args.get('age')
    return render_template('training.html', gender=gender, age=int(age_str))


if __name__ == '__main__':
    app.run(debug=True)