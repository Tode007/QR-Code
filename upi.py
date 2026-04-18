import qrcode

#Taking upi id 
upi_id = input("enter ur UPI ID = ")
#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#defining the payement URL based on the UPI ID and the payment app
phonepe_url = f'ur;://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
#create QR codes for each payment app
phonepe_qr =qrcode.make(phonepe_url)

#save qr code

phonepe_qr.save('phonepe_qr.png')

#display the qr codes by using pilo
phonepe_qr.show()