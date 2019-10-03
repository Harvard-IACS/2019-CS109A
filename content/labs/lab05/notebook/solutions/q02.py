#heart_df.replace({'sex': {0.: 'F', 1.: 'M'}}, inplace=True)  
# We would use a countplot
ax = sns.countplot(x="sex", data=heart_df)
ax.set_title('Percentage of M vs. F who seek cardio examinations');
