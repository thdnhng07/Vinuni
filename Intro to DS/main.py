import numpy as np
import matplotlib.pyplot as plt

# Define weights
B1 = 2
B2 = -3

# Generate some random points
np.random.seed(0)
X1 = np.random.uniform(0, 5, 100)  # Random x1 values
X2 = np.random.uniform(0, 5, 100)  # Random x2 values

# Compute the classification
Y_hat = np.sign(B1 * X1 + B2 * X2)

# Plot points
plt.figure(figsize=(6,6))
plt.scatter(X1[Y_hat == 1], X2[Y_hat == 1], color='blue', label='+1 class')
plt.scatter(X1[Y_hat == -1], X2[Y_hat == -1], color='red', label='-1 class')

# Plot decision boundary (2x1 - 3x2 = 0) => x2 = (2/3)x1
x_vals = np.linspace(0, 5, 100)
y_vals = (2/3) * x_vals
plt.plot(x_vals, y_vals, 'k--', label='Decision Boundary')

plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("Linear Classifier with Sign Function")
plt.show()

# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go

# # Define weights
# B1 = 2
# B2 = -3

# # Generate some random points
# np.random.seed(0)
# X1 = np.random.uniform(0, 5, 100)  # Random x1 values
# X2 = np.random.uniform(0, 5, 100)  # Random x2 values

# # Compute the classification
# Y_hat = np.sign(B1 * X1 + B2 * X2)

# # Convert classes to colors
# colors = np.where(Y_hat == 1, "blue", "red")

# # Create scatter plot
# fig = px.scatter(x=X1, y=X2, color=colors, labels={'x': 'x1', 'y': 'x2'}, title="Linear Classifier with Sign Function")

# # Add decision boundary (2x1 - 3x2 = 0) → x2 = (2/3) * x1
# x_vals = np.linspace(0, 5, 100)
# y_vals = (2/3) * x_vals
# fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Decision Boundary', line=dict(color='black', dash='dash')))

# # Show the plot
# fig.show()

