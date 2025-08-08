from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'  # Add a secret key for sessions
db = SQLAlchemy(app)

# Load ML models and data
model = joblib.load(r"C:\Users\saipr\Downloads\homemade_remedies old version\Project\remedy_predictor.pkl")
vectorizer = joblib.load(r"C:\Users\saipr\Downloads\homemade_remedies old version\Project\vectorizer.pkl")
df = pd.read_csv(r"C:\Users\saipr\Downloads\homemade_remedies old version\Project\remedies.csv")
remedy_dict = dict(zip(df["ailment"], df["remedies"]))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    health_condition = db.Column(db.String(50), nullable=False)
    health_details = db.Column(db.Text, nullable=True)

@app.route("/")
def index():
    return redirect(url_for('registration'))

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            health_condition = request.form.get('health_condition')
            health_details = request.form.get('health_details')
            
            # Check if email already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return render_template("registration.html", error="Email already registered. Please use a different email.")
            
            new_user = User(
                name=name,
                email=email,
                password=password,
                health_condition=health_condition,
                health_details=health_details
            )
            db.session.add(new_user)
            db.session.commit()
            
            session['user_id'] = new_user.id
            return redirect(url_for('home'))
            
        except Exception as e:
            db.session.rollback()
            return render_template("registration.html", error="Registration failed. Please try again.")
            
    return render_template("registration.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if 'user_id' not in session:
        return redirect(url_for('registration'))
        
    user = User.query.get(session['user_id'])
    prediction = ""
    remedy = ""
    
    common_solutions = {
        'diabetes': {
            'High blood sugar': 'Take prescribed medication, drink water, exercise gently',
            'Fatigue': 'Rest, check blood sugar, eat small frequent meals',
            'Blurred vision': 'Check blood sugar, rest eyes, consult doctor if persistent',
            'Frequent urination': 'Monitor fluid intake, check blood sugar levels',
            'Slow healing wounds': 'Keep wound clean, monitor blood sugar, consult doctor'
        },
        'hypertension': {
            'Headache': 'Rest in quiet dark room, practice deep breathing',
            'Dizziness': 'Sit or lie down, avoid sudden movements',
            'Shortness of breath': 'Rest, practice breathing exercises, check BP',
            'Chest discomfort': 'Seek immediate medical attention',
            'Nosebleed': 'Sit upright, lean forward, apply cold compress'
        },
        'arthritis': {
            'Joint pain': 'Apply ice/heat, gentle stretching, take prescribed medication',
            'Morning stiffness': 'Gentle stretching, warm shower, gradual movement',
            'Joint swelling': 'Rest, elevate joint, apply ice',
            'Limited mobility': 'Gentle exercises, physical therapy exercises',
            'Muscle weakness': 'Progressive strength training, proper rest'
        },
        'asthma': {
            'Wheezing': 'Use inhaler, sit upright, practice breathing techniques',
            'Coughing': 'Stay hydrated, use humidifier, avoid triggers',
            'Chest tightness': 'Use rescue inhaler, practice relaxation techniques',
            'Shortness of breath': 'Use inhaler, sit upright, practice pursed lip breathing',
            'Night symptoms': 'Use air purifier, elevate head while sleeping'
        },
        'heart_disease': {
            'Chest pain': 'Seek immediate medical attention, rest, take prescribed medication',
            'Irregular heartbeat': 'Sit down, practice deep breathing, contact doctor',
            'Fatigue': 'Rest, stay hydrated, monitor symptoms',
            'Swelling in legs': 'Elevate legs, reduce salt intake, monitor symptoms',
            'Shortness of breath': 'Rest, sit upright, seek medical attention if severe'
        }
    }
    
    if request.method == "POST":
        symptoms = request.form["symptoms"]
        vector_input = vectorizer.transform([symptoms])
        prediction = model.predict(vector_input)[0]
        remedy = remedy_dict.get(prediction, "No remedy found.")
    
    health_recommendations = {
        'diabetes': {
            'diet': ['Low sugar foods', 'High fiber foods', 'Whole grains'],
            'exercise': ['Regular walking', 'Swimming', 'Light aerobics'],
            'medications': ['Blood sugar monitoring', 'Insulin management'],
            'natural_remedies': [
                'Cinnamon (helps lower blood sugar)',
                'Fenugreek seeds (improve insulin function)',
                'Bitter gourd (reduces blood glucose)',
                'Amla (Indian gooseberry for blood sugar control)',
                'Turmeric (anti-inflammatory properties)'
            ]
        },
        'hypertension': {
            'diet': ['Low sodium foods', 'DASH diet', 'Potassium-rich foods'],
            'exercise': ['Moderate cardio', 'Stress reduction activities'],
            'medications': ['Blood pressure monitoring', 'Regular checkups'],
            'natural_remedies': [
                'Garlic (helps lower blood pressure)',
                'Hibiscus tea (natural diuretic)',
                'Beetroot juice (rich in nitrates)',
                'Flaxseed (rich in omega-3)',
                'Celery (contains blood pressure-lowering compounds)'
            ]
        },
        'arthritis': {
            'diet': ['Anti-inflammatory foods', 'Omega-3 rich foods', 'Whole grains'],
            'exercise': ['Low-impact exercises', 'Swimming', 'Gentle yoga'],
            'medications': ['Joint health supplements', 'Pain management'],
            'natural_remedies': [
                'Turmeric with black pepper (anti-inflammatory)',
                'Ginger (reduces joint pain)',
                'Eucalyptus oil (topical pain relief)',
                'Green tea (antioxidant properties)',
                'Apple cider vinegar (anti-inflammatory)'
            ]
        },
        'asthma': {
            'diet': ['Anti-inflammatory foods', 'Vitamin C rich foods'],
            'exercise': ['Breathing exercises', 'Swimming', 'Yoga'],
            'medications': ['Inhaler management', 'Regular checkups'],
            'natural_remedies': [
                'Honey (soothes throat and reduces coughing)',
                'Caffeine (mild bronchodilator)',
                'Ginger tea (anti-inflammatory)',
                'Steam inhalation with eucalyptus',
                'Omega-3 fatty acids (reduce inflammation)'
            ]
        },
        'heart_disease': {
            'diet': ['Heart-healthy foods', 'Low-fat proteins', 'Whole grains'],
            'exercise': ['Monitored cardio', 'Walking', 'Light exercises'],
            'medications': ['Blood pressure monitoring', 'Cholesterol management'],
            'natural_remedies': [
                'Garlic (reduces cholesterol)',
                'Fish oil (omega-3 fatty acids)',
                'Hawthorn berry (improves heart function)',
                'CoQ10 (heart health supplement)',
                'Green tea (antioxidant properties)'
            ]
        }
    }
    
    recommendations = health_recommendations.get(user.health_condition, {})
    solutions = common_solutions.get(user.health_condition, {})
    
    return render_template(
        "index.html",
        user=user,
        recommendations=recommendations,
        prediction=prediction,
        remedy=remedy,
        common_solutions=solutions
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def service():
    return render_template("services.html")

@app.route("/doctors")
def doctors():
    return render_template("doctors.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            return render_template("registration.html", login_error="Invalid email or password")
            
    return render_template("registration.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('registration'))

# Remove duplicate routes for services and doctors

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
