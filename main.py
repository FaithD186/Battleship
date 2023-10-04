import random


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
        if self.difficulty.lower() == "hard":
            # Extra space is needed in front of letter labels to accommodate the
            # width of double-digit numbers of rows
            letter_to_print = "  "
        else:
            letter_to_print = " "

        # Print column labels (letters)
        for i in range(len(self.cols)):
            letter_to_print += " " + self.cols[i]
        print(letter_to_print)

        # Print the grid with row labels (numbers)
        for i in range(len(self.cols)):
            if self.difficulty.lower() == "hard" and i <= 9:
                # Extra space needed for single digit number labels to
                # accommodate width of double-digit numbers of rows
                row = " " + str(i) + " "
            else:
                row = str(i) + " "
            for ch in self.grid[i]:
                row += ch + " "
            print(row)

    def place_2x1_ship(self, coord, direction):
        """Returns a grid with placed 2x1 ship if given coordinates and direction
        for the ship is valid and within bounds.
        Returns None if coordinates are invalid.
        """
        # Convert letter coordinate to index number on grid (e.g. A becomes 0)
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
                    letter_coord + 2 >= len(self.cols) or \
                    coord[1] in self.cols[-2:]:
                print("\nShip is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0])][letter_coord + 1] == "." or \
                        not self.grid[int(coord[0])][letter_coord + 2] == ".":
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
                    (int(coord[0]) + 2) not in self.rows or \
                    int(coord[0]) >= self.rows[-2]:
                print("Ship is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0]) + 1][letter_coord] == "." or \
                        not self.grid[int(coord[0]) + 2][letter_coord] == ".":
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
                    letter_coord + 3 >= len(self.cols) or \
                    coord[1] in self.cols[-3:]:
                print("Ship is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0])][letter_coord + 1] == "." or \
                        not self.grid[int(coord[0])][letter_coord + 2] == "." or \
                        not self.grid[int(coord[0])][letter_coord + 3] == ".":
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
                    (int(coord[0]) + 3) not in self.rows or \
                    int(coord[0]) >= self.rows[-3]:
                print("Ship is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0]) + 1][letter_coord] == "." or \
                        not self.grid[int(coord[0]) + 2][letter_coord] == "." or \
                        not self.grid[int(coord[0]) + 3][letter_coord] == ".":
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
                    letter_coord + 4 >= len(self.cols) or \
                    coord[1] in self.cols[-4:]:
                print("Ship is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0])][letter_coord + 1] == "." or \
                        not self.grid[int(coord[0])][letter_coord + 2] == "." or \
                        not self.grid[int(coord[0])][letter_coord + 3] == "." or \
                        not self.grid[int(coord[0])][letter_coord + 4] == ".":
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
                    (int(coord[0]) + 4) not in self.rows or \
                    int(coord[0]) >= self.rows[-4]:
                print("Ship is out of bound. Please try again.")
                return None
            else:
                if not self.grid[int(coord[0]) + 1][letter_coord] == "." or \
                        not self.grid[int(coord[0]) + 2][letter_coord] == "." or \
                        not self.grid[int(coord[0]) + 3][letter_coord] == "." or \
                        not self.grid[int(coord[0]) + 4][letter_coord] == ".":
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

        Returns the updated game grid if the placement is valid, returns None
        if placement is invalid.
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

    def is_hit(self, coord, player_type):
        """Check if coordinate hit or miss a ship coordinate.
        If it is a hit, remove the coordinate from ship list and returns True.
        If it is a miss returns False"""
        for ship in self.ships:
            for coordinate in ship:
                if coordinate == (int(coord[0]), coord[1].upper()):
                    # if player_type == "human_player":
                    #     print("Your ship has been hit.")
                    ship.remove(coordinate)
                    return True
        return False

    def mark_hit_or_miss(self, coord, is_hit, player_type):
        """Modifies target grid to represent hit ('X') and misses ('O')
        Modifies on human player's grid only if it's a hit ('X')."""
        letter_coord = self.cols.index(coord[1].upper())
        if is_hit:
            self.grid[int(coord[0])][letter_coord] = "X"
        else:
            if player_type == "computer_player":
                self.grid[int(coord[0])][letter_coord] = "O"


class Player:
    """Player class for setting up player attributes, such as the player's
    guesses
    """
    def __init__(self, grid):
        self.grid = grid
        self.guesses = []

    def guess_coord(self, guess):
        """If guess is already in self.guesses, returns None.
        If guess if not in self.guesses, adds to the list of guesses"""
        if guess not in self.guesses:
            self.guesses.append(guess)
        else:
            return None


class Game:
    """Game class for handling game attributes"""
    def __init__(self, human_grid, computer_grid, current_player, next_player):
        self.human_grid = human_grid
        self.computer_grid = computer_grid
        self.next_player = next_player
        self.current_player = current_player

    def sunk_ship(self, player, opponent):
        if [] in opponent.ships:
            print("You have sunk a ship!")

    def game_over(self, human_player, computer_player):
        """When one player has sunk all their opponent's ships, the game
        is over and the player is declared the winner"""
        if all(x == [] for x in human_player.ships):
            print("You have lost! Game over.")
            return True
        if all(x == [] for x in computer_player.ships):
            print("You have won! Game over.")
            return True
        return False


def handle_input(ship_type):
    """Handles user input with placing ships on the board.

    Returns a tuple containing the coordinate (as a tuple) and the direction if
    it is a valid input, or None for invalid input.
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


def place_ship(ship_type, grid, player_type, difficulty):
    """Function for placing ships on the grid based on player type (human
    player or computer player).
    """
    if player_type == "human_player":
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

    else:
        if difficulty.lower() == "easy":
            cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
            rows = list(range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]

        elif difficulty.lower() == "medium":
            cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G"]
            rows = list(range(10))

        else:  # self.difficulty.lower == "hard"
            cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K",
                         "L", "M", "N", "O"]
            rows = list(range(15))

        placed_ship = None
        while placed_ship is None:
            dir = random.choice(["h", "v"])
            tuple_coord = (random.choice(rows), random.choice(cols))
            checker = grid.preliminary_checks(tuple_coord, dir)

            if checker is None:
                continue

            if ship_type == "2x1":
                placed_ship = grid.place_2x1_ship(tuple_coord, dir)
            elif ship_type == "3x1":
                placed_ship = grid.place_3x1_ship(tuple_coord, dir)
            elif ship_type == "4x1":
                placed_ship = grid.place_4x1_ship(tuple_coord, dir)
            elif ship_type == "5x1":
                placed_ship = grid.place_5x1_ship(tuple_coord, dir)


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
    # =========================== Board Setup ===============================

    # Setting up the grid based on chosen grid size
    difficulty_level = input("What difficulty level do you want? Choose Easy "
                             "or Medium, or Hard: ")
    while difficulty_level.lower() not in ["easy", "medium", "hard"]:
        difficulty_level = input("Invalid input. Choose Easy, Medium, or Hard: ")

    grid = Grid(difficulty_level)
    print("")
    grid.print_grid()
    print("")

    # placing the 2x1 ship
    place_ship("2x1", grid, "human_player", difficulty_level)

    # placing the 3x1 ships
    place_ship("3x1", grid, "human_player", difficulty_level)
    place_ship("3x1", grid, "human_player", difficulty_level)

    # placing the 4x1 ship
    place_ship("4x1", grid, "human_player", difficulty_level)

    # placing the 5x1 ship
    place_ship("5x1", grid, "human_player", difficulty_level)

    # Setting up computer's grid and ship placements
    print("\nThe computer will now place its ships. This process will be "
          "hidden in the final version.")
    input("Press Enter to continue...")
    print("\nThe computer will begin to place its ships:")

    computer_grid = Grid(difficulty_level)
    place_ship("2x1", computer_grid, "computer_player", difficulty_level)
    place_ship("3x1", computer_grid, "computer_player", difficulty_level)
    place_ship("3x1", computer_grid, "computer_player", difficulty_level)
    place_ship("4x1", computer_grid, "computer_player", difficulty_level)
    place_ship("5x1", computer_grid, "computer_player", difficulty_level)

    print("\nComputer's final grid:")
    computer_grid.print_grid()

    print("Computer player's ship placements:", computer_grid.ships)
    print("Human player's ship placements:", grid.ships)

    # ============================= Instructions =============================
    input("Press Enter to continue to instructions. ")
    print("\nPrepare for battle!")
    print("The target grid will be below your own grid. Guess coordinates "
          "from the target grid -- if you manage to hit a part of your "
          "opponent's ships, that coordinate will be marked with a 'X' on the"
          "target grid; if it is a miss, it will be a 'O'.\n")
    print("Your opponent will also be guessing coordinates, and if they manage "
          "to hit one of your ships, an 'X' will be marked on your grid. "
          "The first to sink all of their opponent's ships wins!")
    input("Press Enter to start...")

    # ================================= Game Setup =============================

    # Creating instances of human and computer player, as well as initializing
    # the target grid

    human_player = Player(grid)
    computer_player = Player(computer_grid)

    target_grid = Grid(difficulty_level)

    battleship_game = Game(grid, computer_grid, human_player, computer_player)

    print("Your grid:")
    grid.print_grid()

    print("Target Grid:")
    target_grid.print_grid()

    # Determine valid column and row boundaries based on difficulty level
    if difficulty_level.lower() == "easy":
        cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
        rows = list(range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]

    elif difficulty_level.lower() == "medium":
        cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G"]
        rows = list(range(10))

    else:  # self.difficulty.lower == "hard"
        cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K",
                "L", "M", "N", "O"]
        rows = list(range(15))

    # ================================= Game Loop =============================
    while not battleship_game.game_over(grid, computer_grid):
        # Human's turn first
        valid_guess = False
        tuple_guess = ()
        print("Your turn!")

        while not valid_guess:
            new_guess = input("Enter your guess, in coordinates (i.e. 1, F): ")
            # Process the guessed coordinates to ensure it's a valid guess
            # i.e. is a valid coordinate, has not been guessed, and is
            # within bound
            tuple_guess = new_guess.split(',')
            tuple_guess = [value.strip() for value in tuple_guess]
            tuple_guess = tuple(tuple_guess)

            try:
                # Check if the first part of the coordinate is a valid integer
                int_value = int(tuple_guess[0])
            except ValueError:
                print("\nInvalid coordinates. Input a letter and a number, "
                      "separated by a colon, e.g. 1, F. Please try again")
                continue

            # Check if the second part of the coordinate is a single letter
            if not (isinstance(tuple_guess[1], str) and tuple_guess[1].isalpha()):
                print("\nInvalid coordinates. Input a letter and a number, "
                      "separated by a colon, e.g. 1, F. Please try again.")
                continue
            # Check if coordinate has been guessed before
            if tuple_guess in human_player.guesses:
                print("\nYou have already guessed this coordinate. Try again.")
                continue
            # Check if coordinate is within bound
            if int(tuple_guess[0]) < 0 or int(tuple_guess[0]) >= len(cols) or \
                    tuple_guess[1].upper() not in cols:
                print("\nCoordinates are invalid. Please try again.")
                continue

            valid_guess = True
            # Add this valid guess to the list of guesses
            human_player.guesses.append(tuple_guess)

        # Modify target grid according to hit/miss
        is_hit = computer_grid.is_hit(tuple_guess, "computer_player")
        target_grid.mark_hit_or_miss(tuple_guess, is_hit, "computer_player")

        print("\nYour grid:")
        grid.print_grid()

        print("\nTarget grid:")
        target_grid.print_grid()

        if is_hit:
            print("\nIt's a hit at ", (int(tuple_guess[0]), tuple_guess[1].upper()), "!")
        else:
            print("\nIt's a miss.")

        print("Computer's remaining ships (for debugging purposes):")
        print(computer_grid.ships)

        # Check if game is over after human player's turn
        if battleship_game.game_over(grid, computer_grid):
            break

        # Computer's turn
        input("\nComputer will guess now. Press Enter to continue. ")

        # Simplest algorithm: random guesses
        tuple_guess_computer = (random.choice(rows), random.choice(cols))
        while tuple_guess_computer in computer_player.guesses:
            tuple_guess_computer = (random.choice(rows), random.choice(cols))

        # To implement: Harder algorithms - strategic guessing (guessing
        # randomly, if hit, guess coordinates around that point)

        computer_player.guesses.append(tuple_guess_computer)
        is_hit = grid.is_hit(tuple_guess_computer, "human_player")
        grid.mark_hit_or_miss(tuple_guess_computer, is_hit, "human_player")

        print("\nYour grid:")
        grid.print_grid()
        print("\nTarget grid:")
        target_grid.print_grid()

        print("\nComputer guesses", tuple_guess_computer)
        if is_hit:
            print("You've been hit at ", (int(tuple_guess_computer[0]),
                                          tuple_guess_computer[1].upper()), "!")
        else:
            print("Your ships are safe.")
