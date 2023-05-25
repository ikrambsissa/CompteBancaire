from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk


class BankingApp:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title('Banking App')
        self.balance = 0.0
        self.create_widgets()

    def create_widgets(self):
        img = Image.open('bnk.jpg')
        img = img.resize((150, 150))
        self.img_tk = ImageTk.PhotoImage(img)

        Label(self.fenetre, text="LA BANK", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10)
        #Label(self.fenetre, text="the most secure bank you've probably used", font=("Calibri", 12)).grid(row=1, sticky=N)
        Label(self.fenetre, image=self.img_tk).grid(row=2, sticky=N, pady=15)

        # Button(self.fenetre, text="Register", font=("Calibri", 12), width=20, command=self.register).grid(row=3, sticky=N)
        Button(self.fenetre, text="Log In", font=("Calibri", 12), width=20, command=self.authenticate).grid(row=4, sticky=N, pady=10)

    def finish_reg(self):
        messagebox.showinfo("Registration", "Registration completed.")

    def register(self):
        register_screen = Toplevel(self.fenetre)
        register_screen.title('Register')

        Label(register_screen, text="Please enter your details below to register", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
        Label(register_screen, text="Name", font=("Calibri", 12)).grid(row=1, sticky=W)
        Label(register_screen, text="Age", font=("Calibri", 12)).grid(row=2, sticky=W)
        Label(register_screen, text="Gender", font=("Calibri", 12)).grid(row=3, sticky=W)
        Label(register_screen, text="Password", font=("Calibri", 12)).grid(row=4, sticky=W)

        temp_name = StringVar()
        temp_age = StringVar()
        temp_gender = StringVar()
        temp_password = StringVar()

        Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
        Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
        Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
        Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)

        Button(register_screen, text="Register", command=self.finish_reg, font=("Calibri", 12)).grid(row=5, sticky=N, pady=10)

    def authenticate(self):
        login_screen = Toplevel(self.fenetre)
        login_screen.title('Log In')

        Label(login_screen, text="Username:", font=("Calibri", 12)).grid(row=0, sticky=W)
        Label(login_screen, text="Password:", font=("Calibri", 12)).grid(row=1, sticky=W)

        username_entry = Entry(login_screen, font=("Calibri", 12))
        username_entry.grid(row=0, column=1)
        password_entry = Entry(login_screen, show="*", font=("Calibri", 12))
        password_entry.grid(row=1, column=1)

        Button(login_screen, text="Log In", command=lambda: self.check_authentication(username_entry, password_entry), font=("Calibri", 12)).grid(row=2, columnspan=2, pady=10)

    def check_authentication(self, username_entry, password_entry):
        # Récupération des informations de connexion saisies par l'utilisateur
        username = username_entry.get()
        password = password_entry.get()

        # Ouverture du fichier login_info.txt en mode lecture
        with open("login_info.txt", "r") as file:
            lines = file.readlines()
            stored_username = lines[0].strip().split(": ")[1]
            stored_password = lines[1].strip().split(": ")[1]

        # Comparaison des informations de connexion saisies avec celles du fichier
        if username == stored_username and password == stored_password:
            messagebox.showinfo("Authentication", "Authentication successful")
            self.show_operations_window()
        else:
            messagebox.showerror("Authentication", "Authentication failed")

    def show_operations_window(self):
        operations_screen = Toplevel(self.fenetre)
        operations_screen.title('Banking Operations')
        operations_screen.geometry("300x200")  # Définition des dimensions de la fenêtre

        Button(operations_screen, text="Retirer de l'argent", command=self.withdraw_money, font=("Calibri", 12)).grid(row=0, pady=10, padx=10)
        Button(operations_screen, text="Diposer de l'argent", command=self.deposit_money, font=("Calibri", 12)).grid(row=1, pady=10, padx=10)
        Button(operations_screen, text="Afficher le Solde", command=self.check_balance, font=("Calibri", 12)).grid(row=2, pady=10, padx=10)

    def withdraw_money(self):
        messagebox.showinfo("Withdraw Money", "Performing withdrawal operation...") 
        self.fenetre.destroy() 
        newtk = Tk()  
        newtk.title("retirer")  
        newtk.geometry("300x300")
        titer = Label(newtk,text="retirer L'argent",font=("Arial",20,"bold")) 
        titer.place(x=20,y=60) 
        argent = Entry(newtk,width=30) 
        argent.place(x=20,y=100) 
        btn = Button(newtk,text="retirer",padx=15,pady=6,command=self.retirer)  
        status = Label(newtk,text="confirme",fg="blue") 
        status.place(x=20,y=180)
        btn.place(x=20,y=130) 

        newtk.mainloop()

    def retirer(self) :  

        lines = file.readlines()
        montant = int(lines[2].strip().split(": ")[1]) 
        
        print("hello welcom")
    def deposit_money(self):
        messagebox.showinfo("Deposit Money", "Performing deposit operation...")

    def check_balance(self):
        messagebox.showinfo("Check Balance", "Performing balance check operation...")

    def run(self):
        self.fenetre.mainloop()


if __name__ == '__main__':
    app = BankingApp()
    app.run() 
