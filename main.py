# by Vanessa Stimpel-Kolundzic

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
convert_const = 5/9
speed_of_ligth = 3*10**8

# 1 convert Fahrenheit to Temp
def f_to_c(f_temp):
  c_temp = (f_temp -32)*convert_const
  return round(c_temp,1)

# 2 Test the function with 100 Fahrenheit
f100_in_celsius = f_to_c(100)
print(f"{f100_in_celsius} °C")

# 3 convert Temp to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp *(9/5) + 32
  return(round(f_temp,1))

# 4 test the function with 0 Celcius
c0_in_fahrenheit = c_to_f(0)
print(f"{c0_in_fahrenheit} °F")

# 5 define function to calculate force
def get_force(mass,acceleration):
  return mass*acceleration

# 6 get train's acceleration
train_acceleration = get_force(train_mass,train_acceleration)

#7 print results
print(f"The GE train supplies {train_acceleration} Newtons of force.")

# 8 Calculate momentum c*m = p, this is not the kinetic energy , which m*c**2 = E in relativistic epression, momentum is velocity * mass.
def get_energy(mass):
  energy_rel = mass*speed_of_ligth**2
  return energy_rel

# 9 get energy of bomb
# Tsar Bomba released 2.07e+17 for 2.3 kg
bomb_energy =get_energy(1)

# 10 print results
print(f"A 1kg bomb supplies {bomb_energy:.1e} Joules. In comparison the Tsar Bomb released 2.07e+17 Joules with a mass of 2.3 kg ")
# 11 calculate work
def get_work(mass, acceleration,distance):
  return get_force(mass,acceleration)*distance

# 12 get work 
train_work = get_work(train_mass,train_acceleration,train_distance)

# 13 print the result
print(f"The GE train does {train_work:.1e} Joules of work over {train_distance} meters.")







