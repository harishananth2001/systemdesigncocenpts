DNS — How a browser finds your server
What is DNS?
DNS stands for Domain Name System. It helps translate a domain name into DNS records that tell the browser or network client where and how to find a service.

For example, people remember hospital.example.com more easily than an IP address.

<!-- go and check the image must understant the flowchart  -->

What happens in practice?
Suppose your domain resolves to a server address. The browser uses that DNS answer to find where to connect. It then establishes the appropriate network connection and sends an HTTP request.

DNS records you should know:
Record	Purpose
A	Maps a name to an IPv4 address
AAAA	Maps a name to an IPv6 address
CNAME	Aliases one DNS name to another
MX	Specifies mail servers
TXT	Stores text used for verification and other purposes



DNS answers may be cached, and a domain can point to a load balancer or CDN rather than directly to the application server.

Important: DNS does not return your patient data. It helps your browser locate the service.

Interview question: What happens when you type a website address into your browser?

At a high level: the browser interprets the URL, obtains or reuses DNS information, connects to the destination, negotiates TLS for HTTPS, sends the HTTP request, and processes the response. Caches and connection reuse can skip some steps.