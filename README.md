# 🎓 CareerPath Recommender

A **Streamlit-based AI-powered career guidance system** that recommends suitable career paths based on students' academic background, performance, and personal characteristics.

---

## 📋 Features

- **Multi-Step Form Interface** - Interactive 9-step wizard for data collection
- **Dynamic Subject Selection** - Different subjects for each academic background (ICS, Pre-Medical, Pre-Engineering, Arts, Commerce)
- **AI-Powered Recommendations** - Machine learning model suggests top 3 career paths with confidence scores
- **Comprehensive Career Guidance** - 15-17 bachelor programs per field tailored to Pakistani education system
- **Data Persistence** - Automatically saves student records to CSV with all information
- **Data Export** - Download all student records as CSV file
- **One-Click Launcher** - `START_APP.bat` for easy application launch
- **Real-Time Calculations** - Auto-computes total and average scores

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Framework**: [Streamlit](https://streamlit.io/)
- **Machine Learning**: 
  - Scikit-learn (RandomForestClassifier + StandardScaler)
  - joblib for model serialization
- **Data Processing**: NumPy, Pandas
- **Dependencies**: See `requirements.txt`

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone Repository
```bash
git clone https://github.com/realusmannazir1/CareerPath-Recommender-.git
cd CareerPath_Recommender
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Application

**Option A - Terminal**:
```bash
streamlit run app.py
```

**Option B - One-Click (Windows)**:
Double-click `START_APP.bat` in the project folder

The app opens at: **http://localhost:8501**

---

## 📋 How It Works (9-Step Process)

1. **Name** - Enter student name
2. **Age** - Input age
3. **Gender** - Select Male or Female
4. **Background** - Choose: ICS, Pre-Medical, Pre-Engineering, Arts, or Commerce
5. **Part-Time Job** - Yes/No
6. **Extracurricular** - Yes/No
7. **Weekly Study Hours** - 0-100 hours slider
8. **Subject Scores** - Rate 7 subjects (0-100) based on selected background
9. **Results** - View top 3 career recommendations with confidence scores and save data

---

## 📊 Supported Backgrounds & Careers

### **ICS** (Computer Science)
Programming, Software Engineering, Cybersecurity, Data Science, Web Development, AI/ML Engineer, Cloud Computing, DevOps, Blockchain Developer, Game Development, Networking, IT Consultant, System Administrator, Database Administrator, IT Project Manager, Computer Scientist

### **Pre-Medical**
Doctor, Surgeon, Dentist, Nurse, Pharmacist, Psychologist, Physiotherapist, Medical Technologist, Health Inspector, Radiologist, Laboratory Technician, Anesthetist, Pathologist, Medical Researcher, Public Health Specialist, Medical Records Officer

### **Pre-Engineering**
Civil Engineer, Mechanical Engineer, Electrical Engineer, Electronics Engineer, Chemical Engineer, Petroleum Engineer, Structural Engineer, Environmental Engineer, Telecommunications Engineer, Automobile Engineer, Aerospace Engineer, Mining Engineer, Power Engineer, Infrastructure Engineer, BioMedical Engineer, Control Systems Engineer

### **Arts**
Teacher, Journalist, Lawyer, Psychologist, Historian, Sociologist, Economist, Author, Social Worker, Human Resources, Public Relations, Political Analyst, Diplomat, Cultural Advisor, Criminologist, Librarian, Anthropologist

### **Commerce**
Accountant, Business Analyst, Financial Advisor, Marketing Manager, Entrepreneur, HR Manager, Supply Chain Manager, Auditor, Bank Manager, Investment Analyst, Insurance Agent, Tax Consultant, Sales Executive, Stock Broker, Real Estate Agent, Import/Export Manager

---

## 📁 Project Structure

```
CareerPath_Recommender/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── START_APP.bat                   # One-click launcher (Windows)
├── run_app.bat                     # Alternative launcher
├── student_records.csv             # Auto-generated student database
├── resave_models.py                # Model re-pickling utility
├── .gitignore                      # Git configuration
└── model/
    ├── scaler.pkl                  # Feature scaler
    ├── model.pkl                   # ML model (RandomForest)
    ├── scaler.pkl.backup           # Backup scaler
    └── model.pkl.backup            # Backup model
├── Jupiter file & dataset/
    ├── CareerPath Recommender.ipynb # Analysis notebook
    └── student-scores.csv          # Training dataset
```

---

## 💾 Data Management

### Save Student Records
1. Complete all 9 form steps
2. Review recommendations
3. Click **Save Data** button
4. Data automatically appends to `student_records.csv`

### Download Records
Click **Download Records** button to export CSV with all student data

### CSV Columns
```
Timestamp, Name, Age, Gender, Background, Part-Time Job, 
Extracurricular Activities, Weekly Study Hours, 
[Subject Scores], Total Score, Average Score, 
Top Career Match, Career Match Score
```

---

## 🤖 Machine Learning Details

**Model Architecture**:
- Algorithm: Random Forest Classifier
- Scaler: StandardScaler (feature normalization)
- Features: 13-dimensional input vector
- Output: Top 3 predictions with confidence scores

**Input Features**:
- Gender (encoded: 1=Male, 0=Female)
- Part-Time Job (binary)
- Extracurricular Activities (binary)
- Weekly Study Hours (0-100)
- 7 Subject Scores (0-100 each)
- Total Score (auto-calculated)
- Average Score (auto-calculated)

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Issue: "No such file: model/scaler.pkl"
Run from project root directory:
```bash
cd CareerPath_Recommender
streamlit run app.py
```

### Issue: Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

### Issue: scikit-learn version warning
```bash
python resave_models.py
```

---

## 📦 Requirements

```
streamlit
scikit-learn==1.7.2
numpy
pandas
joblib
xgboost
imbalanced-learn
```

---

## 👨‍💻 Author & Team

**Course**: Introduction to Data Science (3rd Semester)
**Institution**: UET (University of Engineering & Technology)
**Project Type**: Group Semester Project (3 Members)

### Team Members

| Registration Number | Student Name |
|---|---|
| 24PWDSC0178 | Muhammad Usman Nazir |
| 24PWDSC0148 | Syed Abdul Muqsit Shah |
| 24PWDSC0181 | Ihtiram Shahid |

**GitHub**: [@realusmannazir1](https://github.com/realusmannazir1)

---

## 📝 License

This project is open source. Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions welcome! Fork → Feature Branch → Commit → Push → Pull Request

---

## 🎯 Future Enhancements

- [ ] More academic backgrounds
- [ ] Expanded career database
- [ ] Analytics dashboard
- [ ] User authentication
- [ ] API endpoints
- [ ] Multi-language support (Urdu)
- [ ] Mobile app version
- [ ] Advanced filtering & search

---

**Made with ❤️ for student career guidance in Pakistan**
