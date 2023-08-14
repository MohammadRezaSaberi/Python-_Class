import qrcode
# from PIL import Image

# # Set the email address you want to encode
# email = 'saberimr1383@gmail.com'

# # Create a QR code object
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# # Add the email data to the QR code
# qr.add_data(email)
# qr.make(fit=True)

# # Create an image of the QR code with custom colors
# img = qr.make_image(fill_color='blue', back_color='white')

# # Save the image to a file
# img.save('email_qr.png')

# # Open the image and display it
# img.show()
import qrcode

# Set the data you want to encode
data = 'Hello, World!'

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color='black', back_color='white')

# Save the image to a file
img.save('qr.png')
