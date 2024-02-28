from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "marine-embassy-413623"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load", 
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://pokemon_tcg_dataflow_metadata/udf.js",
        "JSONPath": "gs://pokemon_tcg_dataflow_metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "marine-embassy-413623:pokemon_tcg_dataset.pokemon_tcg_cards",
        "inputFilePattern": "gs://pokemon_tcg_data/pokemon_tcg_cards.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://pokemon_tcg_dataflow_metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)