## Machine Learning project 2018/19: Ensemble Fair Algorithms for Classification

### Installation set-up

* create a virtual environment with Conda
```
conda create --name aif360 python=3.5
```
To activate the environment, type
```
conda activate aif360
```
or `source activate aif360` for older version of conda\
or `activate aif360` for Windows.\
To deactivate the environment, type
```
conda deactivate
```
or similarly `source deactivate`, or `deactivate`

* install requirements provided by `requirements.txt`.\
This file consists of a list of packages used for this project. You can install the requirements in the virtual environment after activating it by typing the following:
```
pip install -r requirements.txt
```

### Project source codes
* [dataset](dataset/) : a folder which contains the three original data sets used in this project (Adult, Compas, German)
* [results](results/) : folder which stores all the results in csv format
* [codes](codes/) : original code for the three classifiers and ensemble. There is an output folder which stores the output data after classification

### Testing examples
To test the codes, first you need to activate the environment, then go to the codes directory.
```
source activate aif360
cd codes
```
We have three scripts which run the project for three different datasets.
* [run_adult.py](codes/run_adult.py) : script to run the project with Adult dataset.
* [run_compas.py](codes/run_compas.py) : script to run the project with Compas dataset.
* [run_german.py](codes/run_german.py) : script to run the project with German dataset.\
\
To run one of the above files, type:
```
python run_<adult/compas/german>.py
```
The three files above save the output (accuracy and fairness scores for multiple runs) to a csv file stored in the results folder.
* [analysis-compas.R](analysis-compas.R) : script for plotting the results obtained from the previous step.
* [alphaCalc.R](alphaCalc.R) : script to create the alpha plot which shows combined scores of accuracy and fairness.\
You can also simply run the demo code in jupyter notebook.
* [demo.ipynb](demo.ipynb) : script for demo. Store results for accuracy and fairness metrics as a dataframe for all classifiers.
