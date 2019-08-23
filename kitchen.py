c = input("Command: ")
d ={}
while c:
  c = c.split()
  if c[0] == "Set":
    d[c[1]] = c[2]
  elif c[0] == "Query":
      if c[1] in d:
          print("You have", d[c[1]], c[1]+".")
      else:
          print("I have no information about", c[1])
  else:
    print("Unknown command!")
  c = input("Command: ")
