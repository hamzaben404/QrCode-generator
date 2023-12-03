import tkinter as tk
from tkinter import Entry, Button, Label, StringVar
import qrcode

def generate_qr_code():
    url = entry_url.get()
    output_name = entry_output_name.get()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image with the specified output name
    img.save(f"{output_name}.png")

    # Display a message
    label_message.config(text="QR Code generated successfully!")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the URL entry field
label_url = Label(root, text="Enter URL:")
label_url.pack(pady=5)
entry_url = Entry(root, width=40)
entry_url.pack(pady=5)

# Create and place the Output Name entry field
label_output_name = Label(root, text="Enter Output Image Name:")
label_output_name.pack(pady=5)
entry_output_name = Entry(root, width=40)
entry_output_name.pack(pady=5)

# Create and place the Generate button
btn_generate = Button(root, text="Generate QR Code", command=generate_qr_code)
btn_generate.pack(pady=10)

# Create a label for displaying messages
label_message = Label(root, text="")
label_message.pack(pady=5)

# Start the main loop
root.mainloop()
