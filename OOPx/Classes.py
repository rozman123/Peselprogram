# -*- coding: latin-1 -*-
from datetime import datetime

class UI:
    ListaOsb=[]
    def __init__(self):  # Inicajalizuje UI i dodaje osoby do listy
        print("Ctrl+c Ko�czy dzia�anie programu.\n")
        city = input("Podaj miasto:\n")
        #name,last_name,nrPESEL=input("Podaj Imi� Nazwisko i PESEL oddzielone spacjami: ").split(' ')
        #nrPESEL=int(nrPESEL)
        name = input("Podaj swoje imie:\n")   # Pobiera od u�ytkownika imie
        last_name = input("Podaj swoje nazwisko:\n")   # Pobiera od u�ytkownika nazwisko
        nrPESEL = input("Podaj sw�j PESEL:\n")   # Pobiera od u�ytkownika PESLE
        #nrPESEL=int(nrPESEL)
        self.SPR_Danych_i_Zapis(city,name,last_name,nrPESEL)


    @classmethod
    def Pentla(cls):
        try:
            while True:
                UI()
                UI.print_List()
        except KeyboardInterrupt:
            UI.Save_List()
            print("Koniec dzia�ania programu!\n")


    def SPR_Danych_i_Zapis(self,city,name,last_name,nrPESEL):
        if(UI.spr_PESEL(nrPESEL,name)):   # Sprawdza czy pesel jest poprawny
            for Osb in self.ListaOsb:
                if(Osb.nrPESEL==nrPESEL):   # Aktualizuje Imi� i Nazwisko Je�li osoba o danym PESELU jest ju� na li�cie
                    Osb.change_city(city)
                    Osb.change_name(name)
                    Osb.change_last_name(last_name)
                    print(f'Zmieniono Dane dla PESEL-u: {nrPESEL}\n')
                    break
            else:
                osb=Osoba(city,name,last_name,nrPESEL)   # Tworzy Osobe
                self.ListaOsb.append(osb)          # i dodaje do Listy
                print('Dodano now� Osob� do listy')
        else:
            print("\nNieporawny nr. PESEL\n")


    @classmethod
    def spr_PESEL(cls, nrPESEL, Imie):  # Sprawdza czy pesel jest poprawny (funkcja)
        PESELx = nrPESEL
        if (not len(PESELx) == 11):
            print(f"B��dna d�. PESELu:{PESELx}!!\n")
            return False
        elif (not cls.PESEL_miesiac_i_stulecie(PESELx)):  # Wywo�uje funkcje do sprawdzeniea peselu
            print("B��dny nr. Miesi�ca i stulecia!!\n")
            return False
        elif(not cls.Spr_plec(PESELx, Imie)):
            print("B��dny nr. p�ci!!")
            return False
        elif(not cls.spr_nr_kontrolny(PESELx)):
            print("B��dny nr. Kontrolny PESELu!!")
            return False
        elif(not cls.spr_czy_urodzony(PESELx)):
            print("Ta osoba si� jeszcze nie urodzi�a!!")
            return False
        else:
            return True  

    @classmethod
    def PESEL_miesiac_i_stulecie(cls, PESELx):  # Sprawdza czy miesi�c i stulecie s� poprawne Zwraca False w przypadku b��du
        miesiac = int(PESELx[2] + PESELx[3])
        if (miesiac > 92 or miesiac < 81) and (miesiac > 32 or miesiac < 21) and (miesiac > 12 or miesiac < 1):
            return False
        else:
            return True

    @classmethod
    def Spr_plec(cls, PESELx, Imie):
        if (Imie.lower()[-1] == 'a' and int(PESELx[-2])%2==0):
            return True
        elif (not (Imie.lower()[-1] == 'a') and int(PESELx[-2]) % 2== 1):
            return True
        else:
            return False

    @classmethod
    def spr_czy_urodzony(cls,PESELx):
        Data_dzis=datetime.now()
        if(int(PESELx[2:4])>20 and int(PESELx[2:4])<33 and (int(PESELx[0:2])>(Data_dzis.year%100) or (int(PESELx[0:2])==(Data_dzis.year%100)  and int(PESELx[2:4])-20>Data_dzis.month) or (int(PESELx[0:2])==(Data_dzis.year%100)  and int(PESELx[2:4])-20==Data_dzis.month and int(PESELx[4:6])>Data_dzis.day))):
            return False
        else:
            return True

    @classmethod
    def spr_nr_kontrolny(cls, PESELx):
        wynik = 0
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        for i, x in zip(PESELx[0:10], wagi):
            temp = (int(i) * x)
            wynik += (temp % 10)
        if (int(PESELx[-1]) == 10-(wynik % 10)):
            return True
        else:
            return False


    @classmethod
    def is_PESEL_in_List(cls,nrPESEL):   # metoda klasy do spr. czy dany pesel jest w li�cie
        for Osb in cls.ListaOsb:
            if (Osb.nrPESEL == nrPESEL):
                return True
        else:
            return False

    @classmethod              # Wy�wietla Liste
    def print_List(cls):
        print(*cls.ListaOsb,sep='\n',end='\n')

    @classmethod
    def Save_List(cls):  # Zapisuje liste do pliku
        nazwa_pliku_to_data=datetime.now().strftime('%d.%m.%y %Hh %Mm %Ss')
        nazwa_pliku_to_data+='.txt'
        file = open(nazwa_pliku_to_data,'w')
        for item in cls.ListaOsb:
            file.write(str(item))

        file.close()



##############################################################################
############################### Klasa Osoba ##################################
##############################################################################



class Osoba:
    def __init__(self,city,name,last_name,nrPESEL):  # Inicjalizuje Osobe
        self.city=city
        self.name=name
        self.last_name=last_name
        self.__nrPESEL=nrPESEL

    @property
    def nrPESEL(self):
        return self.__nrPESEL  # Zwraca Pesel

    def change_name(self, name):
        self.name = name    # Zmienia Imie

    def change_last_name(self, last_name):
        self.last_name = last_name    # Zmieenia nazwisko

    def change_city(self,city):
        self.city=city       #Zmienia miasto

    @nrPESEL.setter
    def nrPESEL(self,nrPESEL):   # Zmieenia PESELU
        self.__nrPESEL=nrPESEL

    def __str__(self):
        return (f'{self.city} {self.name} {self.last_name} {str(self.nrPESEL)}\n')

    def __repr__(self):        # metoda potrzebna do listy w przeciwnym
        return self.__str__()  # wypadku nie zadzia�a print na obiektach
        # w li�cie bo lista ko�ysta z __repr__ a nie __str__
