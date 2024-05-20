def classify_path(start, end, route, distance, elevation_gain):
    points=[0,0,0,0,0]
    if start =="Central":
        points[0]+=1
        points[1]+=1
    if start == "Walchenbrücke":
        points[2]+=1
    if start == "Main building":
        points[3]+=1
        points[4]+=1
    if end == "Main building":
        points[0]+=1
        points[1]+=1
        points[2]+=1
    if end == "Walchenbrücke":
        points[3]+=1
    if end == "Bahnhofquai":
        points[4]+=1
    if 825<distance<835:
        points[0]+=1
        points[2]+=1
        points[3]+=1
    if 835<distance<845:
        points[1]+=1
    if 775<distance<785:
        points[4]+=1
    if 43<elevation_gain<45:
        points[0]+=1
        points[1]+=1
    if 46<elevation_gain<48:
        points[2]+=1
    if -48<elevation_gain<=-46:
        points[3]+=1
    if -46<elevation_gain<=-44:
        points[4]+=1


    
    return points 

def get_max_path(arr):
	max_i=-9
	max_value=-9
	for i in range(len(arr)):
		if arr[i]<i:
			max_i=i
			max_value=arr[i]
	return 	max_i-1		
paths=classify_path("Main building", "Walchenbrücke", "Weinbergstrasse – Leonhardstrasse – Rämistrasse", 840, 47)	 
print(paths)
print(get_max_path(paths))
"""
paths = [
    {"start": "Central", "end": "Main building, center in front on Rämistrasse side", "route": "Weinbergstrasse – Leonhardstrasse – Rämistrasse", "distance": 830, "elevation_gain": 44, "special_notes": "Do not take the shortcut to cut the corner from Weinbergstrasse to Leonhardstrasse."},
    {"start": "Central", "end": "Main building, center in front on Rämistrasse side", "route": "Weinbergstrasse – Leonhardstrasse – Clausiusstrasse – Rämistrasse", "distance": 840, "elevation_gain": 44, "special_notes": "Do not take the shortcut to cut the corner from Weinbergstrasse to Leonhardstrasse."},
    {"start": "Walchenbrücke, east edge", "end": "Main building, center in front on Rämistrasse side", "route": "Walchebrücke – Walchetor (pedestrian passage with a short staircase) – across Stampfenbachstrasse, up the stairs to Leonhardstrasse – Rämistrasse", "distance": 830, "elevation_gain": 47, "special_notes": "Do not take the shortcut to cut the corner from Weinbergstrasse to Leonhardstrasse."},
    {"start": "Main building, center in front on Rämistrasse side", "end": "Walchenbrücke, east edge", "route": "Rämistrasse – Leonhardstrasse – stairs down to Stampfenbachstrasse – Walchetor (pedestrian passage with a short staircase) – Walchebrücke", "distance": 830, "elevation_gain": -47, "special_notes": "Do not take the shortcut to cut the corner from Leonhardstrasse to Weinbergstrasse."},
    {"start": "Main building, center in front on Rämistrasse side", "end": "Junction Bahnhofquai, Bahnhofbrücke", "route": "Rämistrasse – Karl-Schmid-Strasse – Schienhutgasse – Hirschengraben – Central – Bahnhofbrücke", "distance": 780, "elevation_gain": -45, "special_notes": "Make sure to use the Hirschengraben street and not Seilergraben street before Central (they run in parallel, Hirschengraben is elevated above Seilergraben)"}
]

"""