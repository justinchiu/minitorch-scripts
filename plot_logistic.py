import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

mean1 = (1,1)
mean2 = (-1,-1)

std = .5

num_samples = 5

x1 = np.random.normal(mean1, std, (5,2))
x2 = np.random.normal(mean2, std, (5,2))
x = np.concatenate((x1, x2), axis=0)

#w = np.random.normal(0,1, (2,))
w = np.array((10,10))
b = 0

y = 1 / (1 + np.exp(-x @ w + b))

fig = go.Figure(data=[
    go.Scatter3d(z=y, x=x[:,0], y=x[:,1], mode="markers", marker_color="green"),
    go.Scatter3d(
       z=np.zeros(num_samples)-1,
       x=x[:num_samples,0],
       y=x[:num_samples,1],
       mode="markers",
       marker_color="blue",
    ),
    go.Scatter3d(
        z=np.zeros(num_samples)-1,
        x=x[num_samples:,0],
        y=x[num_samples:,1],
        mode="markers",
        marker_color="red",
    ),
])
fig.show()
