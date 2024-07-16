# Vessel Dwelling Time Prediction

This repository contains the code for exploring Ocean AIS dataset and modelling dwell behaviour.

## Build instructions
To set up the project, you'll need to clone this repo, install the requirements and download the dataset.

```
git clone https://github.com/artoriusss/ocean.git
cd ocean
```
Create a virtual environment:
```
python -m venv .venv 
```
Activate the virtual environment:
```
source .venv/bin/activate #Linux & MacOS systems
```

```
.\.venv\Scripts\activate #Windows
```

```
pip install -r requirements.txt
```
You can now download the dataset by running the following command:
```
python -m src.dowload_dataset
```

After performing these steps, you'll be ready to experiment with the code and models. 

### Project structure: 

```
.
├── README.md
├── data
│   └── parquet
├── models
│   └── decision_tree.pkl
├── notebooks
│   ├── 1. EDA.ipynb
│   └── 2. Prediction.ipynb
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── dowload_dataset.py
│   ├── evaluation.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   └── train.py
└── utils
    ├── __init__.py
    └── paths.py
```

### `/notebooks `

Contains Jupyter Notebooks for illustration purposes. In `1. EDA.ipynb`, you can find code for exploratory data analysis. `2. Modelling.ipynb` contains the code for preprocessing, feature selection, model training and evaluation.

### `/src/train.py`

If you just want to run model training with default configurations, run:

```
python -m src.train
```

By default, sklearn's `DesicionTreeRegressor` implementation of Desicion Trees will be run. You can experiment with different `max_depth` parameters by specifying:
`python -m scr.scrip --max_depth 5`, although with the current model configuraition `max_depth=3` yields the best result.

## Performance

Currently, the best result I was capable to achive is the following:

```
-------------------------------------------
Mean Squared Error (MSE): 22.93390748774915
Mean Absolute Error (MAE): 3.382817256720326
R-squared (R²): 0.04388435618894526
Median Absolute Error: 1.6950060070941912
--------------------------------------------
```

Please refer to mentioned notebooks and scripts for more details.