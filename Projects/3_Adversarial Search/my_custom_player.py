
from isolation import DebugState, StopSearch
from sample_players import DataPlayer


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def __init__(self, player_id):
        super().__init__(player_id)
        # print(f'__init__ of CustomPlayer')
        self.score = self.heuristic_2_score


    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        # print('In get_action(), state received:')
        # debug_board = DebugState.from_state(state)
        # print(debug_board)

        # randomly select a move as player 1 or 2 on an empty board, otherwise
        # return the optimal minimax move at a fixed search depth of 3 plies
        self.depth = 0
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            # iterative deepening
            while True:
                try:
                    self.depth += 1
                    action = self.minimax_alpha_beta_search(state, depth=self.depth)

                    # clear every 5 enqueue
                    # if self.queue.qsize() > 5: self.queue.get()
                    self.queue.put(action)
                except StopSearch:
                    # print('catched StopSearch')
                    break
        # print(f'{last action's depth = {self.depth}')

    def _weighted_score(self, state, w_p, w_o):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return w_p * len(own_liberties) - w_o * len(opp_liberties)

    def baseline_score(self, state):
        return self._weighted_score(state, 1, 1)

    def heuristic_1_score(self, state):
        m = state.ply_count / (9 * 11)
        return self._weighted_score(state, 2 * m , 1)

    def heuristic_2_score(self, state):
        m = state.ply_count / (9 * 11)
        return self._weighted_score(state, 1 , 2 * m)

    def minimax_alpha_beta_search(self, state, depth):

        def min_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), depth - 1, alpha, beta))
                if value <= alpha:
                    return value
                beta = min(beta, value)
            return value

        def max_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), depth - 1, alpha, beta))
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            return value

        alpha = float("-inf")
        beta = float("inf")
        best_score = float("-inf")
        best_move = None
        for action in state.actions():
            value = min_value(state.result(action), depth - 1, alpha, beta)
            alpha = max(alpha, value)
            if value > best_score:
                best_score = value
                best_move = action
        if best_move == None : best_move = state.actions()[0]
        return best_move