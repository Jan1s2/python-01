from physics import earth_to_moon, earth_gravity, velocity_all

print("Convert Earth weight to moon weight")
mass = float(input("Weight on earth: "))
print(f"{mass} kg on earth equals {earth_to_moon(mass)} kg on the moon")
mass = float(input("Input mass on earth: "))
print(f"The force is {earth_gravity(mass)} N")
mass = float(input("Input mass of the object: "))
distance = float(input("Input distance between the object and earth: "))
print(f"The force is {earth_gravity(mass, distance)} N")
v = float(input("Velocity: "))
v_l, v_s = velocity_all(v) 
print(f"v compared to light: {v_l}; v to sound: {v_s}")
