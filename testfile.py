import mons
import moves
import abilities
import data_collection

print(len(mons.mons))
mons = mons.mons

backwards = {}

for mon in mons:
    backwards[mons[mon]] = mon

mons.update(backwards)
print(len(mons))
data_collection.write(mons, 'mons2')
    
