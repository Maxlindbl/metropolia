import random
dices = int(input("montaako noppaa haluat heittää?: "))
values = []
for i in range(dices):
    values.append(random.randint(1,6))
print(sum(values))
