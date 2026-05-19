# Import libraries:
import csv
import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
import webbrowser

###########################################################################################

# Custom class to store coordinates on a map, along with distances to other points:

class MapPoints:

    def __init__ (self, address, coordinates, region, avg_km, max_km, min_km):
        self.address = address
        self.coordinates = coordinates
        self.region = region
        self.avg_km = avg_km
        self.max_km = max_km
        self.min_km = min_km

###########################################################################################

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

#############################################################################################

def ImportAddresses(AllMapPoints):

# Read a file of addresses into list of all coordinates:

    with open('Hospital_General_Information.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        for oneLine in csv_reader:

            if oneLine[4] == "CT":
        
                # Concatenate address fields for geocoding:
                OneAddress = (oneLine[2] + "," + oneLine[3] + "," + oneLine[4] + "," + oneLine[5] + ", United States")
    
                # Create instance of map coordinate object:
                OneMapPoint = MapPoints(OneAddress, (), None, None, None, None )

                # Add this map point to the list of all map points:
                AllMapPoints.append (OneMapPoint)

#############################################################################################
                
def GeocodeAddresses(AllMapPoints):

    print ("Begin geocoding....")

    # Select geocoder:
    geolocator = Nominatim(user_agent = "my_geocoding_app")

    # Geocode every address:
    for Point1 in AllMapPoints:
        # Geocode each address:
        location = geolocator.geocode (Point1.address, timeout = 60)
        if location:
            # Save coordinates as a tuple:
            Point1.coordinates = (location.latitude, location.longitude)
        else:
            Point1.coordinates = None
    
#############################################################################################

def CalculateDistances (AllMapPoints, RegionFilter):
    
    print ("Begin calculating distances between coordinates...")

    for Point1 in AllMapPoints:

        if Point1.region in RegionFilter:
        
            MaxDistance = 0
        
            for Point2 in AllMapPoints:
                
                if Point1.coordinates != None and Point2.coordinates != None and Point2.region in RegionFilter:
                    
                    distance = haversine(Point1.coordinates, Point2.coordinates)
                    
                    if  distance > MaxDistance:
                        MaxDistance = distance
                        
            Point1.max_km = MaxDistance

############################################################################################

def FindCentralPoint (AllMapPoints):

    global LowestMaxAddress
    global LowestMaxCoordinates

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


############################################################################################

def FindCentralPointRegion (AllMapPoints, RegionFilter):

    global LowestMaxAddress
    global LowestMaxCoordinates

    # Calculate coordinate with lowest maximum distance. That coordinate will be central to everyone:
    LowestMaxDistance = 999999999999.9
    LowestMaxAddress = ""
    LowestMaxCoordinates = ()
    
    for Point3 in AllMapPoints:
        
        if Point3.region in RegionFilter and Point3.max_km != None and Point3.max_km < LowestMaxDistance and Point3.max_km > 0 :
            
            LowestMaxDistance = Point3.max_km
            LowestMaxAddress = Point3.address
            LowestMaxCoordinates = Point3.coordinates
        
    print ("Best address in region")
    print (LowestMaxAddress)
    print (LowestMaxDistance)
    print (LowestMaxCoordinates)

#############################################################################################

def CreateMap (AllMapPoints):

    global LowestMaxAddress
    global LowestMaxCoordinates
    
    # Create map:
    map = folium.Map(location = [40.21620713307166, -74.67546739319853], zoom_start = 8)

    # Add all coordinates to map:
    for Point3 in AllMapPoints:
        if Point3.coordinates != None and Point3.region == "North":
            folium.Marker(location=[Point3.coordinates[0],Point3.coordinates[1]],popup=Point3.address,icon=folium.Icon(color="green")).add_to(map)
        elif Point3.coordinates != None and Point3.region == "South":
            folium.Marker(location=[Point3.coordinates[0],Point3.coordinates[1]],popup=Point3.address,icon=folium.Icon(color="blue")).add_to(map)

    # Add marker for center of area:
    folium.Marker(location = [CentralPointCoordinates[0], CentralPointCoordinates[1]], \
                  popup = CentralPointAddress, icon = folium.Icon("red")).add_to(map)

    # Add marker for center of North region:
    folium.Marker(location = [NorthCentralPointCoordinates[0], NorthCentralPointCoordinates[1]], \
                  popup = NorthCentralPointAddress, icon = folium.Icon("red")).add_to(map)

    # Add marker for center of South region:
    folium.Marker(location = [SouthCentralPointCoordinates[0], SouthCentralPointCoordinates[1]], \
                  popup = LowestMaxAddress, icon = folium.Icon("red")).add_to(map)
    

    # Save map:
    map.save("NJCentralLocationMap.html")

    # Open map in browser:
    webbrowser.open('file:///C:/PythonProjects/folium_virtual_env/NJCentralLocationMap.html')

############################################################################################

def CreateRegions (AllMapPoints):

    global CentralPointCoordinates
    CentralPointLatitude = CentralPointCoordinates[0]

    print("This is the central point latitude...")

    print (CentralPointLatitude)

    for MyPoint in AllMapPoints:

        if MyPoint.coordinates != None:
            
            if MyPoint.coordinates[0] >= CentralPointLatitude:
                MyPoint.region = "North"
            else:
                MyPoint.region = "South"
    
############################################################################################

# Main code:

global LowestMaxAddress
global LowestMaxCoordinates
global CentralPointCoordinates
global CentralPointAddress
global NorthCentralPointCoordinates
global NorthCentralPointAddress
global SouthCentralPointCoordinates

# List to store all coordinates:
AllMapPoints = []

# Import all addresses from CSV file:
ImportAddresses (AllMapPoints)

# Geocode all addresses:
GeocodeAddresses (AllMapPoints)

# Calculate the lowest of the maximum distance for each point:
CalculateDistances (AllMapPoints, [None])

# Find the central point of the map:
FindCentralPoint (AllMapPoints)
CentralPointCoordinates = LowestMaxCoordinates
CentralPointAddress = LowestMaxAddress

# Use the central point to create 2 regions -- North and South:
CreateRegions (AllMapPoints)

# Create a map of all coordinates and the central location:
#CreateMap (AllMapPoints)

# Calculate the lowest maximum distance for each point in North:
CalculateDistances (AllMapPoints, ["North"])

# Find the central point of the north region:
FindCentralPointRegion (AllMapPoints, ["North"])
NorthCentralPointCoordinates = LowestMaxCoordinates
NorthCentralPointAddress = LowestMaxAddress

# Find the central point of the north region:
FindCentralPointRegion (AllMapPoints, ["South"])
SouthCentralPointCoordinates = LowestMaxCoordinates

# Create a map of all coordinates and the central location:
CreateMap (AllMapPoints)


