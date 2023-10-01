from google.cloud import bigquery
import os
def upload2Data():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"/home/tier1marketspace/ncua/keys/hjs-376018-5dd2d3c1c351.json"

    client = bigquery.Client()

    tableNames = [
    "headfs220",
    "headfs220A",
    "headfs220B",
    "headfs220C",
    "headfs220D",
    "headfs220E",
    "headfs220G",
    "headfs220H",
    "headfs220I",
    "headfs220J",
    "headfs220K",
    "headfs220L",
    "headfs220M",
    "headfs220N",
    "headfs220P",
    "headfs220Q",
    "headfs220R",
    ]



    for x in tableNames:

        # TODO(developer): Set table_id to the ID of the table to create.
        table_id = "hjs-376018.ncua_data.%s" % (x)
        file_path = r"/home/tier1marketspace/ncua/mergedHeaders/%s.csv" % (x)



        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
                write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  #added to have truncate and insert load
        )

        with open(file_path, "rb") as source_file:
            job = client.load_table_from_file(source_file, table_id, job_config=job_config)

        job.result()  # Waits for the job to complete.

        table = client.get_table(table_id)  # Make an API request.
        print(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.schema), table_id
            )
        )