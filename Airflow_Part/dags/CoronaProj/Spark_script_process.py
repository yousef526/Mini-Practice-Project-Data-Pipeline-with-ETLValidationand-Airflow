# way to define spark context

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as SparkTypes
from datetime import datetime

""" import os

# Escape backslashes, use raw string, wrap in quotes
os.environ["PYSPARK_SUBMIT_ARGS"] = r'--jars "E:/Projects/Mini Practice Project Data Pipeline with ETL, Validation, and Airflow/Spark_process/postgresql-42.7.5.jar" pyspark-shell'
 """


spark = SparkSession.builder \
    .appName("CoronaProj") \
    .config("spark.jars", "/opt/airflow/dags/CoronaProj/postgresql-42.7.5.jar") \
    .getOrCreate()
    
sc = spark.sparkContext


spark.conf.set("spark.sql.session.timeZone", "Africa/Cairo")



df = spark.read.option("multiline", "true").json("data.json")

#df.printSchema()


#df.show(n=2,truncate=False)


df2 = df.select(
    F.col("continent"),
    F.col("country"),
    F.col("cases"),
    F.col("deaths"),
    F.col("recovered"),
    F.from_unixtime(F.col("updated")/1000).cast("timestamp").alias("egypt_time"),
)


#df2.show(n=5)


df_clean = df2.filter((F.col("cases") >= 0) & (F.col("deaths") >= 0) & (F.col("recovered") >= 0)).dropna()


total_countries = df_clean.select("country").count()
unique_countries = df_clean.select("country").agg(F.countDistinct("country")).collect()[0][0]

if total_countries == unique_countries:
    print("countries are unqiue")
else:
    raise Exception("Countries are not unique")


#df_clean.show(n=4)


#print(spark.sparkContext._jsc.sc().listJars())



import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="host.docker.internal",
    database="postgres",
    user="postgres",
    password="123456789"
)

cursor = conn.cursor()

# Check if the table exists
cursor.execute("""
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE  table_schema = 'public' 
        AND    table_name   = 'corona_proj'
    );
""")

exists = cursor.fetchone()[0]
#print(exists)
# Create the table if it doesn't exist
if not exists:
    cursor.execute("""
        CREATE TABLE public.corona_proj (
            continent CHAR(50),
            country CHAR(50),
            cases INT,
            deaths INT,
            recovered INT,
            egypt_time TIMESTAMP
        );
    """)
    conn.commit()

cursor.close()
conn.close()


df_clean.write.save(f"/opt/airflow/dags/CoronaProj/GeneratedData/{datetime.now()}/data.csv")

df_clean.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/postgres") \
  .option("dbtable", "public.Corona_Proj") \
  .option("user", "postgres") \
  .option("password", "123456789") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append")\
  .save()






