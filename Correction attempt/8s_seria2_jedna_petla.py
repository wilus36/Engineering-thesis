
from cmath import sqrt
from matplotlib import pylab #import modułu pylab z biblioteki matplotlib
import math
import numpy
        

pylab.rcParams['font.family']='Arial'     #określenie czcionki - arial zawiera polskie znaki

alfa=math.radians(0.56)                    #kąt przechylenia błędnie skalibrowanej osi, względem poprawnej
sinalfa=math.sin(alfa)                     #wartości funkcji trygonometrycznych w/w kąta do wykorzystania później
cosalfa=math.cos(alfa)
tanalfa=math.tan(alfa)

plik1='X8-1-2'                            #określenie wybranej grupy danych
plik1nazwa=plik1+'.txt'                   #zapisanie nazwy grupy danych z rozszerzeniem .txt jako zmiennej
yp=pylab.loadtxt(plik1nazwa).astype(int)              #wczytanie wartości Y punktów pomiarowych z pliku
xp=pylab.arange(yp.size)                  #ustalenie wartości X punktów po kolei, 1,2,3,.. do 2000 i utowrzenie ciągu

wys_bazy=2048                             #wysokość bazowego poziomu odniesienia

y1=[wys_bazy]*2000                                    #to jest teraz ciąg o długości 2000 i stałej wartości 2048 - poprawna pozioma linia odniesienia
y2=(math.tan(math.radians(360)-alfa))*xp+wys_bazy     #to też w takiej konfiguracji - przekoszona linia odniesienia pochylona o kąt alfa

xpk=xp                                           #ciąg od 0 do 1999, czyli 2000 punktów po osi OX - zmienne, które potem będa zawierać skorygowane wartości X punktów
ypk=yp                                           #na razie wartości Y punktów pomiarowych bez zmian - zmienne, które potem będa zawierać skorygowane wartości Y punktów

##### trzeba zrobić pętlę, żeby każdy kolejny punkt o współrzednych XP,YP w kolejności zgodnej z XP był sprawdzany pod kątem poniższych warunków 
##### i odpowiednio korygowany do współrzednych XPK YPK

for i in range(2000): #może zamiast range dać numpy.nditer()?
    xpi=xp[i]                                  #i-te elementy poszczególnych ciągów
    ypi=yp[i]
    xpki=xpk[i]
    ypki=ypk[i]
    y1i=[i]
    y2i=[i]
#warianty do korekty zgodnie z rysunkami
    if ypi > y1i and ypi > y2i:           #punkt pomiarowy nad osią poprawną i niepoprawną
        xpki=(xpi/cosalfa)+(xpi-xpi*tanalfa)*sinalfa
        ypki=(ypi-xpi*tanalfa)

    elif ypi < y1i and ypi > y2i:                      #punkt poiarowy między osiami
        xpki=(sqrt(xpi^2+ypi^2))*math.cos(alfa-math.atan(ypi/xpi))
        ypki=(sqrt(xpi^2+ypi^2))*math.sin(alfa-math.atan(ypi/xpi))

    elif ypi < y1i and ypi < y2i:                      #punkt pomiarowy poniżej obu osi
        xpki=(sqrt(xpi^2+ypi^2))*math.cos(alfa+math.atan(ypi/xpi))
        ypki=(sqrt(xpi^2+ypi^2))*math.sin(alfa+math.atan(ypi/xpi))

    elif ypi == y1i:                                 #punkt na osi poprawnej
        xpki=xpi/cosalfa

    elif ypi == y2i:                                 #punkt na osi niepoprawnej
        xpki=xpi*cosalfa
        ypki=xpi*sinalfa

    else:
        ypki=ypi
        xpki=xpi

##### po uzyskaniu poprawnego przebiegu należy go przesunąć do odpowiednego miejsca na wykresie,
##### więc wszystko jest najpierw w układzie współrzędnych opartych na bitach (OX od 0 do 2000 i OY od 0 do 4096),
##### a dopiero potem powinno być zmienione na układ współrzędnych z osiami w mikrometrach (OX od 0 do 4000 i OY od -500 do +500)
##### po prostu przez przesunięca wartości zmiennych np. o -2048

                               
pylab.plot(xpk,ypk, color='y',label='Skorygowany')     #wykres skorygowany - żółty

plik2='X8-1-2'                                 #wykres do porównania dla testowania skryptu - niebieski
plik2nazwa=plik2+'.txt'
z2=pylab.loadtxt(plik2nazwa)
z2=z2
ni2=z2.size
i2=pylab.arange(ni2)
pylab.plot(i2,z2,color='b',label='Bez zmian') #utworzenie wykresu              

pylab.plot(xp,y1,color='g',label='Oś poprawna')                    #rysowanie osi bazowych poprawna zielona, niepoprawna czerwona
pylab.plot(xp,y2,color='r',label='Oś niepoprawna')

pylab.grid()                                                           #dodanie siatki
pylab.title(u'Łańcuch 8-rzędowy, seria 2',size='large')                #dodanie tytułu wykresu
pylab.xlabel(u'Odcinek pomiaru [µm]')                                  #tytuł osi x
pylab.ylabel(u'Uskok [µm]') 
pylab.legend(title=u'Pomiar',loc='upper left')
pylab.show()