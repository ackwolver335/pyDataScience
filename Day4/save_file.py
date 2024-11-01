# a general file for saving matplotlib charts
import matplotlib.pyplot as plt

# general data values for plotting pie chart
exp_vals = [1400,600,300,410,250]
exp_labels = ['Home Rent','Food','Phone/Internet Bills','Car','Other Utilities']

# plotting chart and others
plt.axis('equal')
plt.pie(exp_vals,labels = exp_labels,radius = 1,autopct = '%0.0f%%',shadow = True,explode = [0,0.2,0.2,0,0],startangle = 90)

# plt.show()          # for showing the plot
# saving the file here
plt.savefig('piefile.png',bbox_inches = 'tight',pad_inches = 1,transparent = True)