from cv_analysis import CVAnalysis
from plotter import Plotter
from constants import Constants

def main():
    # Initialize CV analysis with data file
    cv_analysis = CVAnalysis("CV Data.csv")
    
    # Load and process data
    cv_analysis.load_data()
    cv_analysis.plot_initial_data()
    cv_analysis.select_voltage_range()
    cv_analysis.calculate_parameters()
    cv_analysis.print_results()
    
    # Plot curve fit
    plotter = Plotter(cv_analysis)
    plotter.plot_curve_fit()
    
    # Allow user to update constants and recalculate
    constants = Constants()
    while True:
        if not constants.update_constants():
            break
        cv_analysis.recalculate_parameters(constants)
        cv_analysis.print_results()

if __name__ == "__main__":
    main()
