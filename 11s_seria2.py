#Przejścia 1-3, seria 2, łańcuch X11

from matplotlib import pylab              #import modułu pylab z biblioteki matplotlib

pylab.rcParams['font.family']='Arial'     #określenie czcionki - arial zawiera polskie znaki

plik1='X11-1-2'                           #określenie wybranej grupy danych
plik1nazwa=plik1+'.txt'                   #zapisanie nazwy grupy danych z rozszerzeniem .txt jako zmiennej
z1=pylab.loadtxt(plik1nazwa)              #wczytanie pliku i utworzenie maceirzy
z1=(z1-2048)*(500/2048)+4                 #wyrównanie wykresu do 0 i kompensacja błędu kalibracji profilografu
ni1=z1.size                               #odczyt rozmiaru macierzy
i1=pylab.arange(ni1)*(4/ni1)*1000         #ustawienie zakresu pomiaru
pylab.plot(i1,z1,color='r',label=plik1)   #utworzenie wykresu
          
plik2='X11-2-2'
plik2nazwa=plik2+'.txt'
z2=pylab.loadtxt(plik2nazwa)
z2=(z2-2048)*(500/2048) 
ni2=z2.size
i2=pylab.arange(ni2)*(4/ni2)*1000
pylab.plot(i2,z2,color='b',label=plik2)

plik3='X11-3-2'
plik3nazwa=plik3+'.txt'
z3=pylab.loadtxt(plik3nazwa)
z3=(z3-2048)*(500/2048)+1.8
ni3=z3.size
i3=pylab.arange(ni3)*(4/ni3)*1000
pylab.plot(i3,z3,color='g',label=plik3)
 
pylab.grid()                                                           #dodanie siatki
pylab.title(u'Łańcuch 11-rzędowy, seria 2',size='large')               #dodanie tytułu wykresu
pylab.xlabel(u'Odcinek pomiaru [µm]')                                  #tytuł osi x
pylab.ylabel(u'Uskok [µm]')                                            #tytuł osi y
pylab.legend([plik1, plik2, plik3],title=u'Pomiar',loc='lower right')  #dodanie legendy

pylab.show()                                                           #wywołanie interfejsu matplotlib z wykresem