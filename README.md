                *****************Update is still in-progress***************
This chatbot will answer your questions related to TOGAF10 and based upon 550 page documentation about TOGAF standard stored in terms of embeddings in Chroma DB vector database and using OCI provided API for LLM. 
Oracle Cloud Infrastructure (OCI) Generative AI is a fully managed service that provides a set of state-of-the-art, customizable large language models (LLMs) that cover a wide range of use cases, and which is available through a single API. Using the OCI Generative AI service you can access ready-to-use pretrained models, or create and host your own fine-tuned custom models based on your own data on dedicated AI clusters.

To learn more about OCI genAI services ,refer to this link - 
https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm and 
https://docs.oracle.com/en-us/iaas/api/#/en/generative-ai/20231130/

OCI GenAI Proessional certiication is free until July -2024 with 2 free attempt.
Found this course very useful for certificaiton as well as learning RAG, LLM architecture , Encoding & decoding etc. 
https://blogs.oracle.com/oracleuniversity/post/announcing-oci-2024-generative-ai-professional-certification-and-course

It uses -
- OCI Gen AI API to access pre-trained LLM Model.
- Model name - cohere.embed-english-v3.0
- Langchan_community - LangChain is an open source modular framework for creating applications from large language models (LLMs). You can use LangChain to build chatbots, analyze text, perform Q&A from structured data, interact with APIs, and create applications that use generative AI.

- LangSmith  - LangSmith uses traces to log almost every aspect of LLM runs. These include metrics such as latency, token count, price of runs, and all types of metadata. The Web 
                   UI allows you to quickly filter runs based on error percentage, latency, date, or even by text content using natural language
                   
- RAG - Used for Augmeting prompt with specific context which will be input to LLM.
- Chroma DB - Its vector database, stores TOGAF PDF in terms of embedddings. when query received , get the relevant documents from vector DB and insert into prompt. Embedding model used is cohere.embed-english-v3.0
  
This repo consits of 3 python files and pdf-doc folder. 
demo-chroma-create.py
demo-ou-chatbot-chroma-final.py
LLM_GenerateJobDescription.py

pdf-docs folder containing PDF which will be loaded into Chroma Vector DB as embeddings and provide additonal context to LLM model.
If you face any issue while executing commands for chatbot deployment , can refer to Command execution output file in repo.


References -
https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm
https://github.com/langchain-ai/langchain/blob/master/README.md
https://python.langchain.com/v0.2/docs/integrations/llms/oci_generative_ai/

****Below are the steps on how to deploy chatbot on oracle VM** **This will incur cost for using Oracle VM and hiting Oracle Gen AI services**

Assumption - you have OCI account and created Oracle VM and setup public and priate keys in your account. all the commands shown on screenshot is also avaialble in file https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/master/Oci_GenAI_Python/Command%20execution%20output

** ensure you have downloaded keys from your OCI account for accessing Oracle Instance (VM) on you local machine ( laptop) **

<img width="670" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/c73f6bc2-3545-4678-ad1a-79688130b2fd">

** ssh into oracle VM **

<img width="768" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/d71493b3-d70c-4b00-ba6d-7e7884c1f450">

** create required folders where code python files and other required fileswill be copied and uogarde ubuntu packages**
 

<img width="781" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/26962c1a-520a-4ef5-b1b7-8fcbe363909e">

** install Python on VM **

<img width="490" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/7b51adaa-5bf6-4c47-9d27-93536933a27b">

** install virtual environment **

<img width="1035" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/dcb57c3c-391e-4d88-8a53-7f50f302cfaf">
<img width="1141" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/c60da1b8-bf4e-4d45-96b9-8b98612f7d25">
<img width="807" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/2ed21017-fb85-4d03-a0f6-c9d9c7004bb3">

**Create virtual env and activate **
<img width="1075" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/dcd031c0-56e3-46ec-92a7-3565ed40b39b">

**copy python code for creating Choma DB and chatbot into oracle VM and TOGAF PDF on OCI VM , this command you will be executing on laptop  **

<img width="1468" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/11862855-2a3e-4539-b56f-2065a93cd678">

<img width="707" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/1bb46f38-f17b-44f9-9e85-b449779440ef">

** Install necessary python packages on OCI VM **

install oci
<img width="1392" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/a2ac734c-0f24-408a-bfe0-902865ac48ed">

install oracle-ads
<img width="992" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/2f2a527a-98d1-45af-9d2c-f265e7abca44">
<img width="1454" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/afc6b11f-d821-4ead-b0ba-b0f948dd1a31">

Install langchain

<img width="1020" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/089dd3a5-f71e-4383-a957-16ffffa921ba">
<img width="1443" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/05a7f573-510e-43dc-a1d4-f720d503f381">

Install ChromaDB 

<img width="961" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/0599de3b-84fc-4fe7-9c73-f0fb6a077284">
<img width="1463" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/a4cea1d9-0642-4be7-ac8d-20826c41f866">








