
#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

int main() {
    
    int n;
    if (!(cin >> n)) return 0;
    // discard leftover newline before using getline
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<string> items;
    for (int i = 0; i < n; ++i) {
      //   cout << "Enter string " << (i + 1) << ": ";
        string s;
        if (!getline(cin, s)) break;
        if (s.empty()) { --i; continue; } // skip empty input
        items.push_back(s);
    }

   //  cout << "\nYou entered:\n";
    for (const auto &s : items) {
      // cout << "- " << s;
      if (s.length()<=10) {
        cout << s << '\n';
         // stop processing further inputs
      }
      else if(s.length()>10){
         cout<<s[0]<<s.length()-2<<s.back()<<endl;
      }
      // if (s == "hello") {
      //   cout << " (matched 'hello')";
      // } else if (s.find("test") != string::npos) {
      //   cout << " (contains 'test')";
      // } else if (s.length() > 5) {
      //   cout << " (longer than 5)";
      } 
      
       return 0;
    }

   
