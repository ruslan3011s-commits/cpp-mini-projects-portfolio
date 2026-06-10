def wypis(t):
    for i in range(8):
        for j in range(8):
            print(t[i][j], end=" ")
        print()

def czyzbil(t,fig1,fig2,gdz1,gdz2):
    if t[fig1][fig2]=='W' or t[fig1][fig2]=='w':
        if fig1 != gdz1 and fig2 != gdz2:
            return False
        if fig1==gdz1:
            step = 1 if gdz2>fig2 else -1
            for i in range(fig2+step,gdz2,step):
                if t[fig1][i]!='.':
                    return False
        if fig2 == gdz2:
            step = 1 if gdz1>fig1 else -1
            for i in range(fig1+step,gdz1,step):
                if t[i][fig2]!='.':
                    return False
        return True
    elif t[fig1][fig2]=='G' or t[fig1][fig2]=='g':
        dx = abs(gdz1 - fig1)
        dy = abs(gdz2 - fig2)
        if dx != dy:
            return False
        if fig1>gdz1:
            if fig2<gdz2:
                step = 1
            else:
                step=-1
            st = fig1
            for i in range(fig2+step,gdz2,step):
                st-=1
                if t[st][i] != '.':
                    return False
        if fig1<gdz1:
            if fig2<gdz2:
                step = 1
            else:
                step=-1
            st = fig1
            for i in range(fig2+step,gdz2,step):
                st+=1
                if t[st][i] != '.':
                    return False
        return True
    elif t[fig1][fig2]=='H' or t[fig1][fig2]=='h':
        if fig1==gdz1:
            step = 1 if gdz2>fig2 else -1
            for i in range(fig2+step,gdz2,step):
                if t[fig1][i]!='.':
                    return False
        if fig2 == gdz2:
            step = 1 if gdz1>fig1 else -1
            for i in range(fig1+step,gdz1,step):
                if t[i][fig2]!='.':
                    return False
        if fig1>gdz1:
            if fig2<gdz2:
                step = 1
            else:
                step=-1
            st = fig1
            for i in range(fig2+step,gdz2,step):
                st-=1
                if t[st][i] != '.':
                    return False
        if fig1<gdz1:
            if fig2<gdz2:
                step = 1
            else:
                step=-1
            st = fig1
            for i in range(fig2+step,gdz2,step):
                st+=1
                if t[st][i] != '.':
                    return False
        return True
    return False

def ruch(t,fig1,fig2,gdz1,gdz2):
    if t[fig1][fig2]=='P':
        dx = gdz1 - fig1
        dy = gdz2 - fig2
        if (dx==-1 and dy==0 and t[gdz1][gdz2] == '.') or (fig1==6 and dx==-2 and dy==0 and t[gdz1][gdz2] == '.' and t[fig1-1][fig2]=='.') or (t[gdz1][gdz2] != '.' and dx==-1 and abs(dy)==1):
            return True
    elif t[fig1][fig2]=='p':
        dx = gdz1 - fig1
        dy = gdz2 - fig2
        if (dx==1 and dy==0 and t[gdz1][gdz2] == '.') or (fig1==1 and dx==2 and dy==0 and t[gdz1][gdz2] == '.' and t[fig1+1][fig2]=='.') or (t[gdz1][gdz2] != '.' and dx==1 and abs(dy)==1):
            return True
    elif t[fig1][fig2]=='W' or t[fig1][fig2]=='w':
        dx = abs(gdz1 - fig1)
        dy = abs(gdz2 - fig2)
        if dx==0 or dy==0:
            return True
    elif t[fig1][fig2]=='S' or t[fig1][fig2]=='s':
        dx = abs(gdz1 - fig1)
        dy = abs(gdz2 - fig2)
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True
    elif t[fig1][fig2] == 'G' or t[fig1][fig2] == 'g':
        dx = abs(gdz1 - fig1)
        dy = abs(gdz2 - fig2)
        if dx == dy:
            return True
    elif t[fig1][fig2]=='H' or t[fig1][fig2]=='h':
        dx = abs(gdz1 - fig1)
        dy = abs(gdz2 - fig2)
        if dx==0 or dy==0 or dx==dy:
            return True
    elif t[fig1][fig2]=='K' or t[fig1][fig2]=='k':
        dx = abs(gdz1-fig1)
        dy = abs(gdz2-fig2)
        if (dx != 0 or dy != 0) and dx <= 1 and dy <= 1:
            return True
    return False

def szach(t,ky,kx,kolor):
    if kolor == 'bialy':
        przedzial = ['p','w','s','g','h','k']   #przegrada przeciwnika
        s = 'S'
        g = 'G'
        w = 'W'    #figury ktore daja szach
        h = 'H'
        p = 'P'
    else:
        przedzial = ['P','W','S','G','H','K']
        s = 's'
        g = 'g'
        w = 'w'
        h = 'h'
        p = 'p'
    #Skoczek!:  ggg
    if kx > 0 and ky > 1:
        if t[ky-2][kx-1] == s:
            return True
    if ky > 1 and kx < 7:
        if t[ky-2][kx+1] == s:
            return True
    if kx > 0 and ky < 6:
        if t[ky+2][kx-1] == s:
            return True
    if ky < 6 and kx < 7:
        if t[ky+2][kx+1] == s:
            return True
    if ky > 0 and kx > 1:
        if t[ky-1][kx-2] == s:
            return True
    if ky > 0 and kx < 6:
        if t[ky-1][kx+2] == s:
            return True
    if ky < 7 and kx < 6:
        if t[ky+1][kx+2] == s:
            return True
    if ky < 7 and kx > 1:
        if t[ky+1][kx-2] == s:
            return True
    #Goniec!:    ggg
    #lewa gora
    if ky!=0 and kx!=0:
        step = ky if ky<=kx else kx
        for i in range(1,step+1):
            if t[ky-i][kx-i] in przedzial:
                break
            if t[ky-i][kx-i] == g or t[ky-i][kx-i] == h:
                return True
    #prawa gora
    if kx!=7 and ky!=0:
        pg = 7-kx
        step = pg if pg<=ky else ky
        for i in range(1,step+1):
            if t[ky-i][kx+i] in przedzial:
                break
            if t[ky-i][kx+i] == g or t[ky-i][kx+i] == h:
                return True
    #lewy dol
    if ky!=7 and kx!=0:
        ld = 7-ky
        step = ld if ld<=kx else kx
        for i in range(1,step+1):
            if t[ky+i][kx-i] in przedzial:
                break
            if t[ky+i][kx-i] == g or t[ky+i][kx-i] == h:
                return True
    #prawy dol
    if ky!=7 and kx!=7:
        step = pg if pg<=ld else ld
        for i in range(1,step+1):
            if t[ky+i][kx+i] in przedzial:
                break
            if t[ky+i][kx+i] == g or t[ky+i][kx+i] == h:
                return True
    #Wierz!:   ggg
    #gora
    if ky != 0:
        for i in range(1,ky+1):
            if t[ky-i][kx] in przedzial:
                break
            if t[ky-i][kx] == w or t[ky-i][kx] == h:
                return True
    #dol
    if ky != 7:
        d=7-ky
        for i in range(1,d+1):
            if t[ky+i][kx] in przedzial:
                break
            if t[ky+i][kx] == w or t[ky+i][kx] == h:
                return True
    #lewo
    if kx != 0:
        for i in range(1,kx+1):
            if t[ky][kx-i] in przedzial:
                break
            if t[ky][kx-i] == w or t[ky][kx-i] == h:
                return True
    #prawo
    if kx !=7:
        p = 7-kx
        for i in range(1,p+1):
            if t[ky][kx+i] in przedzial:
                break
            if t[ky][kx+i] == w or t[ky][kx+i] == h:
                return True
    #pionek
    if kolor == 'bialy':
        if kx != 0 and ky != 7:
            if t[ky+1][kx-1] == 'P':
                return True
        if ky != 7 and kx != 7:
            if t[ky+1][kx+1] == 'P':
                return True
    else:
        if ky != 0 and kx != 0:
            if t[ky-1][kx-1] == 'p':
                return True
        if ky != 0 and kx != 7:
            if t[ky-1][kx+1] == 'p':
                return True
    return False

def mat(t,ky,kx,kolor):
    if kolor == 'bialy':
        kol = 'czarny'
    else:
        kol = 'bialy'
    if szach(t,ky,kx,kolor):
        if ky !=0  and kx != 0 and t[ky-1][kx-1]=='.':
            if szach(t,ky-1,kx-1,kolor) == False and szach(t,ky-1,kx-1,kol) == False:
                return False
        if ky != 7 and kx != 7 and t[ky+1][kx+1]=='.':
            if szach(t,ky+1,kx+1,kolor) == False and szach(t,ky+1,kx+1,kol) == False:
                return False
        if ky != 0 and t[ky-1][kx]=='.':
            if szach(t,ky-1,kx,kolor) == False and szach(t,ky-1,kx,kol) == False:
                return False
        if ky != 7 and t[ky+1][kx]=='.':
            if szach(t,ky+1,kx,kolor) == False and szach(t,ky+1,kx,kol) == False:
                return False
        if kx != 7 and t[ky][kx+1]=='.':
            if szach(t,ky,kx+1,kolor) == False and szach(t,ky,kx+1,kol) == False:
                return False
        if ky != 0 and t[ky][kx-1]=='.':
            if szach(t,ky,kx-1,kolor) == False and szach(t,ky,kx-1,kol) == False:
                return False
        if ky != 7 and kx != 0 and t[ky+1][kx-1]=='.':
            if szach(t,ky+1,kx-1,kolor) == False and szach(t,ky+1,kx-1,kol) == False:
                return False
        if ky != 0 and kx != 7 and t[ky-1][kx+1]=='.':
            if szach(t,ky-1,kx+1,kolor) == False and szach(t,ky-1,kx+1,kol) == False:
                return False
        return True
    return False

t = [
    ['w','s','g','h','k','g','s','w'],
    ['p','p','p','p','p','p','p','p'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['P','P','P','P','P','P','P','P'],
    ['W','S','G','H','K','G','S','W']
]

dt = [
    ['1','2','3','4','5','6','7','8'],
    ['9','10','11','12','13','14','15','16'],
    ['17','18','19','20','21','22','23','24'],
    ['25','26','27','28','29','30','31','32'],
    ['33','34','35','36','37','38','39','40'],
    ['41','42','43','44','45','46','47','48'],
    ['49','50','51','52','53','54','55','56'],
    ['57','58','59','60','61','62','63','64']
]

print("Pomocnicze liczby, te liczby oznaczaja miejsce kazdej figury: ")
wypis(dt)
print("\nPlansza: ")
wypis(t)
gra = True
while gra:
    print("Graja biali!")
    e = input("Potrzebujesz pomocnicza tablica? tak/nie: ")
    print()
    if e == 'tak':
        wypis(dt)
    print()
    x = input("Wprowadz numer figury ktora chcesz posunac: ")
    n = input("Wprowadz numer pola gdzie chcesz posunac ta figure: ")
    zlen = False
    zlex=False
    czarni=False
    for i in range(8):
        for j in range(8):
            if zlen == False:
                if n==dt[i][j]:
                    gdz1=i
                    gdz2=j
                    zlen=True
            if zlex==False:
                if x==dt[i][j]:
                    fig1=i
                    fig2=j
                    zlex=True
    if zlen==False or zlex==False:
        print("Zly ruch, zrob inny!")
        continue
    elif ruch(t, fig1,fig2,gdz1,gdz2)==True and t[fig1][fig2] in ['P','W','S','G','H','K']:
        if t[fig1][fig2] in ['W','G','H']:
            if czyzbil(t,fig1,fig2,gdz1,gdz2)==False:
                print("Zly ruch, zrob inny!")
                continue
        if t[gdz1][gdz2] not in ['P','W','S','G','H','K']:
            if t[gdz1][gdz2] in ['p','w','s','g','h']:
                print("Zbito figure przeciwnika!")
            kolor = 'czarny'
            if szach(t,gdz1,gdz2,kolor):
                print("Zly ruch, zrob inny!")
                continue
            t[gdz1][gdz2]=t[fig1][fig2]
            t[fig1][fig2]='.'
            #Gdzie krol:
            jest = False
            for i in range(8):
                for j in range(8):
                    if t[i][j] == 'k':
                        ky=i
                        kx=j
                        jest = True
                        break
                if jest:
                    break
            kolor = 'bialy'
            if szach(t,ky,kx,kolor):
                print("Szach czarnym!")

            if mat(t,ky,kx,kolor):
                print("Biali wygrali!, Koniec gry!")
                gra=False
                break
            czarni=True
        else:
            print("Zly ruch, zrob inny!")
            continue
    else:
        print("Zly ruch, zrob inny!")
        continue
    print()
    wypis(t)
    print()
    while czarni:
        print("Graja czarni!")
        e = input("Potrzebujesz pomocnicza tablica? tak/nie: ")
        print()
        if e == 'tak':
            wypis(dt)
        x = input("Wprowadz numer figury ktora chcesz posunac: ")
        n = input("Wprowadz numer pola gdzie chcesz posunac ta figure: ")
        zlen = False
        zlex=False
        for i in range(8):
            for j in range(8):
                if zlen == False:
                    if n==dt[i][j]:
                        gdz1=i
                        gdz2=j
                        zlen=True
                if zlex==False:
                    if x==dt[i][j]:
                        fig1=i
                        fig2=j
                        zlex=True
        if zlen==False or zlex==False:
            print("Zly ruch, zrob inny!")
            continue
        elif ruch(t, fig1,fig2,gdz1,gdz2)==True and t[fig1][fig2] in ['p','w','s','g','h','k']:
            if t[fig1][fig2] in ['w','g','h']:
                if czyzbil(t,fig1,fig2,gdz1,gdz2)==False:
                    print("Zly ruch, zrob inny!")
                    continue
            if t[gdz1][gdz2] not in ['p','w','s','g','h','k']:
                if t[gdz1][gdz2] in ['P','W','S','G','H']:
                    print("Zbito figure przeciwnika!")
                kolor = 'bialy'
                if szach(t,gdz1,gdz2,kolor):
                    print("Zly ruch, zrob inny!")
                    continue
                t[gdz1][gdz2]=t[fig1][fig2]
                t[fig1][fig2]='.'
                #Gdzie krol:
                jest = False
                for i in range(8):
                    for j in range(8):
                        if t[i][j] == 'K':
                            ky=i
                            kx=j
                            jest = True
                            break
                    if jest:
                        break
                kolor = 'czarny'
                if szach(t,ky,kx,kolor):
                    print("Szach bialym!")
                if mat(t,ky,kx,kolor):
                    print("Czarni wygrali!, Koniec gry!") 
                    gra = False
                    break  
                czarni=False
            else:
                print("Zly ruch, zrob inny!")
                continue
        else:
            print("Zly ruch, zrob inny!")
            continue
        print()
        wypis(t)
        print()
        k=input("Chcesz skonczyc gre? tak/nie: ")
        if k=='tak':
            gra=False