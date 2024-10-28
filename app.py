from flask import Flask # type: ignore

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Hello, World!"

# Dynamic route that accepts a name as a URL parameter
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
