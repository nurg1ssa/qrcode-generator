import qrcode
from enum import IntEnum

class ErrorCorrectionLevel(IntEnum):
    """Enumeration for valid error correction levels."""
    L = qrcode.constants.ERROR_CORRECT_L
    M = qrcode.constants.ERROR_CORRECT_M
    Q = qrcode.constants.ERROR_CORRECT_Q
    H = qrcode.constants.ERROR_CORRECT_H

def generate_qr_code(text, file_name, version=None, margin=4, box_size=10,
                    error_correction=ErrorCorrectionLevel.L, fill_color="black", back_color="white",
                    module_size=6):
    if error_correction not in ErrorCorrectionLevel.__members__.values():
        raise ValueError("Invalid error correction level.")

    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction.value,
        box_size=box_size,
        border=margin,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(file_name)

    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    text = "https://github.com/nurg1ssa"
    file_name = "qr_code.png"
    generate_qr_code(text, file_name, version=5, error_correction=ErrorCorrectionLevel.H,
                    fill_color="blue", back_color="yellow")
