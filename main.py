import customtkinter as hp


hp.set_appearance_mode("dark")
hp.set_appearance_mode("dark-blue")

def is_click():
    print('i have been clicked')



if __name__ =="__main__":
    root = hp.CTk()
    root.title('starbucks')    
    root.geometry("700x400")
    root.resizable(0, 0)
    root.columnconfigure(0, weight=1)
    root.iconbitmap('images/pngwing.com (1).ico')



    first_botton = hp.CTkButton(master=root, text="click me", command=is_click)
    first_botton.grid(row=0, column=0, pady = (20, 0), sticky='nswe')


root.mainloop()