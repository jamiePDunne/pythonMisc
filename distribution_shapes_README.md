# Distribution Shapes

This is a simple Python script that demonstrates how to generate random data from different probability distributions and plot their histograms using the `seaborn` and `matplotlib` libraries.

## Dependencies
- `seaborn`
- `matplotlib`
- `numpy`

## Installation
1. Clone this repository or download the script file.

   ```shell
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. Install the required dependencies using `pip`.

   ```shell
   pip install seaborn matplotlib numpy
   ```

## Usage
1. Import the necessary libraries in your Python script.

   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt
   import numpy as np
   ```

2. Define the parameters for the random data generation. In this example, we generate data from three different distributions: normal, uniform, and gamma.

   ```python
   data_normal = np.random.normal(loc=0, scale=1, size=1000)  # Normal distribution
   data_uniform = np.random.uniform(low=-1, high=1, size=1000)  # Uniform distribution
   data_gamma = np.random.gamma(shape=2, scale=1, size=1000)  # Gamma distribution
   ```

3. Plot the histograms using `seaborn.histplot`. We enable kernel density estimation (KDE) and provide labels for each distribution.

   ```python
   sns.histplot(data_normal, kde=True, label='Normal')
   sns.histplot(data_uniform, kde=True, label='Uniform')
   sns.histplot(data_gamma, kde=True, label='Gamma')
   ```

4. Set the title and labels for the plot.

   ```python
   plt.title('Distribution Shapes')
   plt.xlabel('Value')
   plt.ylabel('Count')
   ```

5. Display the legend.

   ```python
   plt.legend()
   ```

6. Show the plot.

   ```python
   plt.show()
   ```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request in the [GitHub repository](https://github.com/yourusername/yourrepository).

## License
This project is licensed under the [MIT License](LICENSE).
