#! /bin/bash

echo -e " Tic Tac Toe Game \n Box size is 3x3 initially it will be filled with E\n E here dentoes that the particular spot is empty"

declare -a row0=('E' 'E' 'E')
declare -a row1=('E' 'E' 'E')
declare -a row2=('E' 'E' 'E')

echo -e "Initial 3x3 matrix \n"
echo ${row0[@]}
echo ${row1[@]}
echo ${row2[@]}

echo -e "\nPlayer 1 has 'x' as his symbol and player 2 'o'"
echo -e "\nUser has to input his choice is following format '0 1' where 0,1 denotes his position in matrix" 

player=1


# function for input
func(){
read -p "Player input : " pos pos1

if [ $pos -eq 0 ] && [ $pos1 -eq 0 ] && [ $player -eq 1 ] && [ ${row0[0]} == 'E' ]
then
    row0[0]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 0 ] && [ $pos1 -eq 1 ] && [ $player -eq 1 ] && [ ${row0[1]} == 'E' ]
then 
    row0[1]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 0 ] && [ $pos1 -eq 2 ] && [ $player -eq 1 ] && [ ${row0[2]} == 'E' ]
then 
    row0[2]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 1 ] && [ $pos1 -eq 1 ] && [ $player -eq 1 ] && [ ${row1[1]} == 'E' ]
then 
    row1[1]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 1 ] && [ $pos1 -eq 2 ] && [ $player -eq 1 ] && [ ${row1[2]} == 'E' ]
then 
    row1[2]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 1 ] && [ $pos1 -eq 0 ] && [ $player -eq 1 ] && [ ${row1[0]} == 'E' ]
then 
    row1[0]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2

elif [ $pos -eq 2 ] && [ $pos1 -eq 0 ] && [ $player -eq 1 ] && [ ${row2[0]} == 'E' ]
then 
    row2[0]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 2 ] && [ $pos1 -eq 1 ] && [ $player -eq 1 ] && [ ${row2[1]} == 'E' ]
then 
    row2[1]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2
elif [ $pos -eq 2 ] && [ $pos1 -eq 2 ] && [ $player -eq 1 ] && [ ${row2[2]} == 'E' ]
then 
    row2[2]=x
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=2

elif [ $pos -eq 0 ] && [ $pos1 -eq 0 ] && [ $player -eq 2 ] && [ ${row0[0]} == 'E' ]
then
    
    row0[0]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 0 ] && [ $pos1 -eq 1 ] && [ $player -eq 2 ] && [ ${row0[1]} == 'E' ]
then 
    row0[1]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 0 ] && [ $pos1 -eq 2 ] && [ $player -eq 2 ] && [ ${row0[2]} == 'E' ]
then 
    row0[2]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 1 ] && [ $pos1 -eq 1 ] && [ $player -eq 2 ] && [ ${row1[1]} == 'E' ]
then 
    row1[1]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 1 ] && [ $pos1 -eq 2 ] && [ $player -eq 2 ] && [ ${row1[2]} == 'E' ]
then 
    row1[2]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 1 ] && [ $pos1 -eq 0 ] && [ $player -eq 2 ] && [ ${row1[0]} == 'E' ]
then 
    row1[0]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1

elif [ $pos -eq 2 ] && [ $pos1 -eq 0 ] && [ $player -eq 2 ] && [ ${row2[0]} == 'E' ]
then 
    row2[0]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 2 ] && [ $pos1 -eq 1 ] && [ $player -eq 2 ] && [ ${row2[1]} == 'E' ]
then 
    row2[1]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
elif [ $pos -eq 2 ] && [ $pos1 -eq 2 ] && [ $player -eq 2 ] && [ ${row2[2]} == 'E' ]
then 
    row2[2]=o
    echo ${row0[@]}
    echo ${row1[@]}
    echo ${row2[@]}
    player=1
else
    echo "Wrong input it is next player's turn"
fi
}

draw=0
check_func(){
    if [ ${row0[0]} != 'E' ] && [ ${row0[1]} != 'E' ] && [ ${row0[2]} != 'E' ] && [ ${row1[0]} != 'E' ] && [ ${row1[1]} != 'E' ] && [ ${row1[2]} != 'E' ] && [ ${row2[0]} != 'E' ] && [ ${row2[1]} != 'E' ] && [ ${row2[2]} != 'E' ]
    then 
        ((draw=1))
    fi
}

win=0
# no winner so win = 0

check_win(){
    if [ ${row0[0]} == 'x' ] && [ ${row0[1]} == 'x' ] && [ ${row0[2]} == 'x' ]
    then 
        ((win=1))
    elif [ ${row1[0]} == 'x' ] && [ ${row1[1]} == 'x' ] && [ ${row1[2]} == 'x' ]
    then 
        ((win=1))
    elif [ ${row2[0]} == 'x' ] && [ ${row2[1]} == 'x' ] && [ ${row2[2]} == 'x' ]
    then 
        ((win=1))

    elif [ ${row0[0]} == 'o' ] && [ ${row0[1]} == 'o' ] && [ ${row0[2]} == 'o' ]
    then 
        ((win=2))
    elif [ ${row1[0]} == 'o' ] && [ ${row1[1]} == 'o' ] && [ ${row1[2]} == 'o' ]
    then 
        ((win=2))
    elif [ ${row2[0]} == 'o' ] && [ ${row2[1]} == 'o' ] && [ ${row2[2]} == 'o' ]
    then 
        ((win=2))

    elif [ ${row0[0]} == 'x' ] && [ ${row2[0]} == 'x' ] && [ ${row1[0]} == 'x' ]
    then 
        ((win=1))
    elif [ ${row0[1]} == 'x' ] && [ ${row1[1]} == 'x' ] && [ ${row2[1]} == 'x' ]
    then 
        ((win=1))
    elif [ ${row0[2]} == 'x' ] && [ ${row1[2]} == 'x' ] && [ ${row2[2]} == 'x' ]
    then 
        ((win=1))

    elif [ ${row0[0]} == 'o' ] && [ ${row2[0]} == 'o' ] && [ ${row1[0]} == 'o' ]
    then 
        ((win=2))
    elif [ ${row0[1]} == 'o' ] && [ ${row1[1]} == 'o' ] && [ ${row2[1]} == 'o' ]
    then 
        ((win=2))
    elif [ ${row0[2]} == 'o' ] && [ ${row1[2]} == 'o' ] && [ ${row2[2]} == 'o' ]
    then 
        ((win=2))
    
    elif [ ${row0[0]} == 'o' ] && [ ${row1[1]} == 'o' ] && [ ${row2[2]} == 'o' ]
    then 
        ((win=2))

    elif [ ${row0[0]} == 'x' ] && [ ${row1[1]} == 'x' ] && [ ${row2[2]} == 'x' ]
    then 
        ((win=1))

    elif [ ${row0[2]} == 'o' ] && [ ${row1[1]} == 'o' ] && [ ${row2[0]} == 'o' ]
    then 
        ((win=2))

    elif [ ${row0[2]} == 'x' ] && [ ${row1[1]} == 'x' ] && [ ${row2[0]} == 'x' ]
    then 
        ((win=1))
    fi
}


while [ $draw == 0 ]  && [ $win == 0 ];
do
    func
    check_win
    check_func
done

if [ $draw == 1 ]
then 
    echo -e "\nThe game is draw"
elif [ $win == 1 ]
then
    echo -e "\n Player 1 wins"
elif [ $win == 2 ]
then
    echo -e "\n Player 2 wins"
fi