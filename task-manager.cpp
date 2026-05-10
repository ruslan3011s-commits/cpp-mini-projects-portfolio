#include <iostream>
#include <vector>
#include <string>
using namespace std;
void dodaj(vector<string>&v,string task)
{
    cout << "Wpisz task ktory chce dodac: ";
    cin.ignore();
    getline(cin,task);
    v.push_back(task);
}
void pokaz(vector<string>&v)
{
    cout << "Masz takie taski: " << endl;
    for(int i=0;i<v.size();i++)
    {
        cout << i+1 << ". " << v[i] << endl;
    }
}
void usun(vector<string>&v,int n)
{
    v.erase(v.begin()+(n-1));
    cout << "Usunieto." << endl;
}
void ogolnie()
{
    vector<string>v;
    bool menedzer=true;
    int wybor;
    string task;
    int n;
    while(menedzer)
    {
        cout << "1. Dodaj task" << endl;
        cout << "2. Pokaz task" << endl;
        cout << "3. Usun task" << endl;
        cout << "4. Exit" << endl;
        cout << "Wprowadz opcje: ";
        cin >> wybor;
        cout << endl;
        if(wybor==1)
        {
            dodaj(v,task);
        }
        else if(wybor==2)
        {
            pokaz(v);
        }
        else if(wybor==3)
        {
            cout << "Podaj jaki task chcesz usunac: ";
            cin >> n;
            if(n>v.size() || n<1)
            {
                cout << "Nie ma takiego tasku pod takim numerem." << endl;
            }
            else{
                usun(v,n);
            }
        }
        else if(wybor==4)
        {
            cout << "Dziekuje za korzystanie)" << endl;
            menedzer=false;
        }
        else{
            cout << "Nie ma takiej opcji z takim numerem, sprobuj jeszcze raz." << endl;
        }
        cout << endl;
    }
}
int main()
{
    ogolnie();
}