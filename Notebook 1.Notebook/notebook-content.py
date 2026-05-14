# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2b8a7bbc-ec35-4576-82dc-50357a47730e",
# META       "default_lakehouse_name": "lkh1",
# META       "default_lakehouse_workspace_id": "22b62141-7d27-40cd-8359-744a3bbd44c2",
# META       "known_lakehouses": [
# META         {
# META           "id": "2b8a7bbc-ec35-4576-82dc-50357a47730e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/orders.csv")
# df now is a Spark DataFrame containing CSV data from "Files/orders.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('v1')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
