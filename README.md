# 📌 (Description / About)

> Modern arayüze sahip, tamamen internetsiz çalışabilen; hashleme, JWT analizi, hash türü algılama ve çoklu encoding/decoding işlemlerini destekleyen siber güvenlik araç kutusu. 🚀



---



# 🛡️ Cyber Security & Cryptography Swiss Army Knife



Modern, şık ve tamamen çevrimdışı (offline) çalışabilen, siber güvenlik meraklıları ve geliştiriciler için tasarlanmış çok amaçlı kriptografi araç kutusu. Python ve Tkinter ile geliştirilmiştir.



![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)



---



## ✨ Özellikler



* **Hash Oluşturma:** MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 algoritmaları ile anlık hash üretimi.

* **Akıllı Hash Türü Algılama:** Girilen bir hash değerinin karakter uzunluğunu ve yapısını analiz ederek olası türünü otomatik tespit eder.

* **JWT İnceleyici (Decoder):** JSON Web Token (JWT) yapılarını Header ve Payload olarak ayrıştırır ve okunabilir formata getirir.

* **Encoding & Decoding Desteği:**

  * Base64 & Base32

  * Hex (Onaltılık)

  * Binary (İkili Sistem)

  * URL Encoding

  * ASCII Dönüşümleri

* **Çevrimdışı (Offline) Çalışma:** Hiçbir internet bağlantısına ihtiyaç duymadan tam güvenlikli ve bağımsız çalışır.



---



## 🚀 Kurulum & Çalıştırma



Projeyi yerel makinenizde çalıştırmak için şu adımları izleyebilirsiniz:



1. Repoyu klonlayın:

   ```bash

   git clone https://github.com/fnXzbie/Hash_Code_Encrypt-Decrypt.git

   ```

2. Klasörün içine girin:

   ```bash

   cd Hash_Code_Encrypt/Decrypt

   ```

3. Uygulamayı çalıştırın:

   ```bash

   python hashcoder.py

   ```



---



## 📦 Tek Başına (.exe) Çalıştırılabilir Dosya Oluşturma



Projeyi Python kurulu olmayan bilgisayarlarda tekil bir `.exe` olarak çalıştırmak isterseniz **PyInstaller** kullanabilirsiniz:



```bash

python -m pip install pyinstaller

python -m PyInstaller --onefile --noconsole hashcoder.py

```

*(Oluşan `.exe` dosyası `dist` klasörünün altında yer alacaktır.)*



---





## 📜 Lisans

Bu proje MIT lisansı altında açılmıştır. Dilediğiniz gibi geliştirebilir ve özelleştirebilirsiniz.
