import qrcode
def gen_qr(str):
    qr_details = qrcode.QRCode(version=1, box_size=40, border=5)
    qr_details.add_data(str)
    qr_details.make(fit=True)
    qr_img = qr_details.make_image(fill_color="Black", back_color="White")
    qr_img.save("Sourcify.png")
    print("Your qr has been generated")
def main():
    str=input("Enter your required URL")
    gen_qr(str)
if __name__== "__main__":
    main()








