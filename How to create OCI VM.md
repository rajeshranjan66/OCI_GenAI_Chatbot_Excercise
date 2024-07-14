Create Oracle VM as per below in your OCI console under your compartment in US Medwest region as OCI GenAI services are available in this region.

If this region is not available in your OCI account , then you need raised limit increase request with oracle support so that they can provision this region also for you. I have used pay as you go payment method.

1.	Login into OCI console navigate to instance menu

   <img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/f6539914-53df-478b-954a-74bd1178a831">


2.	Click on Create Instance button. Give some meaningful name.

	<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/2a22a7e2-5908-4f2d-ad1a-a6dc1c588522">

3.	Under “Image and shape”, click on “Change Image” and select ubuntu and image name as “Canonical Ubuntu 22.04” and click “Select Image”

   <img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/482a7d43-d3d5-48f8-a7d0-b48df8c8a0c1">

<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/920208b7-c1ea-4db4-8597-0449a8d1646c">

4.	Click on “Change shape”, select shape series – AMD , shape name -VM.Standard.E4.Flex

	<img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/1d780a6f-7e65-4cb7-a4b1-ec97832eefde">

5.	Update number of  CPU as 2 and Memory to 64 GB and select shape

       <img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/3593ca75-ef72-49ab-8bd8-2fbde55fea22">

6.	Under “Add ssh key”, click “Save Private Key” and save on your laptop with name ubuntu-vm-priv.key

       <img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/2e22f0e8-e279-4c41-ad68-6d14ea650e63">

7.	Click on “Create” button to create VM

       <img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/39ab7e98-fac5-4fd2-9493-175a2946c001">

<img width="1282" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/ee04f39a-37c5-460c-b7ce-6e17433db98e">

   
8.    Just verify 8501 port is whitelisted in security list of the subnet.

      <img width="452" alt="image" src="https://github.com/rajeshranjan66/OCI_GenAI_Chatbot_Excercise/assets/78391124/bb83ce2e-b0c4-4328-af69-87bc5e7be671">

9. For security purposes, you can remove 22 and 8501 from 0.0.0.0/0 when you don't want to use chatbot so VM will not be accepting any traffic from internet

