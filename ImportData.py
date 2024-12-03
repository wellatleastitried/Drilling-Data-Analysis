#!/usr/bin/env python3

# Author: Jack Swindell

import pandas as pd

def main():
    file_path = "resources/DrillingData.xlsx"

    dataframe = parse_excel_to_dataframe(file_path)

    print(dataframe.head())

    dataframe.to_csv("resources/DrillingData.csv", index=False)

def parse_excel_to_dataframe(file_path):
    """
    Parse the Export Data table from an Excel file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the Excel file.
    
    Returns:
        pd.DataFrame: DataFrame with renamed columns for compatibility.
    """
    export_data = pd.ExcelFile(file_path).parse("Export Data")

    export_data_renamed = export_data.rename(columns={
    	'Flow In Rate(galUS/min)': 'Flow In Rate (galUS/min)',
        'Pump Pressure(psi)': 'Pump Pressure (psi)',
        'Diff Press(psi)': 'Diff Press (psi)',
        'Top Drive RPM(RPM)': 'Top Drive RPM (RPM)',
        'ROP - Average(ft/hr)': 'ROP - Average (ft/hr)',
        'Bit Weight(klb)': 'Bit Weight (klb)',
        'Top Drive Torque(ft·lbf)': 'Top Drive Torque (ft·lbf)',
        'Block Height(ft)': 'Block Height (ft)',
        'Hook Load(klb)': 'Hook Load (klb)'
    })

    return export_data_renamed

if __name__ == "__main__":
    main()
