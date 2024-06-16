# PySpark Project Setup

This project demonstrates setting up a PySpark environment in Visual Studio Code with Git and a virtual environment (`venv`).

## Prerequisites

- Python
- Java
- Git
- Visual Studio Code

## Setup Instructions

1. **Install Prerequisites**:
    - Download and install [Python](https://www.python.org/downloads/)
    - Download and install [Java JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
    - Download and install [Git](https://git-scm.com/downloads)
    - Download and install [Visual Studio Code](https://code.visualstudio.com/Download)

2. **Create a Project Directory**:
    ```bash
    mkdir pyspark_project
    cd pyspark_project
    ```

3. **Initialize Git Repository**:
    ```bash
    git init
    ```

4. **Create and Activate Virtual Environment**:
    ```bash
    python -m venv venv
    ```
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. **Install PySpark**:
    ```bash
    pip install pyspark
    ```

6. **Open Project in VS Code**:
    ```bash
    code .
    ```

7. **Install Python Extension**:
    - In VS Code, go to the Extensions view and install the Python extension.

8. **Select Python Interpreter**:
    - Press `Ctrl+Shift+P`, type "Python: Select Interpreter", and choose the virtual environment.

9. **Create a Test Script**:
    - Create `pyspark_test.py` and add the following code:
      ```python
      from pyspark.sql import SparkSession

      spark = SparkSession.builder \
          .appName("PySparkTest") \
          .getOrCreate()

      data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
      df = spark.createDataFrame(data, ["Name", "Age"])

      df.show()
      ```

10. **Run the Script**:
    - Run the script using the Python extension in VS Code.

11. Datset used in this file can be downloaded from https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop 

## Usage

Activate the virtual environment and run your PySpark scripts.

- **Activate Virtual Environment**:
  - **Windows**:
    ```bash
    .\venv\Scripts\activate
    ```
  - **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

- **Run PySpark Script**:
  ```bash
  python pyspark_test.py

- **Reference**:
    - PySpark for Data Engineering Beginners: An Extensive Guide - https://pawankg.medium.com/pyspark-for-data-engineering-beginners-an-extensive-guide-ce29520a78ca
    - Case Studies - https://github.com/sauryaritesh/Real-Time-Case-Study-Based-Scenarios-using-PySpark
