**Below are the steps for deploying chatbot on oracle VM. This will incur cost for using Oracle VM and hiting Oracle Gen AI services**

Assumption - you have OCI account and Oracle VM and ownload private keys to connect to VM in your account. All the commands shown on screenshot is also avaialble in file https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/master/Oci_GenAI_Python/Command%20execution%20output

** This deployment will need VM and OCI accuunt and Private key of VM from OCI account which is used to connect to VM. You may refer to below 

[**How to Create OCI config file.md**](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/b1622dc56886eeadeb24277e8906fefc68445a86/How%20to%20Create%20OCI%20config%20file.md)

[**How to create OCI VM.md**](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/b1622dc56886eeadeb24277e8906fefc68445a86/How%20to%20create%20OCI%20VM.md)

 Below Public and private keys will be downloaded while creating VM.
<img width="670" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/c73f6bc2-3545-4678-ad1a-79688130b2fd">

** ssh into oracle VM **

<img width="768" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/d71493b3-d70c-4b00-ba6d-7e7884c1f450">

** create required folders where code python code files and other required files will be copied and uppgrade ubuntu packages**
 

<img width="781" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/26962c1a-520a-4ef5-b1b7-8fcbe363909e">

** install Python on VM **

<img width="490" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/7b51adaa-5bf6-4c47-9d27-93536933a27b">

** install virtual environment **

<img width="1035" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/dcb57c3c-391e-4d88-8a53-7f50f302cfaf">
<img width="1141" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/c60da1b8-bf4e-4d45-96b9-8b98612f7d25">
<img width="807" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/2ed21017-fb85-4d03-a0f6-c9d9c7004bb3">

**Create virtual env and activate **
<img width="1075" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/dcd031c0-56e3-46ec-92a7-3565ed40b39b">

**copy python code for creating Choma DB and chatbot into oracle VM and TOGAF PDF on OCI VM, you will be executing this on laptop  **

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

install streamlit

<img width="1276" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/95425973-3327-4e24-8e88-4bbbcb0fc2a5">

install python-multipart

<img width="809" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/b34b8d2a-9530-45fe-a4ed-6b1534931490">

install pydantic

<img width="920" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/812949e1-6e6f-4a0f-90b2-cccffa549903">

install pypdf


<img width="861" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/0d111834-20e4-484c-ba66-abdf1e435ec6">


install langchain_community

<img width="1342" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/4ec60c73-55ff-444e-8d39-4db86b4545be">


** Setup firewall on OCI VM to open port, OCI VM to allow port 8501 in security list of subset in which VM is created **

<img width="895" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/69e7d487-df38-45c6-941c-0707ff7e642d">

** Copy your OCI configuration file from local machine to Oracle VM, this file will have info related to OCI account , will be used to call OCI Gen AI services from python **

<img width="1454" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/982c0f18-feec-428f-8110-aab3c9f60ecd">

**content of config file.**
(base) Rajeshs-MacBook-Pro:.oci rajeshranjan$ cat config
[DEFAULT]
user=ocid1.user.oc1..XXXXXXXXXXXX
fingerprint=fd:af:db:0XXXXXXXXXXXXXXXX
tenancy=ocid1.tenancy.oc1..XXXXXXXXX
region=us-chicago-1
key_file=~/.oci/oci_api_key.pem

** Below is how directory structure looks like  **

<img width="730" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/c337cbc4-b86f-411c-acd7-20d36378fc20">


** execute demo-chroma-create.py  **

<img width="1446" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/7d0ceadc-3686-4f5a-9f29-e011b961cd44">


** start chromaDB in backgroud and verify  **

<img width="989" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/303b54a9-df32-43a7-b817-8c8b3937bbec">


** execute chatbot python code usin streamlit  **

<img width="843" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/d570a150-3a7b-4621-9e70-e3ee87a26241">


**hit below URL in browser  - **
http://public IP of OCI VM:8501
I added some more PDFs related to TOGAF, executed demo-chroma-create.py , restarted chromaDB
I asked few question and also inputed mutil choice question and chatbot shows correct answer and PDF document with page number where it is getting context from to send to LLM. Few screenshots.
chat history of the session will also be passed to LLM along with original prompt.

<img width="1126" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/df2a1291-f8b3-408c-a406-40b1e8117a2c">



<img width="1162" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/3fdd104b-f0fe-4dad-b432-0a91943a5a89">


<img width="1176" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/bfbac318-048f-4e05-9dc2-f2645628d0dd">



<img width="1148" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/55f9a8cc-9e9a-46da-a02a-d421dbc2062b">






Monitoring, tracing and debugging  with Langsmith => You need to configure you API key of langsmith in chatbot python code.

** Tracing logs for simple question **

<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/327cbe31-c48f-42b8-a922-8d27b8e9cc70">


<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/e450e46b-16ee-4139-897e-ce848fe1a458">


<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/184efcfe-f25b-4cba-91f0-eb0caa155db3">

** Tracing logs for multiple choice question **

<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/81a5ffe3-9a15-44e7-a1cb-0f944805de21">


<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/e883ae14-abfa-47c5-ba54-0670321c9a40">


<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/174dd035-5ddf-49ed-83cc-a77c609adb25">














                                ************************ End of the file********************************************
