class Calculator: 
    "Hesap Makinesi Projesi"
    
    def __init__(self, a, b): 

        self.value1 = a 
        self.value2 = b 
    
    def add(self): 
        "Toplama v1+v2 = Sonuç -> return Sonuç"
        return self.value1 + self.value2 
    
    def subt(self): 
        "Çıkarma v1-v2 = Sonuç -> return Sonuç"
        return self.value1 - self.value2 
         
    def multiply(self): 
        "Çarpma v1*v2 = Sonuç -> return Sonuç"
        return self.value1 * self.value2 
    
    def division(self): 
        "Bölme v1/v2 = Sonuç -> return Sonuç"
        return self.value1 / self.value2 
        
while True:           
    print("Toplama(1),Çıkarma(2), Çarpma(3), Bölme(4)") 
    selection = input("1 - 2 - 3 - 4 \n") 

    a = int(input("Birinci Değer  = ")) 
    b = int(input("İkinci Değer = ")) 

    hesap_mak = Calculator(a,b) 
    if selection == "1":  
        add_result = hesap_mak.add()
        print("\nToplama Sonucu : {}".format(add_result))
    elif selection == "2": 
        subtraction_result = hesap_mak.subt()
        print("\nÇıkarma Sonucu : {}".format(subtraction_result))
    elif selection == "3": 
        multiply_result = hesap_mak.multiply()
        print("\nÇarpma Sonucu : {}".format(multiply_result))
    elif selection == "4": 
        div_result = hesap_mak.division()
        print("\nBölme Sonucu : {}".format(div_result))
    else: 
        print("\nHata! uygun rakam giriniz")