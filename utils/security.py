"""

-----------
Security helpers.

Responsibilities:
- Hash password (one-way)
- Verify password by hashing input again and comparing hashes

Important:
- Hashing is NOT encryption (no decrypt).
- We never store plain passwords in the file.
"""

import hashlib
# Convert password string to a SHA-256 hash for safe storage.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Verify entered password by hashing it and comparing to stored hash.
def verify_password(plain_password, stored_hash):
    return hash_password(plain_password) == stored_hash

