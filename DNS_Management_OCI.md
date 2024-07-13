This document will cover details about setup chatbot to access using DNS name.

1.)  Setup your zone in OCI.
Under Neworking ->DNS Management -> Zone
Click create zone. 
Zone Type : Primary
Zone name : name of your domain which you own.
Zone will be created with 2 default record types - NA & SOA.
<img width="1122" alt="image" src="https://github.com/user-attachments/assets/4b2fde61-c205-4884-aa09-e9c9222789d9">

<img width="1299" alt="image" src="https://github.com/user-attachments/assets/6f8c2cc7-d496-40ca-98fd-91f4df95d3b3">

 First CNAME record for verification of domain from Godaddy when I registered OCI NameServer ( NS record type). This you can add later after zone is created.
 second A type record is for OCI LoadBalancer's public IP
 Third NS record is created by default. I registred these Nameservers with Godaddy because my domain is regsitrered at Godaddy.

 When I add these NS records with Godaddy they show gave CName record to add in zone which is first CNAME record.
 If you domain is also also with Godaddy , refer below to see how it looks like.

 <img width="1352" alt="image" src="https://github.com/user-attachments/assets/ff4867e1-3b1f-4f70-bbec-0ef3a2c78f78">

 
 
 




