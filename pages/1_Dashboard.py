import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("heart.csv")

# Prepare Data
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

# Title
st.title("Heart Disease Prediction System")

st.subheader(
    "AI-Powered Medical Risk Assessment and Disease Prediction"
)

st.markdown("---")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset Records", len(df))

with col2:
    st.metric("Model Accuracy", f"{accuracy*100:.2f}%")

with col3:
    st.metric("Medical Features", X.shape[1])

with col4:
    st.metric("Prediction Type", "Classification")

st.markdown("---")

# Dataset Analytics
st.header("Dataset Analytics")

col1, col2 = st.columns(2)

with col1:
    fig_age = px.histogram(
        df,
        x="age",
        title="Age Distribution"
    )
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    disease_counts = df["target"].value_counts()

    fig_target = px.pie(
        values=disease_counts.values,
        names=["No Disease", "Disease"],
        title="Heart Disease Distribution"
    )

    st.plotly_chart(fig_target, use_container_width=True)

st.markdown("---")

# Feature Importance
st.header("Feature Importance Analysis")

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

fig_imp = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Most Important Medical Features"
)

st.plotly_chart(fig_imp, use_container_width=True)

st.markdown("---")

st.success(
    "Use the Patient Risk Assessment page to analyze a patient's heart disease risk."
)

# Footer
st.markdown("---")

st.caption(
    "Heart Disease Prediction System | Machine Learning Based Medical Risk Assessment"
)