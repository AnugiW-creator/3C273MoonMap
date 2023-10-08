# 3C273MoonMap
  main_plotly.py: Moon with locations of deep moonquakes plotted. Requires 'moon_surface_gs.jpg' and 'nakamura_2005_dm_locations.csv'.

main_matplotlib.py: Rotating Moon with locations of deep moonquakes plotted. Requires 'moon_surface.jpg', 'nakamura_2005_dm_locations' and 'station_location.csv'.

moon_surface.jpg: JPEG of the Moon's surface. Original file was a .tif file, but we converted it to .jpg for ease.

moon_surface_gs.jpg: Moon's surface converted to greyscale.

nakamura_2005_dm_locations.csv: .csv file containing deep moonquake locations (in latitude and longitude). Also contains errors on the latitude and longitude, the depth and depth_errors of each quake and whether it was on the face of the Moon or not (none of which were used in the code).

station_location.csv: Locations of the measuring instruments. 

moon_simulation.py: Simulate the rotating Moon using matplotlib
