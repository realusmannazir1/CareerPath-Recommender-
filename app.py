import streamlit as st
import pickle
import numpy as np
import joblib
import os
import csv
from datetime import datetime
import pandas as pd

# Load the scaler and model using joblib
scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/model.pkl")
class_names = ['Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Unknown',
               'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
               'Banker', 'Writer', 'Accountant', 'Designer',
               'Construction Engineer', 'Game Developer', 'Stock Investor',
               'Real Estate Developer']

# Career recommendations by background
career_by_background = {
    'Pre-Medical': [
        'Doctor', 'Surgeon', 'Dentist', 'Pharmacist', 'Nurse', 'Physiotherapist', 
        'Medical Researcher', 'Biotechnologist', 'Geneticist', 'Lab Technician', 
        'Nutritionist', 'Public Health Officer', 'Medical Writer', 'Psychologist', 
        'Veterinarian', 'Clinical Research Coordinator', 'Forensic Scientist', 
        'Biomedical Engineer', 'Healthcare Administrator', 'Epidemiologist'
    ],
    'Pre-Engineering': [
        'Software Engineer', 'Game Developer', 'Civil Engineer', 'Mechanical Engineer', 
        'Electrical Engineer', 'Electronics Engineer', 'Robotics Engineer', 
        'Data Scientist', 'AI Specialist', 'Industrial Engineer', 'Aerospace Engineer', 
        'Mechatronics Engineer', 'Network Engineer', 'Web Developer', 'App Developer', 
        'Automation Engineer', 'Environmental Engineer', 'Construction Manager', 
        'Technical Consultant', 'Blockchain Developer'
    ],
    'ICS': [
        'Software Engineer', 'Game Developer', 'Data Analyst', 'Web Developer', 
        'Cybersecurity Specialist', 'AI Developer', 'IT Consultant', 'App Developer', 
        'Database Administrator', 'Cloud Engineer', 'Blockchain Developer', 'UI/UX Designer', 
        'Network Engineer', 'Software Tester', 'Stock Investor', 'Digital Marketing Specialist', 
        'Business Analyst', 'E-commerce Manager', 'System Administrator', 'Robotics Programmer'
    ],
    'Arts': [
        'Lawyer', 'Teacher', 'Writer', 'Government Officer', 'Journalist', 'Historian', 
        'Sociologist', 'Psychologist', 'Public Relations Officer', 'Actor', 'Politician', 
        'Diplomat', 'Social Worker', 'Human Rights Advocate', 'Translator', 'Editor', 
        'Event Manager', 'NGO Manager', 'Film Director', 'Museum Curator'
    ],
    'Commerce': [
        'Accountant', 'Business Owner', 'Stock Investor', 'Banker', 'Financial Analyst', 
        'Economist', 'Auditor', 'Entrepreneur', 'Marketing Manager', 'HR Manager', 
        'Insurance Agent', 'Investment Banker', 'Tax Consultant', 'Business Consultant', 
        'Operations Manager', 'Supply Chain Manager', 'Financial Planner', 'Trader', 
        'Risk Manager', 'Corporate Lawyer'
    ]
}

# Career recommendations by background (with detailed programs)
career_recommendations = {
    'ICS': {
        'title': '🖥️ Computer Science & IT Programs',
        'programs': [
            'BS Computer Science',
            'BS Software Engineering',
            'BS Information Technology',
            'BS Artificial Intelligence / Data Science',
            'BS Cyber Security',
            'BS Game Development / Animation',
            'BS Mathematics',
            'BS Statistics',
            'BS Data Science / Analytics',
            'BS Actuarial Science',
            'BBA (Business Administration)'
        ]
    },
    'Pre-Medical': {
        'title': '🏥 Health & Medicine Programs',
        'programs': [
            'MBBS (Medicine & Surgery)',
            'BDS (Dental Surgery)',
            'DPT (Doctor of Physical Therapy)',
            'Pharm-D (Pharmacy)',
            'BS Nursing',
            'BS Biotechnology',
            'BS Microbiology',
            'BS Biochemistry',
            'BS Genetics',
            'BS Molecular Biology',
            'BS Medical Laboratory Technology',
            'BS Nutrition & Dietetics',
            'BS Psychology',
            'BS Zoology',
            'BS Botany',
            'BS Environmental Science'
        ]
    },
    'Pre-Engineering': {
        'title': '🏗️ Engineering & Technology Programs',
        'programs': [
            'BE/BSc Mechanical Engineering',
            'BE/BSc Electrical Engineering',
            'BE/BSc Civil Engineering',
            'BE/BSc Chemical Engineering',
            'BE/BSc Computer Engineering',
            'BE/BSc Electronics Engineering',
            'BS Computer Science',
            'BS Software Engineering',
            'BS Artificial Intelligence / Data Science',
            'BS Information Technology',
            'BS Physics',
            'BS Chemistry',
            'BS Mathematics',
            'BS Statistics',
            'BS Environmental Science',
            'BS Robotics / Mechatronics',
            'BBA (with Maths background)'
        ]
    },
    'Arts': {
        'title': '📚 Humanities & Social Sciences Programs',
        'programs': [
            'BA English',
            'BA Urdu',
            'BA Sociology',
            'BS Psychology',
            'BS International Relations',
            'BS Media & Communication',
            'BS Mass Communication / Journalism',
            'BS Political Science',
            'BS Social Work',
            'LLB (Law)',
            'B.Ed (Education)',
            'BS Fine Arts / Design',
            'BS Fashion Design',
            'BS Film / Animation / Multimedia',
            'BS Performing Arts / Music',
            'BS History / Archaeology'
        ]
    },
    'Commerce': {
        'title': '💼 Business & Commerce Programs',
        'programs': [
            'BBA (Bachelor of Business Administration)',
            'BS Accounting & Finance',
            'BS Economics',
            'BS Management',
            'BS Marketing',
            'BS Entrepreneurship',
            'BS Business Analytics',
            'BS Supply Chain / Logistics',
            'BS Human Resource Management',
            'CA / ACCA / CMA / CPA',
            'BS Banking & Finance',
            'BS Computer Science (some universities)',
            'BS Information Technology',
            'BS Finance + IT (Financial Tech)',
            'LLB (Law after BBA)',
            'BS Stock Market / Investment'
        ]
    }
}


# Subject names
subject_names = ['Math', 'History', 'Physics', 'Chemistry', 'Biology', 'English', 'Geography']

# Recommendations function
def Recommendations(gender, part_time_job, extracurricular_activities, weekly_self_study_hours, scores_dict):
    # Encode categorical variables
    gender_encoded = 1 if gender.lower() == 'female' else 0
    part_time_job_encoded = 1 if part_time_job else 0
    extracurricular_activities_encoded = 1 if extracurricular_activities else 0

    # Create feature array with all 13 features (matching the scaler's expected input)
    feature_array = np.array([[gender_encoded, part_time_job_encoded, extracurricular_activities_encoded,
                               weekly_self_study_hours,
                               scores_dict['math'], scores_dict['history'], 
                               scores_dict['physics'], scores_dict['chemistry'], 
                               scores_dict['biology'], scores_dict['english'], 
                               scores_dict['geography'], scores_dict['total'], 
                               scores_dict['average']]])

    # Scale features
    scaled_features = scaler.transform(feature_array)

    # Predict using the model
    probabilities = model.predict_proba(scaled_features)

    # Get top three predicted classes along with their probabilities
    top_classes_idx = np.argsort(-probabilities[0])[:3]
    top_classes_names_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]

    return top_classes_names_probs

# Function to save student data to CSV
def save_student_data(name, age, gender, background, part_time_job, extracurricular, study_hours, scores_dict, model_recommendations):
    csv_file = "student_records.csv"
    
    # Prepare data row
    row = {
        'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Name': name,
        'Age': age,
        'Gender': gender,
        'Background': background,
        'Part-Time Job': 'Yes' if part_time_job else 'No',
        'Extracurricular Activities': 'Yes' if extracurricular else 'No',
        'Weekly Study Hours': study_hours,
        'Math': scores_dict.get('math', 0),
        'History': scores_dict.get('history', 0),
        'Physics': scores_dict.get('physics', 0),
        'Chemistry': scores_dict.get('chemistry', 0),
        'Biology': scores_dict.get('biology', 0),
        'English': scores_dict.get('english', 0),
        'Geography': scores_dict.get('geography', 0),
        'Total Score': scores_dict.get('total', 0),
        'Average Score': scores_dict.get('average', 0),
        'Top Career Match': model_recommendations[0][0] if model_recommendations else 'N/A',
        'Career Match Score': f"{model_recommendations[0][1]*100:.1f}%" if model_recommendations else 'N/A'
    }
    
    # Check if file exists and write accordingly
    file_exists = os.path.isfile(csv_file)
    
    try:
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys(), extrasaction='ignore')
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)
        
        # Verify data was written by reading last line
        df = pd.read_csv(csv_file)
        if len(df) > 0:
            return True
        else:
            return False
    except PermissionError:
        st.error(f"❌ Permission Error: Cannot write to {csv_file}. Make sure the file is not open in another program.")
        return False
    except Exception as e:
        st.error(f"❌ Error saving data: {str(e)}")
        return False

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'age' not in st.session_state:
    st.session_state.age = None
if 'gender' not in st.session_state:
    st.session_state.gender = "Male"
if 'background' not in st.session_state:
    st.session_state.background = "Pre-Medical"
if 'part_time_job' not in st.session_state:
    st.session_state.part_time_job = False
if 'extracurricular_activities' not in st.session_state:
    st.session_state.extracurricular_activities = False
if 'weekly_self_study_hours' not in st.session_state:
    st.session_state.weekly_self_study_hours = 5
if 'scores' not in st.session_state:
    st.session_state.scores = {subject.lower(): 50 for subject in subject_names}

# Streamlit UI setup
def main():
    st.set_page_config(page_title="📚 Education Recommendation System", page_icon="📚", layout="wide")
    st.title("📚 Education Recommendation System")
    
    st.write(
        """
        Welcome to the Education Recommendation System. This tool helps university students
        in selecting the most suitable studies and courses based on academic performance and background.
        """
    )

    # Step 1: Name
    if st.session_state.step == 1:
        st.header("Step 1: What is your name?")
        st.session_state.name = st.text_input("📝 Enter your name:", value=st.session_state.name, key="input_name")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_1"):
                if st.session_state.name.strip():
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.error("Please enter your name")
        with col2:
            st.button("← Back", disabled=True)

    # Step 2: Age
    elif st.session_state.step == 2:
        st.header("Step 2: What is your age?")
        st.session_state.age = st.number_input("🎂 Enter your age:", min_value=10, max_value=100, value=st.session_state.age if st.session_state.age else 18, key="input_age")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_2"):
                st.session_state.step = 3
                st.rerun()
        with col2:
            if st.button("← Back", key="back_2"):
                st.session_state.step = 1
                st.rerun()

    # Step 3: Gender
    elif st.session_state.step == 3:
        st.header("Step 3: What is your gender?")
        st.session_state.gender = st.radio("👤 Select your gender:", ["Male", "Female"], index=0 if st.session_state.gender == "Male" else 1, key="input_gender")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_3"):
                st.session_state.step = 4
                st.rerun()
        with col2:
            if st.button("← Back", key="back_3"):
                st.session_state.step = 2
                st.rerun()

    # Step 4: Background
    elif st.session_state.step == 4:
        st.header("Step 4: What is your academic background?")
        backgrounds = ['Pre-Medical', 'Pre-Engineering', 'ICS', 'Arts', 'Commerce']
        st.session_state.background = st.radio("📚 Select your background:", backgrounds, 
                                                index=backgrounds.index(st.session_state.background) if st.session_state.background in backgrounds else 0, 
                                                key="input_background")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_4"):
                st.session_state.step = 5
                st.rerun()
        with col2:
            if st.button("← Back", key="back_4"):
                st.session_state.step = 3
                st.rerun()

    # Step 5: Part-Time Job
    elif st.session_state.step == 5:
        st.header("Step 5: Do you have a part-time job?")
        part_time_options = st.radio("💼 Part-Time Job:", ["Yes", "No"], index=0 if st.session_state.part_time_job else 1, key="input_part_time")
        st.session_state.part_time_job = part_time_options == "Yes"
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_5"):
                st.session_state.step = 6
                st.rerun()
        with col2:
            if st.button("← Back", key="back_5"):
                st.session_state.step = 4
                st.rerun()

    # Step 6: Extracurricular Activities
    elif st.session_state.step == 6:
        st.header("Step 6: Do you participate in extracurricular activities?")
        extracurricular_options = st.radio("🎭 Extracurricular Activities:", ["Yes", "No"], index=0 if st.session_state.extracurricular_activities else 1, key="input_extracurricular")
        st.session_state.extracurricular_activities = extracurricular_options == "Yes"
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_6"):
                st.session_state.step = 7
                st.rerun()
        with col2:
            if st.button("← Back", key="back_6"):
                st.session_state.step = 5
                st.rerun()

    # Step 7: Weekly Self-Study Hours
    elif st.session_state.step == 7:
        st.header("Step 7: How many hours do you study per week?")
        st.session_state.weekly_self_study_hours = st.slider("⏱ Weekly Self-Study Hours:", min_value=0, max_value=100, value=st.session_state.weekly_self_study_hours, step=1, key="input_study_hours")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Next →", key="next_7"):
                st.session_state.step = 8
                st.rerun()
        with col2:
            if st.button("← Back", key="back_7"):
                st.session_state.step = 6
                st.rerun()

    # Step 8: Subject Scores
    elif st.session_state.step == 8:
        st.header("Step 8: Enter your subject scores")
        
        for idx, subject in enumerate(subject_names):
            key = subject.lower()
            st.session_state.scores[key] = st.slider(
                f"📊 {subject} Score (0-100):",
                min_value=0,
                max_value=100,
                value=st.session_state.scores.get(key, 50),
                key=f"score_{subject}"
            )

        # Calculate total and average
        total_score = sum(st.session_state.scores.values())
        average_score = total_score / len(subject_names)

        st.write(f"**Total Score**: {total_score}")
        st.write(f"**Average Score**: {average_score:.2f}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Get Recommendations →", key="submit"):
                if average_score < 40:
                    st.error("⚠️ Your average score is below 40. Please aim to pass all subjects.")
                else:
                    st.session_state.step = 9
                    st.rerun()
        with col2:
            if st.button("← Back", key="back_8"):
                st.session_state.step = 7
                st.rerun()

    # Step 9: Results
    elif st.session_state.step == 9:
        st.header("🎯 Your Career Recommendations")
        
        # Display student info
        st.write(f"**Name:** {st.session_state.name}")
        st.write(f"**Age:** {st.session_state.age}")
        st.write(f"**Gender:** {st.session_state.gender}")
        st.write(f"**Background:** {st.session_state.background}")
        st.write(f"**Part-Time Job:** {'Yes' if st.session_state.part_time_job else 'No'}")
        st.write(f"**Extracurricular Activities:** {'Yes' if st.session_state.extracurricular_activities else 'No'}")
        st.write(f"**Weekly Study Hours:** {st.session_state.weekly_self_study_hours}")
        
        # Prepare scores for model (fixed 7 subjects matching original model training)
        scores_dict = {
            'math': st.session_state.scores.get('mathematics', 50),
            'history': st.session_state.scores.get('history', 50) or st.session_state.scores.get('english_literature', 50) or st.session_state.scores.get('general_mathematics', 50),
            'physics': st.session_state.scores.get('physics', 50) or st.session_state.scores.get('statistics', 50),
            'chemistry': st.session_state.scores.get('chemistry', 50) or st.session_state.scores.get('economics', 50),
            'biology': st.session_state.scores.get('biology', 50) or st.session_state.scores.get('psychology', 50),
            'english': st.session_state.scores.get('english', 50),
            'geography': st.session_state.scores.get('motal-e-quran', 50) or st.session_state.scores.get('islamiat', 50),
        }
        
        # Calculate total and average
        scores_dict['total'] = sum(scores_dict.values())
        scores_dict['average'] = scores_dict['total'] / 7
        
        # Get model recommendations
        try:
            model_recommendations = Recommendations(st.session_state.gender, 
                                             st.session_state.part_time_job, st.session_state.extracurricular_activities,
                                             st.session_state.weekly_self_study_hours,
                                             scores_dict)
        except Exception as e:
            st.error(f"Error getting model recommendations: {e}")
            model_recommendations = []
        
        st.markdown("---")
        
        # Show Bachelor Programs by Background
        if st.session_state.background in career_recommendations:
            rec = career_recommendations[st.session_state.background]
            st.markdown(f"## {rec['title']}")
            st.write("**Recommended Bachelor Programs:**")
            for i, program in enumerate(rec['programs'], 1):
                st.write(f"**{i}. {program}**")
        
        st.markdown("---")
        
        # Show AI Model Career Predictions
        if model_recommendations:
            st.markdown("## 🤖 AI Career Path Predictions")
            for idx, (career, probability) in enumerate(model_recommendations, 1):
                percentage = probability * 100
                st.markdown(f"### {idx}. {career}")
                st.write(f"**Match Score:** {percentage:.1f}%")
                st.progress(probability)
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("💾 Save Data", key="save_data"):
                if save_student_data(st.session_state.name, st.session_state.age, st.session_state.gender,
                                     st.session_state.background, st.session_state.part_time_job,
                                     st.session_state.extracurricular_activities, st.session_state.weekly_self_study_hours,
                                     scores_dict, model_recommendations):
                    st.success("✅ Student data saved to student_records.csv")
                else:
                    st.error("❌ Failed to save data")
        
        with col2:
            if st.button("Start Over", key="restart"):
                st.session_state.step = 1
                st.session_state.name = ""
                st.session_state.age = None
                st.session_state.gender = "Male"
                st.session_state.background = "Pre-Medical"
                st.session_state.part_time_job = False
                st.session_state.extracurricular_activities = False
                st.session_state.weekly_self_study_hours = 5
                st.session_state.scores = {}
                st.rerun()
        with col3:
            if st.button("← Back to Scores", key="back_9"):
                st.session_state.step = 8
                st.rerun()
        
        # Show download link for the CSV
        if os.path.isfile("student_records.csv"):
            with open("student_records.csv", "r", encoding='utf-8') as f:
                st.download_button(
                    label="📥 Download All Records (CSV)",
                    data=f.read(),
                    file_name="student_records.csv",
                    mime="text/csv",
                    key="download_csv"
                )

if __name__ == '__main__':
    # Change to the directory where the script is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
