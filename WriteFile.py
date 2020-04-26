with open('text.txt', 'r') as file:
     content = file.readlines()

   #  print(reversed(content))
     with open('text.txt', 'w') as writer:
         for line in reversed(content):
              print(writer.write(line))