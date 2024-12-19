#OrdoCryptum
#Text Based Adventure that guides players through storming a Crypt as a member of the Holy Inquisition of Terra.
#Game should present several options at character creation: Name, Gender, Class (Soldier(Guns), Warrior(Swords), Breacher(Balanced)). Each class will have a starting weapon and stats. 
#The game will keep track of the following: Player HP, Ammo, Status, Items
#Enemy HP, Status, Loot
#Story Location is inside a Crypt in the grim darkness of the 41st Millenium. You must storm the Crypt and destory the Chaos artifact. 

class Player:
  #To create your Inquisitor, we need to select name, gender, and class
  def __init__(self, name, gender, career, items, ammo, alive):
    self.name = input("Greetings, Inquisitor. Enter your credentials below, starting with your name: ")
    self.gender = gender
    self.career = career
    self.health = 10
    self.max_health = 10
    self.items = []
    self.ammo = 0
    self.alive = True

  def __repr__(self):
    return "Inquisitor {name} of the Ordo Cryptum is a {gender} {career} with {health} health remaining, equipped with {items}, and {ammo} bullets.".format(name = self.name, gender = self.gender, career = self.career, health = self.health, items = self.items, ammo = self.ammo)


  def death(self):
    if self.health == 0:
      self.alive = False
      print("{name} has sacrificed their life for the holy Emperor".format(name = self.name))

  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    else:
      print("{name} has taken damage and has {health} health remaining.".format(name = self.name, health = self.health))
    
  def gain_health(self, amount):
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
    print("Inquisitor {name}, has {health} health remaining".format(name = self.name, health = self.health))
        

  # Test section of current code



  

