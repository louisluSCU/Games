import argparse
import random
import os
import time


class LifeGame:

    def __init__(self, size=20, thread=3):
        self.size = size
        self.cells = [[False for _ in range(size+2)] for _ in range(size+2)]
        self.thread = thread

    def start(self, auto=True):
        rand_x = [random.randint(0, self.size-1) for _ in range(int(self.size**2 / 2))]
        rand_y = [random.randint(0, self.size-1) for _ in range(int(self.size**2 / 2))]
        for x, y in zip(rand_x, rand_y):
            self.cells[x][y] = True
        if auto:
            while True:
                self.__draw()
                self.__next_state()
                time.sleep(2)
        else:
            while True:
                self.__draw()
                x, y = input("Select a cell to continue: ").split()
                x = int(x)
                y = int(y)
                while x < 1 or x > self.size or y < 1 or y > self.size:
                    x, y = input("Invalid cell, select a cell to continue: ")
                self.cells[x][y] = not self.cells[x][y]
                self.__next_state()


    def __next_state(self):
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                counter = self.cells[i-1][j-1] + self.cells[i-1][j] + self.cells[i-1][j+1] + self.cells[i][j-1] \
                        + self.cells[i][j+1] + self.cells[i+1][j-1] + self.cells[i+1][j] + self.cells[i+1][j+1]
                if counter == self.thread:
                    self.cells[i][j] = True
                elif counter == self.thread-1:
                    pass
                else:
                    self.cells[i][j] = False

    def __draw(self):
        os.system("clear")
        for i in range(1, self.size+1):
            row = ""
            for j in range(1, self.size+1):
                if self.cells[i][j]:
                    row += "◼ "
                else:
                    row += "◻ "
            print(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int, default=20)
    parser.add_argument('-t', '--thread', type=int, default=3)
    parser.add_argument('-a', '--auto', type=int, default=1)
    args = parser.parse_args()

    lg = LifeGame(args.size, args.thread)
    lg.start(args.auto)
