import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.float_format = '{:.0f}'.format
# Load your data
@st.cache_data
def load_data():
    data = pd.read_csv('cleaned_data.csv', delimiter=';')
    data['price'] = pd.to_numeric(data['price'], errors='coerce')
    data['area'] = pd.to_numeric(data['area'], errors='coerce')
    data.dropna(subset=['price', 'area'], inplace=True)  # Remove rows with NaN in price or area
    data['price_per_area'] = data['price'] / data['area']
    return data

df = load_data()

# Title of the dashboard
st.title('Otodom Warszawa Dashboard')

# Show the first few rows of the DataFrame
st.write("Data Overview:")
st.dataframe(df.head())

# Sidebar filters
district = st.sidebar.selectbox('Select District:', df['district'].unique())
price_filter = st.sidebar.slider('Filter by price per area (max value)', 0, int(df['price_per_area'].max()), int(df['price_per_area'].max()))

# Apply filters
filtered_data = df[(df['district'] == district) & (df['price_per_area'] <= price_filter)]

st.write(f"Filtered Data for {district} with Price per Area ≤ {price_filter}:")
st.dataframe(filtered_data)

# Show statistics for price in the selected district
if not filtered_data.empty:
    st.write("Statistics for Price:")
    st.write(filtered_data['price'].describe())

# Visualization options
option = st.selectbox(
    'Choose the type of chart:',
    ('Price Distribution', 'Price per Area Distribution')
)

if option == 'Price Distribution':
    # Plotting price distribution in the selected district
    fig, ax = plt.subplots()
    filtered_data['price'].dropna().hist(bins=20, ax=ax)
    ax.set_title('Price Distribution')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
elif option == 'Price per Area Distribution':
    # Plotting price per area distribution
    fig, ax = plt.subplots()
    filtered_data['price_per_area'].dropna().hist(bins=20, ax=ax)
    ax.set_title(f'Price per Area Unit Distribution in {district}')
    ax.set_xlabel('Price per Area Unit (per m²)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)


# Optional: Add more visualizations and filters based on other columns like status, rooms, etc.
