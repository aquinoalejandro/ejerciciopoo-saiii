import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self):
        departments = self.data['department'].unique()
        for dept in departments:
            dept_data = self.data[self.data['department'] == dept]
            plt.hist(dept_data['performance_score'], bins=10, alpha=0.5, label=dept)
        plt.xlabel('Performance Score')
        plt.ylabel('Frequency')
        plt.legend()
        plt.title('Histogram of Performance Scores by Department')
        plt.show()

    def plot_scatter(self, x_col, y_col, title):
        plt.scatter(self.data[x_col], self.data[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(title)
        plt.show()
