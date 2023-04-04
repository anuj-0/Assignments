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





    get_highest_covid_cases=df.sort((df.confirm).cast("Long").desc()).select(col("state")).collect()[0][0]
    get_highest_covid_cases.show()


    get_least_covid_cases=df.sort(df.confirm.cast("Long")).select(col("state")).collect()[0][0]
    get_least_covid_cases.show()

def total_cases():
    total_cases=df.select(sum(df.confirm).alias("Total cases")).collect()[0][0]
    total_cases.show()

def most_efficient_state():
    most_efficient_state=df.sort((df.cured.cast("Long")/df.total.cast("Long")).desc()).select(col("state")).collect()[0][0]
    most_efficient_state.show()

def least_efficient_state():
    least_efficient_state=df.sort((df.cured.cast("Long")/df.total.cast("Long")).asc()).select(col("state")).collect()[0][0]
    least_efficient_state.show()

def main():
    spark = SparkSession.builder.master('local[*]').getOrCreate()
    sc = SparkContext.getOrCreate()
    sc.setLogLevel("ERROR")
    response = get_data()
    json_rdd = sc.parallelize(response.json().values())
    df = spark.read.json(json_rdd)
    df = clean_data(df)

    print("Brief view of the data after cleaning: ")
    df.show(10)

    most_affected_state = df.sort((df.death.cast("Long") / df.confirm.cast("Long")).desc()).select(col("state")).collect()[0][0]
    most_affected_state.show()

    least_affected_state = df.sort((df.death.cast("Long") / df.confirm.cast("Long"))).select(col("state")).collect()[0][0]
    least_affected_state.show()

