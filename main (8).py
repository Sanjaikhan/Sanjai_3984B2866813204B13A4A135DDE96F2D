


# Define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket")

# Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting")

# Create objects of Player and Batsman classes
player = Player()
batsman = Batsman()

# Call the play() method for each object
player.play()
batsman.play()