# bigquery-holidays
Python code to generate holidays to put in BigQuery.

This code was written as a part of medium article: https://medium.com/@ael-computas/bigquery-and-holidays-2b26cfb315a6

This program generates holidays from 1900 - 2050 and stores it in GCSas PARQUET files (one for each year).
You will have to load into BigQuery yourself.

````bash
bq --location=EU load --source_format=PARQUET --replace holidays.holidays gs://the-bucket/path/*
````

## Installation

```bash
pip install -r requirements.txt
``` 

## Usage
Edit the main.py and change BASE_PATH to either a local filesystem or your own gcs bucket.

If you want to store in S3 or similar you can do that, but then you would need to update requirements.txt
first and change the smart_open dependencies.

## BigQuery
Feel free use `ael-cx.holidays.holidays` as a source for your own holidays table in BigQuery (until google
adds its own CANON dataset).