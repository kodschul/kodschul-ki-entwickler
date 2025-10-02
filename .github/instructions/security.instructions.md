---
applyTo: "**"
---

description: "Guidelines for generating secure Python code."
Security Guidelines for Python Code Generation:

- Always use camelCase for variable and function names.
- All functions should start with func\_.
- Validate all user inputs and sanitize data before processing.
- Avoid using eval(), exec(), or other dynamic code execution functions.
- Use parameterized queries for all database operations to prevent SQL injection.
- Never hardcode sensitive information (such as passwords, API keys, or secrets) in the code.
- Use secure libraries and frameworks; keep dependencies up to date.
- Handle exceptions gracefully and avoid exposing sensitive information in error messages.
- Use proper access controls and authentication checks where applicable.
- Prefer cryptographically secure random number generators (e.g., secrets module) for sensitive operations.
- Document all security-relevant decisions and code sections.

OWASP Top Ten Guidelines for Secure Python Code Generation:

C1: Implement Access Control

- Enforce least privilege by restricting access to resources and functions based on user roles.
- Use proper authentication and authorization checks before sensitive operations.

C2: Use Cryptography to Protect Data

- Use strong, industry-standard cryptographic libraries (e.g., hashlib, cryptography, secrets).
- Encrypt sensitive data at rest and in transit.
- Never implement custom cryptographic algorithms.

C3: Validate all Input & Handle Exceptions

- Validate and sanitize all user inputs using allow-lists and strict data types.
- Handle exceptions gracefully, logging errors without exposing sensitive information.

C4: Address Security from the Start

- Integrate security requirements and threat modeling early in the development lifecycle.
- Regularly review code for security vulnerabilities.

C5: Secure By Default Configurations

- Disable unnecessary features and services.
- Use secure, minimal default configurations for all components.

C6: Keep your Components Secure

- Regularly update dependencies and libraries to patch known vulnerabilities.
- Use trusted sources for all third-party packages.

C7: Secure Digital Identities

- Store passwords securely using strong hashing algorithms (e.g., bcrypt, Argon2).
- Implement multi-factor authentication where possible.

C8: Leverage Browser Security Features

- Set secure HTTP headers (e.g., Content-Security-Policy, X-Frame-Options).
- Use HTTPS for all communications.

C9: Implement Security Logging and Monitoring

- Log security-relevant events (e.g., authentication attempts, access control failures).
- Monitor logs for suspicious activity and respond promptly.

C10: Stop Server Side Request Forgery

- Validate and restrict outbound requests to trusted destinations.
- Avoid accepting user-supplied URLs for server-side requests.
