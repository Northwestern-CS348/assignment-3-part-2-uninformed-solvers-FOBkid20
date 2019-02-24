from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        peg1 = []
        peg2 = []
        peg3 = []
        pegs = self.kb.kb_ask(parse_input("fact: (on ?d ?p"))
        for disk in pegs:
            d = int(disk.bindings_dict['?d'][4])  # get just the number of 'diskX'
            p = int(disk.bindings_dict['?p'][3])  # get just the number of 'pegX'
            if p == 1:
                peg1.append(d)
            elif p == 2:
                peg2.append(d)
            elif p == 3:
                peg3.append(d)
        peg1.sort()
        peg2.sort()
        peg3.sort()
        world = tuple((tuple(peg1), tuple(peg2), tuple(peg3)))
        return world

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        if movable_statement.predicate != 'movable':
            pass
        else:
            disk = str(movable_statement.terms[0])
            pFrom = str(movable_statement.terms[1])
            pTo = str(movable_statement.terms[2])

            # Retract no longer true facts
            self.kb.kb_retract(parse_input("fact: on " + disk + " " + pFrom))

            # Add new facts
            self.kb.kb_add(parse_input("fact: on " + disk + " " + pTo))
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here
        row1 = [-1, -1, -1]
        row2 = [-1, -1, -1]
        row3 = [-1, -1, -1]
        rows = self.kb.kb_ask(parse_input("fact: (pos ?t ?px ?py"))
        for tile in rows:
            if str(tile.bindings_dict['?t']) == "empty":
                t = -1
            else:
                t = int(tile.bindings_dict['?t'][4])  # get just the number of tileX
            px = int(tile.bindings_dict['?px'][3])  # get just the number of 'posx'
            py = int(tile.bindings_dict['?py'][3])  # get just the number of 'posy'
            if py == 1:
                row1[px-1] = t
            elif py == 2:
                row2[px-1] = t
            elif py == 3:
                row3[px-1] = t
        world = tuple((tuple(row1), tuple(row2), tuple(row3)))
        return world

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        tile = str(movable_statement.terms[0])
        px1 = str(movable_statement.terms[1])
        py1 = str(movable_statement.terms[2])
        px2 = str(movable_statement.terms[3])
        py2 = str(movable_statement.terms[4])

        self.kb.kb_retract(parse_input("fact: pos " + tile + " " + px1 + " " + py1))
        self.kb.kb_add(parse_input("fact: pos " + tile + " " + px2 + " " + py2))
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
