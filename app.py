# version 0.1
import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

color_codes = {
    "color01": "#4355e3",
    "color02": "#1325e3",
    "color03": "#3055e0",
    "color04": "#0351e3",
    "color05": "#2351e3",
    "color06": "#0e55e3",
}

color = os.environ.get('APP_COLOR') or random.choice(["color01", "color02", "color03", "color04", "color05", "color06"])

@app.route("/")
def main():
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=42090, debug=True)
