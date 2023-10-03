class Grid:
    """Grid class for setting up the battleship grid
    """
    def __init__(self, difficulty):
        """
        :param difficulty: Difficulty chosen by user, determines grid size.
            - easy: 8x8 grid
            - medium: 10x10 grid
            - hard: 15x15 grid
        """
        self.difficulty = difficulty
        self.grid = []
        self.__construct_grid()
        self.cols = []
        self.rows = []
        self.__labels()
        self.ships = []

    def __construct_grid(self):
        """Create an empty grid based on chosen difficulty level
            - easy: 8x8 grid
            - medium: 10x10 grid
            - hard: 15x15 grid
        """
        if self.difficulty.lower() == "easy":
            size = 8
        elif self.difficulty.lower() == "medium":
            size = 10
        else:
            size = 15

        for i in range(size):
            row = []
            for j in range(size):
                row.append(".")
            self.grid.append(row)

    def __labels(self):
        """Sets column and row labels for the grid, depending on the difficulty
        level/grid size
        """
        if self.difficulty.lower() == "easy":
            self.cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
            self.rows = list(range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]

        elif self.difficulty.lower() == "medium":
            self.cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G"]
            self.rows = list(range(10))

        else:  # self.difficulty.lower == "hard"
            self.cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K",
                         "L", "M", "N", "O"]
            self.rows = list(range(15))

    def print_grid(self):
        """Print out current board with column labels (letters) and
        row labels (numbers)
        """
        letter_to_print = " "
        # Print column labels (letters)
        for i in range(len(self.cols)):
            letter_to_print += " " + self.cols[i]
        print(letter_to_print)

        # Print the grid with row labels (numbers)
        for i in range(len(self.cols)):
            row = str(i) + " "
            for ch in self.grid[i]:
                row += ch + " "
            print(row)

    def place_2x1_ship(self, coord, direction):
        """Returns a grid with placed 2x1 ship. Returns None if coordinates
        are invalid.
        """
        # convert letter coordinate to index number on grid (e.g. A becomes 0)
        letter_coord = self.cols.index(coord[1].upper())

        if direction == "h":
            # Check if ship will be within horizontal bounds of the board
            if letter_coord + 1 >= len(self.cols):
                print("Ship is out of bound. Please try again.")
                return None
            # Place the left end of the ship
            self.grid[int(coord[0])][letter_coord] = "<"

            # Check if the right end is already occupied
            if self.grid[int(coord[0])][letter_coord + 1] != ".":
                print("\nA ship has already been placed on those coordinates.")
                return None

            # Place the right end of the ship
            self.grid[int(coord[0])][letter_coord + 1] = ">"

            # Ship has been successfully placed.
            # Add the coordinates to ship list
            self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                               (coord[0], self.cols[letter_coord + 1])])

        else:   # direction == "v"
            # Check if ship will be within vertical bounds of the board
            if (int(coord[0]) + 1) not in self.rows:
                print("Ship is out of bound. Please try again.")
                return None
            # Place the top end of the ship
            self.grid[int(coord[0])][letter_coord] = "^"

            # Check if the bottom end is already occupied
            if self.grid[int(coord[0]) + 1][letter_coord] != ".":
                print("\nA ship has already been placed on those coordinates.")
                return None

            # Place the bottom end of the ship
            self.grid[int(coord[0]) + 1][letter_coord] = "v"

            # Ship has been successfully placed. Add the coords to ship list
            self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                               (int(coord[0]) + 1, self.cols[letter_coord])])

        return self.grid

    def place_3x1_ship(self, coord, direction):
        """Returns a grid with placed 3x1 ship. Returns None if coordinates
        are invalid.
        """
        letter_coord = self.cols.index(coord[1].upper())
        if direction == "h":
            if letter_coord + 1 >= len(self.cols) or \
                    letter_coord + 2 >= len(self.cols):
                print("Ship is out of bound. Please try again.")
                return None
            if coord[1] in self.cols[-2:]:
                print("\nShip is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0])][letter_coord + 1] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0])][letter_coord + 2] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None

                self.grid[int(coord[0])][letter_coord] = "<"
                self.grid[int(coord[0])][letter_coord + 1] = "-"
                self.grid[int(coord[0])][letter_coord + 2] = ">"

                self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                                   (int(coord[0]), self.cols[letter_coord + 1]),
                                   (int(coord[0]), self.cols[letter_coord + 2])])

        else:  # direction == 'v'
            if (int(coord[0]) + 1) not in self.rows or \
                    (int(coord[0]) + 2) not in self.rows:
                print("Ship is out of bound. Please try again.")
                return None
            if int(coord[0]) >= self.rows[-2]:
                print("Ship is out of bound.")
                return None
            else:
                if not self.grid[int(coord[0]) + 1][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0]) + 2][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None

                self.grid[int(coord[0])][letter_coord] = "^"
                self.grid[int(coord[0]) + 1][letter_coord] = "|"
                self.grid[int(coord[0]) + 2][letter_coord] = "v"

                self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                                   (int(coord[0]) + 1, self.cols[letter_coord]),
                                   (int(coord[0]) + 2, self.cols[letter_coord])])
        return self.grid

    def place_4x1_ship(self, coord, direction):
        """Returns a grid with placed 4x1 ship. Returns None if coordinates
        are invalid.
        """
        letter_coord = self.cols.index(coord[1].upper())

        if direction == "h":
            if letter_coord + 1 >= len(self.cols) or \
                    letter_coord + 2 >= len(self.cols) or\
                    letter_coord + 3 >= len(self.cols):
                print("Ship is out of bound. Please try again.")
                return None
            if coord[1] in self.cols[-3:]:
                print("\nShip is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0])][letter_coord + 1] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0])][letter_coord + 2] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0])][letter_coord + 3] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None

                self.grid[int(coord[0])][letter_coord] = "<"
                self.grid[int(coord[0])][letter_coord + 1] = "-"
                self.grid[int(coord[0])][letter_coord + 2] = "-"
                self.grid[int(coord[0])][letter_coord + 3] = ">"

                self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                                   (int(coord[0]), self.cols[letter_coord + 1]),
                                   (int(coord[0]), self.cols[letter_coord + 2]),
                                   (int(coord[0]), self.cols[letter_coord + 3])])

        else:  # direction == 'v'
            if (int(coord[0]) + 1) not in self.rows or \
                    (int(coord[0]) + 2) not in self.rows or \
                    (int(coord[0]) + 3) not in self.rows:
                print("Ship is out of bound. Please try again.")
                return None
            if int(coord[0]) >= self.rows[-3]:
                print("Ship is out of bound.")
                return None
            else:
                if not self.grid[int(coord[0]) + 1][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0]) + 2][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0]) + 3][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None

                self.grid[int(coord[0])][letter_coord] = "^"
                self.grid[int(coord[0]) + 1][letter_coord] = "|"
                self.grid[int(coord[0]) + 2][letter_coord] = "|"
                self.grid[int(coord[0]) + 3][letter_coord] = "v"

                self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                                   (int(coord[0]) + 1, self.cols[letter_coord]),
                                   (int(coord[0]) + 2, self.cols[letter_coord]),
                                   (int(coord[0]) + 3, self.cols[letter_coord])])
        return self.grid

    def place_5x1_ship(self, coord, direction):
        """Returns a grid with placed 5x1 ship. Returns None if coordinates
        are invalid.
        """
        letter_coord = self.cols.index(coord[1].upper())

        if direction == "h":
            if letter_coord + 1 >= len(self.cols) or \
                    letter_coord + 2 >= len(self.cols) or \
                    letter_coord + 3 >= len(self.cols) or \
                    letter_coord + 4 >= len(self.cols):
                print("Ship is out of bound. Please try again.")
                return None
            if coord[1] in self.cols[-4:]:
                print("\nShip is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0])][letter_coord + 1] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0])][letter_coord + 2] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0])][letter_coord + 3] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0])][letter_coord + 4] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None

                self.grid[int(coord[0])][letter_coord] = "<"
                self.grid[int(coord[0])][letter_coord + 1] = "-"
                self.grid[int(coord[0])][letter_coord + 2] = "-"
                self.grid[int(coord[0])][letter_coord + 3] = "-"
                self.grid[int(coord[0])][letter_coord + 4] = ">"

                self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                                   (int(coord[0]), self.cols[letter_coord + 1]),
                                   (int(coord[0]), self.cols[letter_coord + 2]),
                                   (int(coord[0]), self.cols[letter_coord + 3]),
                                   (int(coord[0]), self.cols[letter_coord + 4])])

        else:  # direction == 'v'
            if (int(coord[0]) + 1) not in self.rows or \
                    (int(coord[0]) + 2) not in self.rows or \
                    (int(coord[0]) + 3) not in self.rows or \
                    (int(coord[0]) + 4) not in self.rows:
                print("Ship is out of bound. Please try again.")
                return None
            if int(coord[0]) >= self.rows[-4]:
                print("Ship is out of bound.")
                return None
            else:
                if not self.grid[int(coord[0]) + 1][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0]) + 2][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0]) + 3][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None
                if not self.grid[int(coord[0]) + 4][letter_coord] == ".":
                    print("\nA ship is in the way. Pick another coordinate.\n")
                    return None

                self.grid[int(coord[0])][letter_coord] = "^"
                self.grid[int(coord[0]) + 1][letter_coord] = "|"
                self.grid[int(coord[0]) + 2][letter_coord] = "|"
                self.grid[int(coord[0]) + 3][letter_coord] = "|"
                self.grid[int(coord[0]) + 4][letter_coord] = "v"

                self.ships.append([(int(coord[0]), self.cols[letter_coord]),
                                   (int(coord[0]) + 1, self.cols[letter_coord]),
                                   (int(coord[0]) + 2, self.cols[letter_coord]),
                                   (int(coord[0]) + 3, self.cols[letter_coord]),
                                   (int(coord[0]) + 4, self.cols[letter_coord])])
        return self.grid

    def preliminary_checks(self, coord, direction):
        """Conducts preliminary checks on the validity of ship placements,
        regardless of ship types:

        - Checks if coordinates are within bounds of the board
        - Checks if the chosen coordinate is already occupied.

        Returns the updated game grid if the placement is valid,
        returns None if placement is invalid.
        """
        # Convert the letter coordinate to an index
        if not coord[1].upper() in self.cols:
            print("\nCoordinates are invalid. Please try again.")
            return None
        else:
            letter_coord = self.cols.index(coord[1].upper())

        # Check if coordinates are within bounds of the board
        if int(coord[0]) < 0 or int(coord[0]) >= len(self.cols) or \
                coord[1].upper() not in self.cols:
            print("\nCoordinates are invalid. Please try again.")
            return None

        # Check if the ship is out of bounds based on direction
        if direction == "h" and coord[1] == self.cols[-1]:
            print("\nShip is out of bound. Please try again.")
            return None
        if direction == "v" and int(coord[0]) >= self.rows[-1]:
            print("\nShip is out of bound. Please try again.")
            return None

        # Check if the chosen coordinate is already occupied
        if self.grid[int(coord[0])][letter_coord] != ".":
            print("\nA ship has already been placed on those coordinates. "
                  "Please try again.")
            return None

        return self.grid


def handle_input(ship_type):
    """Handles user input with placing ships on the board.

    Returns A tuple containing the coordinate (as a tuple)
    and the direction, or None for invalid input.
    """
    # Prompt the user for the coordinate and split it into a tuple
    coord = input("Where would you like to place your " + ship_type + " ship? Enter a "
                  "coordinate for the upper-left corner of the ship."
                  "(e.g. 1, F): ")
    tuple_coord = coord.split(',')
    tuple_coord = [value.strip() for value in tuple_coord]
    tuple_coord = tuple(tuple_coord)

    try:
        # Check if the first part of the coordinate is a valid integer
        int_value = int(tuple_coord[0])
    except ValueError:
        print("\nInvalid coordinates. Input a letter and a number, "
              "separated by a colon, e.g. 1, F. Please try again")
        return None

    # Check if the second part of the coordinate is a single letter
    if not (isinstance(tuple_coord[1], str) and tuple_coord[1].isalpha()):
        print("\nInvalid coordinates. Input a letter and a number, "
              "separated by a colon, e.g. 1, F. Please try again.")
        return None

    print("")

    # Prompt the user for the direction and ensure it's 'h' or 'v'
    dir = input("Which direction? Enter h for horizontal, v for vertical: ")
    while not (dir == "h" or dir == "v"):
        print("\nInvalid direction. Enter h for horizontal, v for vertical. "
              "Please try again")
        dir = input("Which direction? Enter h for horizontal, v for vertical: ")

    print("")

    return tuple_coord, dir


def place_ship(ship_type, grid):
    """General function for placing ships on the grid
    """
    placed_ship = None
    while placed_ship is None:
        try:
            # Get user input for ship placement
            tuple_coord, dir = handle_input(ship_type)
        except TypeError:
            continue

        # Perform preliminary checks on the chosen coordinates and direction
        checker = grid.preliminary_checks(tuple_coord, dir)
        if checker is None:
            continue

        # Place the ship on the grid based on its type
        if ship_type == "2x1":
            placed_ship = grid.place_2x1_ship(tuple_coord, dir)
        elif ship_type == "3x1":
            placed_ship = grid.place_3x1_ship(tuple_coord, dir)
        elif ship_type == "4x1":
            placed_ship = grid.place_4x1_ship(tuple_coord, dir)
        elif ship_type == "5x1":
            placed_ship = grid.place_5x1_ship(tuple_coord, dir)

    grid.print_grid()


if __name__ == '__main__':
    print("")
    print("""
                                   ~~~  Welcome to  ~~~
                                
        ██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗░██████╗██╗░░██╗██╗██████╗░
        ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██╔════╝██║░░██║██║██╔══██╗
        ██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░╚█████╗░███████║██║██████╔╝
        ██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║██║██╔═══╝░
        ██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗██████╔╝██║░░██║██║██║░░░░░
        ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~O~O~O~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")

    difficulty_level = input("What difficulty level do you want? Choose Easy, "
                             "Medium, or Hard: ")
    while difficulty_level.lower() not in ["easy", "medium", "hard"]:
        difficulty_level = input("Invalid input. Choose Easy, Medium, or Hard: ")

    grid = Grid(difficulty_level)
    print("")
    grid.print_grid()
    print("")

    # placing the 2x1 ship
    place_ship("2x1", grid)

    # placing the 3x1 ships
    place_ship("3x1", grid)
    place_ship("3x1", grid)

    # placing the 4x1 ship
    place_ship("4x1", grid)

    # placing the 5x1 ship
    place_ship("5x1", grid)

    # print(grid.ships)





