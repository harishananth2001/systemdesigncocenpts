<!-- explanation and understating for database -->
Databases — Where application data lives
What is a database?
A database stores and manages information. Instead of keeping patient records in temporary variables, your application saves them so they can be retrieved later.

For this project, we use PostgreSQL, a relational database.
Visual database example
patients table
id	name	age
1	Harish	25
2	Aishwarya	28


doctors table
id	name	department
10	Dr. Kumar	Dental
11	Dr. Priya	General


appointments table
id	patient_id	doctor_id
101	1	10
102	2	11

The appointment table links patients and doctors using foreign keys.

<!-- check the image and understart the flowchart 
database relationship flowchart-->

select_related() can retrieve related foreign-key records efficiently in the same SQL query rather than fetching them separately for each appointment.
Important database concepts
- Primary key: Uniquely identifies a record.
- Foreign key: Establishes a relationship between records.
- Index: Helps locate matching records efficiently.
- Transaction: Groups database operations into a unit of work.
- Constraint: Enforces rules, such as unique email addresses.
Real-time example: Avoid double booking
Suppose two admins try to book the same doctor for the same time. Your application needs to validate availability and protect the booking operation against concurrent requests. Transactions and suitable database constraints can help enforce these rules.

A simple availability check alone is not enough because two requests can pass the check simultaneously.

Interview question: Why do we need database indexes?

Indexes can speed up searches and joins on frequently queried fields. However, indexes consume storage and add overhead to inserts, updates, and deletes, so choose them based on actual query patterns.