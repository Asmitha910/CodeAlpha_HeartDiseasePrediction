import streamlit as st
import pandas as pd
import io
from datetime import datetime

from sklearn.ensemble import RandomForestClassifier
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import plotly.graph_objects as go

st.set_page_config(
    page_title="Patient Assessment",
    page_icon="🩺",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("heart.csv")

X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

st.title("Patient Risk Assessment")

st.subheader(
    "AI-Powered Heart Disease Risk Analysis"
)

def create_pdf(
    patient_name,
    patient_id,
    age,
    gender,
    risk_score,
    prediction_text,
    recommendations
):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "HEART DISEASE PREDICTION REPORT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Patient Name: {patient_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Patient ID: {patient_id}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Age: {age}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Gender: {gender}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Score: {risk_score:.2f}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Prediction: {prediction_text}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Recommendations: {recommendations}",
            styles["Normal"]
        )
    )

    doc.build(content)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

st.header("Patient Information")

patient_name = st.text_input(
    "Patient Name"
)

generated_id = (
    "PAT" +
    datetime.now().strftime("%H%M%S")
)

patient_id = st.text_input(
    "Patient ID",
    value=generated_id
)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 100, 50)

    sex = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    cp = st.number_input(
        "Chest Pain Type",
        0,
        3,
        0
    )

    trestbps = st.number_input(
        "Blood Pressure",
        80,
        250,
        120
    )

    chol = st.number_input(
        "Cholesterol",
        100,
        600,
        200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar",
        [0, 1]
    )

with col2:
    restecg = st.number_input(
        "Resting ECG",
        0,
        2,
        0
    )

    thalach = st.number_input(
        "Maximum Heart Rate",
        60,
        250,
        150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1]
    )

    oldpeak = st.number_input(
        "Old Peak",
        0.0,
        10.0,
        1.0
    )

    slope = st.number_input(
        "Slope",
        0,
        2,
        1
    )

    ca = st.number_input(
        "CA",
        0,
        4,
        0
    )

    thal = st.number_input(
        "Thal",
        0,
        3,
        2
    )
    sex_value = 1 if sex == "Male" else 0

if st.button("🔍 Analyze Risk"):

    patient_data = [[
        age,
        sex_value,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]]

    prediction = model.predict(patient_data)[0]
    probability = model.predict_proba(patient_data)[0][1]

    risk_score = probability * 100

    st.markdown("---")
    st.header("Prediction Report")
    st.markdown(
f"""
### Patient Summary

**Patient Name:** {patient_name}

**Patient ID:** {patient_id}

**Age:** {age}

**Gender:** {sex}
"""
)

    # Gauge Chart
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={
                "text": "Heart Disease Risk Score"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "thickness": 0.3
                },
                "steps": [
                    {
                        "range": [0, 40],
                        "color": "lightgreen"
                    },
                    {
                        "range": [40, 70],
                        "color": "gold"
                    },
                    {
                        "range": [70, 100],
                        "color": "lightcoral"
                    }
                ]
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Percentage",
            f"{risk_score:.2f}%"
        )

    with col2:
        if risk_score < 30:
            st.success("🟢 Low Risk")

        elif risk_score < 60:
            st.warning("🟡 Moderate Risk")

        else:
            st.error("🔴 High Risk")

    # Prediction
    if prediction == 1:

        prediction_text = (
            "High Risk of Heart Disease"
        )

        recommendation_text = """
        • Consult a cardiologist

        • Monitor blood pressure regularly

        • Reduce cholesterol intake

        • Exercise regularly

        • Maintain a healthy diet
        """

        st.error(
            "High Risk of Heart Disease Detected"
        )

    else:

        prediction_text = (
            "Low Risk of Heart Disease"
        )

        recommendation_text = """
        • Continue healthy lifestyle habits

        • Exercise regularly

        • Schedule routine health checkups
        """

        st.success(
            "Low Risk of Heart Disease"
        )

    st.subheader("Patient Summary")

    st.write(
        f"**Patient Name:** {patient_name}"
    )

    st.write(
        f"**Patient ID:** {patient_id}"
    )

    st.write(
        f"**Age:** {age}"
    )

    st.write(
        f"**Gender:** {sex}"
    )

    st.subheader("Recommendations")

    st.info(recommendation_text)

    # PDF Generation

    pdf = create_pdf(
        patient_name,
        patient_id,
        age,
        sex,
        risk_score,
        prediction_text,
        recommendation_text
    )

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf,
        file_name=f"{patient_name}_Heart_Report.pdf",
        mime="application/pdf"
    )
    st.markdown("---")

st.caption(
    "Heart Disease Prediction System | Machine Learning Based Medical Risk Assessment"
)
