# python-qrcode


# How can I make it work?

just open the console where the code is located and type "python app.py" 
(download the following libraries)

# The libraries you need to download to run this code are
- pip install qrcode[pil]

# Photos


![image](https://github.com/ayd1ndemirci/python-qrcode/assets/128159204/dce86a72-624e-4df7-8a97-cf6fef60fad0)

![sefa png](https://github.com/ayd1ndemirci/python-qrcode/assets/128159204/b41d2d92-1101-49e6-bff0-745bb6b59ce3)


# sources I have reviewed
- https://pypi.org/project/qrcode/

Code:
```py
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
```
