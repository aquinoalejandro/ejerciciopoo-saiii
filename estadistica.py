class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        stats = self.data.groupby('department').agg({
            'performance_score': ['mean', 'median', 'std'],
            'salary': ['mean', 'median', 'std'],
            'employee_id': 'count'
        })
        return stats

    def calculate_correlations(self):
        correlations = {
            'years_with_company_performance': self.data['years_with_company'].corr(self.data['performance_score']),
            'salary_performance': self.data['salary'].corr(self.data['performance_score'])
        }
        return correlations
