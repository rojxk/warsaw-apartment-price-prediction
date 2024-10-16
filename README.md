## Warsaw Apartment Price Prediction
This project was developed as part of the "Programming for Data Analysis" course at university. It aims to predict apartment prices in Warsaw, Poland, using machine learning techniques. The system scrapes data from otodom.pl, cleans and preprocesses the data, and then uses an XGBoost Regressor model to make price predictions.

### Project structure
- `scrape_data.ipynb`: Jupyter notebook for scraping data from otodom.pl
- `clean_data.ipynb`: Jupyter notebook for cleaning and preprocessing the scraped data
- `model.ipynb`: Jupyter notebook for developing and training the machine learning model
- `dashboard.py`: Streamlit dashboard for visualizing the data and predictions
- `cleaned_data.csv`: Cleaned data from otodom.pl *(05/2024)*
- `xgboost_model.pkl`: Trained XGBoost model

## Requirements
- Python 3.7+
- Required libraries: pandas, numpy, scikit-learn, xgboost, matplotlib, streamlit, beautifulsoup4, requests

## Model

The project uses XGBoost Regressor for predicting apartment prices. The model takes into account various features such as apartment size, number of rooms, location, and other amenities.

**Model performance metrics:**

Training Set:

- MAE (Mean Absolute Error): 65,470.61 PLN
- MAPE (Mean Absolute Percentage Error): 7.74%

Test Set:

- MAE (Mean Absolute Error): 164,596.84 PLN
- MAPE (Mean Absolute Percentage Error): 10.37%

## Dashboard
![gif](/assets/dashboard.gif)
The Streamlit dashboard provides interactive visualizations of the data and allows users to explore price predictions for different apartment characteristics.

### Steps for running the dashboard:

1. **Clone repository**
```
git clone https://github.com/rojxk/warsaw-apartment-price-prediction.git
```
2. **Run in terminal**
```
streamlit run dashboard.py
```
3. **Access dashboard**
Open web browser and navigate to:  http://localhost:8501
