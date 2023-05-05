## How to create a PCA plot with python

> "This repository is the supplementary material for the blogpost ["How to create a PCA plot with python"](http://127.0.0.1:8000/2023/1/2/how-to-create-a-pca-plot-with-python/)

### Create environment

- install miniconda on your system (simple google search will offer a lot of details on this)
- create your environemt using the environment.yml shared in this folder 
    - `conda create --name pca_env --file environment.yml`
- or create your own environment by specifying all dependencies  

### Run script using Jupyter Notebook
- open terminal and locate the script you want to run then enter: 
    - `conda activate pca_env` 
    - `jupyter notebook`  
- Jupyter Notebook will open in your browser 
- Hit shift+enter to execute each cell

### Run script using Visual Studio Code (VS Code)
- open VS Code
- install the ipython extension
- change the python interpreter and select the conda environment you created 
- open the python script and hit shift+enter to execute each cell