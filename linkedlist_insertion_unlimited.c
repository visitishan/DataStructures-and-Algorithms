#include<stdio.h>
#include<stdlib.h>

struct node
{	int data;
	struct node *next;	
};

void traverse(struct node* start)
{
	while(start!=NULL)
	{
		printf("%d\n",start -> data);
		start = start -> next;
	}
}

int main()
{
	int a,b,ch = 1;
	struct node* temp = NULL;
	struct node* newnode;
	while(ch!=0)
	{
		
		newnode=(struct node*)malloc(sizeof(struct node));
		printf("Enter data:\n");
		scanf("%d",&a);
		newnode -> data = a;
		newnode -> next = temp;
		temp = newnode;
		printf("Data entered is : ");
		printf("%d", newnode -> data);
		printf("\n \t Press any number to enter more, 0 to exit :\n");
		scanf("%d",&ch);
	}

	printf("\n Press 1 to traverse - \n");
	scanf("%d",&b);
	if (b==1)
	{
		traverse(newnode);
	}
	return 0;
}
