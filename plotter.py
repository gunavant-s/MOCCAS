import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, cv_analysis):
        self.cv_analysis = cv_analysis

    def plot_initial_data(self):
        """Plot initial voltage vs. capacitance data"""
        plt.plot(self.cv_analysis.voltage, self.cv_analysis.capacitance, '-o')
        plt.xlabel("Voltage")
        plt.ylabel("1/C^2")
        plt.title("Initial CV Data")
        plt.show()

    def plot_selected_range(self):
        """Plot selected voltage range"""
        start = self.cv_analysis.start_idx
        end = self.cv_analysis.end_idx
        plt.plot(self.cv_analysis.voltage[start:end],
                 self.cv_analysis.capacitance[start:end], '-o')
        plt.xlabel("Voltage")
        plt.ylabel("1/C^2")
        plt.title("Selected Voltage Range")
        plt.show()

    def plot_curve_fit(self):
        """Plot actual data and curve fit"""
        start = self.cv_analysis.start_idx
        end = self.cv_analysis.end_idx
        v = self.cv_analysis.voltage[start:end]
        c = self.cv_analysis.capacitance[start:end]
        
        poly = np.poly1d(self.cv_analysis.curve_fit)
        fitted_c = poly(v)

        plt.plot(v, c, '-o', color='r', label="Actual Data")
        plt.plot(v, fitted_c, '--', color='b', label="Curve Fit")
        plt.legend()
        plt.xlabel("Voltage")
        plt.ylabel("1/C^2")
        plt.title("CV Data with Curve Fit")
        plt.show()
