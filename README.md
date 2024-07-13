                      *****************Chatbot for TOGAF powered by OCI Services ***************
                          
This chatbot will answer your queries related to TOGAF10 concepts and based upon 550 page documentation about TOGAF standard 
TOGAF related documents are stored in terms of embeddings in Chroma DB vector database and using OCI provided API for embdedding models.
Oracle Cloud Infrastructure (OCI) Generative AI is a fully managed service that provides a set of state-of-the-art, 
customizable large language models (LLMs) that cover a wide range of use cases, and which is available through a single API. 
Using the OCI Generative AI service you can access ready-to-use pretrained models, or 
create and host your own fine-tuned custom models based on your own data on dedicated AI clusters.


To learn more about OCI genAI services ,refer to this link - 

[Oracle Generative AI Certification course] (https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)


https://docs.oracle.com/en-us/iaas/api/#/en/generative-ai/20231130/

OCI GenAI Proessional certiication is free until July -2024 with 2 free attempt.
Found this course very useful for certificaiton as well as learning RAG, LLM architecture , Encoding & decoding etc. 
https://blogs.oracle.com/oracleuniversity/post/announcing-oci-2024-generative-ai-professional-certification-and-course

Details of the Chat bot setup and deployment-
- OCI Gen AI API to access pre-trained LLM Model.
- Model name for embedding is cohere.embed-english-v3.0
- Langchan_community - LangChain is an open source modular framework for creating applications from large language models (LLMs). You can use LangChain to build chatbots, analyze text, perform Q&A from structured data, interact with APIs, and create applications that use generative AI.

- LangSmith  - LangSmith uses traces to log almost every aspect of LLM runs. These include metrics such as latency, token count, price of runs, and all types of metadata. The Web  UI allows you to quickly filter runs based on error percentage, latency, date, or even by text content using natural language
                   
- RAG - Used for Augmeting prompt with specific context which will be input to LLM. LLM model used is cohere.command
- Chroma DB - Its vector database, stores TOGAF PDF in terms of embedddings. when query received , get the relevant documents from vector DB and insert into prompt. Embedding model used is cohere.embed-english-v3.0
  
This repo consits of 3 python files and pdf-doc folder. 
[demo-chroma-create.py](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/demo-chroma-create.py)
[demo-ou-chatbot-chroma-final.py](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/demo-ou-chatbot-chroma-final.py)
[LLM_GenerateJobDescription.py](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/LLM_GenerateJobDescription.py)

pdf-docs folder containing PDF which will be loaded into Chroma Vector DB as embeddings and provide additonal context to LLM model.
If you face any issue while executing commands for chatbot deployment , can refer to [Command execution output file[(https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/Command%20execution%20output)  in repo.

Step by step details are on below links-

1. [How to create OCI config file](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/cb05182b29a70524c9b696c6fd05b983cbfbb228/How%20to%20Create%20OCI%20config%20file.md)

   
3. [How to create OCI VM]
   (https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/cb05182b29a70524c9b696c6fd05b983cbfbb228/How%20to%20create%20OCI%20VM.md)
   
5. [How to deploy python code on OCI VM]
   (https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/cb05182b29a70524c9b696c6fd05b983cbfbb228/How_to_deploy_chatbot_in_OCI.md)


References -

https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm

https://github.com/langchain-ai/langchain/blob/master/README.md

https://python.langchain.com/v0.2/docs/integrations/llms/oci_generative_ai/


**hit below URL in browser  - **
http:// public IP of OCI VM:8501
I added some more PDFs related to TOGAF, executed demo-chroma-create.py , restarted chromaDB
I asked few question to chatbot and also inputed mutilple choice question and chatbot shows correct answer and PDF document with page number where it is getting context from to send to LLM. Few screenshots.
chat history of the session will also be passed to LLM along with original prompt.

<img width="1126" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/df2a1291-f8b3-408c-a406-40b1e8117a2c">



<img width="1162" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/3fdd104b-f0fe-4dad-b432-0a91943a5a89">



<img width="1176" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/bfbac318-048f-4e05-9dc2-f2645628d0dd">



<img width="1148" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/55f9a8cc-9e9a-46da-a02a-d421dbc2062b">












