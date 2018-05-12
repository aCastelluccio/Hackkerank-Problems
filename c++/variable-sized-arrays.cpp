#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int q;
    cin>>n;
    cin>>q;
    vector <int> g1[n];
    for(int j = 0; j < n; j++){
        int k;
        cin>>k;
        for(int i = 0; i < k; i++){
            int temp;
            cin>>temp;
            g1[j].push_back(temp);
        }
    }
    for(int i = 0; i < q; i++){
        int arNum;
        cin>>arNum;
        int num;
        cin>>num;
        cout<<g1[arNum].at(num)<<endl;
    }
    return 0;
}
