Latency
How long does a request take? Learn latency with a real-time Angular + Django + PostgreSQL example, a flowchart, code, and interview questions.
1. What is latency?
Latency is the time taken for a request to travel from the client to the server, get processed, and return a response.

In simple English, latency is the delay between clicking a button and receiving the result.

Real-life example: You open your CRM application and click View Customers.
- You click the button in Angular.
- Angular sends an HTTP request to Django.
- Django fetches customer information from PostgreSQL.
- Django returns the data.
- Angular displays the customers.
The time taken for this entire process is the request's round-trip time, although engineers sometimes measure latency at individual stages too.


2.Flowchart — How latency works
1. User clicks “View Customers”

Angular frontend

2. HTTP request sent

Network → Django REST API

3. Django queries PostgreSQL

SQL query + database processing

4. Response returns to Angular

Network → JSON response

5. Customer list is displayed

Angular renders the data


Total request time = network delays + server processing + database work + other overhead



3. Real-time example with latency calculation
Imagine your CRM application returns customer data in the following example timings.
Processing step	Example time
Request travels to server	50 ms
Django processes request	30 ms
PostgreSQL query executes	80 ms
Response travels back	40 ms
Total	200 ms
Here, ms means milliseconds. 1,000 ms = 1 second.
\[
50 + 30 + 80 + 40 = 200\text{ ms}
\]

The user receives the response in approximately 0.2 seconds, excluding any additional browser rendering time.

These are illustrative values, not guaranteed timings. In a real application, database time may already be included in server processing time, so avoid counting it twice.


4. Code example — Measure latency in Angular + Django
A. Django REST API — Measure server processing time
In this example, Django fetches customers from PostgreSQL and reports how long the server-side operation took.
<!-- check py code  -->

Customer is assumed to be your Django model with id, name, and email fields. Configure the URL for this view in your application's urls.py.

How it works:
1. time.perf_counter() records a high-resolution start time.
2. Django queries PostgreSQL for up to 100 customers.
3. The second timer reading measures the elapsed time.
4. Django returns customer data and the measured duration as JSON.
Note: This measures the code section around the query, including Python work and database access. It does not measure the complete network round trip. AllowAny is for demonstration only; use your actual authentication and permission classes in production



B. Angular — Measure the complete API request duration
<!-- check ts code  -->


Make sure HttpClient is configured in your Angular application and Django CORS settings allow your frontend origin.

What is the difference between these two measurements?
- server_processing_ms: time spent in the measured Django code section.
- performance.now() - start: time from starting the browser request until the response arrives and the callback runs. This includes network delays, server processing and other overhead, but not necessarily the time needed to render the entire page.




5. Types of latency
Type |	Meaning |	Example
Network latency	|Time for data to travel across the network	| Angular request travelling to Django
Application latency |	Time spent processing application logic |	Django validating customer data
Database latency | Time spent executing database operations	| PostgreSQL running a query
DNS latency | 	Time taken to resolve a domain name	|Resolving api.example.com
TLS handshake latency | 	Time involved in establishing a secure connection |	Initial HTTPS connection setup



These can overlap or be measured at different levels. For example, database latency is often part of application latency.

6. How can you reduce latency?

1. Optimize database queries
Use appropriate indexes, avoid unnecessary queries, and retrieve only the columns and rows you need.
<!-- check image -->


2. Use caching
Cache frequently requested data with Redis or another suitable cache instead of querying PostgreSQL every time.
<!-- check image -->


3. Use a CDN
Serve static files such as images, CSS and JavaScript from locations closer to users.
<!-- check image -->

4. Monitor API performance
Track response times, slow SQL queries, error rates and percentiles such as p95 latency.
<!-- check image -->


Key takeaway
Low latency = faster responses = better user experience.

For your Angular + Django + PostgreSQL applications, measure both the complete API request duration in Angular and the server-side processing duration in Django. This helps you identify whether the main delay is in the network, backend logic, or database.
