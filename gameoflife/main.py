import tkinter as tk

class GameOfLife():

    SQUARE_SIZE = 30
    TITLE = " Game of Life! "

    __COLOR_DEAD = "black"
    __COLOR_ALIVE = "yellow"
    __COLOR_OUTLINE = "gray"

    # rules:   0, 1, 2, 3, 4, 5, 6, 7, 8 no. of neigbor cells
    __RULES = [0, 0, 1, 2, 0, 0, 0, 0, 0] # 0: die, 1: live, 2: reproduce

    def __init__(self, row, column):
        self.width = column * GameOfLife.SQUARE_SIZE
        self.height = row * GameOfLife.SQUARE_SIZE
        self.__master = tk.Tk(className=GameOfLife.TITLE)
        self.__canvas = tk.Canvas(self.__master, width=self.width + 1, height=self.height + 1)
        self.__canvas.pack()
        self.__cells = CellLayer(row, column)

        self.__render()

        self.__canvas.bind("<Control-ButtonPress>", self.__triggered)
        self.__canvas.bind("<Shift-ButtonPress>", self.__draw)

        tk.mainloop()

    def __draw(self, event:tk.Event):
        x = event.x // GameOfLife.SQUARE_SIZE
        y = event.y // GameOfLife.SQUARE_SIZE        

        self.__cells.s(x, y, 1 if self.__cells.g(x, y) == 0 else 0)
        self.__render()
    
    def __triggered(self, event):
        self.__calculate()
        self.__render()
    
    def __render(self):
        self.__canvas.create_rectangle(0, 0, self.width, self.height, fill=GameOfLife.__COLOR_DEAD)

        for i in range(0, self.width, GameOfLife.SQUARE_SIZE):
            for j in range(0, self.height, GameOfLife.SQUARE_SIZE):
                if self.__cells.g(i // GameOfLife.SQUARE_SIZE, j // GameOfLife.SQUARE_SIZE):
                    self.__canvas.create_rectangle(1 + i, 1 + j, 1 + i + GameOfLife.SQUARE_SIZE, 1 + j + GameOfLife.SQUARE_SIZE, fill=GameOfLife.__COLOR_ALIVE, outline=GameOfLife.__COLOR_OUTLINE)
                else:
                    self.__canvas.create_rectangle(1 + i, 1 + j, 1 + i + GameOfLife.SQUARE_SIZE, 1 + j + GameOfLife.SQUARE_SIZE, fill=GameOfLife.__COLOR_DEAD, outline=GameOfLife.__COLOR_OUTLINE)
    
    def __calculate(self): # dumb way to check tiles
        row = self.height // GameOfLife.SQUARE_SIZE
        col = self.width // GameOfLife.SQUARE_SIZE

        ncell = CellLayer(row, col)

        for i in range(0, row):
            for j in range(0, col):
                adjs = self.__cells.g(i - 1, j - 1) + self.__cells.g(i - 1, j) + self.__cells.g(i - 1, j + 1) + self.__cells.g(i + 1, j - 1) + self.__cells.g(i + 1, j) + self.__cells.g(i + 1, j + 1) + self.__cells.g(i, j - 1) + self.__cells.g(i, j + 1)
                
                if self.__cells.g(i, j):    # if cell is alive
                    if GameOfLife.__RULES[adjs] != 0:
                        ncell.s(i, j, True) # cell will continue to live or born (same thing here)
                else:                       # if cell is dead
                    if GameOfLife.__RULES[adjs] == 2:
                        ncell.s(i, j, True) # cell will born
        self.__cells = ncell


class CellLayer():
    def __init__(self, row, column):
        self.__data = list()
        self.width = column
        self.height = row

        for _ in range(0, row):
            temp = list()
            for _ in range(0, column):
                temp.append(0)
            self.__data.append(temp)
    
    def g(self, row, column, default=False):
        if row < 0 or row >= self.height or column < 0 or column >= self.width:
            return default
        return True if self.__data[row][column] == 1 else False
    
    def s(self, row, column, value:bool):
        if row < 0 or row >= self.height or column < 0 or column >= self.width:
            return
        self.__data[row][column] = 1 if value else 0


if __name__ == "__main__":
    print("Warning this is the unoptimized version!", "->\tHOLD SHITF and left click with mouse to alter cells", "->\tHOLD CTRL and click anywhere to iterate", sep="\n")
    game = GameOfLife(15, 15)