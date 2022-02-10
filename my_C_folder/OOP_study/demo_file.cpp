#include <iostream>
using namespace std;

// Write classes code here
// make base class functions virtual

class Account {
  protected:
  float balance;

  public:
  Account(float bal) {
    balance = bal;
  }

  virtual void deposit(float amount){}
  virtual void withdraw(float amount){}
  virtual void printBalance(){}
};

class Savings: public Account 
{
    float interest_rate = 0.8;

    public:
    Savings(int bal): Account(bal){}

  void deposit( float amount ) 
  {
    balance += amount + (amount * interest_rate);
  }

  void withdrawn(float amount) 
  {
    balance -= amount + (amount * interest_rate);
    
  }

  void printBalance(){
      cout << "Saving Account Remaining Balance: " << balance << endl;
  }
};


class current: public Account
{

public:
current(int bal) : Account(bal){}

  void deposit(float amount) 
  {
    balance += amount;
  }

  void withdrawn(float amount) 
  {
    balance -= amount;
    
  }
  void printBalance()
  {
      cout << "Balance in your Account is: " << balance << endl;
  }
};


int main() {
  // creating savings account object
  Savings s1(50000);
  Account * acc = &s1;   // pointing acc to savings object
  acc->deposit(1000);
  acc->printBalance();
  
  acc->withdraw(3000);
  acc->printBalance();
  
  cout << endl;
  
  // creating current account object
  current c1(50000);
  acc = &c1;     //// pointing acc to current object
  acc->deposit(1000);
  acc->printBalance();
  
  acc->withdraw(3000);
  acc->printBalance();  
}