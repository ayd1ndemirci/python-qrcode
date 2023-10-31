from qrgenerator import QRGenerate


def main():
    text = input("QR Koda dönüştürülecek metin veya site linki yaz.\n")
    qricon = input("QR Kodunuzun dosya adını belirleyin\n")

    QRGenerate(text, qricon)

    print(f"QR kodunuz '{qricon}.png adlı dosyaya kaydedildi'")


if __name__ == main():
    main()