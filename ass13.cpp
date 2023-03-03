#include<iostream>
using namespace std;
#define MAX 5

class Queue
{
	int front, rear, ajob, djob;
	int A[MAX];
	public:
		Queue()
		{
			front = -1; 
			rear = -1;
			ajob = 0;
			djob = 0;
		}

		void display()
		{
			cout<<"Present list is: ";
			int i;
			for (i=front; i<=rear; i++)
			{
				cout<<A[i]<<" ";
			}
		}

		int qempty()
		{
			if (front==-1 || front>rear)
				return 1;
			else
				return 0;
		}

		int qfull()
		{
			if (rear==MAX-1)
				return 1;
			else 
				return 0;
		}
		void qadd(int ajob)
		{
			int x=ajob;
			if (qfull())
					cout<<"Sorry list is full!!"<<endl;
			else
			{
				if(front==-1)
				{
					front=rear=0;
					A[rear]=ajob;
				}
				else
				{
					rear=rear+1;
					A[rear]=ajob;
				}
			}
		}


		void qdelete()
		{
			if (qempty())
				cout<<"Sorry list is empty!!!"<<endl;
			else
				{
					int x=A[front];
					cout<<"Deleted: "<<x<<endl;
					front=front+1;
				}
		}
};

int main()
{
	Queue obj;
	int x,y;
char ans;
do
{
	cout<<"1.Add the job\n2.Delete a job\n3.Display\nEnter your choice: ";
	cin>>x;
	switch (x)
	{
		case 1:
			cout<<"Enter the job number: ";
			int y;
			cin>>y;
			obj.qadd(y);
			break;
		case 2:
			cout<<"Job deleted!!"<<endl;
			obj.qdelete();
			break;
		case 3:
			obj.display();
			break;
		default:
			cout<<"Out of range: ";
			break;
	}
cout<<"Do u want to Continue?(y||n) : - ";
cin>>ans;
}while(ans=='y'||ans=='Y');
	return 0;
}
