"""Generate WhatsApp deep-link QR codes for Bereke KPs."""
import qrcode
from urllib.parse import quote

PHONE = "77778110096"

targets = [
    ("qr-wa-bereke-client", "Здравствуйте! Я клиент Bereke Bank, хочу заказать услугу"),
    ("qr-wa-bereke-employee", "Здравствуйте! Я сотрудник Bereke Bank, хочу заказать услугу"),
]

for name, msg in targets:
    url = f"https://wa.me/{PHONE}?text={quote(msg)}"
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    out = f"images/{name}.png"
    img.save(out)
    print(f"{out}  ({url})")
