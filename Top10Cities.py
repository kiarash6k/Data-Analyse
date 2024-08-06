from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


city_data = np.array([
    ('Tehran', 8693706, 35.6892, 51.3890),
    ('Mashhad', 3001184, 36.2978, 59.6062),
    ('Esfahan', 2243249, 32.6525, 51.6746),
    ('Shiraz', 2450000, 29.5918, 52.5837),
    ('Tabriz', 1558693, 38.0800, 46.2919),
    ('Qom', 1201158, 34.6399, 50.8759),
    ('Ahvaz', 1184788, 31.3183, 48.6706),
    ('Kermanshah', 946651, 34.3142, 47.0650),
    ('Urumieh', 736224, 37.5527, 45.0760)
], dtype=[('name', 'U10'), ('population', 'i4'), ('latitude', 'f4'), ('longitude', 'f4')])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
m = Basemap(llcrnrlon=40., llcrnrlat=25., urcrnrlon=65., urcrnrlat=40.,
            rsphere=(6378137.00, 6356752.3142),
            resolution='i', projection='merc',
            lat_0=32., lon_0=53., lat_ts=20.)

m.drawcoastlines()
m.fillcontinents(color='lightgray')
m.drawcountries()
x, y = m(city_data['longitude'], city_data['latitude'])
m.scatter(x, y, s=city_data['population'] / 5000, color='green', marker='o', edgecolor='k', zorder=5)

def annotate_city(name, x, y):
    plt.annotate(name, (x+200000, y), color='white', weight='bold',
                 fontsize=8, ha='center', va='center')

annotate_vectorized = np.vectorize(annotate_city)
annotate_vectorized(city_data['name'], x, y)

ax.set_title('Top 9 Cities in Iran by Population')
plt.show()
