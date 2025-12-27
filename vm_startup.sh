#!/bin/bash
# Set project, instance, and zone details
INSTANCE_NAME="draftkings-vm"
ZONE="us-central1-a"
PROJECT_ID="nfl-betting-project"
SERVICE_ACCOUNT="terraform-draftkings-gcp"
SERVICE_ACCOUNT_PATH="./nfl-betting-project-54dfcba125fa.json"
VM_USER="script_runner"
USER_PASSWORD='w1ll1amT@ft'


gcloud auth activate-service-account $SERVICE_ACCOUNT@$PROJECT_ID.iam.gserviceaccount.com --key-file=$SERVICE_ACCOUNT_PATH

# Check the instance status
STATUS=$(gcloud compute instances describe $INSTANCE_NAME --zone=$ZONE --project=$PROJECT_ID --format="value(status)")

# Check if the status is 'TERMINATED'
if [ "$STATUS" == "TERMINATED" ]; then
    echo "Instance is stopped. Starting up..."
    gcloud compute instances start $INSTANCE_NAME --zone=$ZONE --project=$PROJECT_ID
    echo "Instance started."
else
    echo "Instance is not stopped. Current status: $STATUS"
fi


source venv/bin/activate

sleep 30

python3 fill_odds.py