from flask import Flask

app = Flask(__name__)
from flask import Flask, render_template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example1')
def example1():
    return render_template('example1.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')