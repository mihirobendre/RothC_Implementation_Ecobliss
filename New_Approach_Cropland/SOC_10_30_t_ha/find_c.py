
from run_rothc import run_rothc, c_input_calculator, solve_carbon_input
import pandas as pd
import numpy as np

'''
starting_c_in = 2

months_df, years_df = run_rothc(
	starting_soil_carbon=31.84,
	total_years=0,
	carbon_input_project = starting_c_in,
	start_year=2030
)

baseline_soc = years_df.at[0,'SOC_t_C_ha']
'''


target_c, baseline_soc, iters = solve_carbon_input(
	starting_soil_carbon=31.84,
	clay=18,
	temp = [27.7, 30.3, 31.8, 30.9, 29.3, 27.6, 26.6, 26, 26.4, 28, 28.8, 27.8],
	rain = [5, 10.9, 20.9, 86.4, 130.1, 141.8, 139.7, 241, 198.1, 82.9, 5.2, 0.3],
	evap = [193.33, 200, 230.67, 225.33, 220, 192, 176, 164, 162.67, 190.67, 192, 192],
	starting_fym = 0.0,
	pc=[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	total_years=0,
	start_year=2026,
	tol=1e-2,
	max_iter = 50,
	c_min=0.0,
	c_max=100.0,
        trm = 1.0
)

print("Solved carbon_input_baseline:", target_c)
print("Resulting baseline_soc:", baseline_soc)
print("Iterations:", iters)
