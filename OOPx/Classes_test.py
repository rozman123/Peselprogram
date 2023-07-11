#-*- coding: latin-1 -*-

from multiprocessing.context import assert_spawning
import pytest
import Classes as c

def test_spr_PESEL():
    try:
        file=open('t_pesele.txt',"r")
        for linia in file.read().split('\n'):
            nr,imie,wynik=linia.split(' ')
            wynik_funkcji=str(c.UI.spr_PESEL(nr,imie))
            assert wynik == wynik_funkcji
    except(AssertionError):
        print(f'Wartoœci: {nr}, {imie}. Expected: {wynik} got {wynik_funkcji}')
        raise AssertionError



def test_Constructor_Osoba1():
    person1=c.Osoba("Poznañ","Gabriel","Nowak",66072959855)
    assert person1.city=="Poznañ"
    assert person1.name=="Gabriel"
    assert person1.last_name=="Nowak"
    assert person1.nrPESEL==66072959855


def test_Constructor_Osoba2():
    person2=c.Osoba("Warszawa","Anastazja","B³ugaszyk",57030668968)
    assert person2.city=="Warszawa"
    assert person2.name=="Anastazja"
    assert person2.last_name=="B³ugaszyk"
    assert person2.nrPESEL==57030668968


person3=c.Osoba("X","Agnieszka","X",69061282262)
person4=c.Osoba("X","Jan","X",58091884157)

def test_change_name():
    person3.name = "Joanna" 
    person4.name = "Marlena" 
    assert person3.name == "Joanna" 
    assert person4.name == "Marlena" 
    
def test_change_last_name():
    person3.last_name = "Adamiec" 
    person4.last_name = "Roszak" 
    assert person3.last_name == "Adamiec" 
    assert person4.last_name == "Roszak" 

def test_change_city():
    person3.city = "Poznañ" 
    person4.city = "Kraków" 
    assert person3.city == "Poznañ" 
    assert person4.city == "Kraków"    

def test_nrPESEL():  
    person3.__nrPESEL = 84120279368
    person4.__nrPESEL = 55111775817