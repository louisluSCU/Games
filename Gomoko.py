import argparse

class Gomoko:

    def __init__(self, size=10, player=2):
        self.size = size
        self.player = player
        self.board = [[0 for j in range(self.size)] for _ in range(self.size)]
        self.piece = {0: " ", 1: "x", 2: "o", 3: "*", 4: ""}
        self.counter = 0
        self.OVER = False
        ans = input("-------- Game ready, do you want to play? Input y/n --------\n")
        if ans == "y":
            self.play()
        else:
            print("Bye")

    def play(self):
        self.__display_board()
        while not self.OVER:
            for p in range(1, self.player + 1):
                pos = input("P{} plays: ".format(str(p)))
                x, y = pos.split()
                while self.board[int(x) - 1][int(y) - 1] != 0:
                    pos = input("Can not play here, P{} plays: ".format(str(p)))
                    x, y = pos.split()
                self.board[int(x) - 1][int(y) - 1] = p
                prev = [int(x)-1, int(y)-1]
                self.counter += 1
                self.__display_board()
                if self.__game_over(prev):
                    self.OVER = True
                    break

    def __game_over(self, prev_move):
        if self.counter == self.size ** 2:
            print("Game tied!")
            return True
        elif self.__check_vertical(prev_move[0], prev_move[1]) \
                or self.__check_horizontal(prev_move[0], prev_move[1]) \
                or self.__check_diagonal(prev_move[0], prev_move[1]):
            print("You win!")
            return True
        else:
            return False

    def __check_vertical(self, x, y):
        tmp = self.board[x][y]
        counter = 0
        i = 1
        while y - i >= 0 and self.board[x][y - i] == tmp:
            counter += 1
            i += 1
        i = 1
        while y + i < self.size and self.board[x][y + i] == tmp:
            counter += 1
            i += 1
        return counter == 4

    def __check_horizontal(self, x, y):
        tmp = self.board[x][y]
        counter = 0
        i = 1
        while x - i >= 0 and self.board[x - i][y] == tmp:
            counter += 1
            i += 1
        i = 1
        while x + i < self.size and self.board[x + i][y] == tmp:
            counter += 1
            i += 1
        return counter == 4

    def __check_diagonal(self, x, y):
        tmp = self.board[x][y]
        counter = 0
        i = 1
        while x - i >= 0 and y - i >= 0 and self.board[x - i][y - i] == tmp:
            counter += 1
            i += 1
        i = 1
        while x + i < self.size and y + i < self.size and self.board[x + i][y + i] == tmp:
            counter += 1
            i += 1
        return counter == 4

    def __display_board(self):
        print(" ", end='')
        for i in range(self.size):
            print("{} ".format(str(i + 1)), end='')
        print("\n", end='')
        for i in range(self.size):
            print(" ", end='')
            for j in range(self.size):
                print("- ", end='')
            print("\n{} ".format(str(i + 1)), end='')
            for j in range(self.size):
                print("|{} ".format(self.piece[self.board[i][j]]), end='')
            print("|\n", end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int, default=10)
    parser.add_argument('-p', '--player', type=int, default=2)
    args = parser.parse_args()

    Gomoko(args.size, args.player)
