                        Beginner level
              ====================================

ls = ["Thandel", "Legend", "Maharshi", "Mirchi", "GunturKaaram"]

ls.insert(2, "HighHeat")         # Inserts "HighHeat" at index 2
ls.append("PellisandaD")         # Adds "PellisandaD" to the end
ls.remove("Mirchi")              # Removes "Mirchi" from the list

print(f"elements in list : {ls}, len of list is : {len(ls)} ")
print(f"elements in list : {[items for items in ls]}, len of list is : {len(ls)} ")
Output:
elements in list : ['Thandel', 'Legend', 'HighHeat', 'Maharshi', 'GunturKaaram', 'PellisandaD'], len of list is : 6
elements in list : ['Thandel', 'Legend', 'HighHeat', 'Maharshi', 'GunturKaaram', 'PellisandaD'], len of list is : 6
