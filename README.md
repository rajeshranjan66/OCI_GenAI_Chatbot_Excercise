                *****************Update is still in-progress***************
This chatbot will answer your questions related to TOGAF10 and based upon 550 page documentation about TOGAF standard stored in Chroma DB vector database and LLM model. Implemention is using Oracle Cloud Infrastructure.

Oracle Cloud Infrastructure (OCI) Generative AI is a fully managed service that provides a set of state-of-the-art, customizable large language models (LLMs) that cover a wide range of use cases, and which is available through a single API. Using the OCI Generative AI service you can access ready-to-use pretrained models, or create and host your own fine-tuned custom models based on your own data on dedicated AI clusters.

To learn more about OCI genAI services ,refer to this link - https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm and https://docs.oracle.com/en-us/iaas/api/#/en/generative-ai/20231130/

OCI GenAI Proessional certiication is free until July -2024 with 2 free attempt.
Found this course very useful for certificaiton as well as learning RAG, LLM architecture , Encoding & decoding etc. 
https://blogs.oracle.com/oracleuniversity/post/announcing-oci-2024-generative-ai-professional-certification-and-course

It uses -
- OCI Gen AI to access pre-trained LLM Model.
- Model name - cohere.embed-english-v3.0
- Langchan_community framework provides wrapper classes for  using OCI generative AI services as an LLM in LangChain Applications.
- LangSmith APIs - LangSmith uses traces to log almost every aspect of LLM runs. These include metrics such as latency, token count, price of runs, and all types of metadata. The Web 
                   UI allows you to quickly filter runs based on error percentage, latency, date, or even by text content using natural language
                   This repo contains project for chatbot implementation using OCI Gen AI services, StreamLit, LangChain framework, Chroma Vector DB and Python
- RAG - Used for Augmeting prompt with specific context which will be input to LLM.
- Chroma DB - Its vector database, stores TOGAF PDF in chunks. when query received , get the relevant documents from vector DB and insert into prompt. Embedding model used is 
  cohere.embed-english-v3.0
  
This repo consits of 3 python files and pdf-doc folder. 
demo-chroma-create.py
demo-ou-chatbot-chroma-final.py
LLM_GenerateJobDescription.py

pdf-docs folder containing PDF which will be loaded into Chroma Vector DB as embeddings and provide additonal context to LLM model.
If you face any issue while executing commands for chatbot deployment , can refer to Command execution output file in repo.


References -
https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/llm/oci_genai.ipynb
https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/embeddings/oci_genai.ipynb
