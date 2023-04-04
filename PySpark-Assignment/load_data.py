import requests
from pyspark.sql.functions import col
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col
from config import Key, Host


def get_data():
    url = "https://covid-19-india2.p.rapidapi.com/details.php"
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": Host
    }
    response = requests.request("GET", url, headers=headers)
    return response


def clean_data(df):
    df = df.drop('_corrupt_record')
    df = df.where((df.state.isNotNull()) & (df.state != ''))
    df = df.withColumn("confirm", col("confirm")
                       .cast("Long")) \
        .withColumn("cured", col("cured").cast("Long")) \
        .withColumn("death", col("death").cast("Long"))

    df = df.select("slno", "state", "confirm", "cured", "death", "total")
    df = df.withColumn('state', regexp_replace('state', '\*', ""))
    return df


