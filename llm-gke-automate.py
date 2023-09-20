# Import the langchain package
import langchain
print(f"LangChain version: {langchain.__version__}")

# Use the GCP AI platform SDK
from google.cloud import aiplatform
print(f"Vertex AI SDK version: {aiplatform.__version__}")

# Use VertexAI from langchain library
from langchain.llms import VertexAI

# Select the LLM Model to use with Vertex. Choose Code Bison for this use-case
from langchain.llms import VertexAI
llm = VertexAI(
    model_name='code-bison@001',
    max_output_tokens=256,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
)

# Design the prompt as below. The objective is to generate kubernetes manifest files for automated deployment 
prompt = """
You are an expert GKE admin working for Google Cloud.  You must provide manifest files in yaml format that can directly deployed to GKE using kubectl apply command. 

Generate a manifest file in yaml format to deploy an nginx application that will need 0.3 vCPU and 250 MB of memory, but should have a limit of  1VCPU and 1GB. The controller should be of type Deployment, application should run on port 80 and should horizontally scale  with a minimum of 2 replicas.
"""
# Store and print the response from LLM
result=llm(prompt)
print(result)

# Write teh response to a physical file that will be automatically applied  using kubernetes API
with open('sample-deployment.yaml', 'w') as writefile:
    writefile.write(result)
