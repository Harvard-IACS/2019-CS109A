fig, ax = plt.subplots(figsize=(20,6)) 
ax = sns.boxplot(x="age", y="restbp", data=heart_df)
ax.set_ylabel(None);
ax.set_xlabel('age', fontsize=14);
ax.set_ylabel('restbp (mmHg)', fontsize=14);
ax.set_title('Percentile Distibution for age and rest blood pressure', fontsize=14);
