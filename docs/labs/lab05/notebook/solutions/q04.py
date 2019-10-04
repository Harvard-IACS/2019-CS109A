# first find percentages
per_men = (heart_df.sex.value_counts()[1])/(heart_df.sex.value_counts()[0]+heart_df.sex.value_counts()[1])
per_wom = (heart_df.sex.value_counts()[0])/(heart_df.sex.value_counts()[0]+heart_df.sex.value_counts()[1])
per_men, per_wom

labels = 'Men', 'Women'
explode = (0, 0.1)  # only "explode" the 2nd slice 
sizes = [per_men, per_wom]

# First and last time I will use a pie chart!!
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
