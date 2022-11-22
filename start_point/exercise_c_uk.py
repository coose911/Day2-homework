united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
del(united_kingdom[1]["capital"])
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom)
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
northern_ireland = {
  "name" : "Ireland",
  "capital" : "Belfast",
  "population" : 1811000
}
united_kingdom.append(northern_ireland)
print(united_kingdom)
# 3. Use a loop to print the names of all the countries in the UK.
for countries in united_kingdom:
  print(countries["name"])

# 4. Use a loop to find the total population of the UK.
total = 0
for populations in united_kingdom:
  total = populations["population"] + total
print(total)