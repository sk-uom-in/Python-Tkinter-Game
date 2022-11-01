# _____________________________________________________________
# Welcome To the Code Of white and Black Game of SAMBBHAV KHARE
# All key Features are mentioned here:
# 1)boss key
# 2)movement
# 3)collision
# 4)cheatcodes
# 5)images
# 6)shapes
# 7)lines
# 8)background
#
#
# _____________________________________________________________
# Code Begins:


# Import libraries:-
from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint as rand
from time import *
from copy import deepcopy

# Global variables
steps = 0
nodes = 0
win_score = 0

p1_name = ""
p2_name = ""
is_timeUp = False
dirn = ""
collided = False

control = True

cheat_active = False
boss_pressed = False
ball_reached = False
gameStarted = False
paused = False
load_clicked = False
loaded_arr = []
name = ["", ""]
pos=None
pos_bar=None
xy = (50, 550, 100, 600)

# creating the HomeScreen canvas
window = Tk()
homescreen_canvas = Canvas(window, width=1280, height=720)
window.resizable(0, 0)
homescreen_canvas.pack(fill=BOTH, expand=True)
filename = PhotoImage(file="gameicon.png")
bossimage = PhotoImage(file="bosskey_img.png")
bossimage2 = PhotoImage(file="bosskey_img2.png")
homescreen_canvas.config(bg="#4F7942")
p1_var = tk.StringVar()
p2_var = tk.StringVar()
# homescreen_canvas.create_line([(0,500), (595, )],
# tag='line',width=2,fill="#dfdfdf")


class Game_window:
    def __init__(self):
        # constructor
        global load_clicked, loaded_arr
        # initialise
        # enterName()
        # self.name=[p1_name,p2_name]
        self.p = 0  # player 1 is Black =0 and player 2 is white =1
        self.passed = False
        self.won = False
        # self.clock_move()
        self.pos_array = []
        for row in range(8):
            self.pos_array.append([])
            for colummn in range(8):
                self.pos_array[row].append(None)
        self.pos_array[3][3] = 1
        self.pos_array[3][4] = 0
        self.pos_array[4][3] = 0
        self.pos_array[4][4] = 1
        if load_clicked:
            self.pos_array = deepcopy(loaded_arr)
            load_clicked = False
        self.pos_old_array = self.pos_array
    # board updation

    def gwin_update(self):
        global collided
        homescreen_canvas.delete("highlight")
        homescreen_canvas.delete("title")
        for r in range(8):
            for c in range(8):
                if self.pos_old_array[r][c] == 0:
                    homescreen_canvas.create_oval(40 + 50 * r,
                                                  40 + 50 * c,
                                                  90 + 50 * (r),
                                                  90 + 50 * (c),
                                                  tags="tile {0}-{1}".format(r,
                                                                             c),
                                                  fill="#000",
                                                  outline="#000")
                    homescreen_canvas.create_oval(40 + 50 * r,
                                                  40 + 50 * c,
                                                  90 + 50 * (r),
                                                  90 + 50 * (c),
                                                  tags="tile {0}-{1}".format(r,
                                                                             c),
                                                  fill="#111",
                                                  outline="#111")
                elif self.pos_old_array[r][c] == 1:
                    homescreen_canvas.create_oval(40 + 50 * r,
                                                  40 + 50 * c,
                                                  90 + 50 * r,
                                                  90 + 50 * c,
                                                  tags="tile {0}-{1}".format(r,
                                                                             c),
                                                  fill="#aaa",
                                                  outline="#aaa")
                    homescreen_canvas.create_oval(40 + 50 * r,
                                                  40 + 50 * c,
                                                  90 + 50 * r,
                                                  90 + 50 * c,
                                                  tags="tile {0}-{1}".format(r,
                                                                             c),
                                                  fill="#fff",
                                                  outline="#fff")
        save_game(self.pos_array)
        homescreen_canvas.update()
    # Animation shrinking and growing
        for r in range(8):
            for c in range(8):
                if self.pos_array[r][c] != self.pos_old_array[r][c] and self.pos_array[r][c] == 1:
                    homescreen_canvas.delete("{0}-{1}".format(r, c))
                    for i in range(25):
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#000",
                            outline="#000")
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#111",
                            outline="#111")
                        if i % 5 == 0:
                            sleep(0.01)
                        homescreen_canvas.update()
                        homescreen_canvas.delete("animated")
                    for i in reversed(range(25)):
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#aaa",
                            outline="#aaa")
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#fff",
                            outline="#fff")
                        if i % 5 == 0:
                            sleep(0.01)
                        homescreen_canvas.update()
                        homescreen_canvas.delete("animated")
                    homescreen_canvas.create_oval(
                        40 + 50 * r,
                        40 + 50 * c,
                        90 + 50 * r,
                        90 + 50 * c,
                        tags="tile",
                        fill="#aaa",
                        outline="#aaa")
                    homescreen_canvas.create_oval(
                        40 + 50 * r,
                        40 + 50 * c,
                        90 + 50 * r,
                        90 + 50 * c,
                        tags="tile",
                        fill="#fff",
                        outline="#fff")
                    homescreen_canvas.update()
                elif self.pos_array[r][c] != self.pos_old_array[r][c] and self.pos_array[r][c] == 0:
                    homescreen_canvas.delete("{0}-{1}".format(r, c))
                    for i in range(25):
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#aaa",
                            outline="#aaa")
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#fff",
                            outline="#fff")
                        if i % 3 == 0:
                            sleep(0.01)
                        homescreen_canvas.update()
                        homescreen_canvas.delete("animated")
                    for i in reversed(range(21)):
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#000",
                            outline="#000")
                        homescreen_canvas.create_oval(
                            40 + i + 50 * r,
                            40 + i + 50 * c,
                            90 - i + 50 * r,
                            90 - i + 50 * c,
                            tags="tile animated",
                            fill="#111",
                            outline="#111")
                        if i % 3 == 0:
                            sleep(0.01)
                        homescreen_canvas.update()
                        homescreen_canvas.delete("animated")
                    homescreen_canvas.create_oval(
                        40 + 50 * r,
                        40 + 50 * c,
                        90 + 50 * r,
                        90 + 50 * c,
                        tags="tile",
                        fill="#000",
                        outline="#000")
                    homescreen_canvas.create_oval(
                        40 + 50 * r,
                        40 + 50 * c,
                        90 + 50 * r,
                        90 + 50 * c,
                        tags="tile",
                        fill="#111",
                        outline="#111")
                    homescreen_canvas.update()
        for r in range(8):
            for c in range(8):
                if self.p == 0:
                    if is_valid(self.pos_array, self.p, r, c):
                        homescreen_canvas.delete("turn")
                        homescreen_canvas.create_text(
                            200, 500, anchor=NW, tags="turn", font=(
                                "bold bembo", 15), text="Turn: Black Player", fill="black")
                        homescreen_canvas.create_oval(68 + 50 * r,
                                                      68 + 50 * c,
                                                      32 + 50 * (r + 1),
                                                      32 + 50 * (c + 1),
                                                      tags="highlight",
                                                      fill="#00008B",
                                                      outline="#00008B")

                else:
                    if is_valid(self.pos_array, self.p, r, c):
                        homescreen_canvas.delete("turn")
                        homescreen_canvas.create_text(
                            200, 500, anchor=NW, tags="turn", font=(
                                "bold bembo", 15), text="Turn: White player", fill="white")
                        homescreen_canvas.create_oval(68 + 50 * r,
                                                      68 + 50 * c,
                                                      32 + 50 * (r + 1),
                                                      32 + 50 * (c + 1),
                                                      tags="highlight",
                                                      fill="#00008B",
                                                      outline="#00008B")
        if not self.won:
            self.score_shower()
            homescreen_canvas.update()
            self.pass_or_not()
        if self.won or collided:
            global win_score, name
            homescreen_canvas.delete(ALL)
            homescreen_canvas.create_text(200, 300, anchor=NW, font=(
                "bold bembo", 50), text=name[self.p] + " is the winner!!")
            homescreen_canvas.update()
            loadscore(name[1 - self.p], win_score)
            sleep(0.002)
            score()

    def move(self, r, c):
        self.pos_old_array = self.pos_array
        self.pos_old_array[r][c] = self.p
        self.pos_array = mover(self.pos_array, r, c)

        self.p = 1 - self.p
        self.gwin_update()

        self.pass_or_not()
        self.gwin_update()

    def score_shower(self):
        global win_score
        homescreen_canvas.delete("score")
        p1_score = 0
        p2_score = 0
        for r in range(8):
            for c in range(8):
                if self.pos_array[r][c] == 1:
                    p2_score += 1
                elif self.pos_array[r][c] == 0:
                    p1_score += 1
        homescreen_canvas.create_text(
            50, 500, anchor="w", tags="score", font=(
                "bembo", 30), fill="white", text=p2_score)
        homescreen_canvas.create_text(
            400, 500, anchor="w", tags="score", font=(
                "bembo", 30), fill="black", text=p1_score)
        win_score = max(p1_score, p2_score)

    def pass_or_not(self):
        global is_timeUp, cheat_active
        shouldpass = True
        for r in range(8):
            for c in range(8):
                if is_valid(self.pos_array, self.p, r, c):
                    shouldpass = False
        if shouldpass and not cheat_active:
            self.p = 1 - self.p
            if self.passed == True:
                self.won = True
            else:
                self.passed = True
        elif cheat_active:
            self.p = 1 - self.p
            cheat_active = False
            collided = False
            homescreen_canvas.delete("active")

        else:
            self.passed = False


def loadscore(name, score):
    with open("scoreboard.txt", "a") as file:
        file.write(name + " " + str(score) + "\n")


def mover(arr, r, c):
    arr_copy = deepcopy(arr)
    if game.p == 0:
        colour = 0
    else:
        colour = 1
    arr_copy[r][c] = colour
    list_neighbour = []
    for i in range(max(0, r - 1), min(r + 2, 8)):
        for j in range(max(0, c - 1), min(c + 2, 8)):
            if arr_copy[i][j] is not None:
                list_neighbour.append([i, j])
    convert = []
    for n in list_neighbour:
        nx = n[0]
        ny = n[1]
        if arr_copy[nx][ny] != colour:
            path = []
            dirn_x = nx - r
            dirn_y = ny - c
            temporary_x = nx
            temporary_y = ny
            while 0 <= temporary_x <= 7 and 0 <= temporary_y <= 7:
                path.append([temporary_x, temporary_y])
                value = arr_copy[temporary_x][temporary_y]
                if value is None:
                    break
                if value == colour:
                    for node in path:
                        convert.append(node)
                    break
                temporary_x += dirn_x
                temporary_y += dirn_y
    for node in convert:
        arr_copy[node[0]][node[1]] = colour
    return arr_copy


def gridmaker(wantgrid=False):
    if wantgrid:
        homescreen_canvas.create_rectangle(
            40, 40, 440, 440, outline="black", width=2)
        w = 440
        h = 440
        for i in range(40, w, 50):
            homescreen_canvas.create_line(
                [(i, 40), (i, h)], tag='grid_line', width=2)
        for i in range(40, w, 50):
            homescreen_canvas.create_line(
                [(40, i), (w, i)], tag='grid_line', width=2)
# Checks validity of move making all sorts of lines to match it


def is_valid(arr, player, r, c):
    if player == 0:
        colour = 0
    else:
        colour = 1
    if arr[r][c] is not None:
        return False
    else:
        is_neighbour = False
        list_neighbour = []
        for i in range(max(0, r - 1), min(r + 2, 8)):
            for j in range(max(0, c - 1), min(c + 2, 8)):
                if arr[i][j] is not None:
                    is_neighbour = True
                    list_neighbour.append([i, j])
        if not is_neighbour:
            return False
        else:
            validity = False
            for n in list_neighbour:
                nx = n[0]
                ny = n[1]
                if arr[nx][ny] == colour:
                    continue
                else:
                    dirn_x = nx - r
                    dirn_y = ny - c
                    temporary_x = nx
                    temporary_y = ny
                    while 0 <= temporary_x <= 7 and 0 <= temporary_y <= 7:
                        if arr[temporary_x][temporary_y] is None:
                            break
                        if arr[temporary_x][temporary_y] == colour:
                            validity = True
                        temporary_x += dirn_x
                        temporary_y += dirn_y
            return validity


def button_maker():
    global gameStarted, paused
    if gameStarted:
        # back button
        homescreen_canvas.create_rectangle(
            0, 670, 50, 720, fill="black", outline="#dfdfdf")
        homescreen_canvas.create_polygon(
            11, 702, 26, 686, 27, 713, fill="white", outline="white")
        homescreen_canvas.create_rectangle(27, 695, 48, 704, fill="white")

        # restart button
        homescreen_canvas.create_rectangle(
            450, 670, 500, 720, fill="black", outline="#dfdfdf")
        homescreen_canvas.create_arc(
            454,
            670,
            500,
            720,
            fill="#000088",
            width="3",
            style="arc",
            outline="white",
            extent=301)
        homescreen_canvas.create_polygon(
            486, 714, 491, 720, 494, 713, fill="white", outline="white")

    else:
        # back button
        homescreen_canvas.create_rectangle(
            0, 670, 50, 720, fill="black", outline="#dfdfdf")
        homescreen_canvas.create_polygon(
            11, 702, 26, 686, 27, 713, fill="white", outline="white")
        homescreen_canvas.create_rectangle(27, 695, 48, 704, fill="white")


# Handles all click events
def click(event):
    global gameStarted, paused, collided, cheat_active
    xMouse = event.x
    yMouse = event.y
    if gameStarted or load_clicked:
        # Mouse Clicks after game has started

        if 0 <= xMouse <= 50 and 670 <= yMouse <= 720:
            homescreen_canvas.delete(ALL)
            gameStarted = False
            homescreen_canvas.create_image(
                50, 100, tags="backgroundimage", image=filename, anchor=NW)
            homescreen_canvas.create_image(
                1180, 620, tags="backgroundimage", image=filename, anchor=SE)
            home()
        elif 450 <= xMouse <= 500 and 670 <= yMouse <= 720:
            start()
        # elif 250<=xMouse<=300 and 670<=yMouse<720:
        #   # paused=True
        #   gameStarted=False
        #   pause()
        else:

            r = int((event.x - 40) / 50)
            c = int((event.y - 40) / 50)
            if 0 <= r <= 7 and 0 <= c <= 7:
                if is_valid(game.pos_array, game.p, r, c):
                    game.move(r, c)

        # Mouse clicks before game started:
    elif not gameStarted and not load_clicked:
        if 172 <= xMouse <= 267 and 200 <= yMouse <= 242:
            gameStarted = True
            start()
        elif 109 <= xMouse <= 328 and 383 <= yMouse <= 421:
            howto_play()
        elif 0 <= xMouse <= 50 and 670 <= yMouse <= 720:
            homescreen_canvas.delete(ALL)
            gameStarted = False
            home()
        elif 149 <= xMouse <= 292 and 480 <= yMouse <= 519:
            homescreen_canvas.delete(ALL)
            homescreen_canvas.create_image(
                50, 100, tags="backgroundimage", image=filename, anchor=NW)
            homescreen_canvas.create_image(
                1180, 620, tags="backgroundimage", image=filename, anchor=SE)
            button_maker()
            gameStarted = True
            start()
        elif 168 <= xMouse <= 272 and 283 <= yMouse <= 322:
            score()

    elif 640 <= xMouse <= 940 and 480 <= yMouse <= 540:
        homescreen_canvas.delete("pause")
        controls()

        home()


def controls():
    global control
    if paused:

        control_win = tk.Toplevel()
        control_win.config(bg="#4F7942")
        control_win.title("Controls")
        window.withdraw()
        control_win.geometry("400x400")
        def gopause():
            control_win.destroy()
            control_win.update()
        def change_con():
            global control
            if control:
                control=False
                # control_win.delete("A&D")
            else:
                control=True
                # control_win.delete("A&D")
        if not control:
            button=ttk.Button(control_win,text=" change to A and D ",command=change_con)
            
        else:
            button=ttk.Button(control_win,text="change to left and right",command=change_con)
            # control_win.delete("L&R")
        button.pack(side=TOP)
        button2 = ttk.Button(control_win, text="back", command=gopause)
        button2.pack(side=BOTTOM)
        control_win.update()


def ball_maker():
    global ball, bar
    ball = homescreen_canvas.create_oval(xy, tags="ball", fill="blue")
    bar = homescreen_canvas.create_rectangle(
        500, 550, 505, 600, tags="bar", fill="red")
    homescreen_canvas.update()


def home():
    homescreen_canvas.create_image(
        50,
        100,
        tags="backgroundimage",
        image=filename,
        anchor=NW)
    homescreen_canvas.create_image(
        1180,
        620,
        tags="backgroundimage",
        image=filename,
        anchor=SE)
    homescreen_canvas.create_text(
        220,
        50,
        anchor="c",
        text="     Sambbhav's \n Black And White Game",
        font=(
            "bembo",
            20,
            "bold"),
        fill="orange")
    homescreen_canvas.create_rectangle(
        168, 283, 272, 322, fill="black", outline="#dfdfdf")
    homescreen_canvas.create_rectangle(
        109, 383, 328, 421, fill="black", outline="#dfdfdf")
    homescreen_canvas.create_rectangle(
        149, 480, 292, 519, fill="black", outline="#dfdfdf")
    homescreen_canvas.create_rectangle(
        172, 200, 267, 242, fill="black", outline="#dfdfdf")
    homescreen_canvas.create_text(
        220, 220, anchor="c", text="Start", font=(
            "bembo", 38), fill="orange")
    homescreen_canvas.create_text(
        220, 300, anchor="c", text="Score", font=(
            "bembo", 38), fill="orange")
    homescreen_canvas.create_text(
        220, 400, anchor="c", text="About Game", font=(
            "bembo", 38), fill="orange")
    homescreen_canvas.create_text(
        220, 500, anchor="c", text="Load", font=(
            "bembo", 38), fill="orange")
    global gameStarted
    gameStarted = False
    homescreen_canvas.update()






def enterName():
    global name, p1_name, p2_name
    name_win = tk.Toplevel()

    name_win.geometry("400x400")
    name_win.config(bg="#4F7942")
    name_win.title("Enter The Name of Players")
    window.withdraw()
    def name_saver():
        global p1_name, p2_name, name
        p1_name = p1_var.get()
        p2_name = p2_var.get()
        p1_var.set("")
        p2_var.set("")
        name[0] = p1_name
        name[1] = p2_name
        window.deiconify()
        name_win.withdraw()
        name_win.update()
    label1 = tk.Label(name_win, text="Player 1:", font=("bold bembo", 10),)
    player1 = tk.Entry(name_win, textvariable=p1_var, font=("bold bembo", 10))
    label2 = tk.Label(name_win, text="Player 2:", font=("bold bembo", 10),)
    player2 = tk.Entry(name_win, textvariable=p2_var, font=("bold bembo", 10))
    button = ttk.Button(name_win, text="Save", command=name_saver)
    label1.grid(row=0, column=0)
    player1.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    player2.grid(row=1, column=1)
    button.grid(row=3, column=1)

    name_win.update()


def start():
    global game, name, p2_name, p1_name, collided, cheat_active
    homescreen_canvas.delete(ALL)
    homescreen_canvas.create_text(
        10,
        5,
        anchor=NW,
        font=(
            "bold bembo",
            20),
        fill="orange",
        text="1)Cheat Code: Shift-Up will skip the next turn of other player 2) Screen size=1280x720")
    homescreen_canvas.create_text(
        600,
        40,
        anchor=NW,
        font=(
            "bold bembo",
            20),
        fill="orange",
        text="3)2nd cheat code to quit game on loosing is make the ball move to the bar")

    enterName()
    # p1_name=input("enter player 1 name:")
    # p2_name=input("enter palyer 2 name:")
    ball_maker()
    # collision_detection()
    name[0] = p1_name
    name[1] = p2_name
    button_maker()
    # homescreen_canvas.create_image(50,100,image=filename,anchor=NW)
    homescreen_canvas.create_image(
        1180,
        620,
        tags="backgroundimage",
        image=filename,
        anchor=SE)

    game = 0
    gridmaker(True)
    game = Game_window()
    game.gwin_update()
    # ball_maker()
    call_destroy()
    homescreen_canvas.update()


def score():
    global pos,pos_bar
    homescreen_canvas.delete(ALL)
    homescreen_canvas.create_image(
        50,
        100,
        tags="backgroundimage",
        image=filename,
        anchor=NW)
    homescreen_canvas.create_image(
        1180,
        620,
        tags="backgroundimage",
        image=filename,
        anchor=SE)
    button_maker()
    homescreen_canvas.create_text(640,10,text="LeaderBoard",font=("bold bembo",50),anchor=NW)
    
    scoreboard = []
    with open("scoreboard.txt", "r") as file:
        for line in file:
            scoreboard.append(line.split())

    def x(item): return item[1]
    scoreboard.sort(key=x, reverse=False)
    j = 0
    for x in range(len(scoreboard)):
        homescreen_canvas.create_text(400,
                                      150 + 25 * (j + 1),
                                      anchor=NW,
                                      font=("bembo",
                                            20),
                                      fill="orange",
                                      text=scoreboard[x])
        # print(scoreboard[x])
        j += 1


def howto_play():
    homescreen_canvas.delete(ALL)
    homescreen_canvas.create_image(
        50,
        100,
        tags="backgroundimage",
        image=filename,
        anchor=NW)
    homescreen_canvas.create_image(
        1180,
        620,
        tags="backgroundimage",
        image=filename,
        anchor=SE)
    button_maker()
    # homescreen_canvas.create_rectangle(50,50,300,400,fill="black",outline="#dfdfdf")
    homescreen_canvas.create_text(
        220, 20, anchor="c", text="About Game", font=(
            "bembo", 20, "bold"), fill="orange")
    homescreen_canvas.create_text(
        200,
        100,
        anchor="c",
        text="1)Player with maximum no.\n of pieces of his colour wins",
        font=(
            "bembo",
            20,
            "bold"),
        fill="orange")
    homescreen_canvas.create_text(
        220, 200, anchor="c", text="2)Black always moves first.", font=(
            "bembo", 20, "bold"), fill="orange")
    homescreen_canvas.create_text(
        240,
        300,
        anchor="c",
        text="3)A move is made by placing a disc of the player's \n color on the board in a position that \n out-flanks one or more of the opponent's discs.",
        font=(
            "bembo",
            20,
            "bold"),
        fill="orange")
    homescreen_canvas.create_text(
        220,
        400,
        anchor="c",
        text="4)A disc or row of discs is outflanked when \n it is surrounded at the \n ends by discs of the opposite color.",
        font=(
            "bembo",
            20,
            "bold"),
        fill="orange")
    homescreen_canvas.create_text(
        220,
        500,
        anchor="c",
        text="5)A disc may outflank any number of discs \n in one or more rows in any \n direction (horizontal, vertical, diagonal).",
        font=(
            "bembo",
            20,
            "bold"),
        fill="orange")
    homescreen_canvas.update()


def motion(event):
    print("Mouse Position:(%s %s)" % (event.x, event.y))
    return


def save_game(arr):
    arr
    s = ""
    with open("pause_list.txt", "a") as myfile:
        for r in range(8):
            for c in range(8):
                s = str(arr[r][c]) + "\n"
                myfile.write(s)


def load_game():
    global load_clicked, loaded_arr
    load_clicked = True
    for r in range(8):
        for c in range(8):
            with open("pause_list.txt", "rt") as myfile:
                loaded_arr[r][c] = str(myfile.readlines())

def pause(event):
    global paused,gameStarted
    if gameStarted:
        gameStarted=False
        paused=True
        pause_win = tk.Toplevel()
        pause_win.config(bg="#4F7942")
        pause_win.title("Game paused")
        window.withdraw()
        pause_win.geometry("400x400")
        def resume():
            global gameStarted
            pause_win.destroy()
            pause_win.update()
            window.deiconify()
            gameStarted=True
        button = ttk.Button(pause_win, text="Resume", command=resume)
        button2=ttk.Button(pause_win,text="Controls",command=controls)
        button3=ttk.Button(pause_win,text="Quit",command=quit)
        button.pack(side=TOP)
        button2.pack(side=BOTTOM)
        button3.pack()
        pause_win.update()
# Boss Key
def boss_key(event):
    global bossimage, boss_pressed, paused
    if boss_pressed == False:
        homescreen_canvas.create_image(
            1280, 720, tags="bosskey", image=bossimage2, anchor=SE)
        homescreen_canvas.create_image(
            0, 0, tags="bosskey", image=bossimage, anchor=NW)
        # window.update()
        homescreen_canvas.config(bg="black")
        window.update() 
        boss_pressed = True

    else:
        homescreen_canvas.delete("bosskey")
        homescreen_canvas.config(bg="#4F7942")
        window.update()
        boss_pressed = False


def cheat_code(event):
    global cheat_active, collided
    if not cheat_active:
        cheat_active = True
        # collided=True
        homescreen_canvas.create_text(500, 50, anchor=NW, tag="active", font=(
            "bold bembo", 50), fill="orange", text="Cheat Code Activated")


def resume(event):
    if not gameStarted and paused:
        load_game()
        start()


def leftkey(event):
    global gameStarted, dirn
    if gameStarted:
        dirn = "left"
        homescreen_canvas.move(ball, -10, 0)
    collision_detection()


def rightkey(event):
    global gameStarted, dirn
    if gameStarted:
        dirn = "right"
        homescreen_canvas.move(ball, 10, 0)
    collision_detection()


def collision_detection():
    global collided,pos,pos_bar
    pos = homescreen_canvas.coords(ball)
    pos_bar = homescreen_canvas.coords(bar)
    if (pos[2] >= pos_bar[0]):
        collided = True
        homescreen_canvas.move(ball, -400, 0)
        homescreen_canvas.update()
        window.destroy()    
def call_destroy():
    if collided:
        window.destroy()
home()
homescreen_canvas.bind('<Button-1>', click)
homescreen_canvas.bind('<Escape>', boss_key)
homescreen_canvas.bind('<Shift-Up>', cheat_code)
homescreen_canvas.bind('<a>', leftkey)
homescreen_canvas.bind('<d>', rightkey)
homescreen_canvas.bind('<Left>', leftkey)
homescreen_canvas.bind('<Right>', rightkey)

homescreen_canvas.bind('<p>', pause)

homescreen_canvas.focus_set()
window.title("Black & White Game")

window.mainloop()
