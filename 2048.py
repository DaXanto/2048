from tkinter import *
from random import randint

root = Tk()

root.title("2048")
root.geometry("600x600+300+100")
root.resizable(width=None, height=None)

canvas = Canvas(root, width=600, height=600,borderwidth=2,  bg="Ivory")

cellsize = 600/4

gride = [[None for j in range(4)]for i in range(4)]

startNumber = [2,2,2,4]

x = randint(0,3)
y = randint(0,3)

z = randint(0,3)
        
gride[x][y] = startNumber[z]

move = 0

couleurs_2048 = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

def moveUp( movePossibilities):
    global move
    for i in range(4):
        for j in range(4):
            if i > 0 and gride[j][i-1] is None and gride[j][i] is not None and movePossibilities[j][i] is True:
                        gride[j][i - 1] = gride[j][i]
                        gride[j][i] = None
                        movePossibilities[j][i] = False
                        movePossibilities[j][i - 1] = True
                        move += 1
            elif i > 0 and gride[j][i-1] == gride[j][i] and gride[j][i] is not None and movePossibilities[j][i] is True:
                gride[j][i - 1] += gride[j][i]
                gride[j][i] = None
                movePossibilities[j][i] = False
                movePossibilities[j][i - 1] = False
                move +=1
            else:
                movePossibilities[j][i] = False
                
def moveDown(movePossibilities):
    global move
    for i in range(3, -1, -1):
        for j in range(4):
            if i < 3 and gride[j][i+1] is None and gride[j][i] is not None and movePossibilities[j][i] is True:
                gride[j][i + 1] = gride[j][i]
                gride[j][i] = None
                movePossibilities[j][i] = False
                movePossibilities[j][i + 1] = True
                move += 1
            elif i < 3  and gride[j][i + 1] == gride[j][i] and gride[j][i] is not None and movePossibilities[j][i] is True:
                gride[j][i + 1] += gride[j][i]
                gride[j][i] = None
                movePossibilities[j][i] = False
                movePossibilities[j][i + 1] = False
                move += 1
            else:
                movePossibilities[j][i] = False
     

def moveLeft(movePossibilities):
    global move
    for i in range(4):
            for j in range(4):
                if j > 0 and gride[j - 1][i] is None and gride[j][i] is not None and movePossibilities[j][i] is True:
                    gride[j - 1][i] = gride[j][i]
                    gride[j][i] = None
                    movePossibilities[j][i] = False
                    movePossibilities[j - 1][i] = True
                    move += 1
                elif j > 0 and gride[j - 1][i] == gride[j][i] and gride[j][i] is not None and movePossibilities[j][i] is True:
                    gride[j - 1][i] += gride[j][i]
                    gride[j][i] = None
                    movePossibilities[j][i] = False
                    movePossibilities[j-1][i] = False
                    move += 1
                else:
                    movePossibilities[j][i] = False

def moveRight(movePossibilities):
    global move
    for i in range(4):
            for j in range(3, -1, -1):
                if j < 3 and gride[j+1][i] is None and gride[j][i] is not None and movePossibilities[j][i] is True:
                    gride[j + 1][i] = gride[j][i]
                    gride[j][i] = None
                    movePossibilities[j][i] = False
                    movePossibilities[j + 1][i] = True
                    move +=1
                elif j < 3 and gride[j+1][i] == gride[j][i] and gride[j][i] is not None and movePossibilities[j][i] is True:
                    gride[j + 1][i] += gride[j][i]
                    gride[j][i] = None
                    movePossibilities[j][i] = False
                    movePossibilities[j+1][i] = False
                    move += 1
                else:
                    movePossibilities[j][i] = False
    
    
def on_key_press(event):
    global move
    movePossibilities = [[True for j in range(4)]for i in range(4)]
    move = 0  
    while True:
 
        if event.keysym == 'Up':
            moveUp(movePossibilities)     
        elif event.keysym == 'Down':
            moveDown(movePossibilities)
        elif event.keysym == 'Left':
            moveLeft(movePossibilities)
        elif event.keysym == 'Right':
            moveRight(movePossibilities)

        count = 0
        for i in range(4):
            for j in range(4):
                if movePossibilities[j][i] == False:
                    count += 1
        if count == 16:
            break 
    canvas.delete("all")
    
    if move != 0:
        place = False
        
        while place == False:
            x = randint(0,3)
            y = randint(0,3)
            z = randint(0,3)
            if gride[x][y] == None:
                gride[x][y] = startNumber[z]
                place = True
    

    for i in range(4):
       for j in range(4):
            value = str(gride[j][i])

            canvas.create_rectangle(j * cellsize, i* cellsize, (j+1)*cellsize,(i+1)*cellsize, outline="Black",width=5)      
            if value != "None":

                canvas.create_rectangle(j * cellsize, i* cellsize, (j+1)*cellsize,(i+1)*cellsize, outline="Black", fill=couleurs_2048.get(gride[j][i],0),width=5)
                canvas.create_text(j * cellsize + cellsize/2,i* cellsize + cellsize/2, text= value,font = ( ' Helvetica' , '30' , ' bold' ))
    canvas.pack()
    root.mainloop()
    
    noMove = 0
    for i in range(4):
        for j in range(4):
            if gride[j][i] == 2048:
                print("vous avez gagné")
                root.destroy()
                exit()
            if gride[j][i] != None:
                noMove += 1
    if noMove == 16 and move == 0:
        print("vous avez perdu")
        exit()

def plateau():
    for i in range(4):
        for j in range(4):
            value = str(gride[j][i])
            canvas.create_rectangle(j * cellsize, i* cellsize, (j+1)*cellsize,(i+1)*cellsize, outline="Black", width=5)      
            if value != "None":
                canvas.create_rectangle(j * cellsize, i* cellsize, (j+1)*cellsize,(i+1)*cellsize, outline="Black", fill=couleurs_2048.get(startNumber[z],0),width=5)
                canvas.create_text(j * cellsize + cellsize/2,i* cellsize + cellsize/2, text= value,font = ( ' Helvetica' , '30' , ' bold' ))
    canvas.pack()
    root.mainloop()
                        
root.bind('<Up>', on_key_press)
root.bind('<Down>', on_key_press)
root.bind('<Left>', on_key_press)
root.bind('<Right>', on_key_press)

plateau()