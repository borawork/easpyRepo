

yil = float(input("şirket yili giriniz :"))

def yillar(yil):
    if (0<yil) and (yil<=3):
        y1 = float(1.0)
        return(f"verilen puan {y1}")
    elif(3<yil) and (yil<=10):
        y2 = float(2.0)
        return(f"verilen puan {y2}")
    elif(10<yil) and (yil<=30):
         y3 = float(3.0)
         return(f"verilen puan {y3}")
    elif(30<yil):
        y4 = float(4.0)
        return(f"verilen puan {y4}")
sonucyillar = yillar(yil)
print(sonucyillar)









  












