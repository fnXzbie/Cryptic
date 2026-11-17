# 📌 (Description / About)



> A modern, fully offline-capable cybersecurity toolkit supporting hashing, JWT analysis, hash type identification, and multi-format encoding/decoding operations. 🚀



---



# 🛡️ Cyber Security & Cryptography



A multi-purpose cryptographic toolkit designed for cybersecurity enthusiasts and developers, featuring a modern, sleek interface and complete offline functionality. Developed with Python and Tkinter.



![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)



---



## ✨ Features



* **Hash Generation:** Instant hash generation using MD5, SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 algorithms.

* **Smart Hash Type Detection:** Automatically detects the potential type of an entered hash value by analyzing its character length and structure.

* **JWT Inspector (Decoder):** Parses JSON Web Token (JWT) structures into Header and Payload segments and presents them in a readable format.

* **Encoding & Decoding Support:**

  * Base64 & Base32

  * Hexadecimal

  * Binary System

  * URL Encoding

  * ASCII Conversions

* **Offline Operation:** Operates completely independently and securely without requiring any internet connection.



---



## 🚀 Installation & Usage



You can follow these steps to run the project on your local machine:



1. Clone the repository:

   ```bash

   git clone https://github.com/fnXzbie/Hash_Coder.git

   ```

2. Navigate into the folder:

   ```bash

   cd Hash_Coder

   ```

3. Run the application:

   ```bash

   python hashcoder.py

   ```



---



## 📦 Creating a Standalone Executable (.exe)



If you want to run the project as a standalone `.exe` on computers without Python installed, you can use **PyInstaller**:



```bash

python -m pip install pyinstaller

python -m PyInstaller --onefile --noconsole hashcoder.py

```

*(The generated `.exe` file will be located under the `dist` folder.)*



---



## 📜 License



This project is licensed under the MIT License. Feel free to modify and customize it as you wish.
