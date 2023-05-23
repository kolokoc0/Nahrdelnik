import tkinter as tk
import random

win=tk.Tk()
win.title('Necklace')

width=750
height=750
needle_x = 0
needle_y = height-40
canvas = tk.Canvas(win,width=width,height=height,bg='white')
canvas.pack()
overlap = []
done = []
cor_speed = -5
needle=tk.PhotoImage(file='koralik_nit.png')
canvas.create_image(needle_x,needle_y, image=needle, anchor=tk.NW)

colours = ["pink","yellow","green","blue"]

ball_number = 40
ball_size = 25
count = 0
vector = []

def balls_creation():
    for i in range(ball_number):
        x = random.randrange(0+ball_size,width-ball_size)
        y = random.randrange(0+ball_size, height-40-ball_size)
        canvas.create_oval(x,y,x+ball_size,y+ball_size,fill=colours[i//10],tag ="move")


def move():
    global count,overlap
    coor=canvas.coords(overlap[0])
    f_pos=[width-ball_size,height-ball_size]
    dx=(f_pos[0]-coor[0]-ball_size//2)
    dy=(f_pos[1]-coor[1]-ball_size//2)
    tag = canvas.itemcget(overlap[0],"tag")
    print(dx,dy)
    if dx!=0 and dy!=0 and tag =="prep":
        if dx>=dy and dy!=0:
            dx=dx//dy
            dy=1
        elif dx>dy and dy==0:
            dy =0
            dx = 1
        else:
            dy=dy//dx
            dx=1
        canvas.move(overlap[0],dx,dy)
    elif dx==0 and dy==0 and tag !="onning":
        canvas.itemconfig(overlap[0],tag="onning")
    elif width-ball_size*3+cor_speed-count*ball_size>=dx>=0 and dy==0 and tag =="onning":
        canvas.move(overlap[0],cor_speed,0)
    elif width-ball_size*3+cor_speed-count*ball_size<=dx and tag =="onning":
        canvas.itemconfig(overlap[0],tag = "done")
    if tag!="done":
        canvas.after(3,move)
    elif tag =="done":
        done.append(overlap[0])
        count+=1
        overlap = [ ]
        

def click(e):
    global overlap
    if len(overlap)==0 and len(done)!=10:
        overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
        tag = canvas.itemcget(overlap[0],"tag")
        tag = tag.split(" ")[0]
        if len(overlap)>=1 and tag =="move":
            canvas.itemconfig(overlap[0],tag="prep")
            move()


canvas.bind("<Button-1>",click)



balls_creation()





win.mainloop()

