import csv
import numpy as np
from scipy import stats
import math
from constants import Constants

class CVAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.voltage = []
        self.capacitance = []
        self.start_idx = 0
        self.end_idx = 0
        self.slope = 0
        self.curve_fit = None
        self.results = {}

    def load_data(self):
        """Load CV data from CSV file"""
        with open(self.file_path, "r") as f:
            data = csv.reader(f)
            for i, row in enumerate(data):
                if i >= 3:  # Skip header rows
                    self.voltage.append(float(row[2]))
                    self.capacitance.append(float(row[3]))

    def plot_initial_data(self):
        """Plot initial voltage vs. capacitance data"""
        from plotter import Plotter
        plotter = Plotter(self)
        plotter.plot_initial_data()

    def select_voltage_range(self):
        """Allow user to select voltage range for analysis"""
        while True:
            print("-2.0 to -1.4 best for straight line")
            start_val = float(input("Enter the starting val of voltage: "))
            end_val = float(input("Enter the ending val of voltage: "))
            self.start_idx = self.find_nearest_index(start_val) - 3
            self.end_idx = self.find_nearest_index(end_val) - 3
            
            from plotter import Plotter
            plotter = Plotter(self)
            plotter.plot_selected_range()
            
            if int(input("Press 1 to try again else 0: ")) != 1:
                break

    def find_nearest_index(self, value):
        """Find index of nearest voltage value"""
        return min(range(len(self.voltage)), key=lambda i: abs(self.voltage[i] - value))

    def calculate_parameters(self, constants=None):
        """Calculate CV parameters based on selected voltage range"""
        if constants is None:
            constants = Constants()

        # Calculate slope of 1/C^2 vs V plot
        self.curve_fit = np.polyfit(self.voltage[self.start_idx:self.end_idx],
                                    self.capacitance[self.start_idx:self.end_idx], 1)
        self.slope = self.curve_fit[0]

        # Define physical constants
        k = 1.380e-23  # Boltzmann constant
        q = 1.6e-19  # Charge of electron
        epsilon_0 = 8.85418e-14  # Vacuum permittivity

        # Calculate semiconductor parameters
        N = 2 / (q * constants.epsilon_s * constants.area**2 * self.slope)
        LD = math.sqrt((constants.epsilon_s * k * constants.temperature) / (q**2 * abs(N)))
        Cs = constants.epsilon_s * constants.area / LD
        Cfb = (constants.Cox * Cs) / (constants.Cox + Cs)
        Vfb = self.voltage[self.find_nearest_index(Cfb)]
        phi_b = -(k * constants.temperature / q) * (math.log(abs(N) / 9.65e9))
        
        # Calculate work function difference based on semiconductor type
        if constants.semiconductor_type.lower() == "n":
            phi_ms = constants.phi_m - (constants.chi + (constants.Eg / 2) - phi_b)
        else:
            phi_ms = constants.phi_m - (constants.chi + (constants.Eg / 2) + phi_b)

        # Calculate effective charge and doping concentration
        Qeff = constants.Cox * (phi_ms - Vfb) / (q * constants.area)
        Neff = Qeff / q

        # Store results
        self.results = {
            "Slope": self.slope,
            "N": N,
            "|N|": abs(N),
            "LD": LD,
            "Cs": Cs,
            "Cfb": Cfb,
            "Vfb": Vfb,
            "phi_b": phi_b,
            "phi_ms": phi_ms,
            "Qeff": Qeff,
            "Neff": Neff
        }

    def recalculate_parameters(self, constants):
        """Recalculate parameters with updated constants"""
        self.calculate_parameters(constants)

    def print_results(self):
        """Print calculated results"""
        for key, value in self.results.items():
            if isinstance(value, float) and abs(value) < 1e-3:
                print(f"{key}: {value:.2e}")
            else:
                print(f"{key}: {value}")
