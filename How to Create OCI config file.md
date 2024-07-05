Creating config file for calling OCI Gen APIs–

Create config file with the name of config under .oci directory under user directory (/Users/rajeshranjan/.oci).  While deploying chatbot on VM, you will need to copy complete .oci folder along with private key file and config file on VM.
Place your private key under. oci folder which will be used for local running of python code and connecting to OCI Gen AI services from laptop.


 



















Below is the content of config file and how to create it.

Line 1 - user=ocid1.user.oc1..aaaaaaaaxxxxxxxxxx   can get from “my Profile” then OCID  of user.

 


Line-2 fingerprint=fd:af:db:XXXXXXXXXXX
  This is API key available in your profile, as shown below. Copy from Fingerprint.

 


Line-3 tenancy=ocid1.tenancy.oc1..aaaaaaxxxxxxxxx get from “Tenancy” then OCID of tenant.

 


Line-4 region=us-chicago-1  For Gen AI OCI services, need to put this region only. 
Line-5 key_file=~/.oci/oci_api_key.pem  This private key file that you downloaded while creating VM
