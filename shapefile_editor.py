import geopandas as gpd;
import matplotlib.pyplot as plt;
import contextily as cx

#Import BC Shapefile to container 'bc'
csd = gpd.read_file("geopandas/SimplyAnalytics_Shapefiles_2023-10-20_16_17_51_ef068b258821baaa7114a00f97684db9/SimplyAnalytics_Shapefiles_2023-10-20_16_17_51_ef068b258821baaa7114a00f97684db9.shp")


cb = gpd.read_file("geopandas/gpr_000b11a_e/gpr_000b11a_e.shp")


csd_new = csd.to_crs('epsg:3347')


cb_new = cb.to_crs('epsg:3347')


new_shape = gpd.clip(csd_new, cb_new)


new_shape.to_file('geopandas/canada/canada.shp')