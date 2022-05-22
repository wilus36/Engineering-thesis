#Pin z nowego łańcucha X8 - grupa kontrolna

from matplotlib import pylab               #import modułu pylab z biblioteki matplotlib

pylab.rcParams['font.family']='Arial'      #określenie czcionki - arial zawiera polskie znaki

plik1='KONTROL'                            #określenie wybranej grupy danych
plik1nazwa=plik1+'.txt'                    #zapisanie nazwy grupy danych z rozszerzeniem .txt jako zmiennej
z1=pylab.loadtxt(plik1nazwa)               #wczytanie pliku i utworzenie maceirzy
z1=(z1-2048)*(500/2048)-6.3                #wyrównanie wykresu do 0 i kompensacja błędu kalibracji profilografu
ni1=z1.size                                #odczyt rozmiaru macierzy
i1=pylab.arange(ni1)*(4/ni1)*1000          #ustawienie zakresu pomiaru
pylab.plot(i1,z1,color='b',label=plik1)    #utworzenie wykresu
          
pylab.grid()                                                           #dodanie siatki
pylab.title(u'Pomiar kontrolny',size='large')                          #dodanie tytułu wykresu
pylab.xlabel(u'Odcinek pomiaru [µm]')                                  #tytuł osi x
pylab.ylabel(u'Uskok [µm]')                                            #tytuł osi y

pylab.show()                                                           #wywołanie interfejsu matplotlib z wykresem