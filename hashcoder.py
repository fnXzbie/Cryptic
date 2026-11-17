import base64
import binascii
import hashlib
import hmac
import json
import tkinter as tk
from tkinter import messagebox, ttk
import urllib.parse


class CyberToolApp:

  def __init__(self, root):
    self.root = root
    self.root.title("rooTfnX-Encoder/Decoder")
    self.root.geometry("900x700")
    self.root.configure(bg="#121212")

    # Stil ve Tema Ayarları (Modern Koyu Tema)
    self.style = ttk.Style()
    self.style.theme_use("clam")
    self.style.configure(
        "TLabel", background="#121212", foreground="#00ffcc", font=("Segoe UI", 10, "bold")
    )
    self.style.configure(
        "TButton",
        background="#1f1f1f",
        foreground="#ffffff",
        font=("Segoe UI", 10, "bold"),
        borderwidth=1,
    )
    self.style.map(
        "TButton", background=[("active", "#00ffcc")], foreground=[("active", "#000000")]
    )
    self.style.configure(
        "TRadiobutton",
        background="#121212",
        foreground="#ffffff",
        font=("Segoe UI", 10),
    )

    # Başlık
    title_label = tk.Label(
        root,
        text="SİBER GÜVENLİK & KRİPTOGRAFİ ARAÇ KUTUSU",
        bg="#121212",
        fg="#00ffcc",
        font=("Segoe UI", 16, "bold"),
    )
    title_label.pack(pady=15)

    # Ana Çerçeve
    main_frame = tk.Frame(root, bg="#121212")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    # Sol Panel: Girdi ve İşlem Seçimi
    left_panel = tk.Frame(main_frame, bg="#1e1e1e", bd=2, relief="groove")
    left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

    tk.Label(
        left_panel,
        text="Girdi Metni / Veri:",
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 5))

    self.input_text = tk.Text(
        left_panel,
        height=10,
        bg="#2d2d2d",
        fg="#00ffcc",
        insertbackground="white",
        font=("Consolas", 10),
    )
    self.input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # İşlem Kategorileri Seçimi
    operation_frame = tk.Frame(left_panel, bg="#1e1e1e")
    operation_frame.pack(fill=tk.X, padx=10, pady=10)

    tk.Label(
        operation_frame,
        text="İşlem Türü Seçin:",
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", pady=5)

    self.op_var = tk.StringVar(value="hash")

    operations = [
        ("Hash Oluştur (MD5, SHA vb.)", "hash"),
        ("Hash Türünü Otomatik Algıkla", "detect"),
        ("JWT Decode / İncele", "jwt"),
        ("Base64 (Encode / Decode)", "base64"),
        ("Base32 (Encode / Decode)", "base32"),
        ("Hex (Encode / Decode)", "hex"),
        ("Binary (Encode / Decode)", "binary"),
        ("URL (Encode / Decode)", "url"),
        ("ASCII (Encode / Decode)", "ascii"),
    ]

    for text, val in operations:
      ttk.Radiobutton(
          operation_frame, text=text, variable=self.op_var, value=val
      ).pack(anchor="w", pady=2)

    # Alt İşlem Butonları (Encode/Decode Yönü için)
    btn_frame = tk.Frame(left_panel, bg="#1e1e1e")
    btn_frame.pack(fill=tk.X, padx=10, pady=15)

    self.process_btn = tk.Button(
        btn_frame,
        text="İŞLEMİ ÇALIŞTIR",
        bg="#00ffcc",
        fg="#000000",
        font=("Segoe UI", 10, "bold"),
        command=self.execute_operation,
        relief="flat",
        cursor="hand2",
    )
    self.process_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5), ipady=5)

    self.decode_btn = tk.Button(
        btn_frame,
        text="TERS ÇEVİR (DECODE)",
        bg="#ff5555",
        fg="#ffffff",
        font=("Segoe UI", 10, "bold"),
        command=self.execute_decode,
        relief="flat",
        cursor="hand2",
    )
    self.decode_btn.pack(
        side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0), ipady=5
    )

    # Sağ Panel: Çıktı Ekranı
    right_panel = tk.Frame(main_frame, bg="#1e1e1e", bd=2, relief="groove")
    right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

    tk.Label(
        right_panel,
        text="Sonuç / Çıktı:",
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 5))

    self.output_text = tk.Text(
        right_panel,
        height=20,
        bg="#2d2d2d",
        fg="#55ff55",
        insertbackground="white",
        font=("Consolas", 10),
    )
    self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    clear_btn = tk.Button(
        right_panel,
        text="EKRANI TEMİZLE",
        bg="#444444",
        fg="#ffffff",
        font=("Segoe UI", 9),
        command=self.clear_fields,
        relief="flat",
    )
    clear_btn.pack(anchor="e", padx=10, pady=10)

  def clear_fields(self):
    self.input_text.delete("1.0", tk.END)
    self.output_text.delete("1.0", tk.END)

  def execute_operation(self):
    data = self.input_text.get("1.0", tk.END).strip()
    if not data:
      messagebox.showerror("Hata", "Lütfen işlenecek bir metin girin!")
      return

    op = self.op_var.get()
    result = ""

    try:
      if op == "hash":
        encoded_data = data.encode("utf-8")
        result += f"--- HASH SONUÇLARI ---\n"
        result += f"MD5    : {hashlib.md5(encoded_data).hexdigest()}\n"
        result += f"SHA-1  : {hashlib.sha1(encoded_data).hexdigest()}\n"
        result += f"SHA-224: {hashlib.sha224(encoded_data).hexdigest()}\n"
        result += f"SHA-256: {hashlib.sha256(encoded_data).hexdigest()}\n"
        result += f"SHA-384: {hashlib.sha384(encoded_data).hexdigest()}\n"
        result += f"SHA-512: {hashlib.sha512(encoded_data).hexdigest()}\n"

      elif op == "detect":
        result = self.detect_hash_type(data)

      elif op == "jwt":
        parts = data.split(".")
        if len(parts) != 3:
          result = (
              "Hata: Geçersiz JWT formatı! (Üç nokta ile ayrılmış olmalıdır)"
          )
        else:
          header = json.loads(
              base64.urlsafe_b64decode(parts[0] + "==").decode("utf-8")
          )
          payload = json.loads(
              base64.urlsafe_b64decode(parts[1] + "==").decode("utf-8")
          )
          result += f"--- JWT HEADER ---\n{json.dumps(header, indent=4)}\n\n"
          result += f"--- JWT PAYLOAD ---\n{json.dumps(payload, indent=4)}"

      elif op == "base64":
        result = base64.b64encode(data.encode("utf-8")).decode("utf-8")

      elif op == "base32":
        result = base64.b32encode(data.encode("utf-8")).decode("utf-8")

      elif op == "hex":
        result = data.encode("utf-8").hex()

      elif op == "binary":
        result = " ".join(format(ord(char), "08b") for char in data)

      elif op == "url":
        result = urllib.parse.quote(data)

      elif op == "ascii":
        result = " ".join(str(ord(char)) for char in data)

      self.output_text.delete("1.0", tk.END)
      self.output_text.insert(tk.END, result)

    except Exception as e:
      messagebox.showerror("İşlem Hatası", f"Bir hata oluştu:\n{str(e)}")

  def execute_decode(self):
    data = self.input_text.get("1.0", tk.END).strip()
    if not data:
      messagebox.showerror("Hata", "Lütfen çözülecek bir metin girin!")
      return

    op = self.op_var.get()
    result = ""

    try:
      if op == "base64":
        result = base64.b64decode(data.encode("utf-8")).decode("utf-8")

      elif op == "base32":
        result = base64.b32decode(data.encode("utf-8")).decode("utf-8")

      elif op == "hex":
        result = bytes.fromhex(data).decode("utf-8")

      elif op == "binary":
        binary_values = data.split()
        result = "".join([chr(int(b, 2)) for b in binary_values])

      elif op == "url":
        result = urllib.parse.unquote(data)

      elif op == "ascii":
        ascii_values = data.split()
        result = "".join([chr(int(a)) for a in ascii_values])

      else:
        result = "Bu mod için tersine çevirme (Decode) desteklenmiyor veya Hash algoritmaları tek yönlüdür (geri döndürülemez)."

      self.output_text.delete("1.0", tk.END)
      self.output_text.insert(tk.END, result)

    except Exception as e:
      messagebox.showerror(
          "Çözüm Hatası", f"Geçersiz veri veya format:\n{str(e)}"
      )

  def detect_hash_type(self, h):
    h = h.strip()
    length = len(h)
    detected = []

    if h.startswith("eyJ") and h.count(".") == 2:
      detected.append("JWT (JSON Web Token)")

    if length == 32 and all(c in "0123456789abcdefABCDEF" for c in h):
      detected.append("MD5")
    if length == 40 and all(c in "0123456789abcdefABCDEF" for c in h):
      detected.append("SHA-1")
    if length == 56 and all(c in "0123456789abcdefABCDEF" for c in h):
      detected.append("SHA-224")
    if length == 64 and all(c in "0123456789abcdefABCDEF" for c in h):
      detected.append("SHA-256")
    if length == 96 and all(c in "0123456789abcdefABCDEF" for c in h):
      detected.append("SHA-384")
    if length == 128 and all(c in "0123456789abcdefABCDEF" for c in h):
      detected.append("SHA-512")

    if not detected:
      return (
          "Bilinmeyen hash türü veya uzunluk/karakter kriterlerine uymuyor."
      )
    return "Muhtemel Hash Türü(leri):\n" + "\n".join(
        [f"✔ {d}" for d in detected]
    )


if __name__ == "__main__":
  root = tk.Tk()
  app = CyberToolApp(root)
  root.mainloop()