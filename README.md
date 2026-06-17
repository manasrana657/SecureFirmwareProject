# Secure Firmware Update Mechanism for IoT Devices

## Project Overview
This project implements a Secure Firmware Update Framework for IoT Devices.

Features:
- Secure Boot Simulation
- RSA Digital Signature Verification
- SHA-256 Integrity Verification
- Rollback Protection
- Secure Firmware Update Server
- Audit Logging
- Web Dashboard
- Firmware Recovery Testing
- NIST IoT Security Compliance Mapping

## Project Structure

bootloader/      -> Secure boot simulation
crypto/          -> RSA signing & verification
device/          -> Device-side verification
dashboard/       -> Web dashboard
server/          -> Firmware update server
docs/            -> Documentation
firmware/        -> Sample firmware files

## Technologies Used

- Python
- Flask
- OpenSSL
- SQLite
- SHA-256
- RSA Cryptography

## Security Features

- Firmware Signature Verification
- Integrity Checking
- Rollback Attack Prevention
- Audit Logging
- Secure Update Distribution

## Author

Manas Rana
