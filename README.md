# 🩺 Homemade Remedies – AI-Powered Health Assistant

Homemade Remedies is a **Flask-based web application** that helps users find natural remedies for common ailments.  
It leverages **Machine Learning** to predict remedies based on symptoms and provides a clean, responsive UI for interaction.

---

## 🚀 Features

- **ML-Powered Predictions** – Suggests remedies based on user input using a trained model (`remedy_predictor.pkl`).
- **Responsive Web UI** – Built with HTML, CSS, and JavaScript for an interactive experience.
- **Static Informational Pages** – About, Contact, Services, and Doctors.
- **User Registration** – Store user details in a SQLite database.
- **Clean Navigation Layout** – Easy to navigate between pages.
- **Custom Styling & Animations** – CSS and JS for a modern, smooth feel.

---

## 🛠 Tech Stack

**Backend:**
- Python 3
- Flask
- scikit-learn (for model training & prediction)
- SQLite (for user data storage)

**Frontend:**
- HTML5, CSS3
- JavaScript
- Bootstrap (if used in templates)
- Custom animations & styles

**Machine Learning:**
- Trained text classifier (`remedy_predictor.pkl`)
- TF-IDF vectorizer (`vectorizer.pkl`)
- CSV datasets (`remedies.csv`, `remedies1.csv`)

---

## 📂 Project Structure

```
homemade_remedies_old_version/
│
├── Project/
│   ├── app.py                  # Main Flask application
│   ├── train_model.py          # Script to train the ML model
│   ├── remedies.csv            # Remedies dataset
│   ├── remedies1.csv           # Alternate/extended dataset
│   ├── remedy_predictor.pkl    # Saved ML model
│   ├── vectorizer.pkl          # Saved TF-IDF vectorizer
│   ├── instance/
│   │   └── users.db            # SQLite database
│   ├── static/                 # CSS, JS, images
│   ├── templates/              # HTML templates
│   └── ...
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/homemade-remedies.git
cd homemade-remedies/Project
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
If `requirements.txt` is missing, install manually:
```bash
pip install flask scikit-learn pandas
```

### 4️⃣ Run the Application
```bash
python app.py
```
Open **http://127.0.0.1:5000/** in your browser.

---

## 🧠 Dataset & Model

- **Dataset**: `remedies.csv` and `remedies1.csv` contain ailments and corresponding natural remedies.
- **Model**: Trained using `train_model.py` with **TF-IDF vectorization** and a classification algorithm (e.g., Naive Bayes / Logistic Regression).
- **Workflow**:
  1. Preprocess text data
  2. Vectorize symptoms using `vectorizer.pkl`
  3. Predict remedies using `remedy_predictor.pkl`

---

## 📸 Screenshots

> *(Replace with actual screenshots from the `static/` folder)*

- **Home Page**  
  ![Home Page](static/images/homepage.png)
- **Prediction Result**  
  ![Prediction](static/images/prediction.png)
- **About Page**  
  ![About](static/images/about.png)

---

## 📌 Future Improvements

- ✅ Add more diverse datasets for better coverage of ailments.
- ✅ Integrate a chatbot for symptom-based Q&A.
- ✅ Enhance UI with Bootstrap/Tailwind.
- ✅ Add user authentication and profile management.
- ✅ Deploy on Render / Railway / Heroku.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 💡 Author

**Saipraneeth Sattu**  
📧 saipraneethsattu@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)
