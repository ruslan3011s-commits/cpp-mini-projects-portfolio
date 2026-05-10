#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
bool ruch(char t[3][3], char numer, char dt[3][3], char znak)
{
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            if(t[i][j]==numer)
            {
                if(dt[i][j] != ' ')
                {
                    return false;
                }
                else{
                    dt[i][j]=znak;
                    return true;
                }
            }
        }
    }
    return false;
}
bool wygranaAI(char krzyz, char dt[3][3], char kolko)
{
    for(int i=0;i<3;i++)
    {
        if(dt[i][0] == dt[i][1] && dt[i][1] == krzyz && dt[i][2]==' ')
        {
            dt[i][2]=krzyz;
            return true;
        }
        if(dt[i][2] == dt[i][1] && dt[i][1] == krzyz && dt[i][0]==' ')
        {
            dt[i][0]=krzyz;
            return true;
        }
        if(dt[i][0] == dt[i][2] && dt[i][2] == krzyz && dt[i][1]==' ')
        {
            dt[i][1]=krzyz;
            return true;
        }
        if(dt[0][i] == dt[1][i] && dt[1][i] == krzyz && dt[2][i]==' ')
        {
            dt[2][i]=krzyz;
            return true;
        }  
        if(dt[2][i] == dt[1][i] && dt[1][i] == krzyz && dt[0][i]==' ')
        {
            dt[0][i]=krzyz;
            return true;
        }
        if(dt[0][i] == dt[2][i] && dt[2][i] == krzyz && dt[1][i]==' ')
        {
            dt[1][i]=krzyz;
            return true;
        }
    }
    if(dt[0][0] == dt[1][1] && dt[1][1] == krzyz && dt[2][2]==' ')
    {
        dt[2][2]=krzyz;
        return true;
    }
    if(dt[2][2] == dt[1][1] && dt[1][1] == krzyz && dt[0][0]==' ')
    {
        dt[0][0]=krzyz;
        return true;
    }
    if(dt[0][0] == dt[2][2] && dt[2][2] == krzyz && dt[1][1]==' ')
    {
        dt[1][1]=krzyz;
        return true;
    }
    if(dt[0][2] == dt[1][1] && dt[1][1] == krzyz && dt[2][0]==' ')
    {
        dt[2][0]=krzyz;
        return true;
    }
    if(dt[2][0] == dt[1][1] && dt[1][1] == krzyz && dt[0][2]==' ')
    {
        dt[0][2]=krzyz;
        return true;
    }
    if(dt[0][2] == dt[2][0] && dt[2][0] == krzyz && dt[1][1]==' ')
    {
        dt[1][1]=krzyz;
        return true;
    }
    return false;
}
bool bronAI(char krzyz, char dt[3][3], char kolko)
{
    for(int i=0;i<3;i++)
    {
        //wierszy
        if (dt[i][0] == dt[i][1] && dt[i][1] == kolko && dt[i][2]==' ')
        {
            dt[i][2]=krzyz;
            return true;
        }
        if(dt[i][2] == dt[i][1] && dt[i][1] == kolko && dt[i][0]==' ')
        {
            dt[i][0]=krzyz;
            return true;
        }
        if(dt[i][0] == dt[i][2] && dt[i][2] == kolko && dt[i][1]==' ')
        {
            dt[i][1]=krzyz;
            return true;
        }
        //kolumny
        if(dt[0][i] == dt[1][i] && dt[1][i] == kolko && dt[2][i]==' ')
        {
            dt[2][i]=krzyz;
            return true;
        }
        if(dt[2][i] == dt[1][i] && dt[1][i] == kolko && dt[0][i]==' ')
        {
            dt[0][i]=krzyz;
            return true;
        }
        if(dt[0][i] == dt[2][i] && dt[2][i] == kolko && dt[1][i]==' ')
        {
            dt[1][i]=krzyz;
            return true;
        }
    }
    //skos1 od lewej
    if(dt[0][0] == dt[1][1] && dt[1][1] == kolko && dt[2][2]==' ')
    {
        dt[2][2]=krzyz;
        return true;
    }
    if(dt[2][2] == dt[1][1] && dt[1][1] == kolko && dt[0][0]==' ')     
    {
        dt[0][0]=krzyz;
        return true;
    }
    if(dt[0][0] == dt[2][2] && dt[2][2] == kolko && dt[1][1]==' ')
    {
        dt[1][1]=krzyz;
        return true;
    }
    //skos2 od prawej
    if(dt[0][2] == dt[1][1] && dt[1][1] == kolko && dt[2][0]==' ')
    {
        dt[2][0]=krzyz;
        return true;
    }
    if(dt[2][0] == dt[1][1] && dt[1][1] == kolko && dt[0][2]==' ')     
    {
        dt[0][2]=krzyz;
        return true;
    }
    if(dt[0][2] == dt[2][0] && dt[2][0] == kolko && dt[1][1]==' ')
    {
        dt[1][1]=krzyz;
        return true;
    }
    return false;
}
bool ruchAI(char krzyz, char dt[3][3], char kolko, char numer, char t[3][3])
{
    if(wygranaAI(krzyz,dt,kolko))
    {
        return true;
    }
    else if(bronAI(krzyz,dt,kolko))
    {
        return true;
    }
    else if(dt[1][1]==' ')
    {
        dt[1][1]=krzyz;
        return true;
    }
    else if(dt[0][0]==' ' || dt[0][0]==' '  && dt[2][0]==dt[0][2] && dt[0][2]==kolko)
    {
        dt[0][0]=krzyz;
        return true;
    }
    else if(dt[2][0]==' ' || dt[2][0]==' '  && dt[0][0]==dt[2][2] && dt[2][2]==kolko)
    {
        dt[2][0]=krzyz;
        return true;
    }
    else if(dt[0][2]==' ' || dt[0][2]==' '  && dt[0][0]==dt[2][2] && dt[2][2]==kolko)
    {
        dt[0][2]=krzyz;
        return true;
    }
    else if(dt[2][2]==' ' || dt[2][2]==' '  && dt[2][0]==dt[0][2] && dt[0][2]==kolko)
    {
        dt[2][2]=krzyz;
        return true;
    }
    else{
        numer = '1'+rand()%9;
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(t[i][j]==numer)
                {
                    if(dt[i][j] != ' ')
                    {
                        return false;
                    }
                    else{
                        dt[i][j]=krzyz;
                        return true;
                    }
                }
            }
        }
    }
    return false;
}
void planszadt(char dt[3][3])
{
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            cout << dt[i][j] << "  ";
        }
        cout << endl;
    }
}
void planszat(char t[3][3])
{
    for(int i=1;i<=9;i++)
    {
        cout << i << "  ";
        if(i%3==0)
            cout << endl;
    }
}
bool wygrana(char znak, char dt[3][3])
{
    if(dt[0][0]==dt[1][1] && dt[1][1]==dt[2][2] && dt[2][2]==znak)
        return true;
    if(dt[0][2]==dt[1][1] && dt[1][1]==dt[2][0] && dt[2][0]==znak)
        return true;
    for(int i=0;i<3;i++)
    {
        if(dt[0][i]==dt[1][i] && dt[1][i]==dt[2][i] && dt[2][i]==znak || dt[i][0]==dt[i][1] && dt[i][1]==dt[i][2] && dt[i][2]==znak)
        {
            return true;
        }
    }
    return false;
}

void ogolnie()
{
    char t[3][3]={'1','2','3',
                  '4','5','6',
                  '7','8','9'};
    char numer, kolko = 'O' , krzyz = 'X';
    bool jeszczegra=true;
    int chce;
    srand(time(0));
    while(jeszczegra)
    {
        bool gra = true;
        planszat(t);
        char dt[3][3] = {' ',' ',' ',
                         ' ',' ',' ',
                         ' ',' ',' '};
        int ile=0;
        while(gra)
        {
            bool zlyruch=true;
            while(zlyruch)
            {
                cout << "Wprowadz ruch Kolkiem: ";
                cin >> numer;
                if(numer < '1' || numer > '9')
                {
                    cout << "Wprowadz liczbe od 1 do 9!!!!!" << endl;
                    continue;
                }
                else{
                    if(ruch(t,numer,dt,kolko))
                    {
                        ile++;
                        zlyruch=false;
                    }
                    else{
                        cout << "Ta pozycja jest zajete!" << endl;
                    }
                }
            }
            planszadt(dt);
            if(wygrana(kolko,dt))
            {
                cout << "Kolko wygralo!!!!!!!" << endl;
                cout << "Chcesz zagrac jeszcze runde?, Jesli tak to napisz '1' a jesli nie to '2': ";
                cin >> chce;
                if(chce==1)
                {
                    gra=false;
                }
                else{
                    gra=false;
                    jeszczegra=false;
                }
            }
            if(ile==9)
            {
                cout << "Remis!!!!!" << endl;
                cout << "Chcesz zagrac jeszcze runde?, Jesli tak to napisz '1' a jesli nie to '2': ";
                cin >> chce;
                if(chce==1)
                {
                    gra=false;
                }
                else{
                    gra=false;
                    jeszczegra=false;
                }
            }
            if(gra)
            {
                bool zlyruchk=true;
                while(zlyruchk)
                {
                    cout << "Komputer wprowadza ruch krzyzem" << endl;
                    if(ruchAI(krzyz,dt,kolko,numer,t))
                    {
                        ile++;
                        zlyruchk=false;
                    }
                }
                planszadt(dt);
                if(wygrana(krzyz,dt))
                {
                    cout << "Krzyz wygral!!!!!!!" << endl;
                    cout << "Chcesz zagrac jeszcze runde?, Jesli tak to napisz '1' a jesli nie to '2': ";
                    cin >> chce;
                    if(chce==1)
                    {
                        gra=false;
                    }
                    else{
                        gra=false;
                        jeszczegra=false;
                    }
                }
            }
        }
    }
}
int main()
{
    ogolnie();
}