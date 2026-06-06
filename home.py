import streamlit as st

st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

st.title("Heart Disease Prediction System")

st.subheader(
    "AI-Powered Medical Risk Assessment and Disease Prediction"
)

st.markdown("---")

st.write("""
This application uses Machine Learning techniques
to predict the likelihood of heart disease based on
patient medical information.

The system analyzes multiple health parameters and
provides intelligent risk assessment, visual analytics,
and personalized recommendations.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### Features

    • Dataset Analytics

    • Feature Importance Analysis

    • Patient Risk Assessment

    • Risk Score Prediction

    • PDF Medical Report
    """)

with col2:
    st.success("""
    ### Technologies Used

    • Python

    • Streamlit

    • Scikit-Learn

    • Plotly

    • Random Forest
    """)

st.markdown("---")

st.warning(
    "Use the navigation menu to access Dashboard and Patient Assessment."
)