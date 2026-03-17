resources:
  jobs:
    medallion_job:
      name: medallion_job

      tasks:
        - task_key: ingest
          spark_python_task:
            python_file: ../src/etl/ingest.py

        - task_key: transform
          depends_on:
            - task_key: ingest
          spark_python_task:
            python_file: ../src/etl/transform.py

        - task_key: gold
          depends_on:
            - task_key: transform
          spark_python_task:
            python_file: ../src/etl/gold.py
