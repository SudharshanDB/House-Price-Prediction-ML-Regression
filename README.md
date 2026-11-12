# House Price Prediction Model

A Web-Based ML House Price Prediction Model using Python. This project uses models such as <br>
1. `KNeighborsRegressor` <br>
2. `LinearRegression` <br>
3. `DecisionTreeRegressor` <br> 
4. `RandomForestRegressor` <br>

These models are available on the `scikit-learn` module, they are used in this project to predict the `price` feature of a property using features such as <br>
(`bedrooms`,	`bathrooms`, `sqft_living`, `sqft_lot`, `floors`, `waterfront`,  `view`, `condition`, `sqft_above`, `sqft_basement`, `yr_built`).
<br><br>

## 📁 Project Structure

The project consists of the following files:
1. **`app.py`**: Python script that contains the streamlit based web UI which uses the binary files used to predict the house prices.
2. **`house_price_prediction.ipynb`**: Jupyter notebook file that contains the basic EDA, and the trained models.
3. **`house_price_prediction_with_user_input.ipynb`**: Jupyter notebook script to predict the house prices using user input of the terminal. 
4. **`scaler.pkl`**: Binary file that contains the standarization functions.
5. **`feature_columns.pkl`**: Binary file that contains the list of feature columns.
6. **`trained_models.pkl`**: Binary file that contains the trained models.
7. **`requirements.txt`**: Contains the python modules used to create this project
<br><br>

## 🚀 Setup & Usage

### 1. Configure the Project

Clone or download this repository to your local machine. <br>

### 2. Download the Dependencies

Run the following command to install the modules listed in the requirements.txt
> **pip install -r requirements.txt** <br>

### 3. Run the ipynb script

Open jupyter notebook by using the following command
> **jupyter notebook**

Open the `house_price_prediction.ipynb` script and run all the cell in it. Upon running, you should be able to see three binary files installed in your directory, these files will be used in `house_price_prediction_with_user_input.ipynb` and `app.py` for accessing the necessary details about the `machine learning models`, `standardization functions` and `feature columns`. <br>

### 4.Run the terminal & web-based application
Afterwards, you can test the model using `house_price_prediction_with_user_input.ipynb` and subsequently you can run the following command
> **python3 -m streamlit run app.py**
Now, you will be able to open the web based application which will be hosted on `http://localhost:8501/` and to exit the program press `Cmd/Ctrl C` in the terminal
