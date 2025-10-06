from random import sample

list_p = [x for x in range(20)]

winners = sample(list_p, 3)
print("Ganadores del sorteo:")
for winner in winners:
    print(winner)
