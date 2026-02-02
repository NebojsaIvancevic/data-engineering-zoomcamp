Q1: 134.5 found in gcs bucket

Q2: green_tripdata_2020-04.csv rendered in kestra flow

Q3:
SELECT
  SUM(row_count) AS total_rows_2020
FROM (
  SELECT COUNT(*) AS row_count FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_01`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_02`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_03`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_04`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_05`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_06`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_07`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_08`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_09`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_10`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_11`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2020_12`
);
result = 24,648,499

Q4:
SELECT
  SUM(row_count) AS total_rows_2020
FROM (
  SELECT COUNT(*) AS row_count FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_01`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_02`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_03`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_04`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_05`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_06`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_07`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_08`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_09`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_10`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_11`
  UNION ALL
  SELECT COUNT(*) FROM `kestra-sandbox-486115.dataengineering_zoomcamp.green_tripdata_2020_12`
);
result = 1,734,051

Q5:
SELECT
  SUM(row_count) AS total_rows_2020
FROM (
  SELECT COUNT(*) AS row_count FROM `kestra-sandbox-486115.dataengineering_zoomcamp.yellow_tripdata_2021_03`
  )
result = 1,925,152

Q6: America/New_York in the Schedule trigger configuration -- from Kestra scheduled trigger documentation page.