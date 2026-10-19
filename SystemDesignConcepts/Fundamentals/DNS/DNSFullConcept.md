DNS (Domain Name System) — Complete Explanation
DNS is an important topic in System Design Fundamentals. I’ll explain each topic in simple English, with real-world examples, flowcharts, commands, and Angular + Django examples.
1. What is DNS?
DNS stands for Domain Name System. It converts a human-readable domain name into an IP address so your computer can find the correct server.

<!-- check image  -->

Imagine you want to call your friend. You remember their name, but your phone uses their number to make the call. DNS works similarly:
- You enter a domain name in the browser.
- DNS looks up the IP address associated with that name.
- Your browser connects to the server using that address.
- The server sends back the website or API response.
Important: DNS does not itself load your website or retrieve your database records. It helps your device locate the server.


2. How DNS works — complete flowchart
Suppose you open a hospital application built with Angular and Django.

1. User / Angular application

Requests api.hospital.example

2. DNS cache check

Browser → operating system → recursive resolver

3. DNS lookup, if needed

Root server → .example TLD server → authoritative DNS server

4. IP address returned

Example: 203.0.113.10

5. HTTPS connection

Browser connects securely to the server

6. Django API → PostgreSQL

The API processes the request and returns JSON

This is a simplified flow: cached DNS answers can skip the root, TLD, and authoritative lookups. Also, DNS resolution and the HTTPS connection are separate operations.

3. The four main components inside DNS
These components work together to find the correct IP address.

1. DNS client

Your computer, phone, or application starts the lookup when it needs to resolve a domain name. The operating system often provides the local DNS client.

Example: You open https://api.hospital.example.

<!-- DNS clint Image -->

2. Recursive DNS resolver

The resolver looks for a cached answer. If it doesn't have one, it finds the answer by querying other DNS servers.

Example: Your network may use a resolver provided by your ISP or a public DNS service.
<!--  Recursive DNS resolver Image -->

3. Root and TLD DNS servers
- Root servers direct the resolver toward the correct top-level domain servers.
- TLD servers handle extensions such as .com, .org, or .in and direct the resolver to the relevant authoritative name servers.
Example: For example.com, the .com TLD server points the resolver toward the domain's authoritative DNS servers.
<!-- Root and TLD DNS servers image -->

4. Authoritative DNS server

This server provides the DNS records for a domain from its configured DNS zone.

Example: It returns the A record for api.example.com, if one is configured.
<!-- Authoritative DNS server image -->

Recursive versus iterative lookup
- Recursive query: The client asks a resolver to obtain the final answer or an error.
- Iterative query: A DNS server can respond with a referral telling the requester which server to ask next.
The usual pattern is that your device sends a recursive query to its resolver, while the resolver follows referrals through the DNS hierarchy


4. Common DNS records — each explained
DNS records are instructions stored in a domain's DNS zone. Different record types serve different purposes.

A

A record — IPv4 address

Maps a hostname to an IPv4 address.

Example: api.example.com → 203.0.113.10

Used when clients need an IPv4 address for a server.



AAAA

AAAA record — IPv6 address

Maps a hostname to an IPv6 address.

Example: api.example.com → 2001:db8::10

IPv6 provides a much larger address space than IPv4.



CNAME

CNAME — alias

Makes one hostname an alias of another hostname.

Example: www.example.com → example.com

The resolver follows the alias to find the final address. A CNAME cannot normally coexist with other ordinary records at the same owner name.



MX

MX — mail exchange

Identifies the mail servers responsible for receiving email for a domain.

Example: example.com → mail.example.com

MX records include a priority value; lower values are preferred when multiple servers are available.



TXT

TXT — text data

Stores text used for domain verification and email security policies.

Examples include Google domain verification, SPF and some DKIM-related DNS data.

TXT records don't directly route web traffic to a server.


Quick memory trick
Record	Remember it as
A	IPv4 address
AAAA	IPv6 address
CNAME	Another hostname
MX	Mail server
TXT	Text, verification, policies


DNS caching and TTL
DNS caching saves previous lookup results so the resolver does not have to repeat the full lookup every time.

TTL means Time to Live. It tells a DNS cache how long an answer may be retained before it needs to be refreshed.




First request

Resolver queries DNS servers and obtains an IP address.

Answer cached — TTL 300 seconds

The answer may be reused for up to 5 minutes.

Within TTL

Reuse the cached answer if it is still valid.


After TTL expires

The resolver may query DNS again.



300 is the TTL in seconds.

Why caching matters:
- Improves lookup speed.
- Reduces repeated DNS queries.
- Reduces load on DNS infrastructure.
- Means DNS changes may not be visible everywhere immediately because caches can retain previous answers until expiry.
Changing a TTL does not instantly clear all existing cached records.



6. DNS lookup using real commands
You can practise DNS from your MacBook Terminal or Linux terminal.
A. Using nslookup
nslookup example.com


This displays information such as the DNS server used and the resolved IP address.

To check a particular record:
nslookup -type=A example.com
nslookup -type=AAAA example.com
nslookup -type=MX example.com
nslookup -type=TXT example.com


B. Using dig
dig is useful for debugging DNS because it shows the question, answer, TTL, and response details.
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com TXT


To see a shorter answer:
dig +short example.com


To inspect the DNS delegation path:
dig +trace example.com


The trace can show referrals from root servers through the TLD to authoritative DNS servers.

Note: these commands query a real domain. The IP addresses and results can change over time.


7.How DNS connects Angular, Django and PostgreSQL
Imagine you deploy your hospital appointment application:
- Angular frontend: app.hospital.example
- Django REST API: api.hospital.example
- PostgreSQL database: private database endpoint
Angular frontend

https://app.hospital.example

DNS resolves the API hostname

api.hospital.example → API server address

HTTPS → Django REST Framework

Receives GET /api/doctors/

PostgreSQL

Django queries the database privately

JSON response → Angular

The browser displays the doctors list.


8. DNS security: DNSSEC, DoH and DoT
DNS is essential, but ordinary DNS queries do not automatically provide every type of security.

DNSSEC — DNS Security Extensions

Uses digital signatures to help validate that DNS data came through an authenticated chain and was not modified undetectably.

It protects DNS data integrity and authenticity, but does not encrypt DNS queries.




DoH — DNS over HTTPS

Sends DNS queries inside HTTPS connections. This helps protect queries from being read or modified by someone observing the network path, although the resolver can still see them.




DoT — DNS over TLS

Protects DNS traffic between the client and resolver using TLS encryption. It is another option for protecting DNS queries in transit.



Common DNS problems
Problem	Meaning	What to check
NXDOMAIN	The queried name does not exist according to the responding DNS server.	Hostname spelling and DNS records
SERVFAIL	The resolver could not complete the lookup.	DNS configuration, delegation and DNSSEC validation
REFUSED	The server refused the query.	Resolver policy and permissions
Stale IP address	A cache may still hold an older answer.	TTL and authoritative records
DNS_PROBE_FINISHED_NXDOMAIN	Browser could not resolve the hostname.	Domain spelling, DNS settings and network
DNS errors and HTTP errors are different. For example, a 404 Not Found usually means the server was reached but the requested HTTP resource was not found. DNS resolution generally happens before the browser can make that HTTP request.

Final output 
Domain name → DNS resolver → DNS records → IP address → HTTPS connection → Django API → Database → JSON response.
