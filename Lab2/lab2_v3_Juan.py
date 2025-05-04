import copy

class Nim(object):
    def __init__(self, board):
        self.board = board

    # Implement any additional functions needed here
    @staticmethod
    def num_moves(board):
        """ Evaluate the boards position value by adding all values """
        total = 0
        for pile in board:
            total += pile
        return total

    def updateBoard(self, pile_num, sticks_num):
        if pile_num < 0 or pile_num >= len(self.board) or sticks_num <= 0 or sticks_num > self.board[pile_num]:
            print("\nThe move specified is incorrect! Please try again\n")
            return False

        if sticks_num == self.num_moves(self.board):
            print("\nThe move specified makes you lose! Please reconsider\n")
            return False

        self.board[pile_num] = self.board[pile_num] - sticks_num
        return True

    def evaluateGame(self):
        if self.num_moves(self.board) == 1:
            print("\nThe game is over!\n")
            return False
        return True

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        """
        Minimax with alpha-beta pruning algorithm

        Parameters:
        - board: 1d matrix where each entry represents pile and value in the entry represents number of sticks
        - depth: depth
        - maximizing_player: boolean which is equal to True when the player tries to maximize the score
        - alpha: alpha variable for pruning
        - beta: beta variable for pruning 
        Returns:
        - Best value 
        - Everything needed to identify next move

        """
        if depth == 0 or self.num_moves(board) == 0:
            if maximizing_player:
                return 1, (-1, -1)
            else:
                return -1, (-1, -1)

        if maximizing_player:
            maxVal = -float("inf")
            next_move = (-1, -1)
            for pile_num in range(len(board)):
                for num_sticks in range(0, board[pile_num]):
                    child = copy.deepcopy(board)
                    child[pile_num] = num_sticks
                    value, ret_next_move = self.minimax(child, depth - 1, False, alpha, beta)
                    if value >= maxVal:
                        if next_move[1] == -1 or (maxVal == value and next_move[1] < (board[pile_num] - num_sticks)) or value > maxVal:
                            next_move = (pile_num, board[pile_num] - num_sticks)
                        maxVal = value
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break

                if beta <= alpha:
                    break
            return maxVal, next_move
        else:
            minVal = float("inf")
            next_move = (-1, -1)
            for pile_num in range(len(board)):
                for num_sticks in range(0, board[pile_num]):
                    child = copy.deepcopy(board)
                    child[pile_num] = num_sticks
                    value, ret_next_move = self.minimax(child, depth - 1, True, alpha, beta)
                    if value <= minVal:
                        if next_move[1] == -1 or (minVal == value and next_move[1] < (board[pile_num] - num_sticks)) or value < minVal:
                            next_move = (pile_num, board[pile_num] - num_sticks)
                        minVal = value
                    beta = min(beta, value)
                    if beta <= alpha:
                        break

                if beta <= alpha:
                    break
            return minVal, next_move

    def agent_decision(self):
        _, move = self.minimax(self.board, sum(self.board), True, -float("inf"), float("inf"))
        return move


if __name__ == "__main__":

    """
    Main game loop
    Firtsly, allow player to choose how many piles will be in the game and number of sticks in each pile

    Implement the game loop
    """

    print("Starting Nim!")

    # initializing size of the game board
    ele = int(input("Input the number of piles "))
    piles = []

    print("Input the number of sticks in each pile (separate with ENTER)")
    for _ in range(ele):
        piles.append(int(input()))

    game = Nim(piles)
    print("Enter the pile to remove from (starting from 0), then space followed by enter the number of sticks to remove")
    print("The person who removes the last stick loses!")
    print("Example: to remove from 2nd pile 3 sticks , enter 2 3")

    player_turn = True
    game_continues = True
    while game_continues:
        print("Pile state %s" % (game.board))
        # Your code starts here

        incorrect_move = True
        while incorrect_move:
            pile_num, sticks_num = None, None

            if player_turn:
                user_input = input("Your move (<pile_nr> <sticks_amount>): ")
                a = [int(x) for x in user_input.split()]
                pile_num, sticks_num = a[0] - 1, a[1]
            else:
                ## Agent's turn
                pile_num, sticks_num = game.agent_decision()
                print(f"Agent move: {pile_num + 1}, {sticks_num}")

            incorrect_move = not game.updateBoard(pile_num, sticks_num)
            if incorrect_move and not player_turn:
                raise Exception(f"ERROR: Incorrect machine move! ({pile_num}, {sticks_num})")

        game_continues = game.evaluateGame()
        if not game_continues:
            print("Pile state %s" % (game.board))
            if player_turn:
                print("Player wins!")
            else:
                print("Player loses!")
        player_turn = not player_turn
