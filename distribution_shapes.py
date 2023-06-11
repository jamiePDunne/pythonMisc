import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Example data
data_normal = np.random.normal(loc=0, scale=1, size=1000)  # Normal distribution
data_uniform = np.random.uniform(low=-1, high=1, size=1000)  # Uniform distribution
data_gamma = np.random.gamma(shape=2, scale=1, size=1000)  # Gamma distribution

# Plotting
sns.histplot(data_normal, kde=True, label='Normal')
sns.histplot(data_uniform, kde=True, label='Uniform')
sns.histplot(data_gamma, kde=True, label='Gamma')

# Set plot title and labels
plt.title('Distribution Shapes')
plt.xlabel('Value')
plt.ylabel('Count')

# Display the legend
plt.legend()

# Show the plot
plt.show()
