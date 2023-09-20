# Install or update needed software

# Install Google Cloud Vertex AI
pip install google-cloud-aiplatform

# Install  vertexai 
pip3 install vertexai

# Install langchain
pip install langchain

# Install pandas
pip install pandas

# install python client for gcp
pip install google-api-python-client
pip install google-cloud-language

# install pypdf
pip install pypdf

# Execute the python program that  generates a prompt
# and uses code bison to automate the generation of
# k8s podspec (manifest) file  
python llm-gke-automate.py 

#Clean up the manifest file to make it executable by kubectl
sed 's/```//g' sample-deployment.yaml>sample-deployment-v1.yaml

# Verify the manifest file
cat sample-deployment-v1.yaml

# Create a GKE cluster (if not already exists)
gcloud container clusters create llm-gke-deploy-dev-cluster --zone=us-central1-a

# Get credentials for the GKE cluster after its created
gcloud container clusters get-credentials llm-gke-deploy-dev-cluster --zone=us-central1-a

# Deploy the manifest file generated by code bison to the GKE
kubectl apply -f sample-deployment-v1.yaml
