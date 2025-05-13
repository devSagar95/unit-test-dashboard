import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Step 1: Load Jenkins test results CSV
df = pd.read_csv('jenkins_test_results.csv')

# Step 2: Process data - count test status (e.g., SUCCESS vs FAILURE)
status_count = df['Status'].value_counts()

# Step 3: Create a bar chart for test result summary
fig = px.bar(
    x=status_count.index,
    y=status_count.values,
    labels={'x': 'Test Status', 'y': 'Count'},
    title='Test Status Summary'
)

# Optional: Create a histogram of test durations
fig_duration = px.histogram(df, x='Duration', nbins=10, title='Test Duration Distribution')

# Step 4: Build Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Jenkins Unit Test Dashboard'),
    
    dcc.Graph(
        id='test-status-bar',
        figure=fig
    ),

    dcc.Graph(
        id='duration-histogram',
        figure=fig_duration
    ),
])

# Step 5: Run the Dash server
if __name__ == '__main__':
    app.run(debug=True)

