ulkeler = input("ülke giriniz :")

if ulkeler in ["Australia","Canada","Denmark","Germany","Liechtenstein","Luxembourg","Switzerland","Norway","Sweden","European Union","Singapore","United States","Austria",
               "Finland","New Zealand","France","Taiwan","United Arab Emirates","Hong Kong","Qatar""Belgium","Isle of Man","Macau","United Kingdom","South Korea",
               "Cayman Islands","Czech Republic","Estonia","Ireland","Kuwait","Israel","Bermuda","China","Japan","Lithuania","Saudi Arabia"]:
    def ulkelersek4(dortpuan):
        ulkeler4=float(4.0)
        return(f"secilen ulke {ulkeler4} puan ")
    sonucUlkeler4 = ulkelersek4(ulkeler)
    print(sonucUlkeler4)


elif ulkeler in ["Iceland","Malta","Slovakia","Slovenia","Chile","Latvia","Poland","Spain","Portugal","Malaysia","Botswana","Andorra","Thailand","Croatia","Italy",
                 "Bulgaria","Peru","Philippines","Uruguay","Cyprus","Hungary","Indonesia","Mexico","Kazakhstan","India","Panama","Aruba","Colombia","Mauritius",
                 "Montserrat","Romania","Greece"]:
    def ulkelersek3(ucpuan):
        ulkeler3=float(3.0)
        return(f"secilen ulke {ulkeler3} puan")
    sonucUlkeler3 = ulkelersek3(ulkeler)
    print(sonucUlkeler3)


elif ulkeler in ["Azerbaijan","Morocco","Oman","Trinidad and Tobago","Paraguay","Serbia","Guatemala","Vietnam","Brazil","Georgia","Macedonia","San Marino",
                 "Dominican Republic","Ivory Coast","South Africa","Seychelles","Armenia","Bangladesh","Costa Rica","Uzbekistan","Albania","Bahamas","Honduras",
                 "Namibia","Senegal","Jamaica","Jordan","Benin","Fiji","Turkmenistan","Bahrain","Rwanda","Montenegro","Tanzania","Cambodia","Lesotho","Turkey",
                 "Uganda","Zambia","Kenya","Mongolia","Nicaragua","Bosnia and Herzegovina","Kyrgyzstan","Papua New Guinea","Togo","Barbados"]:
    def ulkelersek2(ikipuan):
        ulkeler2=float(2.0)
        return(f"secilen ulke {ulkeler2} puan")
    sonucUlkeler2 = ulkelersek2(ulkeler)
    print(sonucUlkeler2)


elif ulkeler in ["Angola","Cape Verde","Gabon","Madagascar","Moldova","Solomon Islands","St Vincent and the Grenadines","Swaziland","Tajikistan","Cameroon",
                 "Egypt","Iraq","Nigeria","Congo","Maldives","Tunisia","Bolivia","Burkina Faso","Ecuador","El Salvador","Mozambique","Pakistan",
                 "Republic of the Congo","Belize","Ethiopia","Laos","Mali","Niger","Suriname","Russia","Ukraine","Argentina","Belarus","Ghana","Sri Lanka",
                 "Venezuela","Lebanon","Cuba","Puerto Rico","Grenada","Kosovo"]:
    def ulkelersek1(birpuan):
        ulkeler1=float(1.0)
        return(f"secilen ulke {ulkeler1} puan")
    sonucUlkeler1 = ulkelersek1(ulkeler)
    print(sonucUlkeler1)

else:
    print("girdiğiniz ülke adi yanlis tekrar deneyiniz")