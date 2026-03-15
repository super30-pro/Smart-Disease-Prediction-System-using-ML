import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import time

st.set_page_config(page_title="Smart Disease Prediction", layout="wide")

# ---------- SESSION ----------
if "show_symptoms" not in st.session_state:
    st.session_state.show_symptoms = False

# ---------- BACKGROUND FUNCTION ----------
def set_bg():
    with open("medical_bg.jpg","rb") as img:
        data = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------- CSS ----------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
padding-top:0rem;
margin-top:-30px;
}

.main-panel{
background:rgba(255,255,255,0.92);
padding:40px;
border-radius:16px;
}

.main-title{
font-size:48px;
font-weight:700;
color:#0b2545;
text-align:center;
}

.sub-title{
background:#1d3557;
padding:16px;
border-radius:12px;
text-align:center;
color:white;
font-size:20px;
}

.section-title{
font-size:28px;
font-weight:600;
color:#0b2545;
}

.big-text{
font-size:22px;
color:#1b263b;
}

.result-card{
background:white;
padding:40px;
border-radius:18px;
box-shadow:0px 8px 25px rgba(0,0,0,0.18);
text-align:center;
margin-top:20px;
}

.result-card h1{
font-size:50px;
color:#d62828;
}

</style>
""", unsafe_allow_html=True)

# ---------- SHOW BACKGROUND ONLY ON DASHBOARD ----------
if not st.session_state.show_symptoms:
    set_bg()

# ---------- BUTTON ----------
if st.button("🩺 Enter Symptoms"):
    st.session_state.show_symptoms = True

# ---------- MAIN PANEL ----------
st.markdown('<div class="main-panel">', unsafe_allow_html=True)

st.markdown(
"<h1 class='main-title'>🩺 Smart Disease Prediction System</h1>",
unsafe_allow_html=True
)

st.markdown("""
<div class="sub-title">
AI Powered Medical Diagnosis Dashboard
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- SYMPTOMS ----------
if st.session_state.show_symptoms:

    st.subheader("Enter Symptoms")

    col1,col2,col3 = st.columns(3)

    with col1:
        fever = st.selectbox("Fever",["No","Yes"])
        cough = st.selectbox("Cough",["No","Yes"])
        headache = st.selectbox("Headache",["No","Yes"])
        fatigue = st.selectbox("Fatigue",["No","Yes"])
        vomiting = st.selectbox("Vomiting",["No","Yes"])

    with col2:
        skin_rash = st.selectbox("Skin Rash",["No","Yes"])
        body_pain = st.selectbox("Body Pain",["No","Yes"])
        chills = st.selectbox("Chills",["No","Yes"])
        breathlessness = st.selectbox("Breathlessness",["No","Yes"])
        chest_pain = st.selectbox("Chest Pain",["No","Yes"])

    with col3:
        nausea = st.selectbox("Nausea",["No","Yes"])
        diarrhea = st.selectbox("Diarrhea",["No","Yes"])
        loss_of_appetite = st.selectbox("Loss of Appetite",["No","Yes"])
        sore_throat = st.selectbox("Sore Throat",["No","Yes"])
        runny_nose = st.selectbox("Runny Nose",["No","Yes"])

    predict_button = st.button("Predict Disease")

else:

    fever=cough=headache=fatigue=vomiting="No"
    skin_rash=body_pain=chills=breathlessness=chest_pain="No"
    nausea=diarrhea=loss_of_appetite=sore_throat=runny_nose="No"
    predict_button=False

# ---------- CONVERT ----------
def convert(v):
    return 1 if v=="Yes" else 0

fever=convert(fever)
cough=convert(cough)
headache=convert(headache)
fatigue=convert(fatigue)
vomiting=convert(vomiting)

skin_rash=convert(skin_rash)
body_pain=convert(body_pain)
chills=convert(chills)
breathlessness=convert(breathlessness)
chest_pain=convert(chest_pain)

nausea=convert(nausea)
diarrhea=convert(diarrhea)
loss_of_appetite=convert(loss_of_appetite)
sore_throat=convert(sore_throat)
runny_nose=convert(runny_nose)

# ---------- DATA ----------
diagnosis_map={
"Flu":"Viral infection affecting the respiratory system.",
"Dengue":"Mosquito-borne viral infection causing fever and body pain.",
"Pneumonia":"Infection that inflames air sacs in the lungs.",
"Food Poisoning":"Illness caused by contaminated food.",
"Migraine":"Neurological condition causing severe headaches.",
"Common Cold":"Mild viral infection of nose and throat.",
"Typhoid":"Bacterial infection caused by contaminated food or water.",
"General Infection":"General infection symptoms."
}

precaution_map={
"Flu":"Drink warm fluids and take rest.",
"Dengue":"Stay hydrated and consult doctor.",
"Pneumonia":"Seek medical attention.",
"Food Poisoning":"Drink ORS and avoid outside food.",
"Migraine":"Rest in dark room.",
"Common Cold":"Drink warm fluids.",
"Typhoid":"Avoid outside food.",
"General Infection":"Consult doctor if symptoms persist."
}

doctor_map={
"Flu":"General Physician",
"Dengue":"Infectious Disease Specialist",
"Pneumonia":"Pulmonologist",
"Food Poisoning":"Gastroenterologist",
"Migraine":"Neurologist",
"Common Cold":"General Physician",
"Typhoid":"Internal Medicine Specialist",
"General Infection":"General Physician"
}

# ---------- PREDICTION ----------
if predict_button:

    with st.spinner("Analyzing symptoms..."):
        time.sleep(1)

    if fever and cough and sore_throat and runny_nose:
        prediction="Flu"
    elif fever and body_pain and chills:
        prediction="Dengue"
    elif breathlessness and chest_pain and cough:
        prediction="Pneumonia"
    elif fever and vomiting and diarrhea:
        prediction="Food Poisoning"
    elif headache and nausea:
        prediction="Migraine"
    elif fever and fatigue and cough:
        prediction="Common Cold"
    elif fever and loss_of_appetite and fatigue:
        prediction="Typhoid"
    else:
        prediction="General Infection"

    st.subheader("Predicted Result")

    st.markdown(f"""
    <div class="result-card">
    <h2>Predicted Disease</h2>
    <h1>{prediction}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

# ---------- DIAGNOSIS ----------
    st.subheader("Diagnosis")
    st.write(diagnosis_map[prediction])

# ---------- DOCTOR + PRECAUTIONS ----------
    doctor = doctor_map.get(prediction,"General Physician")
    precaution = precaution_map.get(prediction,"Consult doctor")

    colA,colB = st.columns(2)

    with colA:
        st.subheader("Recommended Doctor")
        st.write(doctor)

    with colB:
        st.subheader("Precautions")
        st.write(precaution)

    st.divider()

# ---------- GRAPH ----------
    st.subheader("Disease Probability Chart")

    diseases=list(diagnosis_map.keys())
    probs=[0.85 if d==prediction else 0.02 for d in diseases]

    df=pd.DataFrame({"Disease":diseases,"Probability":probs})

    fig,ax=plt.subplots(figsize=(8,5))

    ax.barh(df["Disease"],df["Probability"],color="#1d3557")

    ax.set_xlabel("Probability")
    ax.set_ylabel("Disease")

    st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)
