from tkinter import *
from tkinter import ttk

def n_frequent_character(n):
    global char_count_list
    global char_count
    
    temp_file = open('Final/Word.txt','a+') # opens word.txt assigns to temp_file in a+ mode
    temp_file.seek(0) # goes to the start of word.txt file
    #print(temp_file.read()) # prints the whole word.txt file

    char_track = [] # holds all characters from temp_file
    # loop to iterate through temp_file and append each char to char_track
    for line in temp_file: 
        line = line.lower()
        #print(line)
        for charcter in line:
            char_track.append(charcter) 

    char_count = dict() # holds num of appearances of chars
    # iterates through char_track and counts appearances of every char saves to char_count
    for i in char_track:
        char_count[i]=char_count.get(i,0)+1
    #print('char count is',char_count)

    char_count_list = [] # holds letter and value (let,val) in tuple pair in list
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




main_window = Tk() #creates main windows where loop takes places
main_window.geometry("600x600")

main_window.title('Main Window Test') 

main_window.columnconfigure(0,weight=1)
main_window.columnconfigure(3,weight=1)

def retrieve_input(): # retrieves input from name_label_entry
    inputValue = collect_n_label_entry.get()
    print(inputValue)
    n_frequent_character(inputValue)

main_window_label = Label(main_window,text='This is the main window')
collect_n_label = Label(main_window, text ='insert # of most frequent chracters to search for: ')
collect_n_label.grid(column=0,row=1,columnspan=2)
collect_n_label_entry = Entry(main_window,width=30) #takes input
collect_n_label_entry.grid(column=2,row=1,columnspan=2)


proceed_button = Button(main_window, text ='Submit',width= 40,command=lambda: retrieve_input()) # submits input taken from name_label_entry sends to terminal
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

#new_window_button = Button(main_window,text ="Click to open a new window",width=60,command = openNewWindow)
#new_window_button.grid(column=1,row=3,columnspan=2)


main_window.mainloop() #starts main window until closed

