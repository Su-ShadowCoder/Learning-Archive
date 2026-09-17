
try:
    pass
except FileNotFoundError:
    print("The file you're trying to access doesn't exist.")


with open("demofile.txt") as f:
  print(f.read())