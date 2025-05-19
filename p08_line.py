import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name = ['Python','Java','C','C++','R','Go','Ruby']
cnt = [2436,2159,1395,1140,890,745,598]

xt = np.arange(len(name))
#---------Draw Bar Chart ---------------
#plt.bar(xt,cnt)
#plt.bar(xt,cnt,color='y')
#plt.bar(xt,cnt,color=['y','b'])
plt.bar(xt,cnt,color=['y','b','g'])
#---------Draw X ticks and tick-labels---------------
ax = plt.gca()
ax.tick_params(axis='x',
               colors='r',
               width = 5,
               size=20,
               tickdir='inout',    # str, ('in', 'out', 'inout')
               #labeltop=True,
               labelbottom=True
               )
plt.xticks( xt, labels= name,
            rotation=60,
            fontsize=12,
            fontweight='bold',
            color = 'b'
           )
#---------Draw Y ticks and tick-labels---------------
ax.yaxis.set_ticks_position('both')
ax.tick_params(axis='y',
               colors='r',
               width = 10,
               size=5,
               tickdir='out',    # str, ('in', 'out', 'inout')
               labelleft=True,
               labelright=True
               )
yt = np.linspace(0,max(cnt),7).astype(int)

plt.yticks( yt,
            labels=yt,
            rotation = 20,
            fontsize=12,
            fontweight='bold',
            color = '#ffffff'
           )
#---------Draw text ---------------
for x, y in zip(xt, cnt):
    plt.text(x, y, str(y), # x, y-1000, str(y),
             ha='center',  # center, left, right
             fontsize=10,
             fontweight='bold',
             va='top',  # bottom,top,center
             color='#FF0000')
#---------Draw Title---------------
plt.title('Popular programming languages',            # str, Title
          fontweight = 'bold',          # str,
          style = 'italic',             # str
          fontsize=25,                  # int
          fontname='Times New Roman',   # str
          color='#FFFFFF',              # str, Fore color
          backgroundcolor='#009090',    # str
          loc='center', #center, right   # str, Location (options=> left, center, right
          pad=20 )                      # float, padding points(pixels) to the bounding box plot
#---------Draw X label---------------
plt.xlabel('Language',                           # str, The label text.
           fontsize=24,                     # int, Font size
           fontname='Times New Roman',      # str, Font Name
           fontweight = 'heavy',
           color='#ffff00',                 # str, Fore Color of the text
           backgroundcolor='#009090',       # str, Back Color of the text
           loc = 'center', # center, right  # str, Location of the text (options => center, left, right
           labelpad = 10                    # float, Spacing in points from the axes bounding box including
                                            # ticks and tick labels.
           )
#---------Draw Y label---------------
plt.ylabel('Count',          # str
           fontsize=24,
           fontweight = 'extra bold',
           color='#ffff00',
           backgroundcolor='#009090',
           fontname='Times New Roman',
           loc = 'top', # center, bottom
           labelpad = 10
           )
#---------Change entite background color of a figure and plot---------------
plt.gcf().patch.set_facecolor('#909090')
ax.set_facecolor('#707070')
#---------Change entite background color of a figure ---------------

ax.axhline(2000, zorder=1, color = 'r', ls='-',lw=3)
ax.axvline(3, zorder=1, color = 'r', ls='-',lw=3)
ax.text(1,1500,s='KKK', ha='center',va='center',
        fontsize=20,
        rotation=40)

plt.tight_layout()
plt.show()


'''
Question:
Create a Python program that reads rainfall data from a CSV or Excel file and 
plots a line chart using Matplotlib and Pandas. 
Ensure the chart is well-labeled, includes a legend, and is saved as an image.
'''