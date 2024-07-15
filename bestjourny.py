from tkinter import *
import tkinter 
from PIL import Image,ImageTk
from tkinter import font
import data
import tkinter.messagebox
from tkinter import ttk
import gmplot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Initialize the main Tkinter window
root = Tk()
root.geometry("1200x600")
root.title("Best Journey for You")

# Initialize frames for different sections
formap = Frame(root)
forlogin = Frame(root)
frame1 = Frame(root)
book = Frame(root)
map1 = Frame(root)
map2 = Frame(root)

# Load data from the data module
api1 = data.apikeys1
api2 = data.apikeys2
city_list = data.datalist

font1 = font.Font(family='Georgia', size='18', weight='bold')
api1=data.apikeys1
api2=data.apikeys2

myFont = font.Font(family='Helvetica')

def choise():
    """
    Function to display the choice screen where the user can choose between a direct flight or a flight with more than one station.
    
    This function sets up the frame1 window with a background image and two buttons for the user's choice.
    
    Input: None
    
    Output: None, but it switches the displayed frame to frame1 and hides other frames (forlogin, formap, map2).
    """
    
    label1 = Label(frame1, image=photo2)
    label1.pack()
    
    btn2 = Button(frame1, text="Direct Flight", font=myFont, command=to_map, fg="red", relief=SUNKEN)
    btn2.place(x=500, y=275)
    
    btn3 = Button(frame1, text="More than one station", font=myFont, command=to_map1, fg="red", relief=SUNKEN)
    btn3.place(x=500, y=310)
    
    frame1.pack(fill='both', expand=1)
    forlogin.pack_forget()
    formap.pack_forget()
    map2.pack_forget()

def ticket():
    """
    Function to display the ticket booking screen where the user can enter travel details and proceed to payment.
    
    This function sets up the book window with a background image and several input fields for the user's travel information.
    
    Input: None
    
    Output: None, but it switches the displayed frame to book and hides the map2 frame.
    """
    label1 = Label(book,image=photo3)
    label1.pack()
    my_list=data.datelist
    my_list1=data.monthlist
    my_list2=["Yes","No"]
    name1 = Label(book, text="From",font="Times 16 italic bold").place(x=800,y=400)
    name2 = Label(book, text="TO",font="Times 16 italic bold").place(x=800,y=430)
    name3 = Label(book, text="Return",font="Times 16 italic bold").place(x=800,y=460)
    # name1.pack(side=RIGHT,padx=100,pady=50)
    nameentry3 = Entry(book,font="Times 16 italic",textvariable=namevalue3,width=20).place(x=855,y=400)
    nameentry4 = Entry(book,font="Times 16 italic", textvariable=namevalue4,width=20).place(x=855,y=430)
    cmb1 = ttk.Combobox(book,value=my_list,width=10).place(x=775,y=490)
    cmb2 = ttk.Combobox(book,value=my_list1,width=15).place(x=875,y=490)
    cmb3 = ttk.Combobox(book,value=my_list2,width=15).place(x=875,y=460)
    btn5 = Button(book, text="Payment",font="Times 16 italic bold",fg="blue",relief=SUNKEN,bg="gray").place(x=800,y=520)
    book.pack(fill='both', expand=1)
    map2.pack_forget()
    
    
def get_val():

    # print(f"{namevalue1.get(),namevalue2.get()}")
    a=data.datacheck(namevalue1.get(),namevalue2.get())
    if a==False:
        tkinter.messagebox.showinfo("Best Journey for you","Sorry we can't Find the Location")
    
def to_map():
    # image1 = Image.open("C:\map1.jpg")
    # # photo = ImageTk.PhotoImage(image1)
    label1 = Label(formap,image=photo)
    label1.pack()
    can_widget = Canvas(formap,width=1200,height=600)
    can_widget.pack()
    can_widget.create_line(0,0,500,200)
    name1 = Label(formap, text="From",font="Times 16 italic bold").place(x=600,y=465)
    name2 = Label(formap, text="TO",font="Times 16 italic bold").place(x=600,y=505)
    nameentry1 = Entry(formap,font="Times 16 italic", textvariable=namevalue1,width=40).place(x=655,y=465)
    nameentry2 = Entry(formap,font="Times 16 italic", textvariable=namevalue2,width=40).place(x=655,y=505)
    # nameentry.pack()
    btn1 = Button(formap,text="See the Route",font="Times 16 italic bold",fg="green",relief=SUNKEN,bg="gray",command=for_plot).place(x=750, y=540)
    btn5 = Button(formap, text="Back", command=choise,font="Times 16 italic bold",fg="red",relief=SUNKEN,bg="gray").place(x=780,y=590)
    formap.pack(fill='both', expand=1)
    frame1.pack_forget()
    
def to_map1():
    # image1 = Image.open("C:\map1.jpg")
    # # photo = ImageTk.PhotoImage(image1)
    label1 = Label(map1,image=photo)
    label1.pack()
    can_widget = Canvas(map1,width=1200,height=600)
    can_widget.pack()
    can_widget.create_line(0,0,500,200)
    name1 = Label(map1, text="Stop",font="Times 16 italic bold").place(x=600,y=465)
    name2 = Label(map1, text="To",font="Times 16 italic bold").place(x=600,y=505)
    name3 = Label(map1, text="From",font="Times 16 italic bold").place(x=600,y=435)
    nameentry1 = Entry(map1,font="Times 16 italic", textvariable=namevalue1,width=40).place(x=655,y=465)
    nameentry2 = Entry(map1,font="Times 16 italic", textvariable=namevalue2,width=40).place(x=655,y=505)
    nameentry2 = Entry(map1,font="Times 16 italic", textvariable=namevalue5,width=40).place(x=655,y=435)
    # nameentry.pack()
    btn1 = Button(map1,text="See Route",font="Times 16 italic bold",fg="green",relief=SUNKEN,bg="gray",command=for_plot1).place(x=750, y=540)
    btn5 = Button(map1, text="Back", command=choise,font="Times 16 italic bold",fg="red",relief=SUNKEN,bg="gray").place(x=780,y=590)
    map1.pack(fill='both', expand=1)
    frame1.pack_forget()
    
    
def to_login():
   btn2 = Button(forlogin, text="Start Your Journey",font=myFont,command=choise,fg="red",relief=SUNKEN).place(x=550,y=525)
   forlogin.pack(fill='both', expand=1)
   formap.pack_forget()
  
def for_plot1():
    city2=namevalue1.get()
    city3=namevalue2.get()
    city1=namevalue5.get()
    if city1=="" or city2=="" or city3=="":
        tkinter.messagebox.showinfo("Best Journey for you","Please Enter the city")
    elif city1.lower() in city_list and city2.lower() in city_list:
        to_map2()
        lst1=[]
        lst2=[]
        for i in range(0,len(city_list)):
            if city1.lower() == city_list[i]:
                lst1.append(api1[i])
                lst2.append(api2[i])
        for i in range(0,len(city_list)):
            if city2.lower() == city_list[i]:
                lst1.append(api1[i])
                lst2.append(api2[i])
        for i in range(0,len(city_list)):
            if city3.lower() == city_list[i]:
                lst1.append(api1[i])
                lst2.append(api2[i])
        print(lst1)
        print(lst2)
        gm = gmplot.GoogleMapPlotter(lst1[0],lst2[2],8)
        gm.scatter(lst1,lst2,'#ff000',size=50,marker=True)
        gm.plot(lst1,lst2,'blue',edge_width=2.5)
        gm.draw("map1.html")
        options = Options()
        browser = webdriver.Chrome(executable_path ='C:\SEM-3\PYTHON\Project\ONLINE FILLING THE FORM\chromedriver_win32\chromedriver.exe',chrome_options=options)
        browser.maximize_window()
        browser.get("file:///C:/SEM-3/DMGT/Practice/map1.html")
        time.sleep(400)
        # browser.implicitly_wait(30)
        # time.sleep(2)
        
    else:
        tkinter.messagebox.showinfo("Best Journey for you","Sorry we can't Find the Location")
        
    
    
def for_plot():
    city1=namevalue1.get()
    city2=namevalue2.get()
    if city1=="" or city2=="" or city1==city2:
        tkinter.messagebox.showinfo("Best Journey for you","Please Enter the city")
    elif city1.lower() in city_list and city2.lower() in city_list:
        to_map2()
        options = Options()
        browser = webdriver.Chrome(executable_path ='C:\SEM-3\PYTHON\Project\ONLINE FILLING THE FORM\chromedriver_win32\chromedriver.exe',chrome_options=options)
        browser.maximize_window()
        browser.get("https://maps.google.co.in/")
        browser.implicitly_wait(30)
        time.sleep(20)

        conti = browser.find_element(By.XPATH,'//*[@id="hArJGc"]')
        conti.click()
        time.sleep(5)

        conti1 = browser.find_element(By.XPATH,'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[6]/button/img')
        conti1.click()
        time.sleep(3)
        # //*[@id="sb_ifc50"]/input
        first_city = browser.find_element(By.XPATH, "//html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
        first_city.send_keys(city1)

        last_city = browser.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/input")
        last_city.send_keys(city2)

        search = browser.find_element(By.XPATH,'//*[@id="directions-searchbox-1"]/button[1]')
        search.click()
        time.sleep(20)
        
        
    else:
        tkinter.messagebox.showinfo("Best Journey for you","Sorry we can't Find the Location")
    
        

def to_map2():
    # image1 = Image.open("C:\map1.jpg")
    # # photo = ImageTk.PhotoImage(image1)
    label1 = Label(map2,image=photo)
    label1.pack()
    can_widget = Canvas(map2,width=1200,height=600)
    can_widget.pack()
    can_widget.create_line(0,0,500,200)
    # nameentry.pack()
    btn1 = Button(map2,text="Ticket Book",font="Times 16 italic bold",fg="green",relief=SUNKEN,bg="gray",command=ticket).place(x=750, y=540)
    btn5 = Button(map2, text="Back", command=choise,font="Times 16 italic bold",fg="red",relief=SUNKEN,bg="gray").place(x=780,y=590)
    map2.pack(fill='both', expand=1)
    formap.pack_forget()
    map1.pack_forget()
    
image1 = Image.open("map.jpg")
photo = ImageTk.PhotoImage(image1)
image2 = Image.open("image1.jpg")
photo1 = ImageTk.PhotoImage(image2)
image3 = Image.open("image3.jpg")
photo2 = ImageTk.PhotoImage(image3)
image4 = Image.open("image4.jpg")
photo3 = ImageTk.PhotoImage(image4)
namevalue1 = StringVar()
namevalue2 = StringVar()
namevalue3 = StringVar()
namevalue4 = StringVar()
namevalue5 = StringVar()
namevalue6 = StringVar()
# label1 = Label(formap, text="Hey ", foreground="green3",image=photo)
# label1 = Label(formap,image=photo)
# label1.pack()
label2 = Label(forlogin,foreground="blue",image=photo1)
label2.pack()
to_login()
# to_map1()
# choise()
# ticket()
root.mainloop()
