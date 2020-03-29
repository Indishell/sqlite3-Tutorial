#include<bits/stdc++.h>
using namespace std;

// gcc main.cpp -o <name you want to give>
// gcc main.cpp -o ki

//  Now, Run in next command
// Run  ki.exe    ( name you want to give.exe)

int minElement(stack<int> ms)
{
    int temp = INT_MIN;

    stack<int> ns = ms;

    while (!ns.empty())
    {

        if(ns.top() > temp)
        {
            temp = ns.top();
        }
        ns.pop();        
    }

    return temp;
}

int main()
{

    stack<int> ms;

    ms.push(1);
    ms.push(-10);
    ms.push(12);
    ms.push(-12);
    ms.push(13);
    ms.push(14);
    ms.push(18);
    ms.push(-1);
    
    
    cout<< "Min element is   " << minElement(ms) <<"\n";
    ms.pop();
    cout<< "Min element is   " << minElement(ms) <<"\n";
    ms.pop();
    cout<< "Min element is   " << minElement(ms) <<"\n";
    ms.pop();
    ms.pop();
    cout<< "Min element is   " << minElement(ms) <<"\n";

    
    return 0;
}
