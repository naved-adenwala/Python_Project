# importing the qrcode module
import qrcode
def qr_Generate():
    link = input("Enter Link to Generate Qrcode : ")
    # creating a QRCode object
    obj_qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 1,)
    # adding link
    obj_qr.add_data(link)
    # using the make_image() function
    qr_img = obj_qr.make_image(fill_color = "black", back_color = "white")
    # saving the QR code image
    qr_img.save("01.png")
    print("QR code has been generated Successfully!!!")

#function
qr_Generate()