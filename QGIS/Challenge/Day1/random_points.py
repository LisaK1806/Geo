import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point
import random

gdf = gpd.read_file("C:/Users/Liza/Documents/my_data/environmental/GIS/challenge/day_1/districts_with_points.geojson")

def generate_random_points(polygon, num_points):
    minx, miny, maxx, maxy = polygon.bounds
    points = []
    while len(points) < num_points:
        point = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(point):
            points.append(point)
    return points
    
all_points = []
for _, row in gdf.iterrows():
    num = int(row['n_points'])
    pts = generate_random_points(row.geometry, num)
    for pt in pts:
        all_points.append({'geometry':pt, 'area_code':row['LSOA21CD']})
        
points_gdf = gpd.GeoDataFrame(all_points, crs=gdf.crs)
points_gdf.to_file("random_points.geojson", driver = "GeoJson")