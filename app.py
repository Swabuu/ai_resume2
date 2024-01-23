from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Anton Ivarsson"
PAGE_ICON = ":wave:"
NAME = "Anton Ivarsson"
DESCRIPTION = """
Cooking something great | Telecom Enthusiast | Ex-Twilio
"""
EMAIL = "antonivarsson@proton.me"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/anton-ivarsson",
    "GitHub": "https://github.com/Swabuu",
}
PROJECTS = {
    ":calling: mccmnc.se - Webscraped mobile network operator data. Includes subscriber counts and network owners as well as the technology used": "https://mccmnc.se/",
    ":iphone: A simple Android application which parses incoming SMS messages and sends the Sender ID, MSISDN (destination), SMS Body and SMSC-address to an external webservice": "https://github.com/Swabuu/testunit"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
st.write("#")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 12 Years experience working with or for Mobile Network Operators
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of mobile networks, the SS7 stack and mobile operator elements
- ✔️ Excellent at troubleshooting and finding insightful data and a way to share them with others 
"""
)


# --- About ---

st.write("#")
st.subheader("About")
st.write(
    """
    #SS7 #A2P #SMS #SMPP

Hi! I'm Anton! 

I'm a telecom enthusiast interested in everything related to mobile networks, A2P (Application-to-Person) SMS and the wholesale messaging community. I'm also very passionate about data (everything from acquiring data, cleaning it and building something beautiful out of it) and learning new technologies.

Professionally I've been both technically and commercially active since 2013, working in the same broader business but for a few different companies, doing a bit of everything. I believe that having a broad understanding of how things work gives you the unique ability to see things that others might not. 
    """)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 📲 The SMPP protocol & the SS7 stack
- 📚 Python Programming
- 📊 Microsoft Office (Excel, MS Access etc) & Google Suite (Google Sheets etc)
- 📈 Tableau, Kibana
- 🗄️ Relational databases & Structured Query Languages (SQL)
- 📉 Data exploration & analysis: Pandas, NumPy
- 👩‍💻 Gathering useful information (building custom web scrapers, extracting information from excel/txt/csv/[filetype] -files programmatically)
- 📚 Data visualisation: Matplotlib, Plottly, Streamlit etc
- 🗄️ Natural language processing: NLTK
- 📚 Front-end frameworks: VueJS, Flask
- ⚙️ Automation


Keywords: SS7, SMPP, HTTPS, A2P & P2P, Routing & Procurement strategy, Business Development, Financial Analyst, Revenue Manager, SQL, Python, Data Analyst, Connectivity, SMS, Carrier Business, Quality Assurance & Monitoring, Business Intelligence, HUB management, Databases
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 0
st.write("🚧", "**Head of Signaling & Fraud Prevention @ Adeo Telecom** | Stockholm, Sweden")
st.write("10/2023 - 12/2023")
st.write(
    """
- ► A2P SMS Messaging Strategy: Develop and implement strategies for Application-to-Person (A2P) SMS messaging, optimizing yield management and revenue management.
- ► SS7 Stack Optimization: Utilise expertise in SS7 stack optimization to enhance network efficiency.
- ► Increase Coverage: Work towards expanding the network coverage to reach a wider audience.
- ► Carrier Relations: Foster and manage strong relationships with carriers, ensuring smooth operations and maximising coverage.
- ► Business Development: Identify and pursue opportunities for business expansion and growth in the A2P SMS industry.
- ► Commercial Way Forward: Contribute to the development of commercial strategies to drive the Company's success.
"""
)

# --- JOB 0
st.write("🚧", "**Routing Manager @ Tele2 Group** | Stockholm, Sweden")
st.write("03/2023 - 08/2023")
st.write(
    """
- ► Develop and support new and existing products to maximize quality, profitability and revenue.
- ► Determine the pricing strategy and positioning of the product line, locally and globally.
- ► Collaborate with the messaging team and partners/suppliers to ensure best offerings for Tele2 partners and assure smooth day-to-day system operations.
- ► Test/implement supplier routes, and review cost/supplier changes to make corresponding routing decisions.
- ► Prepare and distribute reports on trends and new opportunities that arise.
- ► Collect, process and analyze data to identify cost-saving and quality improvement opportunities.
- ► Engage frequently with Account Managers to help build up traffic and support the sales team by providing relevant data and recommendations.
- ► Improving the routing quality, resulting in increased customer satisfaction and reduced churn rate.
- ► Successfully formulating pricing strategies that is boosting product quality, profitability and revenue.
- ► Automating pricelist format conversion and upload, resulting in reduced manual labor and errors.
- ► Implementing quality assurance processes and procedures that improves product quality and reliability.
- ► Maintaining strong supplier relationships that enables fast escalation and resolution of routing failures.
- ► Conducting in-depth traffic analysis that leads to the discovery of new revenue opportunities.
- ► Playing a key role in developing and launching new products that meets partner needs and expectations.
- ► Collaborating with cross-functional teams to deliver outstanding service to partners and drive business growth.
"""
)

# --- JOB 1
st.write("🚧", "**Yield Manager @ Twilio Inc.** | San Fransisco, California, USA")
st.write("01/2021 - 12/2022")
st.write(
    """
- ► In each given moment, and over time, maximize the revenue and GP$ yield harvested from Twilio’s largest messaging accounts for the EMEA market by optimizing the utilization of available routing options.
"""
)
#- ► Responsible for EMEA 
# --- JOB 2
st.write("#")
st.write("🚧", "**International Messaging Specialist @ Twilio Inc.** | San Fransisco, California, USA")
st.write("08/2020 - 01/2021")
st.write(
    """
- ► Optimising routing and procurement decisions within Twilio’s strategic, wholesale and OTT customer base.
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Manager, Routing & Product @ Sipstatus Communications Srl** | Bucharest, Romania")
st.write("02/2020 - 08/2020")
st.write(
    """
- ► Cooking something great on the SMS side of Sipstatus.
"""
)

# --- JOB 4
st.write("#")
st.write("🚧", "**CTO | Soatso AB** | Lachen, Switzerland")
st.write("07/2019 - 01/2020")
st.write(
    """
    Soatso provides reach for providers, excelling in mutual success and long term relations. We have an
incredible toolbox to maximize reach and longevity with a team designed to be streamlined and agile.

- ► SS7 configuration, monitoring, testing
- ► Open IW connectivity (SMS & HLR)
- ► Development of engine modules, mainly in Python
- ► Development of Business Intelligence tool and automatic reporting
- ► Server management (Linux & Windows)
- ► Sales, procurement & strategy
"""
)

# --- JOB 5
st.write("#")
st.write("🚧", "**Director, Business Development @ Calltrade Carrier Services AG | Altendorf, Switzerland**")
st.write("03/2017 - 07/2019")
st.write(
    """
- ► Sales, procurement & strategy
- ► Development of Business Intelligence tools
- ► New business initiatives from idea to realisation
- ► SS7 Connectivity
- ► Face of the company in international business events"""
)

# --- JOB 6
st.write("#")
st.write("🚧", "**Routing Manager, International Carrier Business & A2P @ Tele2 Group**")
st.write("08/2016 - 03/2017")
st.write(
    """
- ► Creation and maintenance of A2P products
- ► Implementation of routing strategies
- ► Maintaining A2P- & P2P-routing tables
- ► HUB management
- ► Route quality assurance & traffic flow monitoring
- ► Price and cost management"""
)

# --- JOB 7
st.write("#")
st.write("🚧", "**Financial SMS Analyst, International Carrier Business & A2P @ Tele2 Group**")
st.write("04/2016 - 08/2016")
st.write(
    """
- ► Creation and maintenance of A2P products
- ► Implementation of routing strategies
- ► Maintaining A2P- & P2P-routing tables
- ► HUB management
- ► Route quality assurance & traffic flow monitoring
- ► Price and cost management"""
)

# --- JOB 8
st.write("#")
st.write("🚧", "**Support Technician @ Bosbec AB**")
st.write("01/2015 - 04/2016")
st.write(
    """
- ► Created a support function, sustainable procedures and support workflows
- ► Procured the messaging services by signing contracts with operators and suppliers to face troubled markets 
- ► Negotiated and communicated with suppliers to keep the routing optimized, stabilized and as profitable as possible
- ► Took care of the project management for delivering workflow solutions to customers
- ► Worked in a smaller dynamic team, all contributing to developing a flexible API to power businesses' workflows
"""
)

# --- JOB 9
st.write("#")
st.write("🚧", "**Routing Officer @ Fortytwo.** | St Julian's Malta")
st.write("01/2015 - 04/2016")
st.write(
    """
- ► Optimized in-house routing systems, wholesale products and tailor-made solutions
- ► Monitored and maintained SMS-MT, SMS-MO and Number Lookup Services
- ► Set up, tested and troubleshooted new providers, connections and routes
- ► Acted as a bridge between the Technical Department and the Commercial Department
- ► Made sure the A2P products were as stable and profitable as possible
- ► Conducted price and market research
- ► "On-Call" for emergencies to ensure quality regardless of the hour
"""
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



# --- Endorsement 1 ---
st.write("#")
st.subheader("Endorsements")
st.write("---")

st.markdown('''
**James Williams**  
Director of Programmes, [Mobile Ecosystem Forum](https://mobileecosystemforum.com/)
> "I am showing my age I know, but I have now worked in the area of Telecommunications for over 20 years. During my time in the industry I have come across many excellent personnel but what makes Anton stand out from the professional and knowledgeable is his genuine, infectious passion for the business. This drives him to update and expand his areas of expertise continually. His excellent skillset, flexibility and the enthusiasm he shows make him an asset for any organisation."
''')

# --- Endorsement 2 ---
st.write("---")

st.markdown('''
**Tanja Andrén**  
Software Development Engineer, [Sinch](https://www.sinch.com/).


> "Anton is an amazing professional with a brilliant mind. I had the privilege to work alongside Anton in 2017 and he kept impressing me with his drive and passion for the business that he manages to build real things from. He has the ability and skill sets to realise any idea, and he has a lot of them. It has been very inspiring to work with Anton and I would recommend him to any team or organisation."
''')

# --- Endorsement 3 ---
st.write("---")

st.markdown('''
**Daniela Jovic** | COO at [Spacemanic](https://www.spacemanic.com/) - We make access to space as easy as ordering a cab! 🛰 Project Captain of the first Croatian satellite: CroCube 📡 #nanosatellite #CubeSat #newspace #spacetechnology #spaceindustry 🚀

Working on a global market in the telecom and mobile industry since 2011. 
> "When it comes to telecommunications, Anton has it all... He represents a great combination of technical and commercial. He can help you with SS7 and SMPP just as much as he can help with creating a great business strategy. What I like about working with Anton the most is, he is always very professional, ready to help... and never boring! Very much like myself, Anton belongs to the group of people for whom SMS and telecommunications became a passion in life. And trust me, he truly is a valuable member of the SMS/telco community."
''')
