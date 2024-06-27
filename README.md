# Lippmann-Schwinger

- Numpy, Devito based Python codes for the Lippmann-Schwinger problem

- Contains all codes to reproduce figures and tables in Part I: Chapter 2 of thesis

# How to reproduce the results? The following steps were tested on Linux (Centos & Ubuntu) only.
- After cloning this repository, install the Python packages as indicated in the file "requirements.txt".
Steps to install the packages are indicated below in the Section **How to install the packages**.

- Navigate to the directory Lippmann-Schwinger/Scripts/BashScripts/

- Run all the scripts serially

- For example, to run **p01.sh**, just type the command
```ruby
bash p01.sh
```

- The above runs will create some files in the directory **Lippmann-Schwinger/Data/**, and all figures will be 
created in the directory **Lippmann-Schwinger/Fig/**.

# Installation
The package requires python 3.9.

Create a conda environment and activate the environemnt. 
```ruby
conda create -n <your-env-name> python=3.9
conda activate <your-env-name>
```
Install the required packages with the following command:
```ruby
pip install -r requirements.txt
```

# Citation
