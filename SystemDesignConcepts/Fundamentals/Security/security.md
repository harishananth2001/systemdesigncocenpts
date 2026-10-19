Security — Protecting the application
What is security?
Security protects your application and its data against unauthorized access, misuse, and attacks.

In the hospital application, only authorized administrators should be able to view or manage patient records.

Two fundamental concepts are authentication and authorization.

Authentication — Who are you?

The user logs in. Django verifies the credentials or validates an existing session or token.


Authorization — What can you do?

Django checks whether that user has permission to view, add, edit, or delete records.

<!-- check image and python code -->

This example restricts the endpoint to authenticated users who satisfy DRF's IsAdminUser permission, which ordinarily checks Django's is_staff flag. If your project needs a specific admin role, define and enforce that role explicitly.
Important security rules
- Never store plaintext passwords. Use Django's password hashing facilities.
- Validate incoming data on the backend.
- Enforce permissions on every protected endpoint.
- Use HTTPS in production.
- Configure CSRF protection when using cookie-based authentication.
- Keep secrets out of Angular code and public repositories.
- Use the Django ORM or parameterized SQL to help prevent SQL injection.
- Avoid logging sensitive patient data or credentials.
Real-time example: Hiding the Delete button in Angular is not enough. A user might send a direct DELETE request. Django must reject that request unless the user is authorized.

Interview question: What is the difference between 401 and 403?

401 indicates that valid authentication is missing or has failed. 403 means the request is understood but access is not permitted.