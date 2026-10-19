<!-- explain and understarting for networking -->
Networking — How data travels between systems
What is networking?
Networking enables devices and servers to exchange data.

Your Angular application may run in the user's browser, Django may run on a cloud server, and PostgreSQL may run on a separate private server. Networking connects these components.
Real-time example
An admin opens the hospital dashboard from a laptop. The browser sends an HTTPS request to Django. Django communicates with PostgreSQL and returns the results.
<!-- go to image and understart that chart -->
Important terms
Term	| Meaning | Example
IP address	|Identifies a network interface |	192.168.1.10
Port |	Identifies a service endpoint |	HTTPS commonly uses 443
TCP |	Reliable, ordered byte stream	Commonly used by HTTPS
UDP	Datagram transport without TCP's built-in reliability	Some real-time media and DNS traffic
HTTP	Web request/response protocol	GET /api/patients/
HTTPS	HTTP protected with TLS	Secure API requests
Firewall	Filters network traffic	Restrict public database access
What happens when a request is sent?
1. The browser prepares the HTTP request.
2. The network stack sends it to the destination.
3. Routers forward packets across the network.
4. The server receives and processes the request.
5. The response travels back to the browser.
This is a simplified explanation; connection establishment, encryption, caching, and network routing add more details.
Practical security rule
Do not expose PostgreSQL directly to the public internet for an ordinary web application. Let Django connect to PostgreSQL through an appropriately restricted network and authenticated database connection.

Interview question: What is the difference between HTTP and HTTPS?

HTTPS uses TLS to protect HTTP communication and authenticate the server. HTTP alone does not provide that transport encryption.