def feedAnimals(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0
    
    count = 0    
    animals.sort()
    food.sort()
    
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
        
    return count


eda = [int(x) for x in input().split()]
zhiv = [int(x) for x in input().split()]
print(feedAnimals(zhiv, eda))
