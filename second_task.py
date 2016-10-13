depth = 0
square_liters = 1000
total_liters = 0
array = input("Input: ")
 
for button in array:
    if button == 'd':
        if depth >= 0:
            total_liters += (depth * square_liters) + (square_liters * 0.5)
        depth += 1
    elif button == 'h':
        if depth >= 0:
            total_liters += (depth * square_liters)
    elif button == 'u':
        depth -= 1
        if depth >= 0:
            total_liters += ((depth) * square_liters) + (square_liters * 0.5)
    
total_liters = int(total_liters)
print(total_liters)
