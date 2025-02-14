#OrdoCryptum
#Text Based Adventure that guides players through storming a Crypt as a member of the Holy Inquisition of Terra.
#Game should present several options at character creation: Name, Gender, Class (Soldier(Guns), Warrior(Swords), Breacher(Balanced)). Each class will have a starting weapon and stats. 
#The game will keep track of the following: Player HP, Ammo, Status, Items
#Enemy HP, Status, Loot
#Story Location is inside a Crypt in the grim darkness of the 41st Millenium. You must storm the Crypt and destory the Chaos artifact. 
import time
import random
import sys

class Player:
  #This is the Player Character. Name, Gender, and Class will be chosen after the start menu. Choosing a class will add items to the inventory

  def __init__(self):
    self.health = 10
    self.max_health = 10
    self.items = []
    self.ammo = 4
    self.alive = True
    self.count = 0
    self.name = input("+++ Greetings, Inquisitor +++\nEnter your credentials below, starting with your name: ")

    time.sleep(1)

    print("+++ Welcome, " + self.name + " +++")

    time.sleep(1)

    self.gender = input("\nInquisitorial ID recgonized, for security purposes, please input gender: ")

    time.sleep(1)
  
    print("+++ Gender is listed as " + self.gender + ". +++\nThis matches Imperial Records.\n")

    time.sleep(1)

    career_select = False 
    while not career_select:
      self.career = input("+++ Please select your chosen career path +++ \n Soldier (Ranged Weapon Specialist)\n Warrior (Melee Specialist)\n Breacher (Balanced Ranged and Melee): ")
      if self.career == "Soldier" or self.career == "soldier":
        self.items.append("Bolter")
        self.items.append("Bandage")
        self.ammo += 2
        print("+++ Registered Class: Soldier +++ \nThe following wargear has been granted:" + str(self.items))
        career_select = True
      if self.career == "Warrior" or self.career == "warrior":
        self.items.append("Power Sword")
        self.items.append("Bandage")
        self.items.append("Bandage")
        print("+++ Registered Class: Warrior +++ \nThe following wargear has been granted:" + str(self.items))
        career_select = True
      if self.career == "Breacher" or self.career == "breacher":
        self.items.append("Shotgun")
        self.items.append("Combat Knife")
        print("+++ Registered Class: Breacher +++ \nThe following wargear has been granted:" + str(self.items))
        career_select = True
      
    if self.health <= 0:
      self.health = 0
      self.death()

    
  def __repr__(self):
    return "Inquisitor {name} of the Ordo Cryptum is a {gender} {career} with {health} health remaining, equipped with {items}, and {ammo} bullets.".format(name = self.name, gender = self.gender, career = self.career, health = self.health, items = self.items, ammo = self.ammo)


# This is if a character's health becomes 0 and they die

  def death(self):
    if self.health == 0:
      self.alive = False
      print("{name} has sacrificed their life for the Holy Emperor\n+++GAME OVER+++".format(name = self.name))
      if self.alive == False:
        sys.exit()  
      

#This is if a character takes damage

  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    else:
      print("{name} has taken damage and has {health} health remaining.".format(name = self.name, health = self.health))

  #This is if a character uses a bandage
    
  def gain_health(self):
    if "Bandage" in self.items:
      self.items.remove("Bandage")
      self.health += 10
    else: print("{name} has no Bandages left".format(name = self.name))
    if self.health >= self.max_health:
      self.health = self.max_health
    print("Inquisitor {name}, has {health} health remaining".format(name = self.name, health = self.health))

  def melee_attack(self, enemy):
    melee_damage = 5
    if "Power Sword" in self.items or "Combat Knife" in self.items:
      print("The blade slashes through the heretic, dealing " + str(melee_damage) + " damage")
      enemy.lose_health(melee_damage)
    else:
      print("Your fist connects with the foe, the sound of crunching bone filling the room, dealing 3 damage")
      enemy.lose_health(3)
      
  def ranged_attack(self, enemy):
    ranged_damage = 10
    if "Bolter" in self.items or "Shotgun" or "Stub Pistol" in self.items:
      if self.ammo == 0:
        print("The weapon clicks uselessly, out of ammo.")
      if self.ammo > 0:
        print("The blast rips through the heretic, dealing " + str(ranged_damage) + " damage")
        enemy.lose_health(ranged_damage)
        self.ammo -= 1
        time.sleep(2)
        print("You have " + str(self.ammo) + " bullets remaining")
    else:
      print("You have no ranged weapon.")
      
 

#enemy number 1: Basic Cultist
class Enemy:

  def __init__(self):
    self.health = 10
    count = 0
    self.alive = True

  def attack(self, player):
    print("The heretic lunges out with a rusty combat knife")
    time.sleep(2)
    player.lose_health(random.randint(1, 3))
  
  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    
  def death(self):
    if self.health == 0:
      self.alive = False
      print("The heretic dies in agony.")
    if self.alive == False:
      del self
    
#Second Enemy Type
class Elite_Enemy:

  def __init__(self):
    self.health = 15
    count = 0
    self.alive = True

  def attack(self, player):
    print("The heretic fires a shot with their laspistol")
    time.sleep(2)
    player.lose_health(random.randint(1, 4))
  
  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.death()
    
  def death(self):
    if self.health == 0:
      self.alive = False
      print("The heretic falls, blood spilling down their lips. They try to form words, but no sound comes out. They slump over, dead.")
    if self.alive == False:
      del self
    
#All combat and combat actions
def combat(player, enemy):
  while enemy.alive == True or player.alive == True:
    time.sleep(2)
    battle = input("The heretic stands before you, weapon in hand. What do you do?\n Melee_Attack: Press 1\n Ranged_Attack: Press 2\n Use Bandage: Press 3\n Run: Press 4\n Supplies: Press 5\n")
    if battle == "1":
      player.melee_attack(enemy)
      time.sleep(2)
      if enemy.health == 0:
        break
      else:  
        enemy.attack(player)

    if battle == "2":
      player.ranged_attack(enemy)
      time.sleep(2)
      if enemy.health == 0:
        break
      else:  
        enemy.attack(player)

    if battle == "3":
      player.gain_health()

    if battle == "4":
      count = random.randint(1, 20)
      if count >= 10:
        print("You flee from the heretic, they slice their knife into you as you escape, dealing 2 damage.")
        player.health -= 2
        break
      else:
        print("You try to flee, but the heretic corners you, their knife slices into you dealing 1 damage.")
        player.health -= 1
    
    if battle == "5":
      print("Health Remaining: " + str(player.health) + "\nAmmo Remaining: " + str(player.ammo) + "\nSupplies: " + str(player.items) + "\n")

    if enemy.alive == False or player.alive == False:
      break   
    
      
  # Test section of current code


#Game Start and Menu

valid = False 
while not valid:
  start = input("+++ Welcome to Ordo Cryptum. To Begin, please press 1 +++\n")
  if start == "1":
    valid = True
    time.sleep(.5)
    player = Player()
    enemy = Enemy()
    elite_enemy = Elite_Enemy()
  else:
      print("+++ Clearance Revoked. Kill Team Inbound. Try Again. +++")

time.sleep(4)

print("+++ BEGIN PURGE +++")

time.sleep(3)

print("In the grim darkness of the far future there is only war. There is no peace amongst the stars, only an eternity of carnage and slaughter, and the laughter of thirsting gods.\n ++PRESS ENTER TO CONTINUE:++\n")

input()

print("The Crypt of St. Lorens stands before you. You are Inquisitor {name} of the Ordo Cryptum. As a member of the Holy Inquisition, you are the last bastion of light against the despair of the darkness. You have been tasked by the Imperium of Man to root out the members of a heretical cult within the crypt, and destroy them.".format(name = player.name))

input()

print("\nBefore you sits an ancient human skull, fragile with age and decay. You can see mechanical devices embedded inside the skull. It appears to be the device that opens the door. Inside its dry eye socket, a dim red light glows. The entry button.")

input()

print("\nDo you press the button? Or walk away?")

entrance = False 
while not entrance:
    button = input("Press the button?: 1 \nWalk Away?: 2\n")
    if button == "1":
      entrance = True
      time.sleep(1)
    if button == "2":
        print("+++ You walk away, shirking your duties. Kill Team Inbound. +++")
        time.sleep(3)
        sys.exit()

        

print("\nThe stone door rumbles open, powered by an unseen source.")

input()

print("\nA single staircase descends into the darkness. Each step downwards lowers the light around you. As you activate your lumen, the click of a sodium lamp igniting fills the silence, and a dim light illuminates your path forward.")

input()

print("\nAt the bottom of the stairs is a small, square room made of ancient stone. Moss covers the walls and the air is thick with the smell of decay.")

input()

print("\nYour lumen shines on the far wall. Carved into the stone are words written in High Gothic:")

input()

print("+++ Ad Imperatorem +++")

input()

print("\nBefore you can examine any further, a heretic dressed in tattered robes springs from the shadows. Their hands are slick with blood, a twisted grin upon their face.\n") 

input()

print("You prepare to grant them the Emperor's mercy.")

input()

combat(player, enemy)

time.sleep(2)

print("Gathering your wits, you look about the humid and dark depths of the crypt.")

input()

print("To your left, a locked wooden door that you can easily smash down.\nTo your right, a smooth stone path slopes down into the darkness.")

input()
#Definitions of both room choices

def left_room1():
  print("The door splinters easily as your armored boot smashes into the rotted wood. The small store room seems to be filled with mostly empty crates and dark, old bloodstains. Another pathway leads further into the crypt at the end of the room. Before you can move deeper, your boot catches on a thin wire on the door")
  input()

  lr1ex = False
  while not lr1ex:
    lr1 = input("Dodge: Press 1\nDisarm: Press 2\nDestroy: Press 3\n")
    if lr1 == "1":
      count = random.randint(1, 20) - 1
      if count >= 10:
        print("You dodge out of the way, avoiding the blades that fire from slots in the wall. The dust settles and you pat yourself down")
      else:
        print("Blades fire from slots in the wall, you move with near inhuman speed, but it's not enough. A blade slashes across your arm, blood seeping from the wound, dealing 2 damage")
        player.health -= 2
        if player.health <= 0:
          player.death()
      lr1ex = True


    if lr1 == "2":
      count = random.randint(1, 20) + 3
      if count >= 10:
        print("You disarm the tripwire, ensuring the trap never triggers. You are now free to search the room for supplies.")
      else:
        print("Blades fire from slots in the wall, you move with near inhuman speed, but it's not enough. A blade slashes across your arm, blood seeping from the wound, dealing 2 damage")
        player.health -= 2
        if player.health <= 0:
          player.death()
      lr1ex = True

    if lr1 == "3":
      count = random.randint(1, 20)
      if count >= 10:
        print("The tripwire is destroyed, splintering as you shatter it with your weapon, leaving you free to search the room.")
      else:
        print("Blades fire from slots in the wall, you move with near inhuman speed, but it's not enough. A blade slashes across your arm, blood seeping from the wound, dealing 2 damage")
        player.health -= 2
        if player.health <= 0:
          player.death()
      lr1ex = True
  else:
    print("Invalid Input")
  


def left_loot1():
  print("There are usable supplies inside the room. You manage to find a bandage, and two bullets.")
  player.items.append("Bandage")
  player.ammo += 2


def right_room1():
  print("Each step you take down the right path leads further and further down. The walls are narrow, squeezing in on your shoulders as you plunge into the darkness.")
  input()
  print("You worry you will get stuck inside the passage, but just as the walls seem to squeeze in around you, it opens up into a small room.")
  input()
  print("You find yourself inside a ritual room. Human remains scatter the floor, viscera and limbs piled in the center. Written in blood on the floor is an eight pointed star: The symbol of Chaos.")
  input()
  print("You recoil as even looking at the symbol causes physical pain.\n")
  input()
  rr1ex = False
  while not rr1ex:
    rr1 = input("What do you do?\nDestroy the symbol: Press 1\nLeave the symbol and continue: Press 2\nCut your hand and offer your own blood: Press 3\n")
    if rr1 == "1":
      count = random.randint(1, 20) + 3
      if count >= 10:
        print("You destroy the symbol easily, relying on the holy oils in your satchel to burn the bodies and symbol away. Just as the Emperor intended.")
        rr1ex = True
      else:
        print("It takes some time, but you manage to destroy the symbol by scrubbing it with your hands. Staring at the symbol for so long causes your very soul to hurt. You lose 2 health")
        player.health -= 2
        if player.health <= 0:
          player.death()
        rr1ex = true

    if rr1 == "2":
      count = random.randint(1, 20)
      if count >= 10:
        print("You leave the symbol. The wretched mark may be terrible, but enacting the Emperor's wrath on the leader is more important.")
        rr1ex = True
      else:
        print("You leave the symbol, but you worry that you are shirking your duties by not taking the time to destroy it. Your paranoia causes you to step carelessly, your foot spearing itself on a spike in the floor. You lose 2 health.")
        player.health -= 2
        if player.health <= 0:
          player.death()
        rr1ex = True

    if rr1 == "3":
      print("You offer your blood to the sacrifice. A voice speaks in your head: 'Excellent my child, I shall grant you the power you seek.'\n You feel as though you've lost something important, a steep price paid. You lose 4 health, but gain 4 ammo")
      player.health -= 4
      player.ammo += 4
      player.count += 1
      if player.health <= 0:
          player.death()
      rr1ex = True
  else:
    print('Invalid Input')
  
# Actual Room Choice Narrative

rc1 = False
while not rc1:
  room_choice_1 = input("\nWhich path do you choose?\nLeft: Press 1\nRight: Press 2\n")
  if room_choice_1 == "1":
    left_room1()
    time.sleep(4)
    left_loot1()
    rc1 = True
  if room_choice_1 == "2":
    right_room1()
    time.sleep(4)
    rc1 = True
  else:
    print("Invalid Input")
  

 
#Section 2

input()

print("The exit takes you down a long, descending cooridor. Quotations of St. Laurens fill the hallway, but all of them have been scratched out. Chaos symbols litter the hall, most of them drawn in human blood. The very hall itself seems to curve and warp as you walk down it.")

input()

print("As you reach the end of the hall, you see the chamber open up into a massive cathedrum room build into the earth. Decaying wood pews stand in lines to either side of you, dust and thick cobwebs coating them. At the dias, a statue of St. Laurens stands behind the pulpit, lit only by hundreds of flickering candles.")

input()

print("A shadowy figure stands at the pulpit. His wretched mask made of leathered flesh. He bares blood soaked teeth at you, drawing a laspistol as you dive for cover.")

input()

combat(player, elite_enemy)
time.sleep(2)

print("\nWith the heretic dead, you can take time to check the room. Crates with strange markings on them lay in one corner, they seem Chaos in origin, and your mind hurts to even look at them. A dataslate rests on the old pulpit, and the heretic may have some supplies.\n")

input()

def pulpit_room():
  pulpit_exit = False
  proom1_looted = False
  hereticlooted = False
  while not pulpit_exit:
   proomchoice = input("What do you do?\n1:Search the Crates\n2:Search the Dataslate\n3:Loot the Heretic\n4:Leave\n")
   if proomchoice == "1":
    print("The crates are covered with Chaos sigils.\n")
    proom1choice = input("1: Destroy the Crates\n2: Loot the Crates\n")
    if proom1choice == "2":
      if proom1_looted == True:
        print("The supplies have been looted, the crates are empty.")
        time.sleep(3)

      if proom1_looted == False:
        print("The supplies inside are useful, but the sigils burn themselves into your brain.\n")
        player.items.append("Bandage")
        player.ammo += 2
        player.count += 1
        proom1_looted = True
        time.sleep(3)

    if proom1choice == "1":
      print("You destroy the supplies, ammunition isn't worth the taint of Chaos.")
      player.count -= 1
      proom1_looted = True
      time.sleep(3)
    
   if proomchoice == "2":
    print("The dataslate reads:\n+++")
    time.sleep(3)

   if proomchoice == "3":
      if hereticlooted == True:
        print("The body is looted, there is nothing more to do here.")
        time.sleep(3)
      if hereticlooted == False:
        print("You loot the heretic's body. You take their Stub Pistol and 1 ammo.")
        player.items.append("Stub Pistol")
        player.ammo += 1
        hereticlooted = True
        time.sleep(3)

   if proomchoice == "4":
    pulpit_exit = True
   
   else:
    print("Invalid Input")

      
pulpit_room()

print("Beyond the cathedral room begins the true tomb of St. Laurens. Rows of cacophogi line the walls on both sides. A plaque indentifies the bodies as the honor guard of the Saint. Sisters of the Ebon Chalice who gave their lives in defense of the Saint.")

input()

print("Sounds eminate from the tomb beyond. The echos of chants and ancient rites. Something terrible is happening at the heart of the crypt. You steel yourself, and move forward.")

input()

print("At the end of the row of carcophogi lies a single split path. Carved into the marble is a set of instructions.")

input()

print("+++Do You Walk the Path of the Saint? Or the Path of the Repentant?+++")

input()

def Saint():
  saintexit = False
  saintenemy = False

  while not saintexit and saintenemy:
    print("You round the corner of the Path of the Saint. Immediately, the world is plunged into darkness. Your lumen barely shines ahead, as if something is swallowing the light itself.")

    input()

    print("A dark voice speaks in your mind its very voice chilling your soul.")

    input()

    print(player.name + ". Servant of the corpse god. Come and serve me instead, together we can bring true peace to this forsaken galaxy.")

    input()

    saintchoice = input("What do you do?\n1:Recite a litany to the Emperor, resisting the entity.\n2:Attack the darkness, looking for a source of the voice.\n3:Agree to join the entity.")

    if saintchoice == "1":
      print("Your litany to the Emperor forces the voice from your mind, a wall of sheer willpower shielding your soul from the entity.")

      input()

      print("A psychic rage roils around you, warping the very halls. Suddenly, from the darkness, another heretic jumps forward, ambushing you.")

      input()

      combat(player, elite_enemy)

      saintenemy = True
      saintexit = True
      
    if saintchoice == "2":
      print("You attack the hallway wildly. The voice laughs inside your head, and from behind you a heretic springs forth, ready to kill you.")

      input()

      combat(player, elite_enemy)

      saintenemy = True
      saintexit = True

    if saintchoice == "3":
      
      print("You feel your mind embrace the voice. It is right, you cannot resist any longer. The corpse god must fall, humanity will never be free from its shackles while under the Imperium. A heretic steps into your path, then moves aside, gesturing you deeper into the crypt.")

      input()

      player.health += 10
      player.count += 1
      saintexit = True
      saintenemy = True


def Repentant():
  repexit = False

  while not repexit:
    print("The path of the repentant is a small, marble hall. Dim torchlight flickers on either side, and a dias of white marble with an ebon chalice starkly stands in the center.")

    input()

    print("")

  



