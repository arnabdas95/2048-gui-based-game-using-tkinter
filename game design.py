import functools
from tkinter import  *
from tkinter import messagebox
import random
import copy
root =Tk()
root.title('2048 G A M E')
root.resizable(height = False, width = False)
#root.geometry('540x663')






# define 2048 grid 4*4
global cancl_timer
swap = 0
sc = min = hr = 0
rows, cols = (4, 4)
grid = [[0 for i in range(rows)] for j in range(cols)]
undo_grid = copy.deepcopy(grid)
# end_game flag for infinite loop
not_end = True
def gird_create():
    for i in range(rows):
       for j in range(cols):
           grid[i][j] = 0
    not_end = True
    global sc ,min,hr,cancl_timer
    root.after_cancel(cancl_timer)
    hr=0
    sc=0
    min =0
    new_num_assign()
    new_num_assign()





def undo_copy():
    global grid,undo_grid
    for i in range(rows):
        for j in range(cols):
            undo_grid[i][j]=grid[i][j]


def undo_game():
    for i in range(rows):
        for j in range(cols):
            grid[i][j]=undo_grid[i][j]
    tk_display()
def grid_compare():
    global grid,undo_grid
    for i in range(rows):
        for j in range(cols):
            if undo_grid[i][j]!=grid[i][j]:
                return 1
    return 0
# check for end of game
# if all the cells are full and no 2048
def check_full_grid():
    zero_flag = False
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                zero_flag = True
            elif grid[i][j] == 2048:
                show_msg(0)
                #end_game()
    if  zero_flag == False:
        show_msg(1)
        #end_game()

def show_msg(x):
    if x ==0:
        tk_display()

        gird_create()
        res = messagebox.askquestion('prompt', 'CONGO .YOU WIN...\nTry New Game')
        if res == 'yes':

            gird_create()
            not_end = True
            clock()

        else:
            exit()

    else:
        tk_display()
        responce = messagebox.askquestion('prompt', 'LOST\nTry New Game')
        if responce == 'yes':
           gird_create()
           not_end = True
           clock()

        else:
           exit()



def colorpicker(i,j):
    if grid[i][j]==2  or grid[i][j]==512:
        return '#94d0cc'
    if grid[i][j]==4 or grid[i][j]==1024:
        return '#eec4c4'
    if grid[i][j]==8:
        return '#f29191'
    if grid[i][j]==16 or grid[i][j]==256:
        return '#d1d9d9'
    if grid[i][j]==32:
        return '#fb9300'
    if grid[i][j] == 64 :
        return '#0a81ab'
    if grid[i][j] == 0:
        return '#feffde'
    if grid[i][j] == 128:
        return '#511281'
    if grid[i][j] ==2048:
        return 'red'

def tk_display():
    for i in range(4):
        for j in range(4):
            Button(root, text=grid[i][j], font="calibri 13", bg=colorpicker(i,j),fg = 'black', height = 5, width = 15,state = 'disabled',relief = 'solid').grid(row=i, column=j)






# define random function that produce 2 or 4 in blank cell
get_num_list = [2, 4]
def get_num():
    return random.choice(get_num_list)


# define random empty cell where random number will generate
def get_random_grid():
    return random.randrange(0, 16)


# devide the get_random_grid into row and coloum
# find blank cell
def new_num_assign():

    row = get_random_grid()
    new_col = row % 4
    new_row = row // 4
    if grid[new_row][new_col] == 0:
        grid[new_row][new_col] = get_num()
    else:
        new_num_assign()

# new_num_assign()
# new_num_assign()
# tk_display()
# left swipe
def left_swap():
    for i in range(rows):
        temp = []
        for j in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0

        for assign_num in range(len(temp)):
            grid[i][assign_num] = temp[assign_num]




# right swipe
def right_swap():

    for i in range(rows):
        temp = []
        for j in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[i][cols - len(temp) + assign_num] = temp[assign_num]




# down swipe
def down_swap():
    for j in range(rows):
        temp = []
        for i in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[rows - len(temp) + assign_num][j] = temp[assign_num]


def up_swap():
    for j in range(rows):
        temp = []
        for i in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[assign_num][j] = temp[assign_num]


# left blending function
def left_blend():
    global swap
    for i in range(rows):
        for j in range(cols-1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] = 2 * grid[i][j]
                grid[i][j + 1] = 0
                swap = 1
    left_swap()


# right blending function
def right_blend():
    global swap
    for i in range(rows):
        for j in range(cols - 1, 0, -1):
            if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] = 2 * grid[i][j]
                grid[i][j - 1] = 0
                swap = 1
    right_swap()


# up_blend
def up_blend():
    global swap
    for i in range(cols):
        for j in range(rows-1):
            if grid[j][i] == grid[j + 1][i] and grid[j][i] != 0:
                grid[j][i] = 2 * grid[j][i]
                grid[j + 1][i] = 0
                swap = 1
    up_swap()


def down_blend():
    global swap
    for i in range(cols):
        for j in range(rows - 1, 0, -1):
            if grid[j][i] == grid[j - 1][i] and grid[j][i] != 0:
                grid[j][i] = 2 * grid[j][i]
                grid[j - 1][i] = 0
                swap = 1
    down_swap()



def clock():
    global sc , min ,hr
    sc= sc+1
    if sc==60:
        min =min+1
        sc = 0
    if min ==60:
        hr = hr+1
        min =0

    global cancl_timer
    #curr_time.config(text = hr + ":" + min + ":" + sc)
    curr_time.config(text ='%i:%i:%i'%(hr,min,sc))
    cancl_timer= curr_time.after(1000,clock)


def newgame():
     gird_create()
     tk_display()
     clock()
def helpme():
     help_notes ='''2048 is played on a plain 4×4 grid, with numbered tiles that slide when a player moves them using the four arrow keys.
     [3] Every turn, a new tile randomly appears in an empty spot on the board with a value of either 2 or 4.
     [4] Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid.
      If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.
      [5][6] The resulting tile cannot merge with another tile again in the same move. Higher-scoring tiles emit a soft glow,[4] and the highest possible tile is 131,072.[7]
    If a move causes three consecutive tiles of the same value to slide together, only the two tiles farthest along the direction of motion will combine.
    If all four spaces in a row or column are filled with tiles of the same value, a move parallel to that row/column will combine the first two and last two.[8]
     A scoreboard on the upper-right keeps track of the user's score.
     The user's score starts at zero, and is increased whenever two tiles combine, by the value of the new tile.[4]
    The game is won when a tile with a value of 2048 appears on the board. Players can continue beyond that to reach higher scores.
[9][10][11] When the player has no legal moves (there are no empty spaces and no adjacent tiles with the same value), the game ends.[2][12]
     '''
     top =Toplevel()
     top.resizable(height=False, width=False)
     #top.geometry('540x663')
     lbl = Label(top,text=help_notes,padx=50,pady=50).pack()
def up():
    undo_copy()
    up_swap()
    up_blend()
    if grid_compare():
        new_num_assign()
    check_full_grid()
    tk_display()
def down():
    undo_copy()
    down_swap()
    down_blend()
    if grid_compare():
        new_num_assign()
    check_full_grid()
    tk_display()
def right():
    undo_copy()
    right_swap()
    right_blend()
    if grid_compare():
        new_num_assign()
    check_full_grid()
    tk_display()
def left():
    undo_copy()
    left_swap()
    left_blend()
    if grid_compare():
        new_num_assign()
    check_full_grid()

    tk_display()

left_arrow =Button(root,text='LEFT',height = 13, width = 40,relief = 'groove',bg="#a3d2ca",command = left).grid(row=5,column=0,rowspan=2,columnspan=2)
right_arrow =Button(root,text='RIGHT',height = 13, width = 40,relief = 'groove',bg="#a3d2ca",command = right).grid(row=5,column=2,rowspan=2,columnspan=2)
up_arrow =Button(root,text='UP',height = 6, width = 25,relief = 'groove',bg="#d8ac9c",command = up).grid(row=5,column=1,columnspan=2)
down_arrow=Button(root,text='DOWN',height = 6, width = 25,relief = 'groove',bg="#d8ac9c",command = down).grid(row=6,column=1,columnspan=2)



new_game_button = Button(root,text='RESTART ',height = 5, width = 19,command = newgame,bg="#94d0cc",relief = 'solid').grid(row = 7,column = 1)
undo = Button(root,text = 'UNDO',height = 5, width = 19,relief = 'solid',bg="#eec4c4",command = undo_game).grid(row = 7,column = 0)
help_button = Button(root,text='HELP',height = 5, width = 19,relief = 'solid',bg="#f29191",command = helpme).grid(row = 7,column = 2)
curr_time = Label(root,text=" ",height = 5, width = 19,relief = 'solid',bg="#feffde")
curr_time.grid(row = 7,column = 3)




new_num_assign()
new_num_assign()
clock()
tk_display()


root.mainloop()