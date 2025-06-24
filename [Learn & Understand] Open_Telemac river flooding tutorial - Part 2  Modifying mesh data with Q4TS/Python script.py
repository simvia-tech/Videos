import numpy as np
from data_manip.extraction.telemac_file import TelemacFile
from matplotlib.path import Path
import matplotlib.pyplot as plt
from postel.plot2d import plot2d_scalar_map
import csv

############# RUN THIS SCRIPT INSIDE THE TELEMAC CONTAINER #################

#To get the polygon CSV from QGIS, click on the polygon you want
#And use the toolbox function "extract vertices" -> Create it as a temporary layer
#Then right click on the temp layer, export, save feature as, format CSV and Geometry: "as_XY"


#inputs...
res_file = '/home/user/.q4ts/yvette_bottom_clc_river.slf'
polygon_csv = '/home/user/data/videos/video_telemac/polygon_vertices.csv'
bottom_shift = -2



def shift_bottom_inside_polyhon(res_file, polygon_csv, bottom_shift):
    #read the .slf file
    res = TelemacFile(res_file, access='rw')

    #append the pollygon cordinates to this list
    polygon_coords = []
    with open(polygon_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x = float(row['X'])
            y = float(row['Y'])
            polygon_coords.append((x, y))
    polygon_coords = np.array(polygon_coords)

    #get x and y values of the mesh, get bottom value
    x, y = res.meshx, res.meshy
    bottom = res.get_data_value('BOTTOM', 0)

    #isolate all points of mesh inside the polygon
    polygon_path = Path(polygon_coords)
    points = np.vstack((x, y)).T
    inside = polygon_path.contains_points(points)

    #for these points, substract this value to bottom
    bottom[inside] += bottom_shift
    res.set_data_value('BOTTOM', 0, bottom)
    res.close()

    #Plotting ...
    res = TelemacFile(res_file)
    bottom = res.get_data_value('BOTTOM', 0)
    fig, ax = plt.subplots(figsize=(12, 6))
    plot2d_scalar_map(fig, ax, res.tri, bottom, data_name='Modified Bottom (m)')
    plt.show()
    res.close()


shift_bottom_inside_polyhon(res_file, polygon_csv, bottom_shift)
