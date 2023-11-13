import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("400x400")  # Set the window size to 400x400 pixels

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None] * 3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = ttk.Button(self.window, text='', style='TButton',
                                                command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j, sticky="nsew")
                self.window.grid_rowconfigure(i, weight=1)
                self.window.grid_columnconfigure(j, weight=1)

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 24, 'bold'))

        # Set colors for 'X' and 'O'
        style.map('X.TButton', foreground=[('active', 'blue'), ('!active', 'blue')],
                  background=[('active', 'lightgray'), ('!active', 'lightgray')])
        style.map('O.TButton', foreground=[('active', 'red'), ('!active', 'red')],
                  background=[('active', 'lightgray'), ('!active', 'lightgray')])

        self.stop_button = ttk.Button(self.window, text='Stop Game', command=self.stop_game)
        self.stop_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col]['state'] = 'disabled'
            self.buttons[row][col]['style'] = f'{self.current_player}.TButton'

            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def stop_game(self):
        response = messagebox.askyesno("Stop Game", "Do you really want to stop the game?")
        if response:
            self.window.destroy()

    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
                    all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
                all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['state'] = 'normal'
                self.buttons[i][j]['style'] = 'TButton'
        self.current_player = 'X'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
