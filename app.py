import streamlit as st
import joblib

MODEL_ACCURACY = 0.93

# Load trained model
model = joblib.load("best_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

# Title
st.title("🌸 Iris Flower Classifier")

st.write(
    "Enter the measurements of an Iris flower "
    "and the machine learning model will predict its species."
)

st.divider()

# Input section
st.subheader("🌱 Flower Measurements")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col2:
    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

st.divider()

# Prediction
if st.button("🔍 Predict Species", use_container_width=True):

    new_flower = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = model.predict(new_flower)

    species = prediction[0]

    st.metric(
        label="Model Accuracy",
        value="93%"
    )

    st.success(f"🌸 Predicted Species: **{species}**")

    species_info = {
        "Iris-setosa": "Setosa is generally smaller and has relatively short petals.",
        "Iris-versicolor": "Versicolor has medium-sized petals and overlaps somewhat with Virginica.",
        "Iris-virginica": "Virginica generally has larger petals and sepals than the other two species."
    }

    if species in species_info:
        st.info(species_info[species])

    st.write("Prediction generated using the trained KNN classification model.")