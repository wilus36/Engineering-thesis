
from cmath import sqrt
from copy import deepcopy
from matplotlib import pylab #import modułu pylab z biblioteki matplotlib
import math
import logging
import numpy
        
logging.getLogger().setLevel(logging.INFO)


pylab.rcParams['font.family']='Arial'     #określenie czcionki - arial zawiera polskie znaki

alfa=math.radians(0.56)                    #kąt przechylenia błędnie skalibrowanej osi, względem poprawnej
sinalfa=math.sin(alfa)                     #wartości funkcji trygonometrycznych w/w kąta do wykorzystania później
cosalfa=math.cos(alfa)
tanalfa=math.tan(alfa)

plik1='X8-1-2'                            #określenie wybranej grupy danych
plik1nazwa=plik1+'.txt'                   #zapisanie nazwy grupy danych z rozszerzeniem .txt jako zmiennej
yp=pylab.loadtxt(plik1nazwa).astype(int)  #wczytanie wartości Y punktów pomiarowych z pliku, 
##### .astype(int) ustala go jako szereg int - nditer w pętli nie wywala wtedy błędu
##### ale on nie może zostać jako szereg całkowitych, bo po korekcie będą wartości z liczbami po przecinku

xp=pylab.arange(yp.size)                  #ustalenie wartości X punktów po kolei, 0,1,2,3,.. do 1999 i utowrzenie ciągu
                                        #wysokość bazowego poziomu odniesienia
reference_point=2048                                    #to jest teraz ciąg o długości 2000 i stałej wartości 2048 - poprawna pozioma linia odniesienia
y2=(math.tan(math.radians(360)-alfa))*xp+reference_point     #to też w takiej konfiguracji - przekoszona linia odniesienia pochylona o kąt alfa

# dgaf about contents, only amount of elements matters
xpk=deepcopy(xp)                                          #szereg od 0 do 1999, czyli 2000 punktów po osi OX - szereg zmiennych, który potem będzie zawierać skorygowane wartości X punktów
ypk=deepcopy(yp)                                          #na razie wartości Y punktów pomiarowych bez zmian - szereg zmiennych, który potem będzie zawierać skorygowane wartości Y punktów
#xpk=pylab.arange(xpk.size)*(4/xpk.size)*1000
##### trzeba zrobić pętlę, żeby każdy kolejny punkt o współrzednych XP,YP w kolejności zgodnej z XP był sprawdzany pod kątem poniższych warunków 
##### i odpowiednio korygowany do współrzednych XPK YPK

#### dwie pętle osobne na szeregi YP i XP

LOOP_0_CONDITION_0 = 'Loop 0, Condition 0'
LOOP_0_CONDITION_1 = 'Loop 0, Condition 1'
LOOP_0_CONDITION_2 = 'Loop 0, Condition 2'
LOOP_0_CONDITION_3 = 'Loop 0, Condition 3'
LOOP_0_CONDITION_4 = 'Loop 0, Condition 4'
LOOP_1_CONDITION_0 = 'Loop 1, Condition 0'
LOOP_1_CONDITION_1 = 'Loop 1, Condition 1'
LOOP_1_CONDITION_2 = 'Loop 1, Condition 2'
LOOP_1_CONDITION_3 = 'Loop 1, Condition 3'
LOOP_1_CONDITION_4 = 'Loop 1, Condition 4'

debug_shit = {
    LOOP_0_CONDITION_0: 0,
    LOOP_0_CONDITION_1: 0,
    LOOP_0_CONDITION_2: 0,
    LOOP_0_CONDITION_3: 0,
    LOOP_0_CONDITION_4: 0,
    LOOP_1_CONDITION_0: 0,
    LOOP_1_CONDITION_1: 0,
    LOOP_1_CONDITION_2: 0,
    LOOP_1_CONDITION_3: 0,
    LOOP_1_CONDITION_4: 0
}

for i in range(2000):
    xpi=xp[i]                                  #i-te elementy poszczególnych szeregów
    ypi=yp[i]
    xpki=xpk[i]
    #ypki=ypk[i]
    y1i=reference_point
    y2i=y2[i]
 #warianty do korekty zgodnie z rysunkami
    if ypi > y1i and ypi > y2i:           #punkt pomiarowy nad osią poprawną i niepoprawną
        xpki=(xpi/cosalfa)+(xpi-xpi*tanalfa)*sinalfa
        debug_shit[LOOP_0_CONDITION_0] += 1
    elif ypi < y1i and ypi > y2i:                      #punkt poiarowy między osiami
        xpki=(sqrt(xpi^2+ypi^2))*math.cos(alfa-math.atan(ypi/xpi))
        debug_shit[LOOP_0_CONDITION_1] += 1
    elif ypi < y1i and ypi < y2i:                      #punkt pomiarowy poniżej obu osi
        xpki=(sqrt(xpi^2+ypi^2))*math.cos(alfa+math.atan(ypi/xpi))
        debug_shit[LOOP_0_CONDITION_2] += 1
    elif ypi == y1i:                                 #punkt na osi poprawnej
        xpki=xpi/cosalfa
        debug_shit[LOOP_0_CONDITION_3] += 1
    elif ypi == y2i:                                 #punkt na osi niepoprawnej
        xpki=xpi*cosalfa
        debug_shit[LOOP_0_CONDITION_4] += 1
    else:
        raise("chuj")
        
for j in range(2000):
    xpj=xp[j]                                 #j-te elementy poszczególnych szeregów
    ypj=yp[j]
    #xpkj=xpk[j]
    ypkj=ypk[j]
    y1j=reference_point
    y2j=y2[j]
 #warianty do korekty zgodnie z rysunkami
    if ypj > y1j and ypj > y2j:           #punkt pomiarowy nad osią poprawną i niepoprawną
        ypkj=(ypj-xpj*tanalfa)
        debug_shit[LOOP_1_CONDITION_0] += 1
    elif ypj < y1j and ypj > y2j:                      #punkt poiarowy między osiami
        ypkj=(sqrt(xpj^2+ypj^2))*math.sin(alfa-math.atan(ypj/xpj))
        debug_shit[LOOP_1_CONDITION_1] += 1
    elif ypj < y1j and ypj < y2j:                      #punkt pomiarowy poniżej obu osi
        ypkj=(sqrt(xpj^2+ypj^2))*math.sin(alfa+math.atan(ypj/xpj))
        debug_shit[LOOP_1_CONDITION_2] += 1
    elif ypj == y2j:                                 #punkt na osi niepoprawnej
        ypkj=xpj*sinalfa
        debug_shit[LOOP_1_CONDITION_3] += 1
    else:
        ypkj=ypj
        debug_shit[LOOP_1_CONDITION_4] += 1


##### po uzyskaniu poprawnego przebiegu należy go przesunąć do odpowiednego miejsca na wykresie,
##### więc wszystko jest najpierw w układzie współrzędnych opartych na bitach (OX od 0 do 2000 i OY od 0 do 4096),
##### a dopiero potem powinno być zmienione na układ współrzędnych z osiami w mikrometrach (OX od 0 do 4000 i OY od -500 do +500)
##### po prostu przez przesunięca wartości zmiennych np. o -2048

for ele in debug_shit:
    logging.info(f'{ele}: {debug_shit[ele]}')


x_for_xpk = pylab.arange(xpk.size)*(4/xpk.size)*1000                           
pylab.plot(x_for_xpk,ypk, color='y',label='Skorygowany')     #wykres skorygowany - żółty

plik2='X8-1-2'                                 #wykres do porównania dla testowania skryptu - niebieski
plik2nazwa=plik2+'.txt'
not_changed=pylab.loadtxt(plik2nazwa)
not_changed_size=not_changed.size
not_changed_arranged_x=pylab.arange(not_changed_size)*(4/not_changed_size)*1000
pylab.plot(not_changed_arranged_x,not_changed,color='b',label='Bez zmian') #utworzenie wykresu              

y_reference = [2048 for i in range(2000)]
x_for_xp = pylab.arange(xp.size)*(4/xp.size)*1000
pylab.plot(x_for_xp,y_reference,color='g',label='Oś poprawna')                    #rysowanie osi bazowych poprawna zielona, niepoprawna czerwona
pylab.plot(x_for_xp,y2,color='r',label='Oś niepoprawna')

pylab.grid()                                                           #dodanie siatki
pylab.title(u'Łańcuch 8-rzędowy, seria 2',size='large')                #dodanie tytułu wykresu
pylab.xlabel(u'Odcinek pomiaru [µm]')                                  #tytuł osi x
pylab.ylabel(u'Uskok [µm]') 
pylab.legend(title=u'Pomiar',loc='upper left')
pylab.show()