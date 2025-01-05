import random
import tkinter as tk
from tkinter import ttk, messagebox


""" This class provides a tkinter page to play a guess_game with computer """
class Guess():
   
    """ Making the first page of the game to get the guess range from the user """
    def window(self):
        global window
        window = tk.Tk()
        
        window.geometry('640x480')
        window.title('GUESS GAME')
        window.resizable(height=False, width=False)

        welcome_label = ttk.Label(text='Welcome to our guess game', font=('', 20)).place(x=100, y=20)

        range_label = ttk.Label(text="Set the Range", font=("Arial", 12)).place(x=30, y=150)

        """ Making the first number entry """
        global first_num
        first_num = tk.IntVar()
        first_num_entry = ttk.Entry(master=window, textvariable=first_num).place(x=150, y=200)
        first_num_label = tk.Label(text='From: ').place(x=100, y=200)

        """ Making the last number entry """
        global last_num
        last_num = tk.IntVar(value=100)
        last_num_entry = ttk.Entry(master=window, textvariable=last_num).place(x=150, y=250)
        last_num_label = tk.Label(text='To: ').place(x=100, y=250)

        press_button = ttk.Button(text="Set", command=self.get_values).place(x=400, y=225)

        window.mainloop()

    def get_values(self):
        """ A method to get the value of numbers and store them in a variable"""
        try:

            global f_num, l_num
            f_num = first_num.get()
            l_num = last_num.get()

            global number
            number = random.randint(f_num, l_num)

            window.destroy()
            self.game_window()

            return number


        except (tk.TclError, NameError) as e:

            messagebox.showerror("Invalid", "Please Enter a Valid Number")

    def game_window(self):
        """ Making te second page and play the game """

        global game_window
        game_window = tk.Tk()
        game_window.title("Guess")
        game_window.geometry("640x480")
        game_window.resizable(height=False, width=False)


        Range_label = ttk.Label(text=f"You should guess between {f_num} and {l_num}", font=("Arial", 16)).place(x=100, y=50)

        """ Making user's guesses entry """
        global guess
        guess = tk.IntVar()
        guess_entry = ttk.Entry(textvariable=guess)
        guess_entry.place(x=258, y=200)
        guess_entry.focus()
        guess_l = ttk.Label(text="What is your guess: ", font=('Arial', 12)).place(x=250, y=150)

        submit_b = ttk.Button(text="Submit", 
                              command=lambda:[self.get_guess(), self.result(), guess_entry.delete(0, tk.END), guess_entry.focus()]).place(x=280,y=250)
        return_b = ttk.Button(text="Return", command=lambda:[game_window.destroy(), self.window()])
        return_b.place(x=500, y=400)


    def get_guess(self):

        """ Getting the values of user's guess and store it in a variable """

        try:

            global user_guess
            user_guess = guess.get()
            return user_guess

        except tk.TclError:

            messagebox.showerror("Invalid", "PLease Enter a Valid Number")


    def result(self):
        """ Comparing user's guess with number """

        # Just a counter
        c = 9

        try:

            if c != 0:

                if user_guess == number:
                    messagebox.showinfo("Perfect", "Congrats, the number is {}".format(user_guess))

                    game_window.destroy()

                elif user_guess < number:
                    messagebox.showwarning("Too Low", "You should guess higher")
                    c = c - 1

                elif user_guess > number:
                    messagebox.showwarning("Too High", "You should guess lower")
                    c = c - 1

            else:
                messagebox.showerror("Game Over", "Sorry you are running out of lives")
                game_window.destroy()


        except NameError:
            pass


x = Guess()
x.window()