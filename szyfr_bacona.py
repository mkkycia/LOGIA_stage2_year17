from turtle import *


def zamiana(litera):
    wiki_slownik = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb',
                    'E':'aabaa', 'F':'aabab', 'G':'aabba', 'H':'aabbb',
                    'I':'abaaa', 'J':'abaaa', 'K':'abaab', 'L':'ababa',
                    'M':'ababb', 'N':'abbaa', 'O':'abbab', 'P':'abbba',
                    'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba',
                    'U':'baabb', 'V':'baabb', 'W':'babaa', 'X':'babab',
                    'Y':'babba', 'Z':'babbb'}
    return wiki_slownik[litera]

def kwadrat(a, kolor):
    color('black', kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    lt(90)
    fd(a)
    rt(90)

def szyfruj(slowo):
    if len(slowo)<8:
        a = 400/5
    else:
        a = 700/len(slowo)
    speed(0)
    pu()
    bk(350)
    lt(90)
    bk(2.5*a)
    rt(90)
    pd()
    for i in range(len(slowo)):
        for j in zamiana(slowo[i]):
            if j == 'a':
                kwadrat(a, 'yellow')
            else:
                kwadrat(a, 'blue')
        fd(a)
        rt(90)
        fd(5*a)
        lt(90)

szyfruj('GODZJD')
