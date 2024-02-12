import qrcode
from PIL import Image

from enum import IntEnum

class ErrorCorrectionLevel(IntEnum):
    """Enumeration for valid error correction levels."""
    L = qrcode.constants.ERROR_CORRECT_L
    M = qrcode.constants.ERROR_CORRECT_M
    Q = qrcode.constants.ERROR_CORRECT_Q
    H = qrcode.constants.ERROR_CORRECT_H

def generate_qr_code(text, file_name, version=None, margin=4, box_size=10,
                    error_correction=ErrorCorrectionLevel.L, fill_color="black", back_color="white",
                    module_size=6, quiet_zone=4, image_format="PNG", logo=None):
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

    # Create a new image with the desired size
    img_with_quiet_zone = Image.new("RGB", (img.size[0] * module_size, img.size[1] * module_size), back_color)

    # Paste the QR code image onto the new image
    img_with_quiet_zone.paste(img, (0, 0))

    # Add quiet zone
    quiet_zone_image = Image.new("RGB", (img_with_quiet_zone.size[0] + 2 * quiet_zone, img_with_quiet_zone.size[1] + 2 * quiet_zone), back_color)
    quiet_zone_image.paste(img_with_quiet_zone, (quiet_zone, quiet_zone))

    # Add logo if provided
    if logo:
        # Open the logo image and convert it to RGBA mode
        with open(logo, "rb") as f:
            logo_image = Image.open(f).convert("RGBA")

        quiet_zone_image.paste(logo_image, ((quiet_zone_image.size[0] - logo_image.size[0]) // 2, (quiet_zone_image.size[1] - logo_image.size[1]) // 2), logo_image)

    quiet_zone_image.save(file_name, format=image_format)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    text = "https://github.com/nurg1ssa"
    file_name = "qr_code.png"

    # Example logo
    logo_path = "logo.png"
    try:
        generate_qr_code(text, file_name, version=5, error_correction=ErrorCorrectionLevel.H,
                        fill_color="black", back_color="lightgreen", module_size=3, quiet_zone=5,
                        image_format="PNG", logo=logo_path)
    except FileNotFoundError:
        print(f"Warning: Logo file '{logo_path}' not found. QR code will be generated without a logo.")
        generate_qr_code(text, file_name, version=5, error_correction=ErrorCorrectionLevel.H,
                        fill_color="blue", back_color="yellow", module_size=10, quiet_zone=6,
                        image_format="PNG", logo=None)
