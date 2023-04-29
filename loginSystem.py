from tkinter import *
import bravo_dbms_backend
import bravo_dbms_frontend
import custom_widgets

class LoginSystem:
    def __init__(self, root):
        self.root = root
        title = Label(self.root, text="Bravo Cinema", font=("Helvetica", 25, "bold"), fg="orange", bg="#46464a").pack()
        bravo_dbms_backend.create_logins_table()
        
        #frame for login system
        self.login_frame = Frame(self.root, background="#46464a")
        self.login_frame.place(x=70, y=45)

        self.login_UI()

    #to switch frames
    def delete_widgets(self):
        for widget in self.login_frame.winfo_children():
            widget.destroy()

    def check_widgets(self, *args):
        value = False
        for widget in args:
            if widget == "":
                value = False
                break
            else:
                value = True
        return value

    #this function validates the uses's username when signin up
    def username_validation(self, username):
        symbols = ["!", "“", "*","(", ")", ";", ":", ",",  "‘", "#"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a",
                   "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v",
                   "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I",
                   "O", "P", "A","S", "D", "F", "G", "H", "J", "K", "L",
                   "Z", "X", "C", "V", "B", "N", "M"]
        for symbol in symbols:
            if symbol not in username:
                for number, letter in numbers, letters:
                    if number in username and letter in username:
                        if len(username) > 7:
                            return True
                        else:
                            error_message = "Username must be atleast 8 characters"
                            return error_message
                    else:
                        error_message = "Username must contain a letter and a number"
                        return error_message
            else:
                error_message = "Username cannot have that symbol"
                return error_message

    #this function validates the uses's password when signin up
    def password_validation(self, password):
        symbols = ["!", "“", "*","(", ")", ";", ":", ",",  "‘", "#"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a",
                   "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v",
                   "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I",
                   "O", "P", "A","S", "D", "F", "G", "H", "J", "K", "L",
                   "Z", "X", "C", "V", "B", "N", "M"]
        for symbol in symbols:
            if symbol not in password:
                for number, letter in numbers, letters:
                    if number in password and letter in password:
                        if len(password) > 7:
                            return True
                        else:
                            error_message = "Password must be atleast 8 characters"
                            return error_message
                    else:
                        error_message = "Password must contain a letter and a number"
                        return error_message
            else:
                error_message = "Password cannot have that symbol"
                return error_message
        
    #login UI
    def login_UI(self, *args):
        self.delete_widgets()
        lbl_login = Label(self.login_frame, text="Login", font=("Ariel", 13, "bold"), fg="white", bg="#46464a").pack()
        #username
        lbl_username = custom_widgets.WhiteLabel(self.login_frame, text="Username:").pack(pady=5)
        txt_username = custom_widgets.GreyEntry(self.login_frame)
        txt_username.pack()
        #password
        lbl_password = custom_widgets.WhiteLabel(self.login_frame, text="Password:").pack(pady=5)
        txt_password = custom_widgets.GreyEntry(self.login_frame, show="*")
        txt_password.pack(pady=(2, 0))

        #error message
        lbl_login_error = Label(self.login_frame, bg="#46464a", fg="red", font=("Ariel", 11))
        lbl_login_error.pack()

        #clearing the entry boxes
        def clear_entries():
            txt_username.delete(0, END)
            txt_password.delete(0, END)
        
        #function for the login button
        def login():
            username = txt_username.get()
            password = txt_password.get()
            checkwidgets = self.check_widgets(username, password)
            if checkwidgets:
                if username == "admin":
                    admin_password = bravo_dbms_backend.check_admin(username)
                    if admin_password == password:
                        self.root.destroy()
                        bravo_dbms_frontend.start_admin()
                    else:
                        lbl_login_error.config(text="Invalid username or password")
##                try:
                    rec_password = bravo_dbms_backend.get_password(username)
                    if rec_password == password:
                        self.root.destroy()
                        bravo_dbms_frontend.start_user()
                        #this is where the main program will start
                    else:
                        lbl_login_error.config(text="Invalid username or password")
##                except:
##                    print('the problem')
##                    lbl_login_error.config(text="Invalid username or password")
            else:
                lbl_login_error.config(text="Please fill in your details")

        #buttons
        login_button = custom_widgets.OrangeButton(self.login_frame, text="Login", command=login).pack(pady=(2, 15))
        login_clear_button = Button(self.login_frame, text="Clear", command=clear_entries).pack()
        
        lbl_sign_up = Label(self.login_frame, text="Sign up here",
                            font=("Ariel", 10, "underline"), fg="white", bg="#46464a", cursor=("hand2"))
        lbl_sign_up.pack(pady=5)
        lbl_sign_up.bind("<Button-1>", self.signup_UI)

    #sign in UI
    def signup_UI(self, *args):
        self.delete_widgets()
        lbl_signup = Label(self.login_frame, text="Sign up", font=("Ariel", 13, "bold"), fg="white", bg="#46464a").pack()
        #username
        lbl_new_username = custom_widgets.WhiteLabel(self.login_frame, text="Username:").pack(pady=5)
        txt_new_username = custom_widgets.GreyEntry(self.login_frame)
        txt_new_username.pack()
        #password
        lbl_new_password = custom_widgets.WhiteLabel(self.login_frame, text="Password:").pack(pady=5)
        txt_new_password = custom_widgets.GreyEntry(self.login_frame, show="*")
        txt_new_password.pack()
        #confirm password
        lbl_confirm_password = custom_widgets.WhiteLabel(self.login_frame, text="Confirm Password:").pack(pady=5)
        txt_confirm_password = custom_widgets.GreyEntry(self.login_frame, show="*")
        txt_confirm_password.pack(pady=(2, 0))

        #error message
        lbl_signup_error = Label(self.login_frame, bg="#46464a", fg="red", font=("Ariel", 11))
        lbl_signup_error.pack()

        def clear_entries():
            txt_new_username.delete(0, END)
            txt_new_password.delete(0, END)
            txt_confirm_password.delete(0, END)

        #function for the login button
        def signup():
            username = txt_new_username.get()
            password = txt_new_password.get()
            password2 = txt_confirm_password.get()
            checkwidgets = self.check_widgets(username, password, password2)
            if checkwidgets:
                if password == password2:
                    result = bravo_dbms_backend.find_username(username)
                    if result == True and username != "admin":
                        bravo_dbms_backend.insert_login(username, password)
                        print("signed in")
                        self.root.destroy()
                        bravo_dbms_frontend.start_user()
                        #this is where the main program will start
                    else:
                        lbl_signup_error.config(text="Username is already taken")
                else:
                    lbl_signup_error.config(text="Password must be confirmed")
            else:
                lbl_signup_error.config(text="Please fill in your details")

        #buttons
        signup_button = custom_widgets.OrangeButton(self.login_frame, text="Sign up", command=signup).pack(pady=(2, 15))
        signup_clear_button = Button(self.login_frame, text="Clear", command=clear_entries).pack()
        
        lbl_log_in = Label(self.login_frame, text="Login here",
                            font=("Ariel", 10, "underline"), fg="white", bg="#46464a", cursor=("hand2"))
        lbl_log_in.pack(pady=5)
        lbl_log_in.bind("<Button-1>", self.login_UI)
        

def start():
    root = Tk()
    root.geometry("350x355")
    root.title("Bravo Cinema")
    root.configure(background="#46464a")
    logo = PhotoImage(file="logo.png")
    root.iconphoto(True, logo)
    login = LoginSystem(root)
    root.mainloop()   

if __name__ == "__main__":
    start()

##password = "test"
##print(password)
##enc_password = bravo_dbms_backend.encrypt_pass(password)
##print(enc_password)
##dec_password = bravo_dbms_backend.decrypt_pass(enc_password)
##print(dec_password)
##
##password = "this_is a_test"
##print(password)
##enc_password = bravo_dbms_backend.encrypt_pass(password)
##print(enc_password)
##dec_password = bravo_dbms_backend.decrypt_pass(enc_password)
##print(dec_password)

#bravo_dbms_backend.get_password("test4")
