# Heart Disease Prediction

This project aims to predict the presence of heart disease in patients using a machine learning model. The model is trained on a dataset containing various health metrics and is deployed using a Streamlit web application for easy user interaction.

## Project Structure

```
datasets/
    heart_disease.csv
heart_disease_prediction.py
heart_main.ipynb
models/
    heart_disease_model.sav
predictive_system.py
```

## Files

- **datasets/heart_disease.csv**: The dataset containing health metrics used for training the model.
- **heart_disease_prediction.py**: The main script for the Streamlit web application.
- **heart_main.ipynb**: Jupyter notebook containing the data analysis, model training, and evaluation.
- **models/heart_disease_model.sav**: The saved machine learning model.
- **predictive_system.py**: Script for making predictions using the trained model.

## Installation

### Clone the repository:

```bash
git clone https://github.com/tawiahnyt/Heart-Disease-Prediction.git
cd heart-disease-prediction
```

### Install the required packages:

```bash
pip install -r requirements.txt
```

### Run the Streamlit application:

```bash
streamlit run heart_disease_prediction.py
```

## Usage

### Streamlit Web Application

1. Open the Streamlit application in your browser.
2. Enter the required health metrics in the input form.
3. Click the "Predict" button to get the prediction result.

### Jupyter Notebook

1. Open `heart_main.ipynb` in Jupyter Notebook.
2. Run the cells to load the dataset, train the model, and evaluate it's performance.

## Model Training and Evaluation

The model is trained using the `RandomForestClassifier` from scikit-learn. The training process includes:

1. Loading the dataset.
2. Data preprocessing and standardization.
3. Splitting the data into training and testing sets.
4. Training the `RandomForestClassifier`.
5. Evaluating the model using accuracy, precision, recall, and F1-score.

## Prediction

The `heart_prediction` function in `heart_disease_prediction.py` takes input data, preprocesses it, and uses the trained model to predict the presence of heart disease.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to contribute to this project by opening issues or submitting pull requests. For any questions, please contact the me.
