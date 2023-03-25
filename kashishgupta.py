elif n==8:
    import random
    passlen=int(input("Enter the Length of Password:"))
    x="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?<>"
    password="".join(random.sample(x,passlen))
    print(password)    
elif n==9:
    from langdetect import detect

    text=input("Enter the Sentence:")

    print(detect(text))
elif n==10:
        import qrcode
        import matplotlib.pyplot as plt
        x=input("Enter link you want to convert to convert to QRcode: ")
        img=qrcode.make(x)
        y=input("enter name tou want to save and apply .png: ")
        img.save👍
       
       
        plt.imshow(img,cmap="gray")