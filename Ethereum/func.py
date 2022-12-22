from typing import List, Union, Optional

def create_and_import_dataset_time_series_gcs_sample(
    display_name: str,
    project: str,
    location: str,
    gcs_source: Union[str, List[str]],
):

    aiplatform.init(project=project, location=location)

    dataset = aiplatform.TimeSeriesDataset.create(
        display_name=display_name,
        gcs_source=gcs_source,
    )

    dataset.wait()

    print(f'\tDataset: "{dataset.display_name}"')
    print(f'\tname: "{dataset.resource_name}"')
    


#  [START aiplatform_sdk_create_training_pipeline_forecasting_sample]
def create_training_pipeline_forecasting_sample(
    project: str,
    display_name: str,
    dataset_id: str,
    location: str = "us-central1",
    model_display_name: str = "my_model",
    target_column: str = "target_column",
    time_column: str = "date",
    time_series_identifier_column: str = "time_series_id",
    unavailable_at_forecast_columns: List[str] = [],
    available_at_forecast_columns: List[str] = [],
    forecast_horizon: int = 1,
    data_granularity_unit: str = "week",
    data_granularity_count: int = 1,
    training_fraction_split: float = 0.8,
    validation_fraction_split: float = 0.1,
    test_fraction_split: float = 0.1,
    budget_milli_node_hours: int = 8000,
    timestamp_split_column_name: str = "timestamp_split",
    weight_column: str = "weight",
    time_series_attribute_columns: List[str] = [],
    context_window: int = 0,
    export_evaluated_data_items: bool = False,
    export_evaluated_data_items_bigquery_destination_uri: Optional[str] = None,
    export_evaluated_data_items_override_destination: bool = False,
    quantiles: Optional[List[float]] = None,
    validation_options: Optional[str] = None,
    predefined_split_column_name: Optional[str] = None,
    sync: bool = True,
):
    aiplatform.init(project=project, location=location)

    # Create training job
    forecasting_job = aiplatform.AutoMLForecastingTrainingJob(
        display_name=display_name, optimization_objective="minimize-rmse"
    )

    # Retrieve existing dataset
    dataset = aiplatform.TimeSeriesDataset(dataset_id)

    # Run training job
    model = forecasting_job.run(
        dataset=dataset,
        target_column=target_column,
        time_column=time_column,
        time_series_identifier_column=time_series_identifier_column,
        unavailable_at_forecast_columns=unavailable_at_forecast_columns,
        available_at_forecast_columns=available_at_forecast_columns,
        forecast_horizon=forecast_horizon,
        data_granularity_unit=data_granularity_unit,
        data_granularity_count=data_granularity_count,
        training_fraction_split=training_fraction_split,
        validation_fraction_split=validation_fraction_split,
        test_fraction_split=test_fraction_split,
        predefined_split_column_name=predefined_split_column_name,
        timestamp_split_column_name=timestamp_split_column_name,
        weight_column=weight_column,
        time_series_attribute_columns=time_series_attribute_columns,
        context_window=context_window,
        export_evaluated_data_items=export_evaluated_data_items,
        export_evaluated_data_items_bigquery_destination_uri=export_evaluated_data_items_bigquery_destination_uri,
        export_evaluated_data_items_override_destination=export_evaluated_data_items_override_destination,
        quantiles=quantiles,
        validation_options=validation_options,
        budget_milli_node_hours=budget_milli_node_hours,
        model_display_name=model_display_name,
        sync=sync,
    )

    model.wait()

    print(model.display_name)
    print(model.resource_name)
    print(model.uri)
    return 


def create_batch_prediction_job_bigquery_sample(
    project: str,
    display_name: str,
    model_name: str,
    instances_format: str,
    gcs_source_uri: str,
    predictions_format: str,
    bigquery_destination_output_uri: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform_v1beta1.JobServiceClient(client_options=client_options)
    model_parameters_dict = {}
    model_parameters = json_format.ParseDict(model_parameters_dict, Value())

    batch_prediction_job = {
        "display_name": display_name,
        # Format: 'projects/{project}/locations/{location}/models/{model_id}'
        "model": model_name,
        "model_parameters": model_parameters,
        "input_config": {
            "instances_format": instances_format,
            "gcs_source": {"uris": [gcs_source_uri]},
        },
        "output_config": {
            "predictions_format": predictions_format,
            "bigquery_destination": {"output_uri": bigquery_destination_output_uri},
        },
        # optional
        "generate_explanation": True,
    }
    parent = f"projects/{project}/locations/{location}"
    response = client.create_batch_prediction_job(
        parent=parent, batch_prediction_job=batch_prediction_job
    )
    print("response:", response)