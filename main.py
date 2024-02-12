import qrcode


def generate_qr_code(text, file_name, margin=4, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_H):
    if error_correction not in [qrcode.constants.ERROR_CORRECT_L, qrcode.constants.ERROR_CORRECT_M,
                                qrcode.constants.ERROR_CORRECT_Q, qrcode.constants.ERROR_CORRECT_H]:
        raise ValueError("Invalid error correction level.")

    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=margin,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    text = "https://github.com/nurg1ssa"
    file_name = "qr_code.png"
    generate_qr_code(text, file_name)
