from tkinter import *
from tkinter import ttk
from Maths_Prob import probability_of_char_list
import turtle

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

    print(most_frequent_char)

def pie_math():

    def sortbykey(elem): # sorts cc_list by frequency of characters lowest to highest
        return elem[1]

    up_probability_of_char_list = probability_of_char_list

    print('before sort',up_probability_of_char_list)

    up_probability_of_char_list.sort(key=sortbykey)

    print('after sort',up_probability_of_char_list) # check to see if probability_of_char_list was sorted

pie_math()




main_window = Tk() #creates main windows where loop takes places
main_window.geometry("600x600")

main_window.title('Main Window Test') 

main_window.columnconfigure(0,weight=1)
main_window.columnconfigure(3,weight=1)

def retrieve_input(): # retrieves input from name_label_entry
    try:
        inputValue = collect_n_label_entry.get()
        print(inputValue)
        n_frequent_character(inputValue)
    except ValueError:
        return 'Please input a number'

        
main_window_label = Label(main_window,text='This is the main window')
collect_n_label = Label(main_window, text ='insert # of most frequent chracters to search for: ')
collect_n_label.grid(column=0,row=1,columnspan=2)
collect_n_label_entry = Entry(main_window,width=30) #takes input
collect_n_label_entry.grid(column=2,row=1,columnspan=2)

def draw_graph():

    draw = turtle.Turtle() # assigns turtle to draw
    draw.pencolor('black')
    def get_pos():
        return draw.pos()

    #draw.color('red')
    def draw_grid():

        draw.speed(4)
        
        draw.penup()
        draw.setposition(-800,0)
        draw.pendown()
        draw.forward(2000)
        print(get_pos())
        
        draw.penup()
        draw.setposition(0,0)
        draw.left(90)
        print(get_pos())

        draw.setposition(0,-800)
        print(get_pos())
        draw.pendown()
        draw.forward(2000)
        print(get_pos())
        draw.penup()

    draw_grid()
    draw.setposition(0,0)
    for i in range(0,360):
        draw.pendown()
        draw.speed(0)
        draw.forward(5)
        draw.left(1)
    
    turtle.done()



proceed_button = Button(main_window, text ='Submit',width= 40,command=lambda: retrieve_input()) # submits input taken from name_label_entry sends to terminal retrieve_input()
proceed_button.grid(column=0,row=2,columnspan=2)
end_button = Button(main_window, text ='End',width= 40,command=lambda: main_window.quit() ) # closes window 
end_button.grid(column=2,row=2,columnspan=2)

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(main_window)
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    Label(newWindow,text ="This is a new window")

new_window_button = Button(main_window,text ="Click to draw graph",width=60,command=lambda:draw_graph())
new_window_button.grid(column=1,row=3,columnspan=2)


main_window.mainloop() #starts main window until closed

