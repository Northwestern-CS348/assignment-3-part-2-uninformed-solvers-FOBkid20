
from solver import *

class SolverDFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state have been explored,
        the next explored state should conform to the specifications of
        the Depth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        print('heyhey')
        self.visited[self.currentState] = True  # Mark current state as visited
        print(self.visited)
        print('current state')
        print(self.currentState.state)
        if self.currentState.state == self.victoryCondition:  # Won the game, so stop
            return True
        # Get available moves
        availableMoves = self.gm.getMovables()
        # If there are available moves, go to the correct child
        if availableMoves:  # if we aren't at a leaf
            print('children')
            print(self.currentState.children)
            if len(self.currentState.children) == 0:  # if we haven't yet filled the children attribute
                print('a')
                for move in availableMoves:  # create stack of children in currentState.children
                    self.gm.makeMove(movable_statement=move)  # have to make move in order to create moveChild because need to specify state
                    moveChild = GameState(state=self.gm.getGameState, depth=self.currentState.depth + 1, movableToReachThisState=move)  # create child node
                    self.currentState.children.append(moveChild)  # add possible children based on available moves
                    moveChild.parent = self.currentState  # add current state as parent to children
                    self.gm.reverseMove(movable_statement=move)  # undo move
                print('post-for-loop children')
                print(self.currentState.children)
            print('nextChildToVisit')
            print(self.currentState.nextChildToVisit)
            #if (self.currentState.children[len(self.currentState.children)-1] not in self.visited or self.visited[self.currentState.children[len(self.currentState.children)-1]] == False):  # if there are children left to visit (literally, if the last of the children is not visited)
            if self.currentState.nextChildToVisit < len(self.currentState.children):  # if there are children left to visit
                print('b')
                self.currentState.nextChildToVisit += 1  # when we come back to this state, go to the next child
                self.currentState = self.currentState.children[self.currentState.nextChildToVisit-1]  # update currentState to child
                self.gm.makeMove(movable_statement=self.currentState.requiredMovable)  # move to current state
                return False
            else:  # move up a node
                while (self.currentState.children[len(self.currentState.children)-1] in self.visited and self.visited[self.currentState.children[len(self.currentState.children)-1]] == True):  # if there are no children left to visit (literally, if the last of the children is visited)
                    print('c')
                    if self.currentState.parent is not None:  # not at root node
                        self.gm.reverseMove(self.currentState.requiredMovable)
                        self.currentState = self.currentState.parent
                        continue
                    else:
                        print('d')
                        return False  # no more tree to explore

        # If there are not available moves, go up the tree until there are (You are at a leaf)
        else:
            # if self.currentState.parent == None:  # If there are no available moves left in the tree, return False
            #    return False
            self.gm.reverseMove(self.currentState.requiredMovable)
            self.currentState = self.currentState.parent
            return False




class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Breadth-First Search algorithm.
        Returns:
            True if the desired solution state is reached, False otherwise
        """

        ### Student code goes here
        return True

