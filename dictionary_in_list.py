travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(place,count,siting):
    new_entry={
        "country":place,
        "visits":count,
        "cities":siting,
    }
    travel_log.append(new_entry)
    # new_entry["country"]=place
    # new_entry["visits"]=count
    # new_entry["cities"]=siting
    # travel_log.append(new_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)