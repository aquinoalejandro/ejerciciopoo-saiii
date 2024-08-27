from database import Database
from estadistica import DataAnalysis
from visualizacion import DataVisualization
from dataset import CSVImporter
def main():
    db = Database(host='localhost', user='root', password='', database='CompanyData')

    # creo la tabla si no existe
    db.create_table()

    # importo datos desde el archivo CSV
    importer = CSVImporter(db)
    importer.import_csv('dataset.csv')

    data = db.fetch_data("SELECT * FROM EmployeePerformance")
    analysis = DataAnalysis(data)
    stats = analysis.calculate_statistics()
    correlations = analysis.calculate_correlations()

    print(stats)
    print(correlations)

    viz = DataVisualization(data)
    viz.plot_histogram()
    viz.plot_scatter('years_with_company', 'performance_score', 'Años en la compañia vs Puntaje')
    viz.plot_scatter('salary', 'performance_score', 'Salario vs Puntaje')

if __name__ == "__main__":
    main()
