import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Sethumadhavan V's Portfolio",
    page_icon=":briefcase:",
    layout="wide"
)

# Navigation options
NAV_OPTIONS = {
    "🏠 Home": "Home",
    "📞 Contact": "Contact",
    "🎓 Education": "Education",
    "💡 Skills": "Skills",
    "🚀 Projects": "Projects",
    "🏆 Certifications": "Certifications",
    "📚 Courses": "Courses",
    "🎯 Internship": "Internship",
    "💼 Professional Experience": "Professional Experience",
    "🎉 Extracurricular Activities": "Extracurricular Activities",
}

# Initialize the sidebar with emojis as icons and download resume option
def init_sidebar():
    st.sidebar.header("Navigation")
    selection = st.sidebar.radio("Go to", list(NAV_OPTIONS.keys()))
    st.session_state.page = NAV_OPTIONS[selection]

    st.sidebar.markdown("---")
    st.sidebar.write("📄 **Resume**")
    st.sidebar.markdown(
        "[Download Resume](https://drive.google.com/file/d/1jmzA7mhg4qxoLXuBLNcZEPFHZoanP04C/view?usp=drive_link)"
    )

# Define page content functions
def home_page():
    st.title("👋 Welcome")

    st.write(
        """
Hello! I'm **Sethumadhavan V**, a recent M.Tech graduate in Software Engineering from Vellore Institute of Technology.  
With expertise in **Python** and **SQL**, I am passionate about data analysis and leveraging data to drive impactful business decisions.

I am currently:
- Pursuing a **Doctor of Philosophy (Ph.D.) in Computer Science Engineering and Information Systems** at VIT, Vellore (Jul 2025 – Present).  
- Enhancing my data skills through the **Master Data Science** course at **GUVI - ZEN Class, IIT-M**.

My experience includes:
- Backend development with Python.  
- AI-based automation tools.  
- YouTube data harvesting and warehousing.  
- Interactive data visualization and analytics dashboards.

My goal is to contribute to a dynamic team as an **entry-level data analyst / backend developer**, where I can apply my analytical skills and problem-solving abilities to uncover valuable insights and support data-driven decision-making.

Feel free to explore my projects and get in touch with me for any opportunities!
        """
    )

def contact_page():
    st.header("📞 Contact Information")
    contact_info = """
- **Phone:** [9159299878](tel:9159299878)  
- **Email:** [sethumadhavanvelu2002@gmail.com](mailto:sethumadhavanvelu2002@gmail.com)  
- **Location:** Sholingur  
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/sethumadhavan-v-b84890257/)  
- **GitHub:** [SETHU0010](https://github.com/SETHU0010)  
- **WhatsApp:** [Chat with me](https://wa.me/9159299878)  
    """
    st.markdown(contact_info)
    st.write("### 📄 Download Resume")
    st.markdown(
        "[Download Resume](https://drive.google.com/file/d/1jmzA7mhg4qxoLXuBLNcZEPFHZoanP04C/view?usp=drive_link)"
    )

def education_page():
    st.header("🎓 Education")
    education = """
- **Doctor of Philosophy (Ph.D.) – Computer Science Engineering and Information Systems**  
  *Vellore Institute of Technology, Vellore*  
  📅 **Jul 2025 – Present**

- **Master Data Science**  
  *GUVI - ZEN Class, IIT-M Advanced Programming Professional*  
  📅 **Feb 2024 – Jul 2024**
      
- **M.Tech Integrated Software Engineering**  
  *Vellore Institute of Technology, Vellore*  
  📅 **2019 – 2024**

- **Higher Secondary Education**  
  *Sri Ayyan Vidyashram Higher Sec School*  
  📅 **2018 – 2019**

- **Secondary School Leaving Certificate**  
  *Sri Ayyan Vidyashram Higher Sec School*  
  📅 **2016 – 2017**
    """
    st.markdown(education)

def skills_page():
    st.header("💡 Skills")
    skills_data = {
        "Category": [
            "Technical Skills",
            "Tools and Software",
            "Soft Skills",
            "Languages"
        ],
        "Details": [
            "Python 🐍, SQL 🗃️",
            "Microsoft Office 🖥️, PowerBi 📊, GitHub 🧑‍💻",
            "CRM 🗂️, Critical Thinking 🧠, Time Management ⏱️",
            "Tamil, English"
        ]
    }
    df_skills = pd.DataFrame(skills_data)
    st.dataframe(df_skills, width=700)

def projects_page():
    st.header("🚀 Projects")

    st.markdown("""
### 1. 🔐 Secure Data Sharing of Personal Health Records in SQL Using AES Algorithm  
**Key Skills:** Python, Streamlit, AES, MySQL  
- Developed a secure system for managing and sharing personal health records.  
- Implemented AES encryption for data confidentiality and secure MySQL storage.  
- Enabled keyword-based search and secure user authentication.  
- Built a user-friendly Streamlit interface with role-based access.  
[🔗 GitHub](https://github.com/SETHU0010/SECURE_E_PERSON_HEALTH_CARE_SYSTEM_USING_AES_ALGORITHM)

---

### 2. 🚖 Uber Fare Prediction and Streamlit Web Application  
**Key Skills:** Python, Streamlit, AWS, Regression, EDA, Geospatial Analysis  
- Created a regression model to predict Uber ride fares.  
- Preprocessed geolocation and time-series data for training.  
- Developed a Streamlit app for real-time fare estimates.  
- Deployed on AWS for cloud accessibility and scalability.  
[🚀 App](https://uberfarepredictionandappwebapplication-t3fru4dygszajbwgqppgzv.streamlit.app/)

---

### 3. 🎥 YouTube Data Harvesting and Warehousing using SQL and Streamlit  
**Key Skills:** Python, SQL, Streamlit, MongoDB, API Integration  
- Built a Streamlit app to fetch and store channel/video data from YouTube API.  
- Stored and managed data using SQL and NoSQL (MongoDB).  
- Enabled searchable dashboards for channel metrics and analytics.  
[📺 App](https://youtubedataharvestingandwarehousingusingsqlandapp-nzfhhsps4haa.streamlit.app/)

---

### 4. 🧠 Automated Resume Parsing and Skill Analysis System  
**Key Skills:** Python, Flask, Sentence-BERT, PyPDF2, Gemini API, HTML/CSS  
- Built an NLP-powered app to match resumes with job descriptions.  
- Extracted and analyzed skills, experience, and education from PDF/DOCX files.  
- Used Sentence-BERT and cosine similarity for semantic match scoring.  
- Integrated Google Gemini API for advanced parsing and ranking.  
- Developed an interactive and secure Flask-based web interface.  
[🧑‍💻 GitHub](https://github.com/SETHU0010/Automated-Resume-Parsing)

---

### 5. ⚙️ Load Focus Testing for VTOP Website  
**Key Skills:** Performance Testing, Load Focus, Web Monitoring, Analysis  
- Conducted performance/load testing on the VTOP university portal.  
- Simulated concurrent user access and analyzed bottlenecks.  
- Provided insights to improve backend response and scalability.  
[📈 GitHub](https://github.com/SETHU0010/Load-Focus-Testing-for-VTOP-Website)

---

### 6. ☁️ Privacy Preserving Data Security Model in Cloud Using AES Algorithm  
**Key Skills:** AES, Cloud Security, Python, Cryptography, BYOEK  
- Designed a security model for cloud environments using AES and BYOEK.  
- Addressed secure storage and access of sensitive data in cloud platforms.  
- Evaluated risks and ensured robust access control mechanisms.  
[🔒 GitHub](https://github.com/SETHU0010/Privacy-Preserving-Data-Security-Model-in-Cloud-Using-AES-Algorithm)

---

### 7. 🏭 Industrial Copper Modeling  
**Key Skills:** Python, EDA, Regression, Streamlit, Feature Engineering  
- Solved real-world manufacturing domain problems related to pricing and sales.  
- Performed exploratory data analysis and handled outliers/skewness.  
- Built regression and classification models to predict selling price.  
- Created an interactive Streamlit app for real-time predictions and visualization.  
[🏗️ GitHub](https://github.com/SETHU0010/Industrial-Copper-Modeling)
    """)

def certifications_page():
    st.header("🏆 Certifications")
    st.markdown("""
<div style='color: green; font-size: 16px;'>
✅ <b>Data Science Math Skills</b> – Duke University (Coursera)<br>
✅ <b>Development of Real-Time Systems</b> – EIT Digital (Coursera)<br>
✅ <b>SQL</b> – CareerNinja | LearnTube<br>
✅ <b>Training of Trainers</b> – NPTEL Swayam 2022<br>
✅ <b>Financial Literacy</b> – UNICEF<br>
✅ <b>Fundamentals of Data Analytics</b> – NASSCOM | Learn Future Skills Primely
</div>
    """, unsafe_allow_html=True)

def courses_page():
    st.header("📚 Courses")
    courses = """
- **Introduction to Computer Application**  
  [📄 View Certificate](https://drive.google.com/file/d/1EMy2DzhcBwlNSxjCTci1ONwCcISC7JEH/view?usp=drive_link)

- **Marketing Management**  
  [📄 View Certificate](https://drive.google.com/file/d/1YPcWDWIFmxZ-hQnBnGGqEhEi9sfiYPBY/view?usp=drive_link)

- **PowerBI**  
  [📄 View Certificate](https://www.guvi.in/share-certificate/46442ir71S1h7G6NE4)

- **Generative AI**  
  [📄 View Certificate](https://www.guvi.in/share-certificate/2h47Id1eE19C165f7y)
    """
    st.markdown(courses)

def internship_page():
    st.header("🎯 Internship Experience")
    st.markdown("""
### 🧠 Intelligent Automation Services - Intern  
*Mavdero Technologies (Sep 2023 – Mar 2024)*  
- Developed AI-driven resume parsing & skill-matching tools.  
- Conducted software testing to ensure efficiency & accuracy.  
- Built automation frameworks and debugged real-world AI projects.  

---

### 🎓 Trainer – Data Analytics in Process Industries  
*GUVI Geek Network Pvt. Ltd. | Naan Mudhalvan Initiative*  
- Conducted workshops using Python, SQL, Power BI.  
- Mentored students to build hands-on data science projects.  
- Created course materials and assessments for analytics learning.
    """)

def professional_experience_page():
    st.header("💼 Professional Experience")

    st.markdown("""
### 🧑‍🏫 Teaching Cum Research Assistant (TRA)  
*Vellore Institute of Technology (VIT)*  
📅 **Aug 2025 – Present**

- Assisting in teaching, research, and academic activities under the School of Computer Science Engineering and Information Systems (SCORE).  
- Responsibilities include conducting tutorials, evaluations, and project supervision.  
- Research focus involves continuous learning, publication of Scopus-indexed papers, and contributing to departmental academic excellence.
    """)

def extracurricular_activities_page():
    st.header("🎉 Extracurricular Activities")
    st.markdown("""
- **Cultural Event Organizer** 🎭  
  Managed university cultural events, coordinated logistics, and ensured success.

- **Finance Head** 💰  
  Oversaw budgets, tracked expenses, and ensured transparency for student organizations.
    """)

# Main function
def main():
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    init_sidebar()

    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Contact":
        contact_page()
    elif st.session_state.page == "Education":
        education_page()
    elif st.session_state.page == "Skills":
        skills_page()
    elif st.session_state.page == "Projects":
        projects_page()
    elif st.session_state.page == "Certifications":
        certifications_page()
    elif st.session_state.page == "Courses":
        courses_page()
    elif st.session_state.page == "Internship":
        internship_page()
    elif st.session_state.page == "Professional Experience":
        professional_experience_page()
    elif st.session_state.page == "Extracurricular Activities":
        extracurricular_activities_page()

if __name__ == "__main__":
    main()
