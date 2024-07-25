import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
h0=0
w0=0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)  
   
    if bomb_dir=="U" or bomb_dir=="UR" or bomb_dir=="UL" :
        h=y0-1
        y0=(h0+h)//2
    if bomb_dir=="D" or bomb_dir=="DR" or bomb_dir=="DL" :
        h0=y0+1
        y0=(h0+h)//2
    if bomb_dir=="R" or bomb_dir=="DR" or bomb_dir=="UR"  :
        w0=x0+1
        x0=(w0+w)//2 
    if bomb_dir=="L" or bomb_dir=="DL" or bomb_dir=="UL"  :
        w=x0-1
        x0=(w+w0)//2
  
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(str(x0)+" "+str(y0))
