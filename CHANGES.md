# CHANGES.md

## Overview

This document outlines the key issues identified in the legacy user management API and the improvements made during refactoring. The aim was to enhance **code quality, security, maintainability, and structure**, without adding new features or changing the core functionality.

---

## Major Issues Identified

### 1. **Poor Code Structure**
- All logic was crammed into `app.py`.
- No separation of concerns between routing, business logic, and database operations.

### 2. **Security Risks**
- Plaintext password handling.
- No input sanitization or validation.
- SQL injection risks due to string interpolation in queries.

### 3. **Lack of Error Handling**
- Minimal or no try–except blocks.
- Inconsistent use of HTTP status codes.

### 4. **No Reusability or Modularity**
- Repeated code blocks for database access.
- Hard-to-read and hard-to-maintain monolithic functions.

### 5. **No Logging or Monitoring**
- Debugging was difficult due to lack of logs.

---

## Refactoring Changes Made

### 1. Project Restructure
Split the monolith into a modular structure:

```
.
├── app.py
├── db/
│   └── connection.py
├── models/
│   └── user_model.py
├── services/
│   └── user_services.py
├── routes/
│   └── users.py
├── utils/
│   └── validators.py
├── init_db.py
├── requirements.txt
└── CHANGES.md
```

### 2. Security Improvements
- Added password hashing using `werkzeug.security`.
- Moved SQL logic to parameterized queries to prevent injection attacks.
- Introduced input validation utilities for user data.

### 3. Maintainable Code & Best Practices
- All DB operations centralized in `db.py`.
- Business logic moved to `user_service.py`.
- Created `User` model using Python’s `dataclass`.

### 4. Robust Error Handling
- Wrapped all endpoints with error-safe responses.
- Consistent use of HTTP status codes (`200`, `201`, `400`, `404`, `500`).

### 5. Future Testability
- All business logic is now testable independently of routes.
- Clear separation enables unit and integration testing.

---

## Trade-offs / Assumptions

- Did not introduce full JWT-based authentication to avoid over-engineering.
- Password hashing added, but login still returns raw user data for backward compatibility (should be avoided in production).
- No ORM used to stay close to the original SQLite logic and meet time constraints.

---

## AI Usage Disclosure

### Tools Used

- **ChatGPT-4** – For architectural restructuring, validation logic, and modular Flask patterns.
- **GitHub Copilot** – For fast generation of route handlers, decorators, and Flask boilerplate.
- **Claude** – Reviewed documentation clarity and offered refactoring suggestions.
  
- **Official Flask & OWASP Docs** – For secure API design and RESTful practices.
- **Human Review**: All AI-generated content was reviewed and adapted as per best practices.

---

## With More Time, I Would:
- Implement full JWT-based authentication and role-based access control.
- Replace raw SQL with SQLAlchemy ORM.
- Write unit and integration tests using `pytest`.
- Add `.env`-based config management.
- Use Flask Blueprints for full scalability and Swagger/OpenAPI for documentation.
