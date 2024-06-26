# Brain Tumor Classification MLOPs-Project

## Overview
The Brain Tumor Classification Project is designed to leverage machine learning for the automated classification of brain tumors from MRI images, aiming to enhance diagnostic accuracy and efficiency. By integrating MLOps practices, I aimed to streamline the development, deployment, and maintenance of machine learning models in a production environment.


## Features
- Data preprocessing and augmentation.
- Implementation of machine learning models for image classification.
- Evaluation metrics for model performance.


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Emanalytics7/Brain-Tumor-Classification-Project.git
```
### STEP 01
- Create a conda environment after opening the repository

```bash
conda create -n environment-name python=3.11 -y
```

```bash
conda activate environment-name
```


### STEP 02
- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

