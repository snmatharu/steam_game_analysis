# Steam Market Analysis

Welcome to our Steam Market Insights and Prediction project, a data-driven approach to enhancing decision-making in the video game industry. By analyzing Steam's extensive game data, we provide valuable insights and predictive models that empower developers, publishers, and investors to optimize game pricing, enhance player engagement, and predict market trends effectively.

Explore our [Sample PowerBI Dashboard](https://github.com/snmatharu/steam_game_analysis/tree/main/dashboard) for a live demonstration.

## Prerequisites
- Anaconda or Miniconda installed
- Git installed
- Internet connection
- Minimum 8GB RAM recommended

## Project Overview

In the fast-paced and competitive video game industry, understanding market trends and player preferences is essential for success. Our project leverages the Steam Store dataset to provide insights into game pricing, user engagement, and the factors driving player behavior. By answering key questions—such as how game prices vary by genre and the impact of downloadable content (DLC) on user satisfaction—our analysis helps developers, publishers, and investors make informed decisions. Additionally, our predictive model for peak concurrent users (CCU) offers valuable forecasts, enabling strategic planning for high-demand periods and optimized game development.


## Project Structure

```
main/
├── config.py              # Configuration settings and database connection utilities
├── data_loader.py         # Data loading and Spark DataFrame creation
├── data_transformer.py    # Data transformation and feature engineering
├── environment.yml        # Required environment dependencies
├── main.py                # Main orchestration script
├── model_trainer.py       # Model training and evaluation logic
├── steam_databricks.ipynb # Databricks Notebook 
├── test_setup.py          # Verify the libraries installation
└── visualization.py       # Visualization utilities

```

## Module Details

### `config.py`
- Contains configuration settings and database connection utilities
- Manages MongoDB connection credentials
- Functions:
  - `get_mongo_url()`: Generates MongoDB connection URL

### `data_loader.py`
- Handles data loading from MongoDB and Spark DataFrame creation
- Contains schema definitions and data conversion utilities
- Key functions:
  - `fetch_data_with_pymongo()`: Retrieves data from MongoDB
  - `get_schema()`: Defines the data schema
  - `create_spark_session()`: Initializes Spark session
  - `convert_to_spark_dataframe()`: Converts MongoDB data to Spark DataFrame

### `data_transformer.py`
- Manages data transformation and feature engineering
- Handles date processing and categorical variable encoding
- Key functions:
  - `transform_data()`: Performs basic data transformations
  - `prepare_data_for_modeling()`: Prepares data for ML models

### `model_trainer.py`
- Contains model training and evaluation logic
- Implements multiple regression models
- Key functions:
  - `train_and_evaluate_models()`: Trains and evaluates multiple models:
    - Linear Regression
    - Decision Tree
    - Random Forest

### `visualization.py`
- Provides visualization utilities for model results
- Creates performance comparison plots
- Key functions:
  - `plot_results()`: Visualizes model comparison metrics
  - `plot_feature_importance()`: Shows feature importance for Random Forest model

### `main.py`
- Main script that orchestrates the entire analysis pipeline
- Coordinates data loading, transformation, modeling, and visualization

## Step-by-Step Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/snmatharu/steam_game_analysis.git
cd steam_game_analysis/main
```

### 2. Create and Activate Conda Environment
```bash
# Create environment from yml file
conda env create -f environment.yml

# Activate the environment
conda activate steam_analysis
```

### 3. Verify Installation
Run the following commands to verify your setup:

```bash
# Start Python
python

# In Python console, try importing the required packages
import pyspark
import pymongo
import numpy
import matplotlib
```

### 4. Configure Spark Environment Variables
Add these to your system environment variables (Windows) or ~/.bashrc (Linux/Mac):

#### Windows:
```bash
# Set environment variables in Command Prompt
set JAVA_HOME=C:\Path\To\Your\Java\Installation
set SPARK_HOME=C:\Path\To\Your\Conda\Env\Lib\site-packages\pyspark
set HADOOP_HOME=C:\Path\To\Your\Conda\Env\Lib\site-packages\pyspark
set PATH=%PATH%;%SPARK_HOME%\bin;%HADOOP_HOME%\bin
```

#### Linux/Mac:
```bash
# Add to ~/.bashrc or ~/.zshrc
export JAVA_HOME=/path/to/your/java/installation
export SPARK_HOME=$CONDA_PREFIX/lib/python3.9/site-packages/pyspark
export HADOOP_HOME=$SPARK_HOME
export PATH=$PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin
```

### 5. Jupyter Kernel Setup

1. Install required packages:
```bash
conda activate steam_analysis
conda install -y jupyter ipykernel nb_conda_kernels
```

2. Register the kernel:
```bash
python -m ipykernel install --user --name steam_analysis --display-name "Python (steam_analysis)"
```

3. Configure kernel.json:
Create or modify the kernel.json file at `C:\Users\[YourUsername]\anaconda3\envs\steam_analysis\share\jupyter\kernels\python3\kernel.json`:

```json
{
    "argv": [
        "C:\\Users\\[YourUsername]\\anaconda3\\envs\\steam_analysis\\python.exe",
        "-m",
        "ipykernel_launcher",
        "-f",
        "{connection_file}"
    ],
    "display_name": "Python (steam_analysis)",
    "language": "python",
    "env": {
        "PYTHONPATH": "C:\\Users\\[YourUsername]\\anaconda3\\envs\\steam_analysis\\Lib\\site-packages",
        "SPARK_HOME": "C:\\Users\\[YourUsername]\\anaconda3\\envs\\steam_analysis\\Lib\\site-packages\\pyspark",
        "PYSPARK_PYTHON": "C:\\Users\\[YourUsername]\\anaconda3\\envs\\steam_analysis\\python.exe",
        "PYSPARK_DRIVER_PYTHON": "C:\\Users\\[YourUsername]\\anaconda3\\envs\\steam_analysis\\python.exe"
    }
}
```

### 6. Test the Setup

Test the setup by running `test_setup.py`:

Run the test script:
```bash
python test_setup.py
```

### 7. Run the Project

Run the project by running `main.py`:

Run the main script:
(Make sure you are in steam_game_analysis/main)

```bash
python main.py
```

## Installation Steps for Databricks Analysis (If having difficulty in Local Setup)

### 1. Download the Notebook

1. Download the `steam_databricks.ipynb` file from this repository
2. Navigate to your Databricks workspace(In Community Edition)
3. Click on "Workspace" in the left sidebar
4. Select "Import" from the workspace menu
5. Upload the downloaded `steam_databricks.ipynb` file

### 2. Configure the Cluster

Before running the notebook, configure the Spark settings in your Databricks cluster:

1. Go to the Clusters page in your Databricks workspace
2. Create a new cluster or select an existing one
3. Click on "Edit" for the chosen cluster
4. Expand the "Advanced Options" section
5. Click on "Spark" tab under "Advanced Options"
6. Add the following configurations in the Spark Config box:
```
spark.kryoserializer.buffer.max 2047m
spark.kryoserializer.buffer 512m
```
7. Click "Confirm" to save the configurations

### 3. Execute the Code
1. Press "Run All" in the top options of the notebook to execute the cell and display the results.

## Data Access

The raw data required for our analysis and modeling is sourced from the Steam Store dataset. This dataset is already downloaded and stored in our MongoDB cluster for easy access and efficient querying. If you would like to get the latest dataset, it can be accessed from [Kaggle](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset). 

To access the database, do one of the following:

1. Follow the download instructions on Kaggle and import the data into the MongoDB cluster to update your local environment.
2. Use the guest credentials provided in the repository.

## Additional Tools Required

- [PowerBI](https://app.powerbi.com/)
- [VS Code](https://code.visualstudio.com/)

## Troubleshooting Common Issues

1. **Java Not Found**:
   - Ensure Java is properly installed and JAVA_HOME is set correctly
   - Run `java -version` to verify Java installation

2. **Spark Connection Issues**:
   - Verify Spark installation: `pyspark --version`
   - Check if SPARK_HOME is set correctly

3. **MongoDB Connection Issues**:
   - Test MongoDB connection separately:
   ```python
   from pymongo import MongoClient
   client = MongoClient("mongodb://localhost:27017/")
   ```

4. **Memory Issues**:
   - Increase Spark driver memory in your code:
   ```python
   spark = SparkSession.builder \
       .config("spark.driver.memory", "4g") \
       .getOrCreate()
   ```

5. **Jupyter Kernel Issues**:
   - Verify all paths in kernel.json are correct
   - Try reinstalling the kernel
   - Check environment variables

## Version Information
- Python: 3.9
- PySpark: 3.5.0
- PyMongo: 4.6.1
- Java: OpenJDK 11

## Support

If you encounter any issues:
1. Check the error message and compare against troubleshooting guide
2. Verify all environment variables are set correctly
3. Ensure all dependencies are installed correctly
4. Check system resources (RAM, CPU usage)
5. Review cluster logs for any error messages
6. Raise an issue in this repository