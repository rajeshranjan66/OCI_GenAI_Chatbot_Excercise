L
Lets start witrh creating load balancer. This load balancer will be listening traffice from internet (0.0.0.0/0) on SSL port 643.
After creating LB, will create NSG to allow port 643.
Go to Networking -->Load Balancers -->Load Balancer, click Create Load Balancer and follow screen

<img width="1260" alt="image" src="https://github.com/user-attachments/assets/a511f492-af6e-436e-bb1f-787d2803cc72">


select VCN and public subet

<img width="1232" alt="image" src="https://github.com/user-attachments/assets/a334faf6-1796-4fa9-a80a-ce0c98665573">


select NSG created earlier, I will share screen shots after LB is done.

<img width="1145" alt="image" src="https://github.com/user-attachments/assets/36100d72-906b-4220-b437-ca84da12b38b">

create backend set in which we will add Oracle VM as backend on which chatbot running on port 8501 later . Currently VM also in same public subnet.

<img width="1239" alt="image" src="https://github.com/user-attachments/assets/57380df5-dd11-4957-8b9e-f4bef34ea709">

<img width="982" alt="image" src="https://github.com/user-attachments/assets/34d2ee3f-c66c-4a21-aa17-310a53071e48">

Configure Listner with SSL. You need to add 3 files - 1.) Your crt file 2.) Root CA cert file 3.) Your private key

<img width="1238" alt="image" src="https://github.com/user-attachments/assets/8fdc29fa-0aee-4ae2-9050-3b4f95d7be4b">

<img width="1186" alt="image" src="https://github.com/user-attachments/assets/9c196e72-bf7f-4621-8666-cbf5d41e5a1c">


<img width="1272" alt="image" src="https://github.com/user-attachments/assets/47401f6c-10de-4c18-a81a-61dcc195e69b">

<img width="1237" alt="image" src="https://github.com/user-attachments/assets/345d90ef-b0e7-40da-a347-03d0fd0d282f">

for NSG , go to Networking -> Virtual Cloud Network -> Click VCN-> select Network Security Group
and create NSG called "ForLB" and add security rules as per below -

<img width="1314" alt="image" src="https://github.com/user-attachments/assets/c2bb0934-738c-46b7-8317-c2bf8b5421d1">


**Now we will create Instance configuration and Instance pool in public subnet to add instance pool in LB.**

<img width="1251" alt="image" src="https://github.com/user-attachments/assets/0696b453-c6f6-4503-b5b3-00ef1b919785">

<img width="1053" alt="image" src="https://github.com/user-attachments/assets/cc10ca25-73e3-4fae-a8b7-007d7888730c">

<img width="918" alt="image" src="https://github.com/user-attachments/assets/7e56fae4-3d6f-408e-9ca3-50ae7a154077">


Download public and private keys to connect to Oracle Instance late -
<img width="1140" alt="image" src="https://github.com/user-attachments/assets/444f1e51-22d4-4955-aabc-fb7df7e498a2">

Creating Instance Pool using instance configuration created above -
Click Compute -> select Instance Pools
Select Instance config created above -

<img width="1259" alt="image" src="https://github.com/user-attachments/assets/232c8b40-45f8-446a-b600-313d441b4280">


<img width="1260" alt="image" src="https://github.com/user-attachments/assets/640d4f04-2678-4a3a-a30c-6fa867e527d5">

Once isntance pool is created  
Oracle VM will also be created, Deploy python code following [this document](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/4a648d14c386c1001b5f11fc0ed2ccd7f9d2fcaa/How_to_deploy_chatbot_in_OCI.md)
Attach instance and LB to instance pool

<img width="1263" alt="image" src="https://github.com/user-attachments/assets/e256562a-f0e6-4db7-93f1-49e282951046">

<img width="1248" alt="image" src="https://github.com/user-attachments/assets/81c96fe4-74c1-4992-821f-39f9f042a6b8">


Attach Instance :
<img width="1253" alt="image" src="https://github.com/user-attachments/assets/e104b44e-62a6-496f-8b82-0217a1efc811">

Attach LB :
<img width="1277" alt="image" src="https://github.com/user-attachments/assets/01d4b1e3-860f-4750-8142-d4c1fc19c23a">

<img width="1244" alt="image" src="https://github.com/user-attachments/assets/6ba59f3e-bfeb-4eef-91c7-b804e3b3a34a">

But if you see health check is failing. This is because default port for health check in LB is 80. and there is nothing running at 80 in VM.
so update health check port in LB to 8501.

<img width="1239" alt="image" src="https://github.com/user-attachments/assets/620b52a5-7284-492b-9f2d-c4274423767f">
Add Backend in Backend set in LB - IP addreess is private IP of instance created during instance pool.

<img width="1284" alt="image" src="https://github.com/user-attachments/assets/a9f8cf22-0515-4fa9-893b-c406c815e7a7">

<img width="1283" alt="image" src="https://github.com/user-attachments/assets/9a6b5a86-5a68-4c16-b052-26f917af7cf0">

Ignore 80 in below, seems UI not getting updated, Health check is also using 8501.

<img width="1315" alt="image" src="https://github.com/user-attachments/assets/c99f8fdd-a529-4884-b648-e8b3ba9309b7">


Now below is how LB looks like -

<img width="1308" alt="image" src="https://github.com/user-attachments/assets/7fafe120-c51b-4875-9ead-96d85da98e9c">


<img width="1250" alt="image" src="https://github.com/user-attachments/assets/9ff5ae53-66b4-4415-9bb1-444b57e85655">

Once this done, add public IP of the LB in Zone created. [Refer this](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/456c829cc18d23e6a57f031c72787c1d4722100c/DNS_Management_OCI.md)

Below is how security list looks like. 
all traffic in security list is allowed only from public subnet CIDR.

<img width="1277" alt="image" src="https://github.com/user-attachments/assets/1e791366-2430-497a-a89b-0f591a5a9be4">

create another NSG named  "ForVM". Associate "forVM" NSG to VM where chatbot is running. This NSG "ForVM" will allow traffic to VM on port 8051 and 80 from NSG  "ForVM" of load balancer.

<img width="1309" alt="image" src="https://github.com/user-attachments/assets/47f22876-1225-4e37-9457-c803f7d245d7">

Now you can hit your domain or DNS -

<img width="1347" alt="image" src="https://github.com/user-attachments/assets/c18921a8-6ed9-4aea-b7fd-1371889c2858">






































