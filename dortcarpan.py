import sektorler
import altsektorler2
import kisisayisi
import yillarkod
import bizikullaniyormu

import yillarkod 
yillarkod.sonucyillar





toplamVarlik = float(input("toplam varlik giriniz :"))
netSermaye = float(input("netsermaye giriniz : "))
dağitilmamişKar = float(input("dağitilmamiş kar giriniz : "))
satişlar = float(input("satişlar giriniz :"))
calismaSermayesi = float(input("calisma sermayesi giriniz :"))
faizÖncesiKar = float(input("faiz öncesi kar giriniz : "))
vergiÖncesiKar = float(input("vergi öncesi kar giriniz :"))
kisaVadeliYükümlülükler = float(input("kisa vadeli yükümlülükler giriniz :"))

değişken1 = ((netSermaye / toplamVarlik) * 1.2)
değişken2 = ((dağitilmamişKar / toplamVarlik) * 1.4)
değişken3 = ((satişlar / toplamVarlik) * 1.36)
değişken4 = ((calismaSermayesi / toplamVarlik) * 1.05)
değişken5 = ((faizÖncesiKar / toplamVarlik) * 2.33)
değişken6 = ((vergiÖncesiKar / kisaVadeliYükümlülükler) * 0.66)

result = (değişken1 + değişken2 + değişken3 + değişken4 + değişken5 + değişken6)
print(result)



