"""
-------------
Validation helpers for user inputs.

Responsibilities:
- Validate username and password rules
- Return consistent format: (is_valid: bool, message: str)

Design:
- Services use validators to keep business logic clean.
- Validators do NOT do printing or input().
"""

# Returns (True, "") if valid, otherwise (False, "reason")
def username_validation(username):
    if not username or len(username.strip()) < 3 :
        return False, 'Username too short'
    return True, ""

# Returns (True, "") if valid, otherwise (False, "reason")
def password_validation(password):
    if not password or len(password) < 4:
        return False, 'Password should be more than 4 characters'
    return True, ""

