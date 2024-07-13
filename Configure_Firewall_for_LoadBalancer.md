![image](https://github.com/user-attachments/assets/f3d90ec7-4455-4321-aa75-2f2296bd3aba)In this document  we will see how to add security controls to Load Balancer

Lets start with creating firewall.

Go to Identity & Security ->Web Application Firewall -> Policies and Follow screens as per below -

<img width="1318" alt="image" src="https://github.com/user-attachments/assets/9db63ddb-6391-41d1-b9ef-dfb4f6d1b49a">

<img width="1291" alt="image" src="https://github.com/user-attachments/assets/0259fdfb-7d95-4ef5-978b-1bcf514bf641">

<img width="1287" alt="image" src="https://github.com/user-attachments/assets/2cf82ecb-271b-4638-93ef-e5da4d538963">

<img width="1275" alt="image" src="https://github.com/user-attachments/assets/46e8dfbb-d9c4-4f33-a799-2971d9f38f29">
Select LB which was created earlier. [Refer here](https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/blob/f8c86304fa8074f6eade7f6405b13d68df2d6ab6/Setup_Accessing%20_Chatbot%20_using_Public_DNS.md)

<img width="1280" alt="image" src="https://github.com/user-attachments/assets/7fddf0a8-c54e-465c-b48c-1231789cca48">


<img width="1281" alt="image" src="https://github.com/user-attachments/assets/a243145d-3ec1-4afc-bae7-520e0154154b">

Review and create -

<img width="1298" alt="image" src="https://github.com/user-attachments/assets/fe9230a4-a0e7-4070-aeda-63fdda6d0617">

Enable Protection Rules to test Protection of the web application from some OWASP vulnerabilities like SQL script injection, cross-side scripting etc.

<img width="452" alt="image" src="https://github.com/user-attachments/assets/2ffe6e49-d052-41ad-8594-2a28d708ba7b">
Click in manage request protection -

<img width="452" alt="image" src="https://github.com/user-attachments/assets/1110e02d-d4bb-460c-bfae-fb9a49ed88bf">

Under Rule action, select what is the response returned if any of the rules get satisfied.

<img width="1131" alt="image" src="https://github.com/user-attachments/assets/2fd9b122-30fd-4a8b-8ad7-e82671c672ce">

Click on Add request protection rule and choose all 16 recommended capabilities and click "Choose protection capabilities" -

<img width="1169" alt="image" src="https://github.com/user-attachments/assets/ea1d5840-acd2-4598-855c-5de85e6aded7">

<img width="1199" alt="image" src="https://github.com/user-attachments/assets/8e05da06-2d13-46c7-bb42-2d061f5a2cf2">

<img width="1218" alt="image" src="https://github.com/user-attachments/assets/7e6bdb0d-5c47-4b2a-a87a-539042f82270">

<img width="1199" alt="image" src="https://github.com/user-attachments/assets/09bf9df6-7479-4b69-ba86-1b0415fd5ec4">


<img width="1084" alt="image" src="https://github.com/user-attachments/assets/c541b45d-54dc-483c-97e7-453e7b55ddc8">

Your Protection section under policy will looks like this 

<img width="1214" alt="image" src="https://github.com/user-attachments/assets/06fb474d-71a0-40a0-8640-0e452a82ca87">

Now Let's set rate limit -
















