Encryption — Protecting sensitive information
What is encryption?
Encryption transforms readable data, called plaintext, into ciphertext using a cryptographic algorithm and key. The appropriate decryption key allows the original data to be recovered.

For your hospital system, you need to protect sensitive information such as login credentials and patient records.
Real-time example: HTTPS
When an admin signs in, the browser sends the login request over HTTPS. TLS protects the request while it travels across the network.
<!-- check the image and understart the flowchart -->


Types of data protection
Encryption in transit

Protects information as it travels between the browser and server.

Example: HTTPS using TLS.



Encryption at rest

Protects stored data or storage media.

Example: Database or disk encryption, with appropriate key management.



Password hashing

Stores a one-way password verifier instead of the original password.

Example: Django's configured password hashers.

Important: Encryption vs hashing
Feature	Encryption	Hashing
Purpose |	Confidentiality	|One-way verification or integrity checks
Reversible? |	Yes, with the appropriate key	|Designed to be one-way
Example	| TLS traffic encryption	| Password hashing
Original password recoverable?	| Not applicable to normal password storage	| No, the hash is verified rather than decrypted
For password storage, use a suitable password-hashing algorithm rather than ordinary SHA-256 or reversible encryption.

Interview question: Does HTTPS make the entire application secure?

No. HTTPS protects data in transit, but you still need secure authentication, authorization, input validation, safe storage, and correct server configuration.