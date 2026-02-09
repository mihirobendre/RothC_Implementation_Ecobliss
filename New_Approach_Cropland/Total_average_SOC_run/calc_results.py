
from run_rothc import run_rothc
import pandas as pd

# Project model run
output_months_project, output_years_project = run_rothc(
	starting_soil_carbon=31.84,
	total_years=40,
	start_year=2026,
	clay=18,
	depth=30,
	temp = [27.7, 30.3, 31.8, 30.9, 29.3, 27.6, 26.6, 26, 26.4, 28, 28.8, 27.8],
	rain = [5, 10.9, 20.9, 86.4, 130.1, 141.8, 139.7, 241, 198.1, 82.9, 5.2, 0.3],
	evap = [193.33, 200, 230.67, 225.33, 220, 192, 176, 164, 162.67, 190.67, 192, 192],
	pc = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	dpm_rpm = 1.44,
	carbon_input = None,			# annual input
	farmyard_manure = 0.5535,
	carbon_input_eqm = None,		  # annual input
	farmyard_manure_eqm = 0.1*0.5535,	   # annual input
	additional_c_in = 1.599,
	trm = 0.93
)



# Baseline model run
output_months_baseline, output_years_baseline = run_rothc(
	starting_soil_carbon=31.84,
	total_years=40,
	start_year=2026,
	clay=18,
	depth=30,
	temp = [27.7, 30.3, 31.8, 30.9, 29.3, 27.6, 26.6, 26, 26.4, 28, 28.8, 27.8],
	rain = [5, 10.9, 20.9, 86.4, 130.1, 141.8, 139.7, 241, 198.1, 82.9, 5.2, 0.3],
	evap = [193.33, 200, 230.67, 225.33, 220, 192, 176, 164, 162.67, 190.67, 192, 192],
	pc = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	dpm_rpm = 1.44,
	carbon_input = None,			# annual input
	farmyard_manure = 0.1*0.5535,
	carbon_input_eqm = None,		  # annual input
	farmyard_manure_eqm = 0.1*0.5535,	   # annual input
	additional_c_in = 0.0,
	trm = 1.0
)



with pd.ExcelWriter("year_results.xlsx") as writer:
	output_years_project.to_excel(writer, sheet_name="Project", index=False)
	output_years_baseline.to_excel(writer, sheet_name = "Baseline", index=False)




