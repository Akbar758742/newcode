#include<iostream>
#include <string>
using namespace std;

class teacher{
    private:
    double salary;

    public:
    string name;
    string  dept;
    string subject;
    
    void changedept(string newdept)
    {
        dept=newdept;

    }
    void setsalary(double s)
    {
        salary=s;
    }
    double getsalary()
    {
        return salary;
    }

};

int main()
{
    cout<<"hello"<<endl;
teacher t1;
t1.name="akbar";
t1.dept="cse";
t1.subject="DSA";
//t1.salary=438957;
cout<<t1.name<<endl;
//cout<<t1.salary<<endl;
t1.setsalary(35434);
cout<<t1.getsalary()<<endl;

}