import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Sethumadhavan V's Portfolio", page_icon=":briefcase:", layout="wide")

st.title("Sethumadhavan V")
st.subheader("M.Tech Software Engineering")

# Define the main function
def main():
    # Initialize session state if not present
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    # Top navigation buttons
    st.header("")
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    with col1:
        if st.button("Home"):
            st.session_state.page = "Home"
    
    with col2:
        if st.button("Contact"):
            st.session_state.page = "Contact"
    
    with col3:
        if st.button("Education"):
            st.session_state.page = "Education"
    
    with col4:
        if st.button("Skills"):
            st.session_state.page = "Skills"
    
    with col5:
        if st.button("Projects"):
            st.session_state.page = "Projects"
                
    with col6:
        if st.button("Certifications"):
            st.session_state.page = "Certifications"
    
    with col7:
        if st.button("Courses"):
            st.session_state.page = "Courses"

    with col8:
        if st.button("Extracurricular Activities"):
            st.session_state.page = "Extracurricular Activities"
                
    # Display the selected section
    if st.session_state.page == "Home":
        st.title("👋 Welcome to Sethumadhavan V's Portfolio")
        st.write(
            "Hello! I’m Sethumadhavan V, a recent M.Tech graduate in Software Engineering from Vellore Institute of Technology, currently based in Sholingur. I’m passionate about data analysis and leveraging my expertise in Python and SQL to turn complex data into actionable insights.\n\n"
            "My academic and project experiences have equipped me with a solid foundation in data analysis, visualization, and software development. I am skilled in creating dynamic data solutions and ensuring data security and integrity through encryption and advanced algorithms.\n\n"
            "I am currently advancing my knowledge in Master Data Science at GUVI - ZEN Class, IIT-M, and hold certifications in SQL, PowerBI, Marketing Management, and Financial Literacy. These qualifications enhance my ability to manage, analyze, and visualize data effectively.\n\n"
            "In addition to technical skills, I excel in critical thinking, time management, and CRM, which enable me to tackle data challenges with creativity and efficiency. I am eager to contribute to a dynamic team and apply my skills to drive impactful business decisions. Feel free to explore my portfolio and connect with me on LinkedIn or GitHub to learn more about my work."
        )

    elif st.session_state.page == "Contact":
        st.header("📞 Contact Information")
        contact_info = """
        - **Phone:** [9159299878](tel:9159299878)
        - **Email:** [sethumadhavanvelu2002@gmail.com](mailto:sethumadhavanvelu2002@gmail.com)
        - **Location:** Sholingur
        - **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/sethumadhavan-v-b84890257/)
        - **GitHub:** [SETHU0010](https://github.com/SETHU0010)
        - **WhatsApp:** [Chat with me](https://wa.me/9159299878)
        """
        st.markdown(contact_info)
    
    elif st.session_state.page == "Certifications":
        st.header("🏆 Certifications")
        # Define certification data
        certifications = {
            "Certification": [
                "Introduction to Computer Application",
                "Marketing Management",
                "Data Science Math Skills",
                "Development of Real-Time Systems",
                "SQL",
                "Training of Trainers",
                "Financial Literacy",
                "Fundamentals of Data Analytics",
                "PowerBI"
            ],
            "Institution": [
                "VIT Online Learning (VITOL) Institute",
                "VIT Online Learning (VITOL) Institute",
                "Duke University | Coursera",
                "EIT Digital | Coursera",
                "CareerNinja | LearnTube",
                "NPTEL Swayam 2022",
                "UNICEF",
                "Learn Future Skills Primely | NASSCOM 2022",
                "GUVI Geek Networks, IITM Research Park"
            ]
        }
        # Display certifications as a DataFrame
        df_certifications = pd.DataFrame(certifications)
        st.dataframe(df_certifications)
    
    elif st.session_state.page == "Education":
        st.header("🎓 Education")
        education = """
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
    
    elif st.session_state.page == "Skills":
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
    
    elif st.session_state.page == "Projects":
        st.header("🚀 Projects")
        st.write("""
        ### 1. Secure Data Sharing of Personal Health Records in SQL Using AES Algorithm
        Implemented AES algorithm for protecting personal health records in SQL environments. Developed efficient algorithms for
        keyword-based searching and data sharing operations. Ensured privacy and security in data management.

        Project Link: [GitHub](https://github.com/SETHU0010/SECURE_E_PERSON_HEALTH_CARE_SYSTEM_USING_AES_ALGORITHM)

        ### 2. Uber Fare Prediction and Streamlit Web Application
        Developed a machine learning model to predict Uber fares and created a Streamlit web app for real-time fare estimates. 🚖💵 
        Utilized Python 🐍, AWS ☁️, and Streamlit 🌐 to deliver accurate predictions and a user-friendly interface. Demonstrates skills 
        in data science 📊, machine learning 🤖, and cloud deployment ☁️🚀.

        Project Link: [Streamlit App](https://uberfarepredictionandappwebapplication-t3fru4dygszajbwgqppgzv.streamlit.app/)

        ### 3. YouTube Data Harvesting and Warehousing using SQL and Streamlit
        Led the performance testing of the VTOP website with Load Focus. Configured and executed load tests, monitored real-time
        performance, and analyzed metrics to identify and address bottlenecks. Generated detailed reports and provided actionable 
        insights to enhance website stability and user experience under high traffic conditions. Successfully improved site resilience 
        and performance through rigorous testing and analysis.

        Project Link: [Streamlit App](https://youtubedataharvestingandwarehousingusingsqlandapp-nzfhhsps4haa.streamlit.app/)

        ### 4. Load Focus Testing for VTOP Website
        Implemented AES algorithm for protecting personal health records in SQL environments. Developed efficient algorithms for
        keyword-based searching and data sharing operations. Ensured privacy and security in data management.

        Project Link: [GitHub](https://github.com/SETHU0010/Load-Focus-Testing-for-VTOP-Website)

        ### 5. Privacy Preserving Data Security Model in Cloud Using AES Algorithm
        Experienced professional with expertise in cloud computing security and data protection. Skilled in implementing cryptographic 
        algorithms and BYOEK platforms to ensure secure storage and access control of sensitive data in the cloud. Proven track record 
        of developing and evaluating security models to address privacy concerns and mitigate potential risks.

        Project Link: [GitHub](https://github.com/SETHU0010/Privacy-Preserving-Data-Security-Model-in-Cloud-Using-AES-Algorithm)

        ### 6. Industrial Copper Modeling
        Addressed challenges in sales and pricing data with Python 🐍, data preprocessing, EDA, and regression/classification modeling. 
        Developed a Streamlit GUI for interactive data exploration. Employed feature engineering and model optimization to enhance 
        predictive accuracy and insights. Demonstrated proficiency in handling manufacturing domain-specific data and providing actionable 
        insights through effective visualization and analysis.

        Project Link: [GitHub](https://github.com/SETHU0010/Industrial-Copper-Modeling)
        """)
    
    elif st.session_state.page == "Courses":
        st.header("📚 Courses")
        courses = """
        - **Master Data Science**  
          GUVI - ZEN Class ,IIT-M Advanced Programming Professional
          
          Feb 2024 - Jul 2024
          
        """
        st.markdown(courses)
    
    elif st.session_state.page == "Extracurricular Activities":
        st.header("🎉 Extracurricular Activities")
        extracurricular_activities = """
        - **Cultural Event Organizer**  
          Organized and managed cultural events at VIT, enhancing leadership and teamwork skills.
          
        - **Finance Head**  
          Managed finances for various student clubs and events, ensuring budget adherence and financial transparency.
        """
        st.markdown(extracurricular_activities)

# Run the main function
if __name__ == "__main__":
    main()
