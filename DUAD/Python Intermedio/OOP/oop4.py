# Cree las siguientes clases:
# Head
# Torso
# Arm
# Hand
# Leg
# Feet
# Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
# Por ejemplo (este código esta incompleto, pero describe la idea):
# class Torso:
# 	def __init__(self, head, right_arm, ...):
# 		self.head = head
# 		self.right_arm = right_arm
# 		...
		
# class Hand:
# 	def __init__(self):
# 		pass

# class Arm:
# 	def __init__(self, hand):
# 		self.hand = hand


# right_hand = Hand()
# right_arm = Arm(right_hand)
# torso = Torso(head, right_arm, ...)
class Head:
    def __init__(self):
        print("A head has been created!")

class Hand:
    def __init__(self):
        print("A hand has been created!")

class Foot:
    def __init__(self):
        print("A foot has been created!")

class Arm:
    def __init__(self, hand):
        self.hand = hand
        print("An arm has been created and connected to a hand!")

class Leg:
    def __init__(self, foot):
        self.foot = foot
        print("A leg has been created and connected to a foot!")

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        print("The torso has been created and all body parts have been connected!")

class Human:
    def __init__(self, torso):
        self.torso = torso
        print("All body parts are connected")
        print("Exodia Obliterate!")

def main():
    head = Head()

    right_hand = Hand()
    left_hand = Hand()
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)

    right_foot = Foot()
    left_foot = Foot()
    right_leg = Leg(right_foot)
    left_leg = Leg(left_foot)

    torso = Torso(head,right_arm,left_arm,right_leg,left_leg)

    human = Human(torso)

if __name__ == "__main__":
    main()