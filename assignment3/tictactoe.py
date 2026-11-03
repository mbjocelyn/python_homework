# Task 6 

class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        for row in self.board_array:
            if row[0] != " " and row[0] == row[1] == row[2]:
                return (True, row[0] + " wins!")

        for column in range(3):
            if (
                self.board_array[0][column] != " "
                and self.board_array[0][column]
                == self.board_array[1][column]
                == self.board_array[2][column]
            ):
                return (True, self.board_array[0][column] + " wins!")

        if self.board_array[1][1] != " ":
            if (
                self.board_array[0][0]
                == self.board_array[1][1]
                == self.board_array[2][2]
            ):
                return (True, self.board_array[1][1] + " wins!")

            if (
                self.board_array[0][2]
                == self.board_array[1][1]
                == self.board_array[2][0]
            ):
                return (True, self.board_array[1][1] + " wins!")

        if all(" " not in row for row in self.board_array):
            return (True, "Cat's Game.")

        if self.turn == "X":
            return (False, "X's turn.")
        else:
            return (False, "O's turn.")


if __name__ == "__main__":
    board = Board()
    print(board)

    game_over, message = board.whats_next()

    while not game_over:
        print(message)
        move_string = input("Enter your move: ").strip().lower()

        try:
            board.move(move_string)
            print(board)
        except TictactoeException as error:
            print(error.message)

        game_over, message = board.whats_next()

    print(message)
