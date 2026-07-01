from dotenv import load_dotenv
import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------- LOAD ENV ---------------- #
import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Indian Legal Advisor",
    page_icon="⚖️",
    layout="centered"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

/* Remove Streamlit Header */
header[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Hide Streamlit Menu & Footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main Background */
.stApp {
    background-image: linear-gradient(
        rgba(0,0,0,0.80),
        rgba(0,0,0,0.80)
    ),
    url("https://images.unsplash.com/photo-1589829545856-d10d557cf95f");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Main Container */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 2rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    background-color: rgba(0,0,0,0.45);
    border-radius: 20px;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #FFD700;
    text-shadow: 2px 2px 10px black;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 24px;
    color: white;
    margin-bottom: 30px;
    text-shadow: 1px 1px 8px black;
}

/* Global Text */
html, body, p, li, span, label, div {
    color: white !important;
}

/* Input Box */
.stTextInput input {
    background-color: rgba(255,255,255,0.95) !important;
    color: black !important;
    border-radius: 12px;
    padding: 14px !important;
    font-size: 18px !important;
    border: none !important;
}

/* Placeholder */
.stTextInput input::placeholder {
    color: gray !important;
}

/* Button */
.stButton button {
    background-color: #35063E !important;
    color: black !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 10px 24px !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

.stButton button:hover {
    background-color: #35063E !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: rgba(20,20,20,0.92);
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Expander */
.streamlit-expanderHeader {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background-color: rgba(0,0,0,0.65);
    border-radius: 15px;
    padding: 15px;
    margin-top: 15px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Chat Text */
[data-testid="stChatMessage"] * {
    color: white !important;
    font-size: 17px !important;
    line-height: 1.8 !important;
}

/* Spinner */
.stSpinner * {
    color: white !important;
}

/* Footer */
.footer {
    text-align: center;
    color: white;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown(
    "<div class='main-title'>⚖️ Nyaya AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Your Smart Indian Legal Advisor Assistant</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:

    st.title("⚖️ Nyaya AI")

    st.markdown("---")

    st.subheader("📚 What You Can Ask")

    st.write("""
    • Indian Constitution  
    • IPC / BNS Sections  
    • Consumer Rights  
    • Cyber Crime Laws  
    • FIR & Police Procedures  
    • Legal Rights of Citizens  
    • Employment & Labour Laws  
    • Property & Family Laws  
    • Criminal & Civil Cases  
    """)

    st.markdown("---")

    st.subheader("🔥 Popular Queries")

    st.write("""
    • Can police check my phone?  
    • What to do after cyber fraud?  
    • Difference between FIR & NCR  
    • Is recording calls legal in India?  
    • Consumer complaint process  
    • Rights during arrest  
    """)

    st.markdown("---")

    st.warning("""
⚠️ This AI provides legal information and guidance only.
It is NOT a substitute for a licensed advocate.
""")

# ---------------- EXAMPLES ---------------- #
with st.expander("💡 Example Questions"):

    st.write("""
    • What are my rights during police arrest in India?  
    • Is online betting legal in India?  
    • What should I do after a cyber crime?  
    • Explain IPC Section 420  
    • What is Article 21 of Indian Constitution?  
    • Can my employer fire me without notice?  
    • What should I do if someone blackmails me online?  
    • Is recording a phone call legal in India?  
    • Consumer court complaint process  
    • Can police arrest without warrant?  
    """)

# ---------------- PROMPT ---------------- #
template = """
You are Nyaya AI, an expert Indian Legal Advisor AI
with deep knowledge of:

- Indian Constitution
- IPC (Indian Penal Code)
- BNS (Bharatiya Nyaya Sanhita)
- CrPC / BNSS
- Consumer Laws
- Cyber Laws
- Civil & Criminal Laws
- Labour Laws
- Family Laws
- Property Laws
- Fundamental Rights
- Legal Procedures in India

Your job is to help common people understand laws
in simple beginner-friendly language.

Instructions:

- Explain laws in very simple English.
- Mention relevant sections/articles whenever useful.
- Tell whether an action is legal or illegal.
- Explain possible consequences or punishments if needed.
- Guide users on what steps they should take in difficult situations.
- Give practical legal awareness and safety advice.
- Use proper headings and bullet points.
- Keep tone professional, supportive, and easy to understand.
- If a situation is serious, advise consulting a licensed lawyer
  or approaching police/legal authorities.
- Never encourage illegal activities.
- If asked how to commit crimes, hack, scam, or avoid law enforcement,
  politely refuse.

Question:
{query}
"""

prompt = ChatPromptTemplate.from_template(template)

# ---------------- MODEL ---------------- #
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.5
)

# ---------------- CHAIN ---------------- #
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt | model | parser

# ---------------- INPUT ---------------- #
user_input = st.text_input(
    "Ask anything about Indian laws, constitution, rights, or legal issues:",
    placeholder="Example: What should I do if someone threatens me online?"
)

# ---------------- RESPONSE ---------------- #
if st.button("Get Legal Advice"):

    if user_input.strip() == "":
        st.warning("Please enter your legal question.")

    else:

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Analyzing legal query..."):

            response = chain.invoke({
                "query": user_input
            })

        with st.chat_message("assistant"):
            st.markdown(str(response.content))

# ---------------- FOOTER ---------------- #
st.markdown(
    """
    <div class='footer'>
        ⚖️ Nyaya AI • Indian Legal Awareness Assistant
    </div>
    """,
    unsafe_allow_html=True
)
