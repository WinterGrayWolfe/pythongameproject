#OrdoCryptum
#Text Based Adventure that guides players through storming a Crypt as a member of the Holy Inquisition of Terra.
#Game should present several options at character creation: Name, Gender, Class (Soldier(Guns), Warrior(Swords), Breacher(Balanced)). Each class will have a starting weapon and stats. 
#The game will keep track of the following: Player HP, Ammo, Status, Items
#Enemy HP, Status, Loot
#Story Location is inside a Crypt in the grim darkness of the 41st Millenium. You must storm the Crypt and destory the Chaos artifact. 


class Player:
  #This is the Player Character. Name, Gender, and Class will be chosen after the start menu. Choosing a class will add items to the inventory

  def __init__(self):
    self.health = 10
    self.max_health = 10
    self.items = []
    self.ammo = 5
    self.alive = True
    self.name = input("+++ Greetings, Inquisitor +++\nEnter your credentials below, starting with your name: ")
    print("+++ Welcome, " + self.name + " +++")
    self.gender = input("Inquisitorial ID recgonized, for security purposes, please input gender:")
    print("+++ Gender is listed as " + self.gender + ". +++\nThis matches Imperial Records.")
    self.career = input("+++ Please select your chosen career path +++ \n Soldier (Ranged Weapon Specialist)\n Warrior (Melee Specialist)\n Breacher (Balanced ranged and Melee): ")
    if self.career == "Soldier":
      self.items.append("Bolter")
      self.items.append("Bandage")
      print("+++ Registered Class: Soldier +++ \nThe following wargear has been granted:" + str(self.items))
    if self.career == "Warrior":
      self.items.append("Power Sword")
      self.items.append("Bandage")
      print("+++ Registered Class: Warrior +++ \nThe following wargear has been granted:" + str(self.items))
    if self.career == "Breacher":
      self.items.append("Shotgun")
      self.items.append("Combat Knife")
      print("+++ Registered Class: Breacher +++ \nThe following wargear has been granted:" + str(self.items))

  def __repr__(self):
    return "Inquisitor {name} of the Ordo Cryptum is a {gender} {career} with {health} health remaining, equipped with {items}, and {ammo} bullets.".format(name = self.name, gender = self.gender, career = self.career, health = self.health, items = self.items, ammo = self.ammo)

# This is if a character's health becomes 0 and they die

  def death(self):
    if self.health == 0:
      self.alive = False
      print("{name} has sacrificed their life for the holy Emperor".format(name = self.name))
      valid = False

#This is if a character takes damage

  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    else:
      print("{name} has taken damage and has {health} health remaining.".format(name = self.name, health = self.health))

  #This is if a character uses a bandage
    
  def gain_health(self, amount):
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
    print("Inquisitor {name}, has {health} health remaining".format(name = self.name, health = self.health))
        

  # Test section of current code


#Game Start and Menu
valid = False 
while not valid:
    start = input("+++ Welcome to Ordo Cryptum. To Begin, please press 1 +++\n")
    if start == "1":
      valid = True
      player = Player()
    else:
        print("+++ Clearance Revoked. Kill Team Inbound. Try Again. +++")



  