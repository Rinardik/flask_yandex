from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list_prof/<list_code>')
def training(list_code):
    if 'ol' in list_code.lower():
        code_prof = "ol"
    elif 'ul' in list_code.lower():
        code_prof = "ul"
    else:
        code_prof ='error'
    return render_template('training.html', code_prof=code_prof)

if __name__ == '__main__':
    app.run(debug=True)