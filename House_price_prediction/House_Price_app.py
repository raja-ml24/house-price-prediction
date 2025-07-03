import streamlit as st 
import joblib
import numpy as np

model = joblib.load('house_price_model.pkl')
st.title("🏠 House Price Prediction App")

bedrooms = st.number_input("Bedrooms",min_value=0,max_value=10,step=1)
bathrooms = st.number_input("Bathrooms",min_value=0.0,max_value=10.0,step=0.25)
sqft_living = st.number_input("Sqrt Living")
sqft_lot = st.number_input("sqrt Lots")
floors = st.number_input("Floors", min_value=0.0, max_value=4.0, step=0.25)
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.slider("View", 0, 4)
condition = st.slider("Condition", 1, 5)
sqft_above = st.number_input("Sqft Above")
sqft_basement = st.number_input("Sqft Basement")
yr_built = st.number_input("Year Built", min_value=1900, max_value=2023)

if st.button("Predict Price"):
    input_data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                            waterfront, view, condition, sqft_above,
                            sqft_basement, yr_built]])
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")



