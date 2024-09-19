from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my simple Flask app!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name', 'Stranger')
        return f"Hello, {name}!"
    return '''
        <form method="POST">
            <label for="name">Enter your name:</label>
            <input type ="text" id="name" name="name">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
