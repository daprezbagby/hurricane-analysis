# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:
def damages_to_float(lst):
  new_lst = []
  for i in lst:
    if i == "Damages not recorded":
      new_lst.append(float(0))
    elif i[-1] == "M":
      new_lst.append(float(i[:-1]) * 10 ** 6)
    elif i[-1] == "B":
      new_lst.append(float(i[:-1]) * 10 ** 9)
  return new_lst

damages_float = damages_to_float(damages)
#print(damages_float)

# write your construct hurricane dictionary function here:
def hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
  return hurricanes

hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages_float, deaths)
#print(hurricanes["Cuba I"])

# write your construct hurricane by year dictionary function here:
def hurricanes_by_year_dict(hurricanes):
  hurricanes_by_year = {}
  for key, value in hurricanes.items():
    current_year = hurricanes[key].get("Year")
    current_cane = value
    if current_year in hurricanes_by_year.keys():
      hurricanes_by_year[current_year] = hurricanes_by_year[current_year] + [current_cane]
    else:
      hurricanes_by_year[current_year] = [current_cane]
  return hurricanes_by_year

hurricanes_by_year = hurricanes_by_year_dict(hurricanes)
#print(hurricanes_by_year[2005])

# write your count affected areas function here:
def count_affected_areas(hurricanes):
  affected_areas = []
  for key in hurricanes.keys():
    current_areas = hurricanes[key].get("Areas Affected")
    for area in current_areas:
      affected_areas.append(area)
  affected_areas_dict = {}
  for area in affected_areas:
    if area in affected_areas_dict.keys():
      affected_areas_dict[area] = affected_areas_dict[area] + 1
    else:
      affected_areas_dict[area] = 1
  return affected_areas_dict

affected_areas_counts = count_affected_areas(hurricanes)
#print(affected_areas_counts)

# write your find most affected area function here:
def most_affected_area(affected_areas_counts):
  max_area = ""
  max_count = 0
  for key, value in affected_areas_counts.items():
    if value > max_count:
      max_area = key
      max_count = value
  return max_area, max_count

max_area, max_count = most_affected_area(affected_areas_counts)
#print("The most affected area is " + max_area + ", having been impacted " + str(max_count) + " times.")

# write your greatest number of deaths function here:
def most_deadly_hurricane(hurricanes):
  max_cane = ""
  max_deaths = 0
  for key, value in hurricanes.items():
    if value["Deaths"] > max_deaths:
      max_deaths = value["Deaths"]
      max_cane = key
  return max_cane, max_deaths

max_cane, max_deaths = most_deadly_hurricane(hurricanes)
#print("Hurricane " + max_cane + " was the deadliest hurricane, killing " + str(max_deaths) + " people.")

# write your catgeorize by mortality function here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def hurricanes_by_mortality_rating_dict(hurricanes, mortality_scale):
  hurricanes_by_mortality_rating = {}
  for value in hurricanes.values():
    current_deaths = value["Deaths"]
    current_cane = value
    if current_deaths > mortality_scale[4]:
      mortality_rating = 5
    elif current_deaths > mortality_scale[3]:
      mortality_rating = 4
    elif current_deaths > mortality_scale[2]:
      mortality_rating = 3
    elif current_deaths > mortality_scale[1]:
      mortality_rating = 2
    else:
      mortality_rating = 1
    if mortality_rating in hurricanes_by_mortality_rating.keys():
      hurricanes_by_mortality_rating[mortality_rating] = hurricanes_by_mortality_rating[mortality_rating] + [current_cane]
    else:
      hurricanes_by_mortality_rating[mortality_rating] = [current_cane]
  return hurricanes_by_mortality_rating

hurricanes_by_mortality_rating = hurricanes_by_mortality_rating_dict(hurricanes, mortality_scale)
#print(hurricanes_by_mortality_rating[5])

# write your greatest damage function here:
def most_damaging_hurricane(hurricanes):
  max_cane = ""
  max_damage = 0
  for key, value in hurricanes.items():
    if value["Damage"] > max_damage:
      max_damage = value["Damage"]
      max_cane = key
  return max_cane, max_damage

max_cane, max_damage = most_damaging_hurricane(hurricanes)
#print("Hurricane " + max_cane + " caused the greatest damage at $" + str(max_damage) + ".")

# write your catgeorize by damage function here:
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
def hurricanes_by_damage_rating_dict(hurricanes, damage_scale):
  hurricanes_by_damage_rating = {}
  for value in hurricanes.values():
    current_damage = value["Damage"]
    current_cane = value
    damage_rating = 0
    if current_damage > damage_scale[4]:
      damage_rating = 5
    elif current_damage > damage_scale[3]:
      damage_rating = 4
    elif current_damage > damage_scale[2]:
      damage_rating = 3
    elif current_damage > damage_scale[1]:
      damage_rating = 2
    else:
      damage_rating = 1
    if damage_rating in hurricanes_by_damage_rating.keys():
      hurricanes_by_damage_rating[damage_rating] = hurricanes_by_damage_rating[damage_rating] + [current_cane]
    else:
      hurricanes_by_damage_rating[damage_rating] = [current_cane]
  return hurricanes_by_damage_rating

hurricanes_by_damage_rating = hurricanes_by_damage_rating_dict(hurricanes, damage_scale)
#print(hurricanes_by_damage_rating[5])