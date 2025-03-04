# MOCCAS: MOS Capacitor Characterization and Analysis Suite

## Description

MOCCAS (MOS Capacitor Characterization and Analysis Suite) is a Python-based tool designed for comprehensive analysis of MOS (Metal-Oxide-Semiconductor) capacitors. It processes Capacitance-Voltage (CV) measurement data, calculates key semiconductor parameters, and provides graphical representations of the results.

## Features

- CV data processing from CSV files
- Interactive voltage range selection
- Calculation of crucial MOS capacitor parameters:
  - Doping concentration (N)
  - Debye length (LD)
  - Flatband capacitance (Cfb)
  - Flatband voltage (Vfb)
  - Work function difference (φms)
  - Effective charge (Qeff)
  - Effective doping concentration (Neff)
- Visualization capabilities:
  - Raw CV data plots
  - Selected voltage range analysis
  - Curve fitting and parameter extraction

## Installation

1. Clone the repository:
git clone https://github.com/gunavant-s/MOCCAS.git

2. Navigate to the project directory:
cd MOCCAS

3. Install required dependencies:
pip install -r requirements.txt


## Usage

1. Execute the main script:
python main.py

2. Follow the interactive prompts to:
- Import your CV data
- Define the voltage range for analysis
- Input necessary constants
- View calculated results and generated plots
- Optionally refine constants and recalculate

## Project Structure

- `main.py`: Program entry point
- `cv_analysis.py`: Core CVAnalysis class for data processing
- `plotter.py`: Visualization module
- `constants.py`: Physical and user-defined constants management

## Dependencies

- numpy
- matplotlib
- scipy

## Contributing

Contributions to enhance MOCCAS are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Gunavant Setty - gsetty@ncsu.edu

Project Link: [https://github.com/gunavant-s/MOCCAS](https://github.com/gunavant-s/MOCCAS)

