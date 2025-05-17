import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Sethumadhavan V's Portfolio", page_icon=":briefcase:", layout="wide")

# Initialize the sidebar with emojis as icons and download resume option
def init_sidebar():
    st.sidebar.header("Navigation")
    nav_options = {
        "🏠 Home": "Home",
        "📞 Contact": "Contact",
        "🎓 Education": "Education",
        "💡 Skills": "Skills",
        "🚀 Projects": "Projects",
        "🏆 Certifications": "Certifications",
        "📚 Courses": "Courses",
        "🎯 Internship": "Internship",  # New Internship Page
        "🎉 Extracurricular Activities": "Extracurricular Activities",
    }
    selection = st.sidebar.radio("Go to", list(nav_options.keys()))
    st.session_state.page = nav_options[selection]

# Define page content functions
def home_page():
    st.title("👋 Welcome ")
    
    st.write(
        """
        Hello! I'm Sethumadhavan V, a recent M.Tech graduate in Software Engineering from Vellore Institute of Technology. With expertise in Python and SQL, I am passionate about data analysis and leveraging data to drive impactful business decisions.

        Currently, I am further honing my skills through the Master Data Science course at GUVI - ZEN Class, IIT-M. My experience includes working on diverse projects like secure data sharing, YouTube data harvesting, and interactive data visualization.

        My goal is to contribute to a dynamic team as an entry-level data analyst, where I can apply my analytical skills and problem-solving abilities to uncover valuable insights and support data-driven decision-making.

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
    st.markdown("[Download Resume](https://drive.google.com/file/d/1jmzA7mhg4qxoLXuBLNcZEPFHZoanP04C/view?usp=drive_link)")

def education_page():
    st.header("🎓 Education")
    education = """

    - **Master Data Science**  
      GUVI - ZEN Class ,IIT-M Advanced Programming Professional  
      Feb 2024 – Jul 2024
      
    - **M.Tech Integrated Software Engineering**  
      Vellore Institute of Technology, Vellore  
      2019 – 2024

    - **Higher Secondary Education**  
      Sri Ayyan Vidyashram Higher Sec School  
      2018 – 2019

    - **Secondary School Leaving Certificate**  
      Sri Ayyan Vidyashram Higher Sec School  
      2016 – 2017
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
    st.write("""
    ### 1. Secure Data Sharing of Personal Health Records in SQL Using AES Algorithm
    Implemented AES algorithm for protecting personal health records in SQL environments.

    [🔗 GitHub](https://github.com/SETHU0010/SECURE_E_PERSON_HEALTH_CARE_SYSTEM_USING_AES_ALGORITHM)

    ### 2. Uber Fare Prediction and Streamlit Web Application
    ML model + Streamlit app for Uber fare estimates.  
    [🚀 Streamlit App](https://uberfarepredictionandappwebapplication-t3fru4dygszajbwgqppgzv.streamlit.app/)

    ### 3. YouTube Data Harvesting and Warehousing using SQL and Streamlit
    End-to-end solution for channel/video data tracking.  
    [🎥 App](https://youtubedataharvestingandwarehousingusingsqlandapp-nzfhhsps4haa.streamlit.app/)

    ### 4. Load Focus Testing for VTOP Website
    Performance testing using Load Focus tools.  
    [📈 GitHub](https://github.com/SETHU0010/Load-Focus-Testing-for-VTOP-Website)

    ### 5. Privacy Preserving Data Security Model in Cloud Using AES Algorithm
    AES and BYOEK for cloud storage privacy.  
    [🔒 GitHub](https://github.com/SETHU0010/Privacy-Preserving-Data-Security-Model-in-Cloud-Using-AES-Algorithm)

    ### 6. Industrial Copper Modeling
    Manufacturing data modeling using Streamlit & ML.  
    [🏭 GitHub](https://github.com/SETHU0010/Industrial-Copper-Modeling)
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
    - 💡 Developed AI-driven resume parsing & skill-matching tools  
    - 🔍 Conducted software testing to ensure efficiency & accuracy  
    - 🧰 Built automation frameworks and debugged real-world AI projects  

    ---

    ### 🎓 Trainer – Data Analytics in Process Industries  
    *GUVI Geek Network Pvt. Ltd. | Naan Mudhalvan Initiative*  
    - 🧪 Conducted workshops using Python, SQL, Power BI  
    - 👥 Mentored students to build hands-on data science projects  
    - 🛠️ Created course materials and assessments for analytics learning
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
    elif st.session_state.page == "Extracurricular Activities":
        extracurricular_activities_page()

if __name__ == "__main__":
    main()
