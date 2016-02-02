"""Describes the tiles in the world space."""
__author__ = 'Phillip Johnson'

import items, enemies, actions, world, time


class MapTile:
    """The base class for a tile within the world space"""
    def __init__(self, x, y):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

    def quest(self):
        """Checks User Answer and Returns a Puzzle Item"""
        while True:
            if(re.match(quest_answer, user_answer)):
                return "Correct"
            print("Incorrect Answer, Try Again")
            user_answer = raw_input

    def quest_answer(self):
        """Answer to the Quest"""
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        The year is 1943.
        Europe is in the grip of The Nazis.
        Britain stands alone.

        You are a highly trained code-breaker. Your mission is to crack the
        enigma code that the Germans are using to send their transmissions.

        You are not along though, British agents have been sent all over the world
        with pieces of the Enigma code.

        Your mission is to find them, learn what they know, and crack the code.        
        """
        
    def modify_player(self, the_player):
        #Room has no action on player
        pass

class NewYork(Maptile):
    def intro_text(self):
        return
        """ New York. The big apple awaits you...
        """

    def modify_player(self, the_player):
        #room has no action on player
        pass

class Paris(Maptile):
    def intro_text(self):
        return """
        Paris. There are enemy soldiers everywhere. You must move quickly.
        """

class PuzzleRoom(MapTile):
    """A room that poses a puzzle for the workshop participants to solve."""
    def __init__(self, x, y, puzzle):
        self.puzzle = puzzle
        super().__init__(x, y)

    def quest_answer(self)

    def quest(self)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)

class EmpireState(Puzzle):
    def __init__(self, x, y):
        super().__init__(x, y, puzzle.EmpireState())

    def intro_text(Self):
        if self.puzzle.is_unsolved():
            return """
            You stand under the Empire State building and admire it for its size,
            a masterpiece of human engineering. You become aware that amongst the
            hustle and bustle of people there is someone watching you.

            A woman wearing a brown suede jacket comes over to you as you turn
            to face them. She hands you a piece of paper.

            "It's from a German officer called Ferdinand to his wife, Augustine."
        
            The woman turns away from you and walks quickly away from you
            as if she is worried what might happen if she stays.

            Written on the paper is the following:

            Dear Augustine,

            I am due to leave for Paris in the morning. I hope the French do not give
            us too much trouble.

            I love you,

            Ferdinand
            """
        else:
            return """You gaze up at the Empire State building. It's time to move
            on.
            """

    def quest(self):        

class LeaveGameRoom(MapTile):
    def intro_text(self):
        return """
        You cracked the Enigma code!

        Britain can now defeat the Nazis!
        
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True

