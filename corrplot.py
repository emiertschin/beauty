import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import Colormap, Normalize, LinearSegmentedColormap
import csv
import openpyxl


df = pd.read_excel('correlation_body.xlsx', sheet_name='categories') # can also index sheet by name or fetch all sheets

data=df.loc[:,~df.columns.isin(['ID','Price'])]
print(data.corr())

cmap_colors = [(0, 0, 1), (1, 1, 1), (1, 0, 0)]  # Blue, White, Red
cmap = LinearSegmentedColormap.from_list("Custom_CMAP", cmap_colors, N=256)


# Set the normalization scale for the colormap
plt.matshow(data.corr(), cmap=cmap, vmin=-1,vmax=1)

# Add x-axis and y-axis labels
plt.xticks(range(len(data.columns)), data.columns, rotation='vertical')
plt.yticks(range(len(data.columns)), data.columns)

plt.xlabel('Columns')
plt.ylabel('Columns')

plt.colorbar()

plt.show()


df = pd.DataFrame(data.corr())
df.to_csv('corroutput_body.csv',index=False)