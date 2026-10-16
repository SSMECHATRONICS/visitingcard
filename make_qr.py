"""Run ONCE to make the print-ready QR for your visiting card.
Usage:  python make_qr.py https://yourname.github.io/card/
Needs:  pip install segno
The QR only encodes the URL, so it never changes. Edit profile.json to change what people see.
"""
import sys, segno
url = sys.argv[1] if len(sys.argv) > 1 else input("Final permanent URL of your card page: ").strip()
qr = segno.make(url, error=("h"))        # high error correction: survives print wear
qr.save("card_qr.svg", scale=10, border=4)             # vector - best for printers
qr.save("card_qr.png", scale=30, border=4, dpi=600)    # 600 dpi raster
print("Saved card_qr.svg and card_qr.png for", url)
