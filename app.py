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

Ma passion pour les données m’a conduit d’un rôle de développeur full-stack à un professionnel de la science des données et de l’IA, en créant un profil hybride qui enrichit ma vision technologique. Avec 3 ans d’expérience, dont 2 ans dans la data et 1 an dans le développement, ce parcours reflète mon esprit 🔍 analytique et ma soif d’apprendre, me poussant vers le développement de l’IA.

Armé d’une solide formation 🎓 académique et d’une expérience avérée en gestion de 📈 projets informatiques et en analyse de données, j’excelle dans la transformation des données en informations stratégiques. Mon intérêt pour l’entrepreneuriat, en particulier dans l’immobilier 🏠, ajoute une autre couche à mon expertise, en mélangeant l’innovation technologique avec un sens aigu des affaires pour remodeler les stratégies immobilières grâce à une approche axée sur les données.

Expertise: Data Analysis | Big Data | Python | Scikit-learn | Keras | TensorFlow | Streamlit | Microsoft Azure | Microsoft Power BI | APIs and Event-Driven Architectures | Internal and External Communication | Project Management | Stakeholder Relation Management | Solution and Conflict Management

Expérience internationale : Maîtrise de l’anglais et du français parlés et écrits.
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
CHEF DE PROJET MARKETING DATA IA |
Depuis octobre 2024 | Globecast France, Issy-les-Moulineaux

🚀 Mission 1 : Développement d’une data pipeline ETL (AWS S3 + Jupyter) et d’une web app (Streamlit + API OpenAI) pour automatiser la gestion des plans de services.
Résultat : automatisation à 90 %, validation automatique, réduction des erreurs de configuration et allocation optimisée des ressources.

💡 Mission 2 : Organisation de sessions de formation sur la conception d’agents IA marketing.
Résultats : montée en compétence des équipes non techniques et premières implémentations concrètes d’agents IA dans les workflows.

______________________________________________________________________________________________________________________________________________________________________________________________________

DATA SCIENTIST |
De mars à août 2024 | IDAOS, Paris

🤖 Mission : Création d'une solution de modération augmentée basée sur l’approche RAG avec LLM et Streamlit.
Résultats : vectorisation de documents internes et réponses générées en temps réel, réduisant le temps de réponse de +85 %.

______________________________________________________________________________________________________________________________________________________________________________________________________

DIGITAL DATA ANALYST |
D'août 2023 à février 2024 | TOOMOON, Paris

🔍 Mission : Analyse des données web immobilières, veille stratégique et visualisation interactive.
Résultats : détection de tendances clés pour améliorer la gestion des plaintes locataires et l’aide à la décision.

______________________________________________________________________________________________________________________________________________________________________________________________________

HEALTH DATA ANALYST |
De mars 2022 à mai 2023 | COPADES, Freelance

📚 Mission : Analyse des performances des agents de santé et création de dashboards via Power BI.
Résultats : suivi efficace des indicateurs clés.

______________________________________________________________________________________________________________________________________________________________________________________________________

ASSISTANT DÉVELOPPEUR BACK-END |
De août 2021 à décembre 2021 | ICMGC, Abidjan

📘 Mission : Développement d’une bibliothèque numérique pour centraliser et gérer l’accès aux ressources documentaires..
Résultat : mise en œuvre de PHP, JavaScript, SQL et UML, permettant une gestion optimisée des ressources et une amélioration significative de l’accès aux livres.

______________________________________________________________________________________________________________________________________________________________________________________________________

ASSISTANT DÉVELOPPEUR BACK-END |
De juillet 2020 à décembre 2020 | ETS AL SIDICK, Abidjan

🛠 Mission : Développement d’une application de gestion de factures avec symfony et react.
Résultat : application structurée selon la méthode MERISE ; automatisation et fiabilité accrues du processus.

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
st.subheader(":green[🛠 COMPETENCES]")
st.write("---")
col11, col12 = st.columns(2, gap="small")
with col11:
    st.write(
    """
- 🧠 **Compétences Non Techniques**  
💬 Communication efficace  
🧠 Esprit critique  
🔎 Veille stratégique  
🧩 Résolution de problèmes  
⚖️ Sens de l’éthique  
🤝 Collaboration en équipe  

- 🛠 **Compétences Techniques**  
Frameworks / Cloud / Visualisation :  
Docker, Spark, AWS (S3), Git, Snowflake  
Power BI, Tableau, Access  
Symfony, React, Streamlit, SQL Server  
Scikit-learn, Keras, TensorFlow  

Langages de Programmation :  
🐍 Python | 📊 R | 💾 SQL / NoSQL | 🌐 PHP | 📈 SAS  

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



    
