CREATE OR REPLACE EXTERNAL TABLE `zoomcamp-487513.nytaxi.fhv_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://zoomcamp-kestra-kv-1/fhv_tripdata_2019-*.csv']
);


SELECT count(*) FROM `zoomcamp-487513.nytaxi.fhv_tripdata`;


SELECT COUNT(DISTINCT(dispatching_base_num)) FROM `zoomcamp-487513.nytaxi.fhv_tripdata`;


CREATE OR REPLACE TABLE `zoomcamp-487513.nytaxi.fhv_nonpartitioned_tripdata`
AS SELECT * FROM `zoomcamp-487513.nytaxi.fhv_tripdata`;

CREATE OR REPLACE TABLE `zoomcamp-487513.nytaxi.fhv_partitioned_tripdata`
PARTITION BY DATE(dropoff_datetime)
CLUSTER BY dispatching_base_num AS (
  SELECT * FROM `zoomcamp-487513.nytaxi.fhv_tripdata`
);

SELECT count(*) FROM  `zoomcamp-487513.nytaxi.fhv_nonpartitioned_tripdata`
WHERE DATE(dropoff_datetime) BETWEEN '2019-01-01' AND '2019-03-31'
  AND dispatching_base_num IN ('B00987', 'B02279', 'B02060');


SELECT count(*) FROM `zoomcamp-487513.nytaxi.fhv_partitioned_tripdata`
WHERE DATE(dropoff_datetime) BETWEEN '2019-01-01' AND '2019-03-31'
  AND dispatching_base_num IN ('B00987', 'B02279', 'B02060');