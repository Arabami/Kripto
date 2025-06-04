from flask import Flask, render_template, request, send_file
import os
from cipher_algorithms import vigenere, vigenere_auto, vigenere_extended, affine, playfair, hill, gronsfeld
import io
from werkzeug.utils import secure_filename
import math 

app = Flask(__name__)
app.secret_key = 'some_secret_key'
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def format_output(text, group_5=False):
    text = text.replace(" ", "")
    if group_5:
        return ' '.join(text[i:i+5] for i in range(0, len(text), 5))
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    result = ''
    cipher_type = ""
    key = ""
    mode = ""
    plaintext = ""
    output_format = ""

    if request.method == "POST":
        cipher_type = request.form.get("cipher")
        key = request.form.get("key")
        mode = request.form.get("mode")
        plaintext = request.form.get("plaintext", "")
        file = request.files.get("file")
        output_format = request.form.get("output_format")
        group_5 = output_format == "group5"

        try:
            # Jika ada file, baca sebagai konten teks
            if file:
                filename = secure_filename(file.filename)
                content = file.read()
                try:
                    plaintext = content.decode('utf-8', errors='replace')
                except Exception:
                    result = "File tidak dapat dibaca sebagai teks."
                    return render_template("index.html",
                                           result=result,
                                           cipher_type=cipher_type,
                                           key=key,
                                           mode=mode,
                                           plaintext="",
                                           output_format=output_format)

            # Jalankan cipher sesuai pilihan
            if cipher_type == "vigenere":
                result = vigenere.encrypt(plaintext, key) if mode == "encrypt" else vigenere.decrypt(plaintext, key)

            elif cipher_type == "vigenere_auto":
                result = vigenere_auto.encrypt(plaintext, key) if mode == "encrypt" else vigenere_auto.decrypt(plaintext, key)

            elif cipher_type == "vigenere_extended":
                if file:
                    if mode == "encrypt":
                        result_bytes = vigenere_extended.encrypt(content, key)
                        output_filename = f"encrypted_{filename}"
                    else:
                        result_bytes = vigenere_extended.decrypt(content, key)
                        output_filename = f"decrypted_{filename}"

                    output_path = os.path.join(DOWNLOAD_FOLDER, output_filename)
                    with open(output_path, "wb") as f:
                        f.write(result_bytes)

                    return send_file(output_path, as_attachment=True)
                else:
                    if mode == "encrypt":
                        encrypted_bytes = vigenere_extended.encrypt(plaintext.encode('latin1'), key)
                        result = encrypted_bytes.decode('latin1')
                    else:
                        cipher_bytes = plaintext.encode('latin1')
                        decrypted_bytes = vigenere_extended.decrypt(cipher_bytes, key)
                        result = decrypted_bytes.decode('utf-8', errors='replace')

            elif cipher_type == "affine":
                a, b = map(int, key.split(","))
                result = affine.encrypt(plaintext, a, b) if mode == "encrypt" else affine.decrypt(plaintext, a, b)

            elif cipher_type == "playfair":
                result = playfair.encrypt(plaintext, key) if mode == "encrypt" else playfair.decrypt(plaintext, key)

            elif cipher_type == "hill":
                nums = list(map(int, key.split(',')))
                size = int(math.sqrt(len(nums)))
                key_matrix = [nums[i:i+size] for i in range(0, len(nums), size)]
                result = hill.encrypt(plaintext, key_matrix) if mode == "encrypt" else hill.decrypt(plaintext, key_matrix)
            
            elif cipher_type == "gronsfeld":
                result = gronsfeld.encrypt(plaintext, key) if mode == "encrypt" else gronsfeld.decrypt(plaintext, key)

            result = format_output(result, group_5)
            app.config["last_result"] = result

        except Exception as e:
            result = f"Terjadi kesalahan: {e}"

    return render_template("index.html",
                           result=result,
                           cipher_type=cipher_type,
                           key=key,
                           mode=mode,
                           plaintext=plaintext if not request.files.get("file") else "",
                           output_format=output_format)

@app.route("/download")
def download():
    data = io.BytesIO()
    data.write(app.config.get("last_result", "").encode())
    data.seek(0)
    return send_file(data, as_attachment=True, download_name="hasil.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
