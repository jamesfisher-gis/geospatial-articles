from osgeo import gdal
import numpy as np

import matplotlib.pyplot as plt

# Url to publicly available geo-image. This is an NAIP image of New Orleans, Louisiana, USA
url = "https://prd-tnm.s3.amazonaws.com/StagedProducts/NAIP/la_2015/29090/m_2909007_ne_15_1_20150430_20151019.jp2"

ds = gdal.Open('/vsicurl/%s' %(url))

print(gdal.Info(ds))

# NAIP is 4 bands Red (1), Green (2), Blue (3), and IR (4)
band1 = ds.GetRasterBand(1)
band2 = ds.GetRasterBand(2) 
band3 = ds.GetRasterBand(3) 

# Read as numpy arrays
b1 = band1.ReadAsArray()
b2 = band2.ReadAsArray()
b3 = band3.ReadAsArray()

# Visualize the image
img = np.dstack((b1, b2, b3))
f = plt.figure()
plt.imshow(img)
plt.show()