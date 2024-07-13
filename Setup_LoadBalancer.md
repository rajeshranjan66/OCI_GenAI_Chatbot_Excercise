Lets create load balancer. This load balancer will be listening traffice from internet (0.0.0.0/0) on SSL port 643.
After creating LB, will create NSG to allow port 643.
Go to Networking -->Load Balancers -->Load Balancer, click Create Load Balancer and follow screen

<img width="1260" alt="image" src="https://github.com/user-attachments/assets/a511f492-af6e-436e-bb1f-787d2803cc72">


select VCN and public subet

<img width="1232" alt="image" src="https://github.com/user-attachments/assets/a334faf6-1796-4fa9-a80a-ce0c98665573">


select NSG created earlier, I will share screen shots after LB is done.

<img width="1145" alt="image" src="https://github.com/user-attachments/assets/36100d72-906b-4220-b437-ca84da12b38b">

add Oracle VM as backend on which chatbot running on port 8501. Currently VM also in same public subnet.

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











