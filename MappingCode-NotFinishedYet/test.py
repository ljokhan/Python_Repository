
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="larry_jokhan_app")


address = "120 Crestview Lane, Sparta, NJ, 07801"

location = geolocator.geocode (address, timeout=120)

if location:
    print (location)
else: print ("not found")



address = "137 Hillside Road, Sparta, NJ 07871"

location = geolocator.geocode (address, timeout=120)

if location:
    print (location)
else: print ("not found")



print ("done")
