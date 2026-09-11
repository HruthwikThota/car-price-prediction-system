
import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Car Price Prediction System",
    page_icon="🚗",
    layout="wide"
)


# --------------------------------------------------
# Load Model Files
# --------------------------------------------------

@st.cache_resource
def load_model_files():
    model = joblib.load("car_price_model.pkl")
    preprocessor = joblib.load("car_price_preprocessor.pkl")
    selector = joblib.load("car_price_selector.pkl")

    return model, preprocessor, selector


@st.cache_data
def load_dataset():
    df = pd.read_csv("car_MSRP.csv")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing numerical values
    df["Engine HP"] = df["Engine HP"].fillna(
        df["Engine HP"].median()
    )

    df["Engine Cylinders"] = df["Engine Cylinders"].fillna(
        df["Engine Cylinders"].median()
    )

    df["Number of Doors"] = df["Number of Doors"].fillna(
        df["Number of Doors"].median()
    )

    # Handle missing categorical values
    df["Engine Fuel Type"] = df["Engine Fuel Type"].fillna(
        df["Engine Fuel Type"].mode()[0]
    )

    df["Market Category"] = df["Market Category"].fillna("Unknown")

    return df


model, preprocessor, selector = load_model_files()
df = load_dataset()


# --------------------------------------------------
# Application Title
# --------------------------------------------------

st.title("🚗 Car Price Prediction System")

st.write(
    "Enter the car specifications below to estimate "
    "the Manufacturer's Suggested Retail Price (MSRP)."
)


# --------------------------------------------------
# Basic Car Information
# --------------------------------------------------

st.header("1. Basic Car Information")

col1, col2, col3 = st.columns(3)

with col1:
    make = st.selectbox(
        "Make",
        sorted(df["Make"].unique())
    )

with col2:
    model_name = st.selectbox(
        "Model",
        sorted(df["Model"].unique())
    )

with col3:
    year = st.number_input(
        "Year",
        min_value=int(df["Year"].min()),
        max_value=int(df["Year"].max()),
        value=2015,
        step=1
    )


# --------------------------------------------------
# Engine Information
# --------------------------------------------------

st.header("2. Engine Information")

col1, col2, col3 = st.columns(3)

with col1:
    engine_fuel_type = st.selectbox(
        "Engine Fuel Type",
        sorted(df["Engine Fuel Type"].unique())
    )

with col2:
    engine_hp = st.number_input(
        "Engine HP",
        min_value=0.0,
        max_value=1500.0,
        value=178.0,
        step=1.0
    )

with col3:
    engine_cylinders = st.number_input(
        "Engine Cylinders",
        min_value=0.0,
        max_value=20.0,
        value=4.0,
        step=1.0
    )


# --------------------------------------------------
# Transmission and Driving Information
# --------------------------------------------------

st.header("3. Transmission and Driving Information")

col1, col2, col3 = st.columns(3)

with col1:
    transmission_type = st.selectbox(
        "Transmission Type",
        sorted(df["Transmission Type"].unique())
    )

with col2:
    driven_wheels = st.selectbox(
        "Driven Wheels",
        sorted(df["Driven_Wheels"].unique())
    )

with col3:
    number_of_doors = st.number_input(
        "Number of Doors",
        min_value=2.0,
        max_value=4.0,
        value=4.0,
        step=1.0
    )


# --------------------------------------------------
# Vehicle Information
# --------------------------------------------------

st.header("4. Vehicle Information")

col1, col2, col3 = st.columns(3)

with col1:
    market_category = st.selectbox(
        "Market Category",
        sorted(df["Market Category"].unique())
    )

with col2:
    vehicle_size = st.selectbox(
        "Vehicle Size",
        sorted(df["Vehicle Size"].unique())
    )

with col3:
    vehicle_style = st.selectbox(
        "Vehicle Style",
        sorted(df["Vehicle Style"].unique())
    )


# --------------------------------------------------
# Mileage and Popularity
# --------------------------------------------------

st.header("5. Mileage and Popularity")

col1, col2, col3 = st.columns(3)

with col1:
    highway_mpg = st.number_input(
        "Highway MPG",
        min_value=0,
        max_value=400,
        value=35,
        step=1
    )

with col2:
    city_mpg = st.number_input(
        "City MPG",
        min_value=0,
        max_value=200,
        value=25,
        step=1
    )

with col3:
    popularity = st.number_input(
        "Popularity",
        min_value=0,
        max_value=10000,
        value=2031,
        step=1
    )


# --------------------------------------------------
# Prediction Section
# --------------------------------------------------

st.divider()

st.subheader("Get Estimated MSRP")

predict_button = st.button(
    "Predict MSRP",
    type="primary"
)


# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------

if predict_button:

    # Validate input values
    if engine_hp <= 0:
        st.error("Please enter a valid Engine HP greater than 0.")

    elif engine_cylinders <= 0:
        st.error("Please enter a valid number of engine cylinders.")

    elif highway_mpg <= 0 or city_mpg <= 0:
        st.error("Highway MPG and City MPG must be greater than 0.")

    elif popularity < 0:
        st.error("Popularity cannot be negative.")

    else:

        # Create input DataFrame
        input_data = pd.DataFrame({
            "Make": [make],
            "Model": [model_name],
            "Year": [year],
            "Engine Fuel Type": [engine_fuel_type],
            "Engine HP": [engine_hp],
            "Engine Cylinders": [engine_cylinders],
            "Transmission Type": [transmission_type],
            "Driven_Wheels": [driven_wheels],
            "Number of Doors": [number_of_doors],
            "Market Category": [market_category],
            "Vehicle Size": [vehicle_size],
            "Vehicle Style": [vehicle_style],
            "highway MPG": [highway_mpg],
            "city mpg": [city_mpg],
            "Popularity": [popularity]
        })

        try:
            # Apply preprocessing
            input_transformed = preprocessor.transform(input_data)

            # Apply feature selection
            input_selected = selector.transform(input_transformed)

            # Generate prediction
            prediction = model.predict(input_selected)

            predicted_price = prediction[0]

            # Display result
            st.success(
                f"Estimated MSRP: ${predicted_price:,.2f}"
            )

            st.info(
                "The prediction was generated using the trained "
                "Linear Regression model."
            )

        except Exception as error:
            st.error(
                "An error occurred while generating the prediction."
            )

            st.write("Please check whether all input values are valid.")
