Latency — How long a request takes
Latency means delay. In system design, you should specify what delay you mean: network latency, server processing time, or the total time from a user's request to the completed response.

Suppose an admin clicks “View Appointments.” The table appears after 800 milliseconds. The user experiences that as a delay.

<!-- check image -->

Latency vs throughput
- Latency: How long one operation takes.
- Throughput: How many operations a system completes per unit of time.
A system might handle 1,000 requests per second but still have slow individual requests under load. These are different performance measurements.
How to reduce latency
1. Add appropriate database indexes.
2. Avoid fetching unnecessary columns or records.
3. Use pagination for large tables.
4. Fix N+1 database query problems in Django.
5. Cache data that can safely be reused.
6. Use a CDN for static frontend assets.
7. Keep backend and database communication efficient.
8. Measure p95 and p99 response times, not just averages.
For example, if the admin needs 20 appointments per page, retrieve 20 records instead of thousands

<!-- code  start -->
Appointment.objects.order_by("-id")[:20]
<!-- code end -->


This limits the result set to 20 records. For a production application, use proper pagination and a suitable indexed ordering field.

Interview question: How would you investigate a slow API?

Measure the request duration, inspect server logs and traces, check database query times, identify unnecessary queries, inspect payload sizes, and profile the bottleneck before optimizing it.