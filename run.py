from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/new_flash')
def new_flash():
    return render_template('new-name.html')

@app.route('/getstarted')  # Update the route name
def get_started():
    return render_template('getstarted.html')

@app.route('/append')
def append():
    return render_template('append.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/your-flashcards')
def your_flashcards():
    return render_template('your-flashcards.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/single-flashcard')
def single_flashcard():
    return render_template('single-flashcard.html')

if __name__ == '__main__':
    app.run(debug=True)
