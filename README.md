# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
Ellen Ko

## Lab Question Answers
Question 1: Why are RESTful APIs scalable?
REST optimizes client-server interaction through statelessness, which removes the server load because past client request information does not have to be retained by the server. It also was well-managed caching, which partially or completely eliminates some client-server interactions. 

Question 2: According to the definition of “resources” provided in the AWS article above,what are the resources the mail server is providing to clients?
Resources are the information that different applications provide to their clients. The mail server provides the clients their email that they have sent and received. 

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
It does not use put, a method which updates existing resources on the server. A possible way we could extend the mail server to use this method is to allow password changes, which would update the server with the new password information. 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!
It allows for the blocking of anonymous traffic. It can also allow for the control the number of calls made to the API, the identification of usage patterns in the API’s traffic, and the filtration of logs by API key. 
Source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key


...
