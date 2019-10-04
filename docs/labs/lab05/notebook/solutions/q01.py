fig, ax = plt.subplots(figsize=(8,6)) 
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
ax = sns.distplot(heart_df.age, kde=False, bins=10);
ax.set_xlim(0, 90);
ax.set_title('Ages seeking cardio exams');
#ax.set_xlabel('age of patient')
