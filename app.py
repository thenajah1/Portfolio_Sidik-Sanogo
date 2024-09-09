from pathlib import Path
import  json
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


#----- PATH SETINGS ----------------#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
#resume_file = current_dir / "actif" / "CV-Datascience_Sidik_SANOGO.pdf"#
profile_pic = current_dir / "actif" / "phot.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio Sidik"
PAGE_ICON = ":computer:"
DESCRIPTION = """

My passion for data has led me from a full-stack developer role to becoming a professional in data science and AI, crafting a hybrid profile that enriches my technological vision. With 3 years of experience, including 2 years in data and 1 year in development, this journey reflects my analytical mindset 🔍 and my eagerness to learn, driving me into AI development.

Armed with a solid academic background 🎓 and proven experience in IT project management 📈 and data analysis, I excel at transforming data into strategic insights. My interest in entrepreneurship, particularly in real estate 🏠, adds another layer to my expertise, blending technological innovation with sharp business acumen to reshape real estate strategies through a data-driven approach.

Expertise: Data Analysis | Big Data | Python | Scikit-learn | Keras | TensorFlow | Streamlit | Microsoft Azure | Microsoft Power BI | APIs and Event-Driven Architectures | Internal and External Communication | Project Management | Stakeholder Relation Management | Solution and Conflict Management

International Experience: Fluent in spoken and written English and French.
"""
#EMAIL = "sidiksanogo766@gmail.com"#
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/aboubacar-sidik-sanogo1/",
    "GitHub": "https://github.com/thenajah1",
    "FaceBook": "https://www.facebook.com/sance.sanogo/",
    "Instagram": "https://www.instagram.com/st___najah/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
#with open(resume_file, "rb") as pdf_file:
    #PDFbyte = pdf_file.read()#
profile_pic = Image.open(profile_pic)

# ------------- Animations ----------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return  json.load(f)

# --- Main SECTION ---
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.image(profile_pic, width=260)
with col3:
    lottie_hello = load_lottiefile("lottiefiles/Hello animation.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height =None,
        width=None,
        key=None,
    )
    lottie_hi = load_lottiefile("lottiefiles/Robo Hi.json")
    st_lottie(
        lottie_hi,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height =None,
        width=None,
        key=None,
    )
with col2:
    st.title(":red[Sidik SANOGO]")
    st.write(DESCRIPTION)
    #st.download_button(
       # label=" 📄 Télécharger mon cv",
        #data=PDFbyte,
        #file_name=resume_file.name,
        #mime="application/octet-stream",
    #)
   # st.write("📫 :red[**EMAIL** :] ", EMAIL)

# --- SOCIAL LINKS ---
st.write('📲:red[Connect With Me :]👇\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- EXPERIENCE PROFESSIONNELLE ---
st.write('\n')
st.subheader(":green[📜EXPERIENCES PROFESSIONNELLES]")
st.write("---")
col21, col22 = st.columns(2, gap="small")
with col21:
    st.write(
    """
DATA SCIENTIST |
Depuis mars 2024 | IDAOS, Paris

🐍 Mission 1: Data analysis and AI application development using embeddings with a Streamlit interface to optimize moderation.
Method and Result: Leveraged Python and OpenAI API for quick access to user response data, achieving a time savings of over 85%.

💡Mission 2: Implementation of scripts to detect negative e-reputation and automation of AO (Appel d'Offres) searches.
Method and Result: Utilized web scraping and NLP techniques to filter articles and automate searches, reducing the time required for detecting negative articles and AO searches by 50%.

📰 Mission 3: Conducted training sessions on GenAI.
Method and Result: Developed interactive training modules on using GenAI, enabling teams to quickly master generative AI tools, thereby increasing efficiency and innovation in projects.

______________________________________________________________________________________________________________________________________________________________________________________________________

DIGITAL DATA ANALYST |
D'août 2023 à février 2024 | IDAOS, Paris

🔍 Mission: Exploratory data analysis of real estate web data, strategic monitoring, and use of visualization tools.
Method and Result: Conducted analysis using linear regression and time series, revealing key trends to refine decisions on tenant complaints.


______________________________________________________________________________________________________________________________________________________________________________________________________

ASSISTANT DÉVELOPPEUR Back-End |
De juillet 2020 à janvier 2021 | ICMGC, Abidjan

📚 Mission: Analysis of healthcare agents' performance and creation of activity monitoring reports.
Method and Result: Analyzed key performance indicators and created interactive dashboards with Power BI, enabling effective monitoring of agent productivity.


______________________________________________________________________________________________________________________________________________________________________________________________________

ASSISTANT DÉVELOPPEUR Backend |
De juillet 2019 à janvier 2020 | ETS AL SIDICK, Abidjan

🛠 Mission: Developed a digital library.
Method and Result: Utilized PHP, JavaScript, SQL, and ULM, leading to efficient resource management and improved access to documents.

"""
)
with col22:
    lottie_hello = load_lottiefile("lottiefiles/Education.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )

# --- SKILLS ---
st.write('\n')
st.subheader(":green[🛠 COMPETENCES TECHNIQUES]")
st.write("---")
col11, col12 = st.columns(2, gap="small")
with col11:
    st.write(
    """
- Frameworks et Outils

🌐 Web & UI: Symfony, React, Streamlit, Radarly, Phantom Buster

🐳 Conteneurisation et Big Data: Docker, Spark, Hadoop

🗃 Bases de Données & BI: Oracle, Access, Odoo CRM, Excel, Power BI, Tableau, MongoDB

- Langages de Programmation

🐍 Python: Utilisation de bibliothèques de pointe pour le Machine Learning et le Deep Learning, telles que Scikit-learn, TensorFlow, PyTorch, et Keras, ainsi que Pandas pour la manipulation de données et Matplotlib/Seaborn pour la visualisation.

📊 R: Application de dplyr et ggplot2 pour l'analyse et la visualisation des données, ainsi que Shiny pour le développement d'applications web interactives.

🌐 PHP: Mise en œuvre de Laravel (un framework web moderne pour PHP) et utilisation de Composer pour la gestion des dépendances.


📈 SAS: Maîtrise de PROC SQL pour l'interrogation de bases de données et de SAS Macro Language pour l'automatisation des analyses répétitives.

💾 SQL / NoSQL: Connaissance approfondie de MySQL/PostgreSQL pour SQL et MongoDB pour NoSQL, avec un focus sur l'optimisation des requêtes et la modélisation de données.

🔐 PL/SQL: Développement de procédures stockées, fonctions, et déclencheurs pour maximiser les performances et la sécurité dans les environnements Oracle Database.

"""
)

with col12:
    lottie_hello = load_lottiefile("lottiefiles/Skills.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )


st.write('\n')
st.subheader(":green[👨‍🎓DIPLOMES & FORMATIONS]")
st.write("---")
col31, col32 = st.columns(2, gap="small")
with col31:
    st.write("""
         🎓 MASTER INTELLIGENCE ARTIFICIELLE & MANAGEMENT
Décembre 2021 - Juin 2023 | IA SCHOOL, Paris

📊 Probabilités & Statistiques / Machine & Deep Learning: Approfondissement des connaissances théoriques et pratiques essentielles à l'intelligence artificielle, couvrant les techniques avancées de modélisation, d'analyse et de prédiction.

______________________________________________________________________________________________________________________________________________________________________________________________________

👨‍🎓 LICENCE PROFESSIONNELLE EN INFORMATIQUE
Novembre 2018 - Juillet 2021 | HETEC, Abidjan

🛠 Management de projet informatique, Datawarehouse: Acquisition de compétences clés en gestion de projets technologiques et en conception de solutions de stockage de données pour soutenir la prise de décision.

______________________________________________________________________________________________________________________________________________________________________________________________________

🖥 BTS INFORMATIQUE DÉVELOPPEUR D'APPLICATION
Septembre 2018 - Juillet 2020 | HETEC, Abidjan

🌐 Webmaster, Web Design & Infographie: Formation spécialisée dans le développement web, la conception graphique et l'infographie, préparant à la création de sites web visuellement attrayants et fonctionnels.    
    """
    )
with col32:
    lottie_hello = load_lottiefile("lottiefiles/Certifiactions.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )

# --- Projects  ---
st.write('\n')
st.subheader(":green[📚PROJECTS]")
st.write("---")
col41, col42 = st.columns(2, gap="small")
with col41:
    st.markdown("###### [🏀 IA : Prédiction du salaire des joueurs de la NBA Utilisation de modèles de Machine Learning pour analyser et prédire les salaires des joueurs de la NBA en fonction de leurs performances et statistiques, offrant des insights pour les négociations de contrats et les stratégies d'équipe.](https://github.com/thenajah1/NBA-PLAYER-SALARY-PREDICTION)")
    
    st.markdown("###### [🎥 IA : Étude exploratoire des données de sites de films piratés Analyse approfondie des tendances de consommation sur les sites de films piratés, permettant de comprendre les préférences des utilisateurs et d'orienter les stratégies de lutte contre le piratage.](https://github.com/thenajah1/ETUDE-EXPLORATOIRE-DES-DONNEES-DES-SITES-DE-PIRATAGE-DE-FILM)")
    
    st.markdown("###### [🌟 IA : Gestion des Talents à l'Ère de l'Intelligence Artificielle Conception d'un système basé sur l'IA pour optimiser la gestion des talents dans les entreprises, en prédisant les besoins en recrutement et en développement professionnel à travers l'analyse de données.](https://github.com/thenajah1/Gestion-des-Talents-IA)")
    
    st.markdown("###### [🔍 IA : Détection des fausses informations sur les réseaux sociaux Développement d'un outil IA capable d'identifier et de signaler les fausses informations diffusées sur les réseaux sociaux, contribuant à la lutte contre la désinformation.](https://github.com/thenajah1/Detection-des-fausses-informations-sur-les-reseaux-sociaux)")
    
    st.markdown("###### [🌱 IA : Développement de solutions innovantes pour faciliter l'adoption de pratiques de consommation plus durables et éthiques Création de modèles prédictifs visant à encourager les comportements de consommation responsables, à travers l'analyse des tendances de consommation et la suggestion de pratiques durables.](https://github.com/thenajah1/flash)")
    
    st.markdown("###### [📚 DEV : Développement d'une bibliothèque numérique en utilisant PHP, JavaScript (JS), et SQL, permettant un accès facile et organisé à une large gamme de ressources numériques pour les utilisateurs.](https://github.com/thenajah1/DEV)")

with col42:
    lottie_hello = load_lottiefile("lottiefiles/Projects.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )



    
