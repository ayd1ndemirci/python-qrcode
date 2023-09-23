import qrcode

def QRGenerate(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename + ".png")

text = input("QR Koda dönüştürülecek metin veya site linki yaz.\n")
qricon = input("QR Kodunuzun dosya adını belirleyin\n")

QRGenerate(text, qricon)

print(f"QR kodunuz '{qricon}.png adlı dosyaya kaydedildi'")
