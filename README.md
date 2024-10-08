# EDA Streamlit Application

## 📄 Description

This repository contains a **Streamlit application** designed for **Exploratory Data Analysis (EDA)**. The application allows users to upload **Parquet files**, interact with the data, and perform various EDA tasks such as viewing data summaries, visualizing distributions, and analyzing correlations. The project also provides a logging system to track user interactions and operations.

## 🛠️ Installation

To install the package and its dependencies, run the following command:

```bash
pip install -r requirements.txt







# EDA Streamlit App

## 📁 Project Structure

Below is the structure of the key files and classes within the project:

### 1. `models/data_model.py`
**Class**: `DataModel`

This class is responsible for loading and analyzing Parquet files. It provides methods to inspect the data, categorize columns, and generate summaries.

#### 📜 Methods:
- `__init__(self, file)`: Initializes the data model with a file.
- `load_data(self, file)`: Loads the data from the given file.
- `get_data(self)`: Returns the loaded data.
- `find_dtypes(self)`: Identifies data types for each column.
- `update_dataframes(self)`: Updates internal data structures.
- `numerical_col(self)`: Identifies numerical columns.
- `categorical_col(self)`: Identifies categorical columns.
- `datetime_col(self)`: Identifies datetime columns.
- `numerical_describe(self)`: Provides summary statistics for numerical columns.
- `categorical_describe(self)`: Provides summary statistics for categorical columns.
- `datetime_describe(self)`: Provides summary statistics for datetime columns.

---

### 2. `page/eda.py`
**Class**: `EDA`

This class provides the EDA functionality, enabling users to explore the dataset through various visualizations and summaries.

#### 📜 Methods:
- `__init__(self)`: Initializes the EDA page.
- `display(self)`: Displays the EDA interface.
- `show_data_summary(self, data)`: Shows a summary of the dataset.
- `plot_histograms(self, data, columns)`: Plots histograms for numerical columns.
- `plot_categorical_distributions(self, data, columns)`: Plots distributions for categorical columns.
- `plot_correlation_matrix(self, data, columns)`: Plots the correlation matrix for numerical columns.
- `plot_time_series(self, data, columns)`: Plots time series data for datetime columns.
- `plot_boxplots(self, data, columns)`: Plots boxplots for selected columns.

---

### 3. `page/home.py`
**Class**: `HomePage`

This class handles the homepage functionality where users can set their username and upload data files.

#### 📜 Methods:
- `__init__(self)`: Initializes the home page.
- `display(self)`: Displays the home page interface.

---

### 4. `utils/logger.py`
**Class**: `OperationLogger`

A logging system to track user interactions and operations. It stores logs in a CSV file for future reference.

#### 📜 Methods:
- `__init__(self, log_file='utils/operation_logs.csv')`: Initializes the logger with the specified log file.
- `ensure_log_file_exists(self)`: Ensures that the log file exists.
- `log_operation(self, user, operation, columns=None)`: Logs a user operation.
- `append_logs_to_csv(self)`: Appends log entries to the CSV file.
- `show_logs(self)`: Displays the log data.

---

### 5. `page/data_manager.py`
**Class**: `DataManager`

This class is responsible for loading the data model and providing access to the loaded data for further analysis.

#### 📜 Methods:
- `__init__(self)`: Initializes the DataManager.
- `load_data(self, file)`: Loads the dataset and creates a DataModel instance.
- `get_data_model(self)`: Provides access to the DataModel instance.

---

## 📝 Features

- **Data Upload**: Upload Parquet files for analysis.
- **Summary Statistics**: Automatically generate summary statistics for numerical, categorical, and datetime data.
- **Visualizations**: Visualize the data with histograms, boxplots, correlation matrices, and time series plots.
- **Operation Logging**: Tracks user operations and saves logs for auditing or review purposes.

---

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/your-repo/eda-streamlit-app.git
