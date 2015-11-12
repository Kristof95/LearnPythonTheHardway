import hashmap

states = hashmap.new()
hashmap.set(states, 'Northrend', 'NR')
hashmap.set(states, 'Deepstorm', 'DS')
hashmap.set(states, 'Eastern Kingdoms', 'EK')
hashmap.set(states, 'Kalimdor', 'K')
hashmap.set(states, 'Pandaria', 'P')

cities = hashmap.new()
hashmap.set(cities, 'O', 'Abroad Earth')
hashmap.set(cities, 'Azeroth', 'Earth')

print ('-' * 10)
print ("NR State has: %s" % hashmap.get(cities, 'NR'))
print ("DS State has: %s" % hashmap.get(cities, 'DS'))

print ('-' * 10)
print("O's abbreviation is: %s" % hashmap.get(states, 'Eastern Kingdoms'))
print("Azeroth's abbreviation is: %s" % hashmap.get(states, 'Kalimdor'))

print ('-' * 10)
print ("O has: %s" % hashmap.get(cities, hashmap.get(states, 'Abroad Earth')))
print ("Azeroth has: %s" % hashmap.get(cities, hashmap.get(states, 'Earth')))

print ('-' * 10)
hashmap.list(states)

print ('-' * 10)
hashmap.list(cities)

print ('-' * 10)
state = hashmap.get(states, 'Goldshire')

if not state:
  print ("Sorry, no Goldshire.")

city = hashmap.get(cities, 'GS', 'Does Not Exist')
print ("The city for the state 'GS' is: %s" % city)
