import random
from words import rwords
import urllib.request
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

window_color = '#142F43'
label_color = '#FFAB4C'
button_color = '#FF5F7E'
font1 = ("Helvetica", 36)
font2 = ("Helvetica", 12)


class word_window:
    def __init__(self):
        # define global variable (maybe class)
        self.correct_word = ''
        self.alpha_set = set()
        self.used_alpha = []

        # create a window
        self.window = tk.Tk()
        # name window
        self.window.title("HangMan More! More Hangman!")
        # define width and height
        window_width = 600
        window_height = 600
        # get the screen dimension
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        # choose icon
        self.window.iconbitmap('farm.ico')

        # label word
        self.label_word = ttk.Label(self.window, background=label_color, font=font1)
        self.label_word['text'] = 'Hi, word'
        self.label_word.pack(ipadx=20, ipady=20, fill='x')
        # label word meaning
        self.label_meaning = ttk.Label(self.window, background=label_color, font=font2)
        self.label_meaning['text'] = 'Hi, meaning'
        self.label_meaning.pack(ipadx=20, ipady=20, fill='x')
        # entry input alpha
        text = tk.StringVar()
        self.guess_box = ttk.Entry(self.window, textvariable=text)
        self.guess_box.pack()
        # label used alpha
        self.label_used = ttk.Label(self.window, background=label_color, font=font1)
        self.label_used['text'] = 'Hi, used'
        self.label_used.pack(ipadx=20, ipady=20, fill='x')

        # add start button bind event
        self.button_start = ttk.Button(self.window, text='Start Guess', command=self.button_start_clicked)
        self.button_start.pack()
        # add guess button bind event
        self.button_guess = ttk.Button(self.window, text='Guess the alpha', command=self.button_guess_clicked)
        self.button_guess.pack()
        self.window.mainloop()

    # define click event
    def button_start_clicked(self):
        print("Game Start!")
        # choose a word
        self.correct_word = random.choice(rwords)
        show_list = '-' * len(self.correct_word)
        self.label_word['text'] = ''.join(show_list)

        # search the meaning
        word_url = "https://www.oxfordlearnersdictionaries.com/us/definition/english/" + \
                   self.correct_word + "?q=" + self.correct_word
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"}
        req = urllib.request.Request(word_url, headers=header)
        res = urllib.request.urlopen(req)
        if res:
            long_txt = res.read().decode('UTF-8')
            soup = BeautifulSoup(long_txt, 'html.parser')
            meaning = soup.find("span", "def")
            # show the meaning as a hint
            if meaning:
                self.label_meaning['text'] = meaning.text
            # store all correct alpha
            self.alpha_set = set(self.correct_word)
            self.used_alpha = []
            print(self.alpha_set)
            print(self.used_alpha)

    def button_guess_clicked(self):
        print(self.alpha_set)
        print(self.used_alpha)
        #         show_list=[w if w in self.used_alpha else '-' for w in self.correct_word ]
        #         self.label_word['text'] =''.join( show_list )
        if len(self.alpha_set) > 0:
            guess_alpha = self.guess_box.get()
            self.used_alpha.append(guess_alpha)
            self.alpha_set.discard(guess_alpha)
            self.label_used['text'] = ''.join(self.used_alpha)
            show_list = [w if w in self.used_alpha else '-' for w in self.correct_word]
            self.label_word['text'] = ''.join(show_list)


w = word_window()
ww = w.window