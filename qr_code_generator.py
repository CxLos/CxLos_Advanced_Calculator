# qr_code_generator.py
"""
Generate a QR code for the DockerHub repository of this project.
"""
import qrcode

DOCKERHUB_URL = "https://hub.docker.com/repository/docker/cxlos/cxlos_advanced_calculator/general"
OUTPUT_PATH = "qr_codes/cxlos_advanced_calculator_repo_qr.png"

if __name__ == "__main__":
    qr = qrcode.QRCode()
    qr.add_data(DOCKERHUB_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="black")
    img.save(F"qr_codes/{OUTPUT_PATH}")
    print(f"QR code saved to {OUTPUT_PATH}")

# Push to DockerHub:

# docker build -t cxlos/cxlos_advanced_calculator:latest .
# docker push cxlos/cxlos_advanced_calculator:latest