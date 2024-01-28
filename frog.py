def s(positions,pos,pos2):
    temp = positions[pos]
    positions[pos] = positions[pos2]
    positions[pos2] = temp

positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']
print(positions)
print("Current status of the game : ")
print("[ 0    1    2    3    4    5    6]")
print(positions)
po = positions.copy()[::-1]
print(po)
while(True):
    pos = input("Press q to quit else \nEnter position of piece:")
    if pos == 'q':
        print("You Lose")
        break
    elif int(pos) < 0 or 6 < int(pos):
        print("Invalid Move")
    else:
        pos = int(pos)
        pos2 = 0
        if positions[pos] == '-':
            print("Invalid Move")
            # break
        if positions[pos] == 'G':
            if pos+1 <=6 and positions[pos+1]=='-':
                pos2 = pos+1
                s(positions,pos,pos2)
            elif pos+2 <=6 and positions[pos+2] == '-':
                if positions[pos+1]=='B':
                    pos2 = pos+2
                    s(positions,pos,pos2)
            else:
                print("Invalid Move")
        if positions[pos] == 'B':
            if pos-1 >=0 and positions[pos-1]=='-':
                pos2 = pos-1
                s(positions,pos,pos2)
            elif pos-2 >=0 and positions[pos-2] == '-':
                if positions[pos-1]=='G':
                    pos2 = pos-2
                    s(positions,pos,pos2)
            else:
                print("Invalid Move")
        
    print(positions)
    if positions == po:
        print("you win")
        break
