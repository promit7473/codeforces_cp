#include <iostream>
#include <vector>
 int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
        int t;
    std::cin >> t;
     std::string inp;
    std::cin>>inp;
     int a = 0;
    int d = 0;
    for(int i=0; i<t; ++i){
        if(inp[i]=='A'){
            a++;
        }
        else{
            d++;
        }   
    }
    if(a>d){
    std::cout<<"Anton"<<std::endl;
    }
    else if(d>a){
        std::cout<<"Danik"<<std::endl;
    }
    else {
        std::cout<<"Friendship"<<std::endl;
    }
     return 0;
 }