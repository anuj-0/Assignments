from pyspark.sql.types import *
from pyspark.sql.functions import *
from flask import Flask, jsonify
from pyspark.sql.functions import sum
import requests
from pyspark.sql.functions import col
from pyspark import SparkContext
from pyspark.sql import SparkSession
# from config import KEY
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col
from load_data import get_data, clean_data

if __name__ == "__main__":
    spark = SparkSession.builder.master('local[*]').getOrCreate()
    sc = SparkContext.getOrCreate()
    sc.setLogLevel("ERROR")
    response = get_data()
    json_rdd = sc.parallelize(response.json().values())
    df = spark.read.json(json_rdd)
    df = clean_data(df)

    print("Brief view of the data after cleaning: ")
    df.show(10)

    # 1. Most affected state among all the states(total death / total covid cases).
    most_affected_state = df.sort((df.death.cast("Long") / df.confirm.cast("Long")).desc()).select(col("state")).collect()[0][0]
    print(f" Most affected state among all the states: {most_affected_state}")

    # 2 Least affected state among all the states(total death / total covid cases).
    least_affected_state = df.sort((df.death.cast("Long") / df.confirm.cast("Long"))).select(col("state")).collect()[0][0]
    print(f"Least affected state among all the states: {least_affected_state}")

    # 3. State with the highest covid cases.
    state_with_highest_covid_cases = df.sort(df.confirm.cast("Long").desc()).select(col("state")).collect()[0][0]
    print(f"State with the highest covid cases: {state_with_highest_covid_cases}")

    # 4. State with minimum covid cases.
    state_with_least_covid_cases = df.sort(df.confirm.cast("Long")).select(col("state")).collect()[0][0]
    print(f"State with the least covid cases: {state_with_least_covid_cases}")

    # 5. Total cases.
    total_cases = df.select(sum(df.confirm).alias("Total cases")).collect()[0][0]
    print(f"Total cases: {total_cases}")

    # 6. State that handled the covid most efficiently( total recovery / total covid cases).
    most_efficient_state = df.sort((df.cured.cast("Long") / df.total.cast("Long")).desc()).select(col("state")).collect()[0][0]
    print(f"State that handled the covid most efficiently {most_efficient_state}")

    # 7. State that handled the covid least efficiently( total recovery / total covid cases).
    least_efficient_state = df.sort((df.cured.cast("Long") / df.total.cast("Long")).asc()).select(col("state")).collect()[0][0]
    print(f"State that handled the covid least efficiently {least_efficient_state}")
