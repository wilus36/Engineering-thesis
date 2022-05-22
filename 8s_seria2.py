#Przejścia 1-3, seria 2, łańcuch X8

from matplotlib import pylab #import modułu pylab z biblioteki matplotlib
import math
        

pylab.rcParams['font.family']='Arial'     #określenie czcionki - arial zawiera polskie znaki

alfa=math.radians(0.5)
sinalfa=math.sin(alfa)
cosalfa=math.cos(alfa)
tanalfa=math.tan(alfa)

beta=2*3.14159265359-alfa
sinbeta=math.sin(beta)
cosbeta=math.cos(beta)
tanbeta=math.tan(beta)

plik1='X8-1-2'                            #określenie wybranej grupy danych
plik1nazwa=plik1+'.txt'                   #zapisanie nazwy grupy danych z rozszerzeniem .txt jako zmiennej
z1=pylab.loadtxt(plik1nazwa)              #wczytanie pliku i utworzenie macierzy

stop1=(2048+sinalfa*2000)
skok1=(stop1-2048)/2000
k1=pylab.arange(2048,stop1,skok1)       ####TO JEST PRÓBA KOREKTY POZIOMU BAZOWEGO, ALE NIC NIE DAJE macierz co schodzi w dół zgodnie z kątem przeckoszenia


z1=(z1-k1)*(500/k1)+2.3               #wyrównanie wykresu do 0 i kompensacja błędu kalibracji profilografu    K1=2048 dla 1, 2047 dla 2 itd.
ni1=z1.size                               #odczyt rozmiaru macierzy
i1=pylab.arange(ni1)*(4/ni1)*1000         #ustawienie zakresu pomiaru

z1p=(i1*sinbeta+z1*cosbeta)       #TO JEST SAM OBRÓT WYKRESU WZGLĘDEM PUNKTU 0,0, ALE TEŻ NIE DZIAŁA XD9
i1p=(i1*cosbeta-z1*sinbeta)

pylab.plot(i1p,z1p,color='r',label=plik1)   #utworzenie wykresu
          
plik2='X8-2-2'
plik2nazwa=plik2+'.txt'
z2=pylab.loadtxt(plik2nazwa)
z2=(z2-2048)*(500/2048)+1
ni2=z2.size
i2=pylab.arange(ni2)*(4/ni2)*1000
pylab.plot(i2,z2,color='b',label=plik2)

plik3='X8-3-2'
plik3nazwa=plik3+'.txt'
z3=pylab.loadtxt(plik3nazwa)
z3=(z3-2048)*(500/2048)+16.3
ni3=z3.size
i3=pylab.arange(ni3)*(4/ni3)*1000
pylab.plot(i3,z3,color='g',label=plik3)

pylab.grid()                                                           #dodanie siatki
pylab.title(u'Łańcuch 8-rzędowy, seria 2',size='large')                #dodanie tytułu wykresu
pylab.xlabel(u'Odcinek pomiaru [µm]')                                  #tytuł osi x
pylab.ylabel(u'Uskok [µm]')                                            #tytuł osi y
pylab.legend([plik1, plik2, plik3],title=u'Pomiar',loc='lower right')  #dodanie legendy

pylab.show()                                                           #wywołanie interfejsu matplotlib z wykresem