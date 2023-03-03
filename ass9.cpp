#include<iostream>
#include<cstdlib> 
#include<string.h>
using namespace std; 
struct node
{
	int prn;
	char name[30]; 
	struct node *next;
}*start;

class pinnacle
{
	public :
	node *create(int ,char []); 
	void add_president(); 
	void add_secretary(); 
	void display();
	void add_member(); 
	void d_president(); 
	void d_secretary();
	void d_member(); 
	void no_members(); 
	void reverse();

};


node *pinnacle::create(int prn, char name[30])
{
	struct node *temp;
	temp = new(struct node); 
	if (temp == NULL)
		{
			cout<<"Memory not allocated "<<endl; 
			return 0;
		}
	else
		{
			strncpy(temp->name, name, 30); 
			temp->prn = prn;
			temp->next = NULL; 
			return temp;
}
}

void pinnacle:: add_president()
{
	int prn;
	char name[30]; 
	cout<<"\nEnter prn no. : "; 
	cin>>prn;
	cout<<"Enter President name : "; 
	cin>>name;
	struct node *temp, *p;
	temp = create(prn,name); 
	if (start == NULL)
		{
			start = temp;
			start->next = NULL;
		}
	else
		{
			p = start; 
			start = temp;
			start->next = p;
		}
cout<<"President Inserted at beginning"<<endl;
}

void pinnacle:: add_secretary()
{
	int prn;
	char name[30]; cout<<"\nEnter prn no. : "; 
	cin>>prn;
	cout<<"Enter Secretary name : "; 
	cin>>name;
	struct node *temp, *s;
	temp = create(prn,name); 
	s = start;
	while (s->next != NULL)
		{
			s = s->next;		
		}
	temp->next = NULL; 
	s->next = temp;
	cout<<"Secretary Inserted"<<endl;
}


void pinnacle :: display()
{
	struct node *temp; 
	if (start == NULL)
		{
			cout<<"The List is Empty"<<endl; 
			return;
		}
	temp = start;
	cout<<"\n.... Members of list	";
	while (temp != NULL)
		{
			cout<<"\nPRN NO. : "<<temp->prn<<" NAME : "<<(temp->name) ; 
			temp = temp->next;
		}

}


void pinnacle :: add_member()
{
	int prn,counter=0; 
	char name[30];
	cout<<"\nEnter prn no. : "; 
	cin>>prn;
	cout<<"Enter Member name : "; 
	cin>>name;
	struct node *temp, *s, *ptr; 
	temp = create(prn,name);
	s=start;
	while (s != NULL)
		{
			s = s->next;
			counter++;
		}
	if (start == NULL)
		{
			start = temp;
			start->next = NULL;
		}	
	else
		{
			s=start;
		for (int i = 1; i < (counter) ; i++)
			{
				ptr = s;
				s = s->next;
			}
				ptr->next = temp; 
				temp->next = s;
}
}


void pinnacle :: d_president()
{
	struct node *s; 
	s = start;
	start = s->next; 
	free(s);
}

void pinnacle :: d_secretary()
{
	struct node *s; 
	s=start;
	while(s->next->next != NULL)
		{
			s=s->next;
		}
	free(s->next);
	s->next=NULL;
}
void pinnacle :: d_member()
{
	int pos, i, counter = 0; 
	if (start == NULL)
	{
		cout<<"List is empty"<<endl; 
		return;
	}
cout<<"Enter the position of member to be deleted: "; 
cin>>pos;
	struct node *s, *ptr; 
	s = start;
	if (pos == 1)
		{
			start = s->next;
		}
	else
		{
		while (s != NULL)
			{
				s = s->next; counter++;
			}
				if (pos > 0 && pos <= counter)
					{
						s = start;
					for (i = 1;i < pos;i++)
						{
							ptr = s;
							s = s->next;
						}
						ptr->next = s->next;
					}
				else
					{
						cout<<"Position out of range"<<endl;
					}
				free(s);
				cout<<"Member Deleted"<<endl;
		}
		}


void pinnacle :: no_members()
{
	int count=0; 
	struct node *s; 
	s=start;
	while(s != NULL)
	{
		s=s->next; 
		count++;
	}
		cout<<"Number of members in the group = "<<count<<endl;
}
void pinnacle :: reverse()
{
	struct node *ptr1, *ptr2, *ptr3; 
	if (start == NULL)
	{
		cout<<"List is empty"<<endl; return;
	}
	if (start->next == NULL)
	{
		return;
	}
	ptr1 = start;
	ptr2 = ptr1->next; 
	ptr3 = ptr2->next; 
	ptr1->next = NULL; 
	ptr2->next = ptr1; 
	while (ptr3 != NULL)
		{
			ptr1 = ptr2; 
			ptr2 = ptr3;
			ptr3 = ptr3->next; 
			ptr2->next = ptr1;
		}
	start = ptr2;
}
int main()
{ 
	int choice;
	pinnacle sl; 
	start = NULL; 
	while (1)	
	{
		cout<<"\n1.Add President"<<endl; 
		cout<<"2.Add Secretary"<<endl; 
		cout<<"3.Display"<<endl; 
		cout<<"4.Add_Member"<<endl; 
		cout<<"5.Delete President"<<endl; 
		cout<<"6.Delete Secretary"<<endl; 
		cout<<"7.Delete Member"<<endl; 
		cout<<"8.No of members"<<endl; 
		cout<<"9. Reverse "<<endl; 
		cout<<"10.Exit "<<endl; 
		cout<<"\nEnter your choice : "; 
		cin>>choice;
	switch(choice)
	{ 
	case 1:
		cout<<"\nAdd President : ";
		sl.add_president(); 
		cout<<endl;  
	break;
	case 2:
		cout<<"\nAdd Secretary : "; 
		sl.add_secretary(); 
		cout<<endl;
	break; 
	case 3:
		cout<<"\n"; sl.display(); cout<<endl; 
	break;
	case 4:
		cout<<"\nAdd Member "; 
		sl.add_member();
		cout<<endl;
	break; 
	case 5:
		cout<<"\nDelete President "; 
		sl.d_president();
		cout<<endl; 
		break;
	case 6:
		cout<<"\nDelete Secreatery "; 
		sl.d_secretary();
		cout<<endl; 
		break;
	case 7:
		cout<<"\nDelete Member "; 
		sl.d_member(); 
		cout<<endl;
		break; 
	case 8:
		cout<<"\nTotal Members "; 
		sl.no_members(); 
		cout<<endl;
		break; 
	case 9:
		cout<<"\nReverse Members ";
		sl.reverse();
		cout<<endl; 
		break;
	case 10:
		cout<<"\nConcatenate Members : ";
		cout<<endl;
		break;
	case 0 :
		cout<<"\nExiting"<<endl; 
		exit(1);
	default:
		cout<<"\nWrong choice"<<endl;
}
}
return 0;
}









