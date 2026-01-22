
# Battery RUL Prediction Streamlit App

**What is this?**
A ready-to-run Streamlit app that predicts Remaining Useful Life (RUL) of a battery using a Random Forest regressor.
The repository includes a simulated dataset, a training script, and a pre-trained model.

**Structure**
- app.py            -> Streamlit app
- train_model.py    -> Optional script to retrain model
- data/battery_data.csv -> Simulated dataset (1200 cycles)
- model/rul_model_rf.joblib -> Trained RandomForest model
- requirements.txt  -> Python dependencies

**How to run**
1. (Optional) create a virtual environment: `python -m venv .venv && source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

**Notes**
- The dataset is simulated for demo purposes. Replace `data/battery_data.csv` with real measurements for production.
- To retrain, run: `python train_model.py --data data/battery_data.csv --out model/rul_model_rf.joblib`
