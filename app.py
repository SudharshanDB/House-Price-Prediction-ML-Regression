import streamlit as st
import pandas as pd
import joblib

trained_models_list = joblib.load("trained_models_list.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("House Price Predictor")
st.write("Use this app to estimate the current property value in the King County, WA")

model_names = []
for name, model in trained_models_list:
    model_names.append(name)

selected_model = st.selectbox("Choose a model", model_names)
model_dictionaries = dict(trained_models_list)
chosen_model = model_dictionaries[selected_model]

bedrooms = st.number_input("Bedrooms", value = 3)
bathrooms = st.number_input("Bathroom", value = 2.0)
sqft_living = st.number_input("Sqft Living", value = 2100)
sqft_lot = st.number_input("Sqft Lot", value = 6500)
floors = st.number_input("Floors", value = 1.0)
waterfront = st.selectbox("Waterfront [0 = 'No', 1 = 'Yes']", [0,1])
view = st.slider("View (0-4)", 0, 4, 0)
condition = st.slider("Condition (1-5)", 1, 5, 3)
sqft_above = st.number_input("Sqft Above", value = 1600)
sqft_basement = st.number_input("Sqft Basement", value = 500)
yr_built = st.number_input("Year Built", value = 1998)

if st.button("Calculate Price"):
    new_house = {
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': sqft_living,
        'sqft_lot': sqft_lot,
        'floors': floors,
        'waterfront': waterfront,
        'view': view,
        'condition': condition,
        'sqft_above': sqft_above,
        'sqft_basement': sqft_basement,
        'yr_built': yr_built
    }

    input_df = pd.DataFrame([new_house], columns = feature_columns)
    input_scaled = scaler.transform(input_df)
    base_price = chosen_model.predict(input_scaled)[0]
    final_price = 2.7 * base_price
    st.success(f"Estimated Price: ${final_price: .2f}")
