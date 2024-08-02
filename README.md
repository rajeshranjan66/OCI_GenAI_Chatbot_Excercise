                      **Building a Personalized Chatbot With LangChain and Oracle Generative AI Service **

                          
This chatbot will respond to your queries  and questions related to TOGAF 10 concepts.


To learn about OCI Generative AI services ,refer to [Oracle Generative AI Certification course](https://mylearn.oracle.com/ou/course/oci-generative-ai-professional/136035/2126370) I found this course very useful for certificaiton as well as learning RAG, LLM architecture , Encoding & decoding etc. 

OCI GenAI Proessional certiication is free until July -2024 with 2 free attempt.[Check this blog for more details about certification details](https://blogs.oracle.com/oracleuniversity/post/announcing-oci-2024-generative-ai-professional-certification-and-course)


Below is the architecture of the RAG based chatbot -

<img width="1151" alt="image" src="https://github.com/user-attachments/assets/d5acbae3-77b1-48a2-ba34-314c90d402de">


Oracle Cloud Infrastructure (OCI) Generative AI is a fully managed service that provides a set of state-of-the-art, 
customizable large language models (LLMs) that cover a wide range of use cases, and which is available through a single API. 
Using the OCI Generative AI service you can access ready-to-use pretrained models, or 
create and host your own fine-tuned custom models based on your own data on dedicated AI clusters.

- In this implementation TOGAF standard and additional documents are stored in form of embeddings in Chroma vector database.
- OCI Gen AI API to access pre-trained LLM Model for embdedings and responding to user queries.
- Model name for embedding is cohere command.
- Langchan  - An opensource framework used for developing applications powered by LLMs. LangChain provides many libraries, APIs and templates to make it easy for us to develop applications powered by LLMs. LangChain integrates with OCI services , and can be used to invoke the OCI Gen AI APIs.
  
- LangSmith  - LangSmith uses traces to log almost every aspect of LLM runs. These include metrics such as latency, token count, price of runs, and all types of metadata. The Web  UI allows you to quickly filter runs based on error percentage, latency, date, or even by text content using natural language
                   
- RAG - Used for Augmeting prompt with specific context which will be the input to LLM. This chatbot uses OCI Generative AI embedding 
   models together with a Cohere command pre-trained LLM to implement a RAG pattern.
- Chroma DB - Its open source vector database, stores TOGAF PDF in terms of embedddings. when query received , get the relevant documents from vector DB and insert into prompt. Embedding model used is cohere.embed-english-v3.0

This repo consits of 3 python files and pdf-doc folder. 


[chroma_DB_Embeddings.py](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/chroma_DB_Embeddings.py)


[chatbot_with_Chroma.py](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/chatbot_with_Chroma.py)


[LLM_GenerateJobDescription.py](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/LLM_GenerateJobDescription.py)

pdf-docs folder containing PDF which will be loaded into Chroma Vector DB as embeddings and provide additonal context to LLM model.
If you face any issue while executing commands for chatbot deployment, refer to [Command execution output file](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/fdab025d4b9bc407fbea452a8d0702bd8deb1c21/Oci_GenAI_Python/Command%20execution%20output)  in repo.

**Step by step details with screenshots are on below links with-in repo-**

1. [How to create OCI config file](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/cb05182b29a70524c9b696c6fd05b983cbfbb228/How%20to%20Create%20OCI%20config%20file.md)

   
2. [How to create OCI VM](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/cb05182b29a70524c9b696c6fd05b983cbfbb228/How%20to%20create%20OCI%20VM.md)
   
3. [How to deploy chatbot python code on OCI VM](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/cb05182b29a70524c9b696c6fd05b983cbfbb228/How_to_deploy_chatbot_in_OCI.md)

4. (Optional) If you want to setup your own DNS for accessing chatbot via LB, [Click here](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/089ca612f73b669ce55062534f17532b8bae0dab/Setup_Accessing%20_Chatbot%20_using_Public_DNS.md)for setup using OCI Services like Zone, Load Balancer, Oracle VM, Instance configuration etc.

5. (Oprional) Creating Web Applicaiton firewall with Rate limit, protection rules etc and attaching to LB. [Check this out](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/1390268247ba78ad807a7c253572351a7e9813a8/Configure_Firewall_for_LoadBalancer.md)
   
References -

https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm

https://github.com/langchain-ai/langchain/blob/master/README.md

https://python.langchain.com/v0.2/docs/integrations/llms/oci_generative_ai/

https://blogs.oracle.com/ai-and-datascience/post/developing-ai-apps-oci-generative-ai-langchain

https://streamlit.io/generative-ai

**hit below URL in browser to see how chatbot looks like or [checkout some sample screens here](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/8401e36d1715cf96ba08fa8ecc5c545fd279ff3b/TOGAF_Chatbot_screenshot_one_session.pdf) **


http:// public IP of OCI VM:8501 if setup is done using above #1, #2, #3
https:// domain name/ if #4 and #5 is also completed.


<img width="1126" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/df2a1291-f8b3-408c-a406-40b1e8117a2c">



<img width="1162" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/3fdd104b-f0fe-4dad-b432-0a91943a5a89">



<img width="1176" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/bfbac318-048f-4e05-9dc2-f2645628d0dd">



<img width="1148" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/55f9a8cc-9e9a-46da-a02a-d421dbc2062b">


when you access from .com URL - UI is bit updated
<img width="863" alt="image" src="https://github.com/user-attachments/assets/fc3efd06-3080-46bd-98dc-bfeef89d6419">











