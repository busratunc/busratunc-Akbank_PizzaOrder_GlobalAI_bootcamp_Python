#GlobalAI bootcamp Pizza Order Proje
#Büşra tunç

#ilgili kütüphaneler eklendi
import csv 
import datetime

#Pizza üst sınıfı
class Pizza:
    #pizzanın açıklaması için get_description fonksiyonu tanımlandı
    def get_description(self):  
        return self.__class__.__name__
    #pizzanın fiyatı için get_cost fonksiyonu tanımlandı
    def get_cost(self):  
        return self.__class__.cost

#Pizza alt sınıfları
class Klasik(Pizza):
    cost = 20.0
    def __init__(self):
        self.description = 'Klasik pizza seçtiniz. sucuk, zeytin, biber ve ekstra peynir içermektedir'
        print(self.description)
    def __repr__(self): #main içerisinde tanımı çağrı yaptığımda fonksiyon repr üzerinden döndürüyor
        return self.description
class Margarita(Pizza):
    cost = 35.0
    def __init__(self):
        self.description = 'Margarita pizza seçtiniz.  parmesan peyniri, nane, sucuk, biber içermektedir'
        print(self.description)
    def __repr__(self): 
        return self.description
class TurkPizza(Pizza):
    cost = 35.0
    def __init__(self):
        self.description = 'Türk pizza seçtiniz.  sucuk, biber, zeytin, kaşar, ekstra domates sosu içermektedir'
        print(self.description)
    def __repr__(self): 
        return self.description
class SadePizza(Pizza):
    cost = 20.0
    def __init__(self):
        self.description = 'Sade pizza seçtiniz.  sucuk içermektedir'
        print(self.description)
    def __repr__(self): 
        return self.description
#Sos üst sınıfı
class Decorator(Pizza):
    def __init__(self, sos):
        self.component = sos
    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)
    def get_description(self):
        return self.component.get_description() + \
            ' : ' + Pizza.get_description(self)


#Sos alt sınıfları
class Zeytin(Decorator):
    cost = 2.0
    def __init__(self, sos):
        Decorator.__init__(self, sos)
class Mantar(Decorator):
    cost = 3.0
    def __init__(self, sos):
        Decorator.__init__(self, sos)
class KeciPeyniri(Decorator):
    cost = 2.0
    def __init__(self, sos):
        Decorator.__init__(self, sos)
class Et(Decorator):
    cost = 5.0
    def __init__(self, sos):
        Decorator.__init__(self, sos)
class Sogan(Decorator):
    cost = 2.0
    def __init__(self, sos):
        Decorator.__init__(self, sos)
class Misir(Decorator):
    cost = 2.0
    def __init__(self, sos):
        Decorator.__init__(self, sos)

#menuyu çağıran fonksiyon
def menu():
    menufile = open ("menu.txt","r",encoding='utf-8') #menunun yazili olduğu txt dosyasını çağırdım
    for i in menufile: #menu.txt içindekileri ekrana basmak için for döngüsü kullandım
         print(i,end="") 
    print('\n')
    menufile.close() 


#kullanıcdan bilgi alan ve tablo içine yazan fonksiyon
def kullanici_info(ucret):
    isim= input ('isim giriniz: ')
    tc= input ('tc giriniz : ')
    kart_no= input ('kart numara giriniz : ')
    kart_tarih = input ('son kullanma tarihi giriniz (AA/YY) : ' )
    kart_cvc = input ('cvc:' )
    sifre = input ('sifre:' )
    ucret=ucret
    tarih = datetime.datetime.today()
    with open('Orders_Database.csv', 'a') as orders: #csv dosyası olarak açıyorum ve içerisine kullanıcıdan algığımız bilgileri yazdırıyoruz
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([isim, tc, kart_no, kart_tarih, kart_cvc, sifre, tarih, ucret])

#Ana fonksiyon
def main():

    
  
    menu() #ekrana menuyu bastırdım
    taban= input('pizza tabanı seçiminiz:  ', ) #kullanıcıdan taban seçimi alıyorum
    sos = input ('sos seçiminiz:  ', )  #kullanıcıdan üst sos seçimi alıyorum
    taban=int(taban) # if kontrolü yapabilmek için str değerleri int e çeviriyorum
    sos=int(sos)
    if taban>4 or sos<11 or sos>16: 
        print("geçersiz değer girildi") #seçim değerleri dışında veri girildiğini bildiriyorum
    else:
        print('fiyat hesaplanıyor..')
    #kullanıcının taban seçimine göre ücret miktarı fonksiyonlardan çekiliyor
    if(taban==1): #menu seçimine göre ilgili pizza alt sınıfından ücret bilgisini çağırıyorum
        Klasik.get_description
        ucrett= Klasik.cost
        A= Klasik() #klasik pizza tanımını ekrana bastırıyorum
    elif(taban==2):
        Margarita.get_description
        ucrett=Margarita.cost
        A=Margarita()
    elif(taban==3):
        TurkPizza.get_description
        ucrett= TurkPizza.cost
        A=TurkPizza()
    elif(taban==4):
        SadePizza.get_description
        ucrett=SadePizza.cost
        A=SadePizza()
    else:
        print('taban seçimi yanlış girildi')
    
    #kullanıcının sos seçimine göre ücret miktarı fonksiyonlardan çekiliyor
    if(sos==11):
        ucrets= Zeytin.cost
    elif(sos==12):
        ucrets = Mantar.cost
    elif(sos==13):
        ucrets= KeciPeyniri.cost
    elif(sos==14):
        ucrets=Et.cost
    elif(sos==15):
        ucrets= Sogan.cost
    elif(sos==16):
        ucrets= Misir.cost
    else:
        print('sos seçimi yanlış girildi') #menude yazmayan bir değer girildiği için program kapatılıyor
        
    #ucrett --> taban ucreti / ucrets --> sos ucreti / ucret ise odenecek total miktar
    ucret=ucrett+ucrets
    print('taban ucreti ', ucrett, 'sos ucreti', ucrets, 'odenecek toplam ücret', ucret)
    kullanici_info(ucret) #kullanıcıdan bilgileri alan vs csv içine yazan fonksiyonu çağırıyorum



if __name__ == '__main__':
    main()