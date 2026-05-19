# Import libraries:
import csv
import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
import webbrowser

# Custom class to store coordinates on a map, along with distances to other points:
class MapPoints:

    def __init__ (self, address, coordinates, avg_km, max_km, min_km):
        self.address = address
        self.coordinates = coordinates
        self.avg_km = avg_km
        self.max_km = max_km
        self.min_km = min_km

# Calculates distance between 2 coordinates:
def haversine(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Coordinates in decimal degrees
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    
    return distance

# Main code:

# Select geocoder:
geolocator = Nominatim(user_agent = "my_geocoding_app")

# List to store all coordinates:
AllMapPoints = []

# Read a file of addresses into list of all coordinates:
with open('Hospital_General_Information.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for oneLine in csv_reader:

        if oneLine[4] == "NJ":

            # Exclude Alaska addresses, since it skewes the results:
        
            # Concatenate address fields for geocoding:
            OneAddress = (oneLine[2] + "," + oneLine[3] + "," + oneLine[4] + "," + oneLine[5] + ", United States")
    
            # Create instance of map coordinate object:
            OneMapPoint = MapPoints(OneAddress, (), None, None, None )

            # Add this map point to the list of all map points:
            AllMapPoints.append (OneMapPoint)

print ("Begin geocoding....")

# Geocode every address:
for Point1 in AllMapPoints:
        # Geocode each address:
        location = geolocator.geocode (Point1.address, timeout = 60)
        if location:
            # Save coordinates as a tuple:
            Point1.coordinates = (location.latitude, location.longitude)
        else:
            Point1.coordinates = None

print ("Begin calculating distances between coordinates...")


for Point1 in AllMapPoints:

    print ("--------------------------------")
    print (Point1.address)
    Counter = 0
    Total = 0
    MaxDistance = 0
    MinDistance = 9999999999
    for Point2 in AllMapPoints:
        if Point1.coordinates != None and Point2.coordinates != None:
            distance = haversine(Point1.coordinates, Point2.coordinates)
            print (distance)
            if  distance > MaxDistance:
                MaxDistance = distance
            if  distance < MinDistance and distance > 0:
                MinDistance = distance
    print ("Minimum &  Maximum distance..,")
    print (MinDistance)
    print (MaxDistance)
    Point1.max_km = MaxDistance
    Point1.min_km = MinDistance

# Create map:
map = folium.Map(location = [40.21620713307166, -74.67546739319853], zoom_start = 8)


4

# Add all coordinates to map:
for Point3 in AllMapPoints:
    if Point3.coordinates != None:
        folium.Marker(location=[Point3.coordinates[0],Point3.coordinates[1]],popup=Point3.address,icon=folium.Icon(color="red")).add_to(map)


# Calculate coordinate with lowest maximum distance. That coordinate will be central to everyone:
LowestMaxDistance = 999999999999.9
LowestMaxAddress = ""
LowestMaxCoordinates = ()
for Point3 in AllMapPoints:
    if Point3.max_km != None and Point3.max_km < LowestMaxDistance and Point3.max_km > 0 :
        LowestMaxDistance = Point3.max_km
        LowestMaxAddress = Point3.address
        LowestMaxCoordinates = Point3.coordinates
    
print ("Best address..")
print (LowestMaxAddress)
print (LowestMaxDistance)
print (LowestMaxCoordinates)

folium.Marker(location = [LowestMaxCoordinates[0], LowestMaxCoordinates[1]], \
              popup = LowestMaxAddress, icon = folium.Icon("green")).add_to(map)

# Save map:
map.save("NJCentralLocationMap.html")

# Open map in browser:
webbrowser.open('file:///C:/PythonProjects/folium_virtual_env/NJCentralLocationMap.html')

