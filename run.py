from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cSuT6KxPuOayBkNnvTWXO0e0J'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizme.db'

db = SQLAlchemy(app)

# Define the User model representing the user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
        # Define the columns of the user table

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
        # Establish the relationship between User and FlashcardSet models

    flashcards = db.relationship('FlashcardSet', backref='user', lazy=True)

    def __repr__(self):
        return f"User(email='{self.email}')"

# Define the FlashcardSet model representing the flashcard_set table. A set of flashcards 
class FlashcardSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flashcards = db.relationship('Flashcard', backref='flashcard_set', lazy=True)

    def __repr__(self):
        return f"FlashcardSet(name='{self.name}')"
    
# Define the Flashcard model representing the flashcard table. Each flashcard has a front and a back
class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(100), nullable=False)
    back = db.Column(db.String(100), nullable=False)
    flashcard_set_id = db.Column(db.Integer, db.ForeignKey('flashcard_set.id'), nullable=False)

    def __repr__(self):
        return f"Flashcard(front='{self.front}', back='{self.back}')"

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Retrieve the user from the database based on the provided email
        user = User.query.filter_by(email=email).first()

        if user:
            # Compare the hashed password stored in the database with the provided password
            if bcrypt.checkpw(password.encode('utf-8'), user.password):
                # Passwords match, user is authenticated
                # Redirect the user to the success route
                return render_template('success.html', user=user)
        
        # Invalid email or password, show an error message
        error_message = "Invalid email or password. Please try again."
        return render_template('login.html', error_message=error_message)

    # GET request, render the login form
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])

@app.route('/signup')
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store the email and hashed password in the database as well as empty flashcards
        user = User(email=email, password=hashed_password, flashcards = [] )
        db.session.add(user)
        db.session.commit()

        # redirect the user to login page
        return render_template('login.html', email=email)

    # GET request, render the sign-up form
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
