#include <iostream>
using namespace std;
int i;
class stack
{
	private:
  	int top;
  	char a[7];
public:
  	stack()
  		{
    			top = -1; 
  		}	
  			int stack_empty();
  			int stack_full();
void stack_push(char x);
char stack_pop();
};

int stack :: stack_empty()
{
    if(top == -1)
     return 1;
    else 
     return 0;
}
int stack :: stack_full()
{
if(top == 9)
     return 1;
    else
     return 0;
}
void stack :: stack_push(char x)
{
    top++;
    a[top] = x;
}
char stack :: stack_pop()
{
    char y;
    y = a[top];
    top--;
    return y;
}
int main()
{
    char z,b[20];
    stack s1;
    cout<<"\nEnter the infix expression :: ";
    cin>>b;
    for(i = 0;b[i]!='\0';i++)
    {
        if(b[i]=='{' || b[i]=='[' || b[i]=='(')
         if(s1.stack_full())
           cout<<"Stack is full"<<endl;
          else
           s1.stack_push(b[i]);
        else
         if(b[i]=='}' || b[i]==']' || b[i]==')' )
         {
            z = s1.stack_pop();
            if(b[i]=='}' && z!='{')
             break;
            if(b[i]==']' && z!='[')
             break;
            if(b[i]==')' && z!='(')
             break;
            else
             continue;
         }
           
    }
    if(s1.stack_empty())
     cout<<"\n Well parenthesized"<<endl;
    else
     cout<<"\n Not Well parenthesized"<<endl;
    return 0;
}

