import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data
data = {
    'S1': [78, 72, 75, 80],
    'S2': [85, 88, 82, 84],
    'S3': [67, 70, 65, 72],
    'S4': [90, 92, 88, 91],
    'S5': [73, 75, 78, 76],
    'S6': [81, 79, 83, 80],
    'S7': [69, 68, 72, 70],
    'S8': [94, 90, 92, 95],
    'S9': [76, 74, 79, 77],
    'S10': [88, 85, 86, 89]
}

# False -> S1..S10 are subjects (relationships between subjects)
# True  -> S1..S10 are students (relationships between students)
COMPARE_STUDENTS = False

df = pd.DataFrame(data)
df.index = [f'Student {i}' for i in range(1, len(df) + 1)]

sns.set_theme(style='whitegrid', palette='deep')

# 2. Basic exploration
print("Dataset:\n", df, "\n")
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum(), "\n")
print("Summary statistics:\n", df.describe().round(2), "\n")

# 3. Subject-wise score distributions
df_long = df.reset_index().melt(id_vars='index', var_name='Subject', value_name='Score')

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_long, x='Subject', y='Score', hue='Subject',
            palette='Set2', legend=False)
plt.title('Box Plot: Subject-wise Score Distribution')
plt.tight_layout()
plt.savefig('01_subject_boxplot.png', dpi=150)
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.histplot(df_long['Score'], bins=10, kde=True, color='steelblue', ax=axes[0])
axes[0].set_title('Overall Score Distribution')
axes[0].set_xlabel('Score')

mean_scores = df.mean().sort_values(ascending=False)
sns.barplot(x=mean_scores.index, y=mean_scores.values, hue=mean_scores.index,
            palette='viridis', legend=False, ax=axes[1])
axes[1].set_title('Mean Score per Subject')
axes[1].set_xlabel('Subject')
axes[1].set_ylabel('Mean Score')
axes[1].set_ylim(60, 100)

plt.tight_layout()
plt.savefig('02_overall_and_mean_scores.png', dpi=150)
plt.show()

# 4. Pairwise relationships (ALL columns, S1 to S10)
pair_df = df.T if COMPARE_STUDENTS else df
label = 'Students' if COMPARE_STUDENTS else 'Subjects'

pair = sns.pairplot(pair_df, kind='reg', diag_kind='kde', height=1.6,
                    plot_kws={'line_kws': {'color': 'red'},
                              'scatter_kws': {'s': 15}})
pair.figure.suptitle(f'Pairwise Relationships Between {label}', y=1.01)
pair.savefig('03_pairplot.png', dpi=150)
plt.show()

# 5. Correlation heatmap
corr = pair_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            vmin=-1, vmax=1, center=0, linewidths=0.5,
            cbar_kws={'label': 'Correlation coefficient'})
plt.title(f'Correlation Heatmap Between {label}')
plt.tight_layout()
plt.savefig('04_correlation_heatmap.png', dpi=150)
plt.show()

# 6. Key findings
print("Highest-scoring subject:", mean_scores.idxmax(), f"({mean_scores.max():.2f})")
print("Lowest-scoring subject :", mean_scores.idxmin(), f"({mean_scores.min():.2f})")
print("Most consistent subject:", df.std().idxmin(), f"(std {df.std().min():.2f})")
print("Most variable subject  :", df.std().idxmax(), f"(std {df.std().max():.2f})")