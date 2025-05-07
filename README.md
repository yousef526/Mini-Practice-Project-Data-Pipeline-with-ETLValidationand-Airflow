# Mini Practice Project: Data Pipeline with ETL Validation and Airflow

This project demonstrates a simple Extract, Transform, Load (ETL) data pipeline using Python, PySpark, and Apache Airflow. It showcases how to fetch data from an API, process it using Spark, and orchestrate the workflow with Airflow.

## Project Structure

```
.
├── Airflow_Part/
│   └── dags/
│       └── etl_dag.py
├── Spark_process/
│   └── spark_etl.py
├── APi call and data download/
│   └── data_fetch.py
├── requirements.txt
└── README.md
```

- **Airflow_Part/**: Contains the Airflow DAG definition for scheduling and orchestrating the ETL tasks.
- **Spark_process/**: Holds the PySpark script responsible for data transformation and validation.
- **APi call and data download/**: Includes the script to fetch data from the API source.
- **requirements.txt**: Lists the Python dependencies required to run the project.

## Features

- **Data Extraction**: Fetches data from a specified API endpoint and stores it locally.
- **Data Transformation**: Utilizes PySpark to clean, transform, and validate the extracted data.
- **Workflow Orchestration**: Leverages Apache Airflow to schedule and monitor the ETL pipeline.

## Prerequisites

- Python 3.6 or higher
- Apache Spark
- Apache Airflow
- Java 8 or higher (required for Spark)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yousef526/Mini-Practice-Project-Data-Pipeline-with-ETLValidationand-Airflow.git
   cd Mini-Practice-Project-Data-Pipeline-with-ETLValidationand-Airflow
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Apache Airflow**:
   - Initialize the Airflow database:
     ```bash
     airflow db init
     ```
   - Create a user account:
     ```bash
     airflow users create \
       --username admin \
       --firstname Firstname \
       --lastname Lastname \
       --role Admin \
       --email admin@example.com
     ```
   - Start the Airflow web server and scheduler:
     ```bash
     airflow webserver --port 8080
     airflow scheduler
     ```

## Usage

1. **Data Extraction**:
   - Navigate to the `APi call and data download/` directory.
   - Run the `data_fetch.py` script to fetch data from the API:
     ```bash
     python data_fetch.py
     ```

2. **Data Transformation**:
   - Navigate to the `Spark_process/` directory.
   - Run the `spark_etl.py` script to process the data using PySpark:
     ```bash
     spark-submit spark_etl.py
     ```

3. **Workflow Orchestration**:
   - Ensure that the Airflow web server and scheduler are running.
   - Access the Airflow web interface at `http://localhost:8080`.
   - Trigger the `etl_dag` to execute the entire ETL pipeline.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

You can download the README file directly and use it for documentation or setup reference.
