# DATA-PIPELINE-DEVELOPMENT

COMPANY: CODTECH IT SOLUTIONS

NAME: VISHAL

INTERN ID:

DOMAIN: CLOUD COMPUTING

DURATION:2 MONTHS

MENTOR: NEELA SANTOSH










Overview

This project delivers a robust and reusable ETL (Extract, Transform, Load) pipeline implemented in Python, leveraging the power of Pandas for data manipulation and Scikit-learn for advanced preprocessing. Developed and tested in PyCharm, this pipeline automates the process of extracting data from structured files, transforming it through cleaning and feature engineering, and loading the results into a clean, model-ready CSV file. It is designed for data scientists and engineers who need to preprocess datasets efficiently, handling both numeric and categorical data with missing values. The pipeline includes comprehensive logging to monitor execution, making it suitable for debugging and production environments. Whether you're preparing data for machine learning, analytics, or reporting, this tool streamlines the process with minimal configuration.

Features

The pipeline provides the following functionality:
Extraction: Reads input data from CSV or Excel files, with fallback to auto-generated sample data if no input is provided.
Transformation:Imputes missing numeric values using the mean strategy for consistency.
Scales numeric features to a standard normal distribution (mean=0, std=1) using StandardScaler.
One-hot encodes categorical variables, ensuring compatibility with machine learning algorithms.
Handles missing categorical values by assigning a 'missing' placeholder.
Loading: Saves transformed data to a specified CSV file in a designated output directory.
Logging: Implements detailed logging to track each step, capturing successes and errors for transparency.
Flexibility: Easily customizable for different datasets and preprocessing needs.


Prerequisites

To run the pipeline, ensure the following are installed:
Python: Version 3.7 or higher.

Libraries:
pip install pandas numpy scikit-learn

PyCharm: Community or Professional Edition (used for development and testing, though optional for users).

Input Data: A CSV or Excel file with numeric and categorical columns, or rely on the script’s sample data.
Writable Directory: Ensure write permissions for the output directory.

Setup and Installation


Install Dependencies: Create a requirements.txt file with:

pandas
numpy
scikit-learn

Install using:

pip install -r requirements.txt



Prepare Input Data: Place your dataset (e.g., input_data.csv) in the project root. Example format:

age,salary,department,experience
25,50000,HR,2
30,60000,IT,5
,55000,HR,3
35,,Finance,7
28,52000,IT,

The script generates sample data if no input file exists, ensuring seamless testing.



Configure Output: The default output is output/processed_data.csv. Modify paths in etl_pipeline.py if needed.



Usage
Running in PyCharm:
Open PyCharm and load the project directory.
Ensure the Python interpreter is set up with the required libraries.

Right-click etl_pipeline.py in the Project Explorer and select "Run 'etl_pipeline'".

The script will execute, producing logs in the console and saving output to output/processed_data.csv.

Running via Command Line:
python etl_pipeline.py

Pipeline Workflow:
Extract: Reads the input file (CSV/Excel).
Transform: Imputes missing values, scales numeric data, and encodes categorical data.
View Results: The output CSV contains standardized numeric columns and one-hot encoded categorical columns. 



Customization

Change File Paths: Edit the main() function in etl_pipeline.py:
input_file = "path/to/your/data.csv"
output_file = "path/to/output/processed_data.csv"


Modify Transformations: Adjust the transform() method to change imputation or scaling. For example, use median imputation:
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])


Extend Functionality: Add new preprocessing steps (e.g., feature selection) by modifying the ColumnTransformer.


Development Environment
IDE: PyCharm Community/Professional
Python Version: 3.9
OS: [Your OS, e.g., Windows/Linux/macOS]
Testing: Tested with sample data and custom datasets.
