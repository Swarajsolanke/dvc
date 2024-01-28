# project setup steps:

1. create conda -p env python==3.8 -y  && source ./venv
2. conda activate /env 
3. pip install -r requirements.txt 


## dvc commands:
1. dvc init 
2. dvc repro (it is used to track the yaml file )
3. dvc dag(to maintain acyclic graph between two stages)


