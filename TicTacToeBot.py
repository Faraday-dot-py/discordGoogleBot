import discord

from DISCORD_TOKEN import DISCORD_TOKEN

import numpy as np

import Constants

dClient = discord.Client()

me = "<@984668893652090960>"

class gameStorage:
    def __init__(self, game):
        self.currentGame = game

    def setGame(self, game):
        self.currentGame = game

    def getGame(self):
        return self.currentGame

currentGame = gameStorage(None)

class TicTacToe:
    def __init__(self, p1, p2):
        board = np.zeros(9, dtype=str)

        for i in range(0, len(board)):
            board[i] = Constants.BLANK

        self.board = board.reshape((3, 3))

        self.playerOne = p1
        self.playerTwo = p2

        self.whoseTurn = False

        self.life = 1

    def step(self, x, y):
        x -= 1
        y -= 1
        try:
            if self.board[x][y] != "":
                return False

            return True
            # self.board[x][y] = "X" if self.whoseTurn == True else "O"

        except IndexError:
            return False

    def getBoardString(self):
        final = """          
        {} | {} | {}
        ----------
        {} | {} | {}
        ----------
        {} | {} | {}
        """.format(self.board[0, 0],
                   self.board[1, 0],
                   self.board[2, 0],
                   self.board[0, 1],
                   self.board[1, 1],
                   self.board[2, 1],
                   self.board[0, 2],
                   self.board[1, 2],
                   self.board[2, 2])

        return final

    def getWinner(self):
        for i in range(0, 8):
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

    def getBoardMessage(self):
        return self.playerOne.mention + self.playerOne.mention + "\n" + self.getBoardString()

    def setPlayer(self, player, id):
        if player:
            self.playerOne = id
        else:
            self.playerTwo = id

    def getPlayer(self, player):
        if player:
            return self.playerOne
        else:
            return self.playerTwo



@dClient.event
async def on_ready():
    print(f"{dClient.user} has connected to Discord!")

@dClient.event
async def on_message(message):
    if message.author == dClient.user:
        return

    if message.channel.id != 984664817946218566:
        return

    msg = message.content.lower()

    author = message.author

    print(author)

    print(str(author.id) + " sent: " + msg)

    if msg.find("!newgame") == 0:
        if currentGame.getGame() != None:
            await message.channel.send(author.mention + ", a game has already begun, please wait until the current game is either canceled or is finished.")
            return

        print("New game")

        await message.channel.send("Whoever would like to play {}, say '!play' to sign up.".format(author.mention))

        currentGame.setGame(TicTacToe(message.author, None))

        return

    if msg.find("!play") == 0:
        if currentGame.getGame() == None:
            await message.channel.send(author.mention + "No game has been started. Please use !newGame to start a game.")
            return

        print("ooh, a game has been started")

        currentGame.currentGame.setPlayer(Constants.PLAYER2, author)

        game = currentGame.getGame()

        await message.channel.send(game.getBoardMessage() + "\nPlayers can move with [!move x y]")

    if msg.find("!move") == 0:
        if currentGame.getGame() == None:
            await message.channel.send(
                author.mention + "No game has been started. Please use !newGame to start a game.")
            return

        x = msg[6:msg[6:].find(" ")]
        y = msg


        game = currentGame.getGame()

        if game.step()














#IMPORTANT - DO NOT REMOVE UNDER ANY CIRCUMSTANCES!!!
dClient.run(DISCORD_TOKEN)
