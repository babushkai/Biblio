# Get project
#!export PROJECT=$(gcloud config list project --format "value(core.project)")
#!echo "Your current GCP Project Name is: "$PROJECT

#or 

# PROJECT_ID = "[your-project-id]"
# if PROJECT_ID == "" or PROJECT_ID is None or PROJECT_ID == "[your-project-id]":
#     # Get your GCP project id from gcloud
#     shell_output = ! gcloud config list --format 'value(core.project)' 2>/dev/null
#     PROJECT_ID = shell_output[0]
#     print("Project ID:", PROJECT_ID)


#!export REGION=us-central1
#!gsutil mb -l ${REGION} gs://${PROJECT}

