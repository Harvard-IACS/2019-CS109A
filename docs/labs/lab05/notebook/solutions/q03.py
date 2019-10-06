categorical = ["sex", "cp", "fbs", "restecg", "exang",  "slope", "ca", "thal", "hd"]
numerical = ["age","restbp", "chol", "thalach",  "oldpeak"]

# pandas trick: give me all rows of numerical columns
sns.set_context("notebook", font_scale=1, rc={"lines.linewidth": 2.5})
df_to_plot = heart_df.loc[:,numerical]
sns.pairplot(df_to_plot);

plt.show()

# Look at correlation coefficients too
corr_matrix = heart_df.corr()
corr_matrix['hd'].sort_values(ascending=False)
