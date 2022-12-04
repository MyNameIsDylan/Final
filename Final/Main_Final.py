import turtle
import tkinter
from tkinter import *
from Maths_Prob import probability_of_char_list

def n_frequent_character(n):
    global char_count

    temp_file = open('Final/Word.txt','a+') # opens word.txt assigns to temp_file in a+ mode
    temp_file.seek(0) # goes to the start of word.txt file
    #print(temp_file.read()) # prints the whole word.txt file

    char_track = [] # holds all characters from temp_file
    # loop to iterate through temp_file and append each char to char_track
    for line in temp_file: 
        line = line.lower()
        #print(line)
        for character in line:
            if character == '\n': #special case for \n 
                char_track.append('\ n')
            elif character != '\n':
                char_track.append(character)

    char_count = dict() # holds num of appearances of chars
    # iterates through char_track and counts appearances of every char saves to char_count
    for i in char_track:
        char_count[i]=char_count.get(i,0)+1
    #print('char count is',char_count)

    char_count_list = [] # holds letter and value (let,val) in tuple pair in list value=frequencey of letter
    maxval = n
    for i in char_count: # convert char_counts from dic to list
        #print(i,"is seen",char_count[i],"times")
        let,val = i,char_count[i]
        letandval = (let,val)
        char_count_list.append(letandval)

    def sortbykey(elem): # sorts cc_list by frequency of characters lowest to highest
        return elem[1]
    char_count_list.sort(key=sortbykey)
    #print(cc_list) # check to see if cc_list was sorted
    
    most_frequent_char =[] # hold most frequent characters 
    def N_ofhighestvalues(n):
        temp_start = -1
        while n != 0:
            char = char_count_list[temp_start][0]
            most_frequent_char.append(char)
            temp_start = temp_start - 1
            n = int(n) - 1

    N_ofhighestvalues(n)
    return most_frequent_char

main_window = tkinter.Tk() #creates main windows where loop takes places
main_window.geometry("600x600")

main_window.title('Main Window Test') 

main_window.columnconfigure(0,weight=1)
main_window.columnconfigure(3,weight=1)

def retrieve_input(): # retrieves input from name_label_entry
    try:
        inputValue = collect_n_label_entry.get()
        most_frequent_char = n_frequent_character(inputValue)
        return most_frequent_char , inputValue

    except ValueError:
        return 'Please input a number'

main_window_label = Label(main_window,text='This is the main window')
collect_n_label = Label(main_window, text ='insert # of most frequent chracters to search for: ')
collect_n_label.grid(column=0,row=1,columnspan=2)
collect_n_label_entry = Entry(main_window,width=30) #takes input
collect_n_label_entry.grid(column=2,row=1,columnspan=2)

def pie_math(most_frequent_char,n):

    def sortbykey(elem): # sorts cc_list by frequency of characters lowest to highest
        return elem[1]

    up_probability_of_char_list = probability_of_char_list
    up_probability_of_char_list.sort(key=sortbykey)
    #print('after sort',up_probability_of_char_list) # check to see if probability_of_char_list was sorted

    total_circle_degree = 360
    total_prob = 1.0
    total_n_prob = 0.0

    most_frequent_char_prob = [] # hold most frequent characters and theyre probabilty
    def N_ofhighestvalues(n):
        temp_start = -1
        while n != 0:
            char = up_probability_of_char_list[temp_start][0]
            prob = up_probability_of_char_list[temp_start][1]
            letandval = char,prob
            most_frequent_char_prob.append(letandval)
            temp_start = temp_start - 1
            n = int(n) - 1
    N_ofhighestvalues(n)
    #print(most_frequent_char_prob,'in pie_math in initiate')

    for i in most_frequent_char_prob:
        total_n_prob = total_n_prob + i[1]
    #print(total_n_prob,'in pie_math in initiate')

    most_frequent_char_area = []
    for i in most_frequent_char_prob:
        item_total_area_taken = (i[1]/total_prob) * total_circle_degree
        #print('item takes up',item_total_area_taken,'of',total_circle_degree)
        char = i[0]
        area = item_total_area_taken 
        letandval = char,area
        most_frequent_char_area.append(letandval)

    return most_frequent_char_area

def draw_graph(most_frequent_char_area):

    color_list=[]
    canvas = tkinter.Canvas(master=main_window,heigh=550,width=600)
    canvas.grid(column=0,row=4,columnspan=4)
    draw = turtle.RawTurtle(canvas)

    def draw_move(action):
        if action == 'tp_orgin':
            draw.penup()
            draw.setposition(x=0,y=0)
        else:
            pass

    def draw_tri(most_frequent_char_area):
        for i in most_frequent_char_area:
            draw_move('tp_orgin')
            draw.pendown()
            draw.forward(150)
            draw_move('tp_orgin')
            draw.right(i[1])
            draw.pendown()
            draw.forward(150)
            draw_move('tp_orgin')
    
    draw.penup()
    draw.right(90)
    draw.forward(150)
    
    draw.left(90)
    draw.fillcolor('#abafb0') #light gray
    draw.begin_fill()
    draw.pendown()
    draw.circle(150)
    draw_move('tp_orgin')

    draw.left(90)
    draw.fillcolor('#04939c') #lightblue
    draw.begin_fill()
    draw_tri(most_frequent_char_area)

    #turtle.write(arg, move=False, align=’left’, font=(‘Arial’, 8, ‘normal’)) 

def initiate():

    most_frequent_char , inputValue = retrieve_input()
    #print(most_frequent_char,'in initiate')
    #print(inputValue,'in initiate')
    most_frequent_char_area = pie_math(most_frequent_char,inputValue)
    print('char and area taken of 360',most_frequent_char_area)
    draw_graph(most_frequent_char_area)
    
proceed_button = Button(main_window, text ='Submit',width= 40,command=lambda: initiate()) # submits input taken from name_label_entry sends to terminal retrieve_input()
proceed_button.grid(column=0,row=2,columnspan=2)
end_button = Button(main_window, text ='End',width= 40,command=lambda: main_window.destroy() ) # closes window 
end_button.grid(column=2,row=2,columnspan=2)

main_window.mainloop() #starts main window until closed

