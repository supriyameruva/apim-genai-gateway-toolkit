import os

apim_subscription_one_key = os.getenv("APIM_SUBSCRIPTION_ONE_KEY")
apim_subscription_two_key = os.getenv("APIM_SUBSCRIPTION_TWO_KEY")
apim_subscription_three_key = os.getenv("APIM_SUBSCRIPTION_THREE_KEY")
apim_endpoint = os.getenv("APIM_ENDPOINT")
app_insights_name = os.getenv("APP_INSIGHTS_NAME")
app_insights_connection_string = os.getenv("APP_INSIGHTS_CONNECTION_STRING")
log_analytics_workspace_id = os.getenv("LOG_ANALYTICS_WORKSPACE_ID")
log_analytics_workspace_name = os.getenv("LOG_ANALYTICS_WORKSPACE_NAME")
simulator_endpoint_ptu1 = os.getenv("SIMULATOR_ENDPOINT_PTU1")
simulator_endpoint_payg1 = os.getenv("SIMULATOR_ENDPOINT_PAYG1")
simulator_endpoint_payg2 = os.getenv("SIMULATOR_ENDPOINT_PAYG2")
simulator_api_key = os.getenv("SIMULATOR_API_KEY")
tenant_id = os.getenv("TENANT_ID")
subscription_id = os.getenv("SUBSCRIPTION_ID")
resource_group_name = os.getenv("RESOURCE_GROUP_NAME")


# Load connection string from environment variable or configuration
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
