class Cat:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def describe(self):
        print("Cat Characteristics:")
        print(f"Arm length: {self.arm_length} units")
        print(f"Leg length: {self.leg_length} units")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail?: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry?: {'Yes' if self.is_furry else 'No'}")

my_cat = Cat(8.0, 9.0, 2, True, True)
my_cat.describe()