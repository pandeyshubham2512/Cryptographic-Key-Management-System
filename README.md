# Cryptographic Key Management System

This project is a secure Python-based Cryptographic Key Management System (KMS) that allows for the generation, storage, rotation, retrieval, and deletion of cryptographic keys. It is intended for educational and demonstration purposes.

## Features
- Secure key generation (symmetric and asymmetric)
- Secure key storage (in-memory for demo; extendable to file or database)
- Key retrieval by ID
- Key rotation
- Key deletion
- Simple command-line interface

## Requirements
- Python 3.8+
- cryptography

## Usage
1. Install dependencies:
   ```powershell
   pip install cryptography
   ```
2. Run the main script:
   ```powershell
   python main.py
   ```

## Security Notice
This project is for demonstration and educational purposes only. For production use, integrate with a hardware security module (HSM) or a cloud KMS, and follow all relevant security best practices.
