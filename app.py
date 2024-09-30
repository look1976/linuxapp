# app.py
import random
from flask import Flask

app = Flask(__name__)

def get_random_color():
    colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White"]
    return random.choice(colors)

@app.route('/')
def display_random_color():
    color = get_random_color()
    return f'<h1 style="color:{color};">Random Color: {color}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
