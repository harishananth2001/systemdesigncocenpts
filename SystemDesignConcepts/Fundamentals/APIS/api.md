// API explain understanding
1. APIs — How applications communicate
What is an API?
API means Application Programming Interface. It defines how one application requests data or services from another application.

Think about ordering food in a restaurant:
- You are the customer.
- The waiter takes your order.
- The kitchen prepares the food.
- The waiter brings the result back to you.
In a web application:
- Angular = customer
- Django REST API = waiter
- PostgreSQL = storage used by the kitchen
- JSON response = result returned to Angular
Real-time example: View hospital patients
An admin clicks View Patients in Angular. Angular sends a request to Django. Django fetches patients from PostgreSQL and returns their details

<!-- go to the image. then understant the flows then check the python and angular code -->


Configure Angular's HttpClient with provideHttpClient() and set the API base URL or development proxy for your environment.
How does it work?
1. Angular sends an HTTP GET request.
2. Django receives the request.
3. Django checks the admin's permissions.
4. Django ORM queries PostgreSQL.
5. Django serializes the records to JSON.
6. Angular receives the response and displays the data.
API methods
Method	Real-time example
GET	View patients
POST	Register a patient
PUT	Replace patient details
PATCH	Update a patient's phone number
DELETE	Delete a patient, if permitted
Interview question: What happens when an API returns 404?

The requested resource or endpoint could not be found. Check the URL, routing configuration, and whether the requested record exists.