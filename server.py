from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/answer', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        user_data = {
            'title': request.form.get('title'),
            'surname': request.form.get('surname'),
            'name': request.form.get('name'),
            'education': request.form.get('education'),
            'profession': request.form.get('profession'),
            'sex': request.form.get('sex'),
            'motivation': request.form.get('motivation'),
            'ready': 'Yes' if 'ready' in request.form else 'No'
        }
        return render_template('auto_answer.html', form=user_data)
    return render_template('form.html')

@app.route('/auto_answer')
def auto_answer():
    user_data = {
        'title': 'Mr.',
        'surname': 'Smith',
        'name': 'John',
        'education': 'Harvard University',
        'profession': 'Инженер-исследователь',
        'sex': 'male',
        'motivation': 'I want to explore new worlds!',
        'ready': 'Yes'
    }
    return render_template('auto_answer.html', form=user_data)

if __name__ == '__main__':
    app.run(debug=True)