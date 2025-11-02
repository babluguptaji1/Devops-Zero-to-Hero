name = input ("Enter your name:")
city = input("Enter your city name:")
city1 = input("Enter your city name:")
city2 = input("Enter your city name:")
print("Hello " + name, " welcome to ", city)
print("I am from " , city1)
print(f"I am from {city2}")
about = f"hello i am {name}, my city name {city1} and i also love city {city2}"
other_name = input ("Enter the other person name:")

print(about.replace("Dosto", other_name))

print(dir(about))
print(help(str.replace))

a = 10.0
b = 20
c = a + b
print(dir(a))
