# def is_Supermoon(Earth_Dist, Age_of_Moon):
    
#     # Defining the threshold for perigee distance (90% of perigee distance)
#     # 1 AU = 149,597,871km
#     perigee_threshold = 0.9 * Earth_Dist * 149597871
    
#     # Check if the moon is at or within 90% of its perigee distance
#     if Earth_Dist <= perigee_threshold:
        
#         # Check if the moon is the brightest at this point in time (assumed condition)
#         if Age_of_Moon >= 14.8 and Age_of_Moon <= 22.1:  # Adjust the threshold based on your data
#             return True

#     return False


# #2023,Oct,2
# EarthDist = 0.0025  
# AgeOfMoon = 17 

# if is_Supermoon(EarthDist, AgeOfMoon):
#     print("Supermoon is predicted!")
# else:
#     print("Not a supermoon.")


# #2025,Jun,23
# EarthDist = 0.0024  
# AgeOfMoon = 27 

# if is_Supermoon(EarthDist, AgeOfMoon):
#     print("Supermoon is predicted!")
# else:
#     print("Not a supermoon.")




import pandas as pd
import numpy as np

# Load the ephemeris data for the moon
ephemeris_data = pd.read_csv("https://github.com/DespCAP/APV_2023/raw/main/ephemeris_moon.csv")

# Calculate the moon's distance from Earth (perigee distance)
perigee_distance = np.min(ephemeris_data["Earth Dist (AU)"])

# Identify the dates when the moon is at or within 90% of its perigee distance
supermoon_days = ephemeris_data[ephemeris_data["Earth Dist (AU)"] <= perigee_distance * 0.9]

ephemeris_data['Age of Moon'] = ephemeris_data['Age of Moon'].str.replace('\D', '', regex=True)


# print(ephemeris_data['Age of Moon'])

ephemeris_data['Age of Moon'] = ephemeris_data['Age of Moon'].astype(float)

# print(ephemeris_data['Age of Moon'])

# Identify the dates when the moon is a full moon

# print(ephemeris_data['Age of Moon'][2])


fullmoon_days = ephemeris_data[ephemeris_data['Age of Moon'] >=14.8 and ephemeris_data['Age of Moon'] <=22.1]

if fullmoon_days and supermoon_days:
  print("SuperMoon Occured")
else:
  print("SuperMoon not Occured")

