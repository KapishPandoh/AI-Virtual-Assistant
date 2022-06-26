#include<iostream>
#include<stdlib.h>
using namespace std;

char board[3][3]={ {'1','2','3'} , {'4','5','6'} , {'7','8','9'} };
int choice,row,col;

char turn = 'X';
bool draw = false;

void display()
{
    cout<<"Player-1 [X]\n";
    cout<<"Player-2 [O]\n";

    cout<<"\t\t   |   |"<<endl;
    cout<<"\t\t "<<board[0][0]<<" | "<<board[0][1]<<" | "<<board[0][2]<<endl;
    cout<<"\t\t___|___|___"<<endl;
    cout<<"\t\t   |   |  "<<endl;
    cout<<"\t\t "<<board[1][0]<<" | "<<board[1][1]<<" | "<<board[1][2]<<endl;
    cout<<"\t\t___|___|___"<<endl;
    cout<<"\t\t   |   |  "<<endl;
    cout<<"\t\t "<<board[2][0]<<" | "<<board[2][1]<<" | "<<board[2][2]<<endl;
    cout<<"\t\t   |   |  "<<endl;

}


void p_turn()
{

    if(turn=='X')
        cout<<"\n\nPlayer-1[X] turn : ";
    else if(turn=='O')
        cout<<"\n\nPlayer-2[O] turn : ";


    cin>>choice;

       switch(choice)
       {
           case 1 : row=0;col=0;break;
           case 2 : row=0;col=1;break;
           case 3 : row=0;col=2;break;
           case 4 : row=1;col=0;break;
           case 5 : row=1;col=1;break;
           case 6 : row=1;col=2;break;
           case 7 : row=2;col=0;break;
           case 8 : row=2;col=1;break;
           case 9 : row=2;col=2;break;

           default :
               cout<<"Invalid move ";
       }


    if(turn=='X' && board[row][col]!='X'&& board[row][col]!='O')
    {
        board[row][col]='X';
        turn='O';
    }

    else if(turn=='O' && board[row][col]!='X'&& board[row][col]!='O')
    {
        board[row][col]='O';
        turn='X';
    }

    else
    {
        cout<<"Box already filled please choose another choice !!"<<endl;
        p_turn();
    }

   system("cls");
}


bool gameover()
{

    for(int i=0;i<3;i++)
    {
        if( (board[i][0]==board[i][1] && board[i][0]==board[i][2]) || (board[0][i]==board[1][i] && board[0][i]==board[2][i])  )
            return false;
    }

     if( (board[0][0]==board[1][1] && board[0][0]==board[2][2]) || (board[0][2]==board[1][1] && board[0][2]==board[2][0])  )
            return false;



    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            if(board[i][j]!='X' && board[i][j]!='O')
                return true;
        }
    }


    draw = true;
    return false;

}


int main()
{
   cout<<"\t\t\tTICK TAC TOE\n";
   cout<<"\t\t\tFor Two Players\n";


      while(gameover())
      {
          display();
          p_turn();
      }


    if(turn == 'O' && draw == false)
        cout<<"\t\t\n\nCongratulations,Player-1 [X] Wins \n";

    else if(turn == 'X' && draw == false)
        cout<<"\t\t\n\nCongratulations,Player-2 [O] Wins \n";
    else
        cout<<"\t\t\n\nThe Match Is Draw\n";

}
