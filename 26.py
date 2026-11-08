import matplotlib.pyplot as plt

# Study hours and examination scores
study_hours = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6,
               6.5, 7, 7.5, 8, 8.5, 9]

scores = [45, 50, 55, 58, 60, 65, 68, 70, 72, 75,
          78, 80, 82, 85, 88, 92]

# Create a window with 2 subplots
plt.figure(figsize=(10, 4))

# First graph - Histogram
plt.subplot(1, 2, 1)
plt.hist(scores, bins=5, edgecolor='black')
plt.xlabel("Examination Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Scores")

# Second graph - Scatter plot
plt.subplot(1, 2, 2)
plt.scatter(study_hours, scores)
plt.xlabel("Study Hours")
plt.ylabel("Examination Score")
plt.title("Study Hours vs Scores")
plt.grid(True)

# Adjust spacing
plt.tight_layout()

# Display both graphs
plt.show()