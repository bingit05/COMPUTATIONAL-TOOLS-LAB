import numpy as np

students = np.array(["S1","S2","S3","S4","S5"])

mid_marks = np.array([

    [65,70,68,72],
    [78,75,80,77],
    [55,60,58,62],
    [82,85,80,88],
    [70,68,72,74]

])

end_marks = np.array([

    [72,78,75,80],
    [84,82,86,83],
    [65,68,66,70],
    [88,90,85,92],
    [78,75,80,82]


])


mid_total = np.sum(mid_marks, axis=1)
end_total = np.sum(end_marks, axis=1)


mid_average = np.mean(mid_marks,axis=1)
end_average = np.mean(end_marks,axis=1)

improvement = ((end_total - mid_total)/mid_total)*100


print("Student\tMid Total\t End Total\tMid Avg\tEnd Avg\t% Improvement")

for i in range(len(students)):
        print(f"{students[i]}\t{mid_total[i]}\t\t{end_total[i]}"
            f"\t\t{mid_average[i]:.2f}\t{end_average[i]:.2f}"
            f"\t{improvement[i]:.2f}%")