import pandas as pd

file_location_csv = '/home/nebojsa/docker-workshop/taxi_zone_lookup.csv'
file_location_parquet = '/home/nebojsa/docker-workshop/green_tripdata_2025-11.parquet'
df_csv = pd.read_csv(file_location_csv)
df_parquet = pd.read_parquet(file_location_parquet)



print(df_csv.info())
print(df_csv.dtypes)
print(df_parquet.info())
print(df_parquet.dtypes)