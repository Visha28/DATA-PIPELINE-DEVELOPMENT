import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ETLPipeline:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.data = None
        self.transformer = None

    def extract(self):
        """Extract data from the input source."""
        try:
            logger.info(f"Extracting data from {self.input_path}")
            if self.input_path.endswith('.csv'):
                self.data = pd.read_csv(self.input_path)
            elif self.input_path.endswith('.xlsx'):
                self.data = pd.read_excel(self.input_path)
            else:
                raise ValueError("Unsupported file format")
            logger.info(f"Successfully extracted {len(self.data)} records")
            return self
        except Exception as e:
            logger.error(f"Extraction failed: {str(e)}")
            raise

    def transform(self):
        """Transform the extracted data."""
        try:
            logger.info("Starting data transformation")

            # Handle missing values and encode categorical variables
            numeric_features = self.data.select_dtypes(include=['int64', 'float64']).columns
            categorical_features = self.data.select_dtypes(include=['object']).columns

            # Define preprocessing steps
            numeric_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ])

            categorical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
            ])

            # Combine transformers
            self.transformer = ColumnTransformer(
                transformers=[
                    ('num', numeric_transformer, numeric_features),
                    ('cat', categorical_transformer, categorical_features)
                ])

            # Fit and transform the data
            transformed_data = self.transformer.fit_transform(self.data)
            
            # Get feature names for the transformed data
            cat_feature_names = self.transformer.named_transformers_['cat']['onehot']\
                .get_feature_names_out(categorical_features)
            all_feature_names = list(numeric_features) + list(cat_feature_names)
            
            # Convert back to DataFrame
            self.data = pd.DataFrame(
                transformed_data,
                columns=all_feature_names
            )
            
            logger.info("Data transformation completed")
            return self
        except Exception as e:
            logger.error(f"Transformation failed: {str(e)}")
            raise

    def load(self):
        """Load the transformed data to the output destination."""
        try:
            logger.info(f"Loading data to {self.output_path}")
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            self.data.to_csv(self.output_path, index=False)
            logger.info(f"Successfully loaded data to {self.output_path}")
            return self
        except Exception as e:
            logger.error(f"Loading failed: {str(e)}")
            raise

    def run(self):
        """Run the complete ETL pipeline."""
        logger.info("Starting ETL pipeline")
        self.extract().transform().load()
        logger.info("ETL pipeline completed successfully")
        return self

def main():
    # Example usage
    input_file = "input_data.csv"
    output_file = "output/processed_data.csv"
    
    # Create sample data if input file doesn't exist
    if not os.path.exists(input_file):
        logger.info("Creating sample data")
        sample_data = pd.DataFrame({
            'age': [25, 30, np.nan, 35, 28],
            'salary': [50000, 60000, 55000, np.nan, 52000],
            'department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
            'experience': [2, 5, 3, 7, np.nan]
        })
        sample_data.to_csv(input_file, index=False)

    # Run pipeline
    pipeline = ETLPipeline(input_file, output_file)
    pipeline.run()

if __name__ == "__main__":
    main()