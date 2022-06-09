import discord

from DISCORD_TOKEN import DISCORD_TOKEN

import numpy as np

dClient = discord.Client()

class TicTacToe:
    def __init__(self, p1, p2):
        board = np.zeros(9, dtype=str)

        self.board = board.reshape((3, 3))

        self.playerOne = p1
        self.playerTwo = p2

        self.whoseTurn = False

    def step(self, x, y):
        x -= 1
        y -= 1
        try:
            if self.board[x][y] != "":
                return "invalidSpace"

            self.board[x][y] = "X" if self.whoseTurn == True else "O"

        except IndexError:
            return "invalidSpace"




    def getWinner(self):
        for i in range(0, 8)
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] != "":
                    return self.board[i][0]

            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] != "":
                    return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]



@dClient.event
async def on_ready():
    print(f"{dClient.user} has connected to Discord!")

@dClient.event
async def on_message(message):
    if message.author == dClient.user:
        return

