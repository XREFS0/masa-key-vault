# MASA KeyVault Password Suite

Cryptographic utility suite comprising password hashing, strength analysis, and credential generators

## Technical Architecture

The application is architected with modular separation of concerns adhering to modern clean code standards:

- **Component Layering**: Isolated view layouts, state managers, and service controllers.
- **Defensive Engineering**: Robust input sanitization and exception management.
- **Modern Design Standards**: High-contrast dark-mode interface styled for optimal usability and visual polish.

## Preview

![Application Interface](screenshots/app_interface.png)

## Features

- Cryptographic hashing suite supporting SHA-256, SHA-512, and MD5 digests.
- Shannon entropy evaluation detecting weak, dictionary, and compromised patterns.
- CSPRNG password generator with custom charset constraints.
- Zero-knowledge local credential storage simulation.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter pillow requests
```

## Execution

Launch the application via Python:

```bash
python "password/password.py"
```

## Project Structure

```
.
├── password
├── screenshots/
│   └── app_interface.png
├── .gitignore
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.
