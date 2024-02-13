class MapElement():
    pass

class Maze():
    pass

class Door(MapElement):
    def
class Game:
    def __init__(self):
        self.maze = None
    def createWall(self):
        return Wall()
    def creteDoor(self):
        return Door()
    def creteDoor(self, door1, door2):

        return door
    def createRoom(self):
        return Room()
    def createMaze(self):
        return Maze()

    def make2RoomsMaze(self):
        self.game = Game()
        room1 = Room(1)
        room2 = Room(2)
        maze.addRoom(room1)
        maze.addRoom(room2)

        door = Door(room1, room2)
        room1.south = door
        room2.north = door
        game.maze = maze
        return self.maze
    def createDoor(self, door1, door2):
        door = Door(door1, door2)

        return door
    def make2RoomsMazeFM(self):
        maze.self.createMaze()
        room1 = self.createRoom()
        room2 = self.createRoom()
        door = self.createDoor(room1, room2)

        roo
        maze = self.createMaze()
        maze.addRoom(room1)
        maze.addRoom(room2)

        return maze


class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Room(MapElement):
    def __init__(self, id):
        pass

class Wall(MapElement):
    def __init__(self):
        pass #walls need aditional attributes
    def entrar(self):
        print("You can't go through walls")

game=Game()
game.make2RoomsMaze()
game.maze.entrar()

#game = Game()
#maze = Maze()
#room1 = Room(1)
#room2 = Room(2)
#maze.addRoom(room1)
#maze.addRoom(room2)

#door = Door(room1, room2)
#room1.south = door
#room2.north = door
#game.maze = maze

