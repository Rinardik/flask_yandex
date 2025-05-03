from flask import Flask, render_template
import json
import random
import os

app = Flask(__name__)

CREW_JSON_PATH = os.path.join(app.root_path, 'templates', 'astr.json')

def get_random_crew_member():
    with open(CREW_JSON_PATH, encoding='utf-8') as f:
        crew = json.load(f)
    return random.choice(crew)

@app.route('/member')
def member():
    member_data = get_random_crew_member()
    return render_template('member.html', member=member_data)

if __name__ == '__main__':
    app.run(debug=True)