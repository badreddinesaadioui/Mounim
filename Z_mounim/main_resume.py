from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Mounim_Saadioui.pdf"
profile_pic = current_dir / "assets" / "mounimpic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Mounim Saadioui"
PAGE_ICON = ":wave:"
NAME = "Mounim Saadioui"
DESCRIPTION = """
@ENSIAS specializing in business intelligence, strategy, and machine learning. 
Actively seeking new opportunities in Data Science & Analytics with a passion for generative AI innovations.
"""
EMAIL = "mounim.saadiouii@gmail.com"
PROJECTS = {
    "🏆 Data Visualization Project - BI Offers Analysis from Job Sites": "https://github.com/mouniiim/data-visualization",
    "🏆 Generative AI Project - Callbot with RAG, Voice-to-Text, and Text-to-Voice": "https://github.com/mouniiim/callbot-voice-ai"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=280)

with col2:
    st.markdown(f"""
    <h5 style='text-align: left; ;font-size: 30px;'>{NAME}</h5>"""
    , unsafe_allow_html=True)
    st.markdown(f"""
    <h5 style='text-align: left; ;font-size: 18px;'>Data Analytics Engineer</h5>"""
    , unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )


# --- SOCIAL LINKS ---
st.write('\n')
import streamlit as st

SOCIAL_MEDIA = {
    "🔗LinkedIn": "https://www.linkedin.com/in/mounim-saadioui/",
    "🤖 GitHub": "https://github.com/mouniiim"
}
EMAIL = "mounim.saadiouii@gmail.com"
cols = st.columns([1, 1, 2]) 
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
cols[2].markdown(f"📩 <a href='mailto:{EMAIL}'>{EMAIL}</a>", unsafe_allow_html=True)



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, R, C, HTML/CSS, JavaScript
- 📊 Data Visualization: Plotly, PowerBI, Matplotlib, Seaborn
- 🗄️ Databases: MySQL, SQL Server, NoSQL
- 🛠️ Tools/Platforms: Git, Docker, Google Cloud, Spark, Hadoop
"""
)
st.write("---")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")


# --- JOB 1
st.write("🚧", "**Data Analyst Scientist | AXA Casablanca, Morocco**")
st.write("Feb 2024 - Present (6 months)")
st.write(
    """
- ► Implemented an analytics model for automating health claim case management, improving automation by 18%.
- ► Contributed to the Golden Record project for client data integration, enhancing unified client identity visibility.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Scientist | YAKEEY, Casablanca, Morocco**")
st.write("Jun 2023 - Aug 2023 (3 months)")
st.write(
    """
- ► Integrated geospatial data from Google Maps into a database of service locations in Morocco.
- ► Developed a scoring system based on the proximity of real estate to services.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Scientist | ENSIAS & CHU Casablanca, Morocco**")
st.write("Mar 2023 - Jun 2023 (4 months)")
st.write(
    """
- ► Improved the quality of medical images and developed a model to extract blood vessels for detecting diabetic retinopathy with 93% accuracy.
- ► Designed a CNN U-Net architecture for retinal image segmentation.
"""
)
st.write("---")

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")

st.write('\n')
st.write("🎓", "**Engineering Degree in Business Intelligence & Data Analytics | ENSIAS**")
st.write("Sep 2021 - Present")
st.write(
    """
- ► Specialization in machine learning, business intelligence, and data analytics.
"""
)
st.write("---")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Publications")

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
