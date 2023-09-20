# llm-gke-deploy-automation
A quick prototype showing a strawman solution approach to improve the Developer Efficiency. This demonstrates using the Code Bison to generate a manifest file and automatically deploying it to GKE

# Synopsis:
This use-case targets Application Developers and Data Scientists who may not be very comfortable with DevOps execution (Cloud plumbing) for deploying their applications to distributed computing systems like GKE. As per the prototype, the user enters designs a prompt (currently hardcoded in the python file) and generates a manifest file using the Code Bison model from Vertex AI. This is refined and automatically deployed to a GKE cluster. The application is available for unit testing for Application Developers and Data Scientists without writing a piece of code or having to dependent on DevOps, SRE teams. This demonstrated the usage of GenAI in improving the Developer efficiency

# Pre-requisites and Assumptions:
1. An active GCP project exists with Vertex AI and Container (GKE) APIs enabled
2. There is a service account or user having the right permissions to call vertex APIs, create a GKE cluster and deploy manifest files to GKE.
3. The script creates a GKE cluster from scratch (as it assumes that there is no GKE cluster present. You could deploy the LLM generated artifact to an existing GKE cluster as well)

# Components
The prototype uses the following GCP components - Vertex AI APIs (Code Bison), Google Kubernetes Engine, Langchain framework and related Python libraries. 

# Steps to run the prototype 
The following steps may be used to run this straw man prototype:
1. Clone the repo
2. Change the directory to the llm-gee-deploy-automation directory
3. Run the llm-gee-deploy-automate.sh script (This has only been tested in Linux)
4. Log on to GKE and verify that pods are running.

# Limitations and Improvements
This is a prototype created to demonstrate the idea and has some limitations. I have coded the GenAI prompt inside the Python code itself as the objective was to quickly demonstrate the feasibility of this idea. I have plans to use Gradio or Streamlit to build a user interface, use prompt templates, few-shot prompts to generate complex artifacts, use variables and run-time parameters for the next version of this prototype. Currently the prototype is directly integrated with GKE, but this could be broadened to commit the generated artifact to a github repository and trigger a CICD pipeline for automation. Customers can also perform instruction tuning to ingest their artifact templates to elicit a similar response from Code Bison output. This use-case can also be extended to other run-times. 
