import turtle
import tkinter
from tkinter import Label,Entry,Button
from Maths_Prob import probability_of_all_characters_list

def n_frequent_character(n):
    global character_appearances

    word_file = open('Final\Word.txt','a+') # opens word.txt assigns to word_file in a+ mode
    word_file.seek(0) # goes to the start of word.txt file

    characters_in_file = [] # holds all characters from word_file
    # loop to iterate through word_file and append each char to characters_in_file
    for line in word_file: 
        line = line.lower()
        for character in line:
            if character == '\n': #special case for \n 
                characters_in_file.append('\ n')
            elif character != '\n':
                characters_in_file.append(character)

    character_appearances_dict = dict() # holds character and number of apperances
    # iterates through characters_in_file and counts appearances of every char saves to character_appearances
    for i in characters_in_file: 
        character_appearances_dict[i]=character_appearances_dict.get(i,0)+1

    

    character_appearances_list = [] # holds letter and value (let,val) in tuple pair in list value=appearances of letter
    for i in character_appearances_dict: # converts character_appearances from dict to list
        letter,appearances = i,character_appearances_dict[i]
        letter_and_appearances = (letter,appearances)
        character_appearances_list.append(letter_and_appearances)

    def sortbykey(elem): # sorts character_appearances_list by frequency of characters lowest to highest
        return elem[1]
    character_appearances_list.sort(key=sortbykey)
    
    n_most_frequent_characters =[] # hold most frequent characters 
    def N_ofhighestvalues(n): # get n(number) of highest value chracters in list
        temp_start = -1
        while n != 0:
            char = character_appearances_list[temp_start][0]
            n_most_frequent_characters.append(char)
            temp_start = temp_start - 1
            n = int(n) - 1

    N_ofhighestvalues(n)
    return n_most_frequent_characters

def pie_math(n_most_frequent_characters,n):
    def sortbykey(elem): # sorts cc_list by frequency of characters lowest to highest
        return elem[1]

    update_probability_of_char_list = probability_of_all_characters_list
    update_probability_of_char_list.sort(key=sortbykey) # sorts characters and theyre probability lowest to highest

    total_circle_degree = 360
    total_prob = 1.0

    n_most_frequent_characters_prob = [] # hold most frequent characters and theyre probabilty
    def N_ofhighestvalues(n): # get n(number) of highest value chracters in list and theyre probability
        temp_start = -1
        while n != 0:
            character = update_probability_of_char_list[temp_start][0]
            probability = update_probability_of_char_list[temp_start][1]
            character_and_probability = character,probability
            n_most_frequent_characters_prob.append(character_and_probability)
            temp_start = temp_start - 1
            n = int(n) - 1
    N_ofhighestvalues(n)

    n_most_frequent_characters_angle = []
    for i in n_most_frequent_characters_prob:
        item_angle = round((i[1]/total_prob) * total_circle_degree,3)
        character = i[0]
        angle = item_angle
        character_and_angle = character,angle
        n_most_frequent_characters_angle.append(character_and_angle)

    other_characters_total_prob = 0.0
    total = 0
    for item in n_most_frequent_characters_prob:
        total = total + item[1]
    other_characters_total_prob = 1.0-total

    return n_most_frequent_characters_angle,n_most_frequent_characters_prob,other_characters_total_prob

def draw_graph(n_most_frequent_characters_angle,n_most_frequent_characters_prob,other_characters_total_prob):

    canvas = tkinter.Canvas(master=main_window,heigh=550,width=600) # creates canvas inside of main_window with sepcified height and width
    canvas.grid(column=0,row=4,columnspan=4) # specifies where canvas is located based on grid format
    draw = turtle.RawTurtle(canvas)
    draw.speed(0)
    color_palette = ['#c3d608','#328cc1','#0b3c5d','#1d2731','#ff3636','#','#','#','#','#']
    def draw_move(action):
        if action == 'tp_orgin':
            draw.setposition(x=0,y=0)
        else:
            pass
    def draw_tri():
        color_track = 1
        for item in n_most_frequent_characters_angle:
            if item != n_most_frequent_characters_angle[0]:
                draw.color('black',color_palette[color_track])
                draw.begin_fill()
                draw.pendown()
                draw.setposition(x1,y1)
                for j in range(int(item[1])):
                    draw.pendown()
                    draw.forward(3)
                    draw.right(1)
                x1,y1 = draw.pos()
                draw_move('tp_orgin')
                draw.end_fill()
                color_track = color_track + 1
            elif item == n_most_frequent_characters_angle[0]:  
                draw.setheading(90)
                draw.color('black',color_palette[0])
                draw.begin_fill()
                draw.pendown()
                draw.forward(180) # go to top of circle
                draw.right(90) # turn right face east
                for j in range(int(item[1])):
                    draw.pendown()
                    draw.forward(3)
                    draw.right(1)
                x1,y1 = draw.pos()
                draw_move('tp_orgin')
                draw.end_fill()

    draw.penup()
    draw.left(90)
    draw.forward(180) 
    draw.color('black','#dee2e6')
    draw.right(90)
    draw.begin_fill()
    draw.pendown()
    for i in range(360):
        draw.pendown()
        draw.forward(3)
        draw.right(1)
    draw.end_fill()
    draw_move('tp_orgin')
    draw_tri()

    prob_count = 0
    for item in n_most_frequent_characters_angle:
        draw.penup()
        draw_move('tp_orgin')
        draw.setheading(90)
        current_write = item[0],n_most_frequent_characters_prob[prob_count][1]
        if item == n_most_frequent_characters_angle[0]:
            total_angle = item[1]
            original_placement = (item[1]/2)
            draw.right(original_placement)
            draw.forward(200)
            draw.write(current_write, font=('Calibri',11,'normal'))
            prob_count = prob_count + 1
        elif item != n_most_frequent_characters_angle[0]:
            original_placement = total_angle + (item[1]/2)
            total_angle = total_angle + item[1]
            draw.right(original_placement)
            draw.forward(200)
            draw.write(current_write, font=('Calibri',11,'normal'))
            prob_count = prob_count + 1

    current_write = 'all other characters', other_characters_total_prob
    draw.penup()
    draw_move('tp_orgin')
    draw.setheading(90)
    draw.right(310)
    draw.forward(290)
    draw.write(current_write, font=('Calibri',11,'normal'))
    

def initiate():
    n_most_frequent_characters , inputValue = retrieve_input()
    n_most_frequent_characters_angle,n_most_frequent_characters_prob,other_characters_total_prob = pie_math(n_most_frequent_characters,inputValue)
    print('character and probability',n_most_frequent_characters_prob)
    print('character and angle',n_most_frequent_characters_angle)
    try:
        draw_graph(n_most_frequent_characters_angle,n_most_frequent_characters_prob,other_characters_total_prob)
    except tkinter.TclError:
        print('Ended window before finishing drawing')

main_window = tkinter.Tk() #creates main windows where loop takes places
main_window.geometry("600x600") # sets height and width of main_window
main_window.title('Main Window Test') # set name of main_window

main_window.columnconfigure(0,weight=1)
main_window.columnconfigure(3,weight=1)

def retrieve_input(): # retrieves input from name_label_entry
    try:
        inputValue = collect_n_label_entry.get()
        n_most_frequent_characters = n_frequent_character(inputValue)
        return n_most_frequent_characters , inputValue
    except ValueError:
        return 'Please input a number'

main_window_label = Label(main_window,text='This is the main window')
collect_n_label = Label(main_window, text ='insert # of most frequent chracters to search for: ')
collect_n_label.grid(column=0,row=1,columnspan=2)
collect_n_label_entry = Entry(main_window,width=30) # creates and takes input
collect_n_label_entry.grid(column=2,row=1,columnspan=2) 
    
submit_button = Button(main_window, text ='Submit',width= 40,command=lambda: initiate()) # submits input taken from name_label_entry sends to terminal retrieve_input()
submit_button.grid(column=0,row=2,columnspan=2)
end_button = Button(main_window, text ='End',width= 40,command=lambda: main_window.destroy() ) # closes window 
end_button.grid(column=2,row=2,columnspan=2)

main_window.mainloop() #starts main window until closed