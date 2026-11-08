
import pandas as pd
import plotly.express as px

# Student examination data
data = {
    'Student': ['S1', 'S2', 'S3', 'S4', 'S5',
                'S6', 'S7', 'S8'],
    'Mathematics': [78, 72, 75, 80, 85, 88, 82, 84]
}

df = pd.DataFrame(data)

# Create an interactive bar chart
fig = px.bar(
    df,
    x='Student',
    y='Mathematics',
    title='Mathematics Marks of Students',
    labels={
        'Student': 'Students',
        'Mathematics': 'Marks'
    },
    color='Mathematics',
    text='Mathematics'
)

# Customize the chart
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Students',
    yaxis_title='Marks',
    yaxis_range=[0, 100]
)

# Display the chart
fig.show()
