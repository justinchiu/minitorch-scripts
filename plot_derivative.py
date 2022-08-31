import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

p = 4
x = np.linspace(0,10)
y = x ** p

x_center = 5.
y_center = 5.


fig = go.Figure(data=[
    go.Scatter(x=x, y=y),
    go.Scatter(x=[x_center], y=[x_center**p], mode="markers", marker_size=25),
])

eps = np.arange(0.01, 4, 0.2)
for epsilon in eps:
    left = (x_center+epsilon, (x_center+epsilon)**p)
    right = (x_center-epsilon, (x_center-epsilon)**p)
    slope = (right[1] - left[1]) / (right[0] - left[0])
    y_line = slope * x + left[1] - slope * left[0]

    fig.add_trace(go.Scatter(
        x=[
            x_center+epsilon,
            x_center-epsilon
        ],
        y=[
            (x_center+epsilon)**p,
            (x_center-epsilon)**p,
        ], mode="markers", marker_size=25,
    ))
    fig.add_trace(go.Scatter(x=x, y=y_line))

fig.data[0].visible = True
fig.data[1].visible = True
fig.data[-1].visible = True
fig.data[-2].visible = True
for i in range(2, len(fig.data)-2):
    fig.data[i].visible = False

# Create and add slider
steps = []
for i in range(len(eps)):
    step = dict(
        method="update",
        args=[{"visible": [True,True] + [False] * (len(fig.data)-2)},]
    )
    step["args"][0]["visible"][2+2*i] = True  # Toggle i'th trace to "visible"
    step["args"][0]["visible"][2+2*i+1] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Epsilon: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()
