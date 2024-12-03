import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    file_path = "DrillingData.xlsx"

    dataframe = parse_excel_to_dataframe(file_path)

    #print(dataframe.head())

    dataframe = detect_sliding(dataframe)

    #print(dataframe.head())

    fig, axs = plt.subplots(ncols = 1, nrows = 10, figsize = (10, 20), layout = "constrained")

    dataframe.plot(x="Depth", y="Flow In Rate (galUS/min)", ax = axs[0])
    dataframe.plot(x="Depth", y="Pump Pressure (psi)", ax = axs[1])
    dataframe.plot(x="Depth", y="Diff Press (psi)", ax = axs[2])
    dataframe.plot(x="Depth", y="Top Drive RPM (RPM)", ax = axs[3])
    dataframe.plot(x="Depth", y="ROP - Average (ft/hr)", ax = axs[4])
    dataframe.plot(x="Depth", y="Bit Weight (klb)", ax = axs[5])
    dataframe.plot(x="Depth", y="Top Drive Torque (ft·lbf)", ax = axs[6])
    dataframe.plot(x="Depth", y="Block Height (ft)", ax = axs[7])
    dataframe.plot(x="Depth", y="Hook Load (klb)", ax = axs[8])
    dataframe.plot(x="Depth", y="Sliding", ax = axs[9])

    plt.show()

    #dataframe.to_csv("resources/DrillingData.csv", index=False)

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

def detect_sliding(depth_data):
    """
    Detect sliding and add a 'Sliding' column to the DataFrame.
    
    Args:
        depth_data (pd.DataFrame): DataFrame containing drilling data.
    
    Returns:
        pd.DataFrame: Updated DataFrame with 'Sliding' column.
    """
    num_elements = len(depth_data)
    ratio_array = []
    sliding_now = 0

    # Initialize the Sliding column with default value 0
    depth_data['Sliding'] = 0

    for i in range(num_elements):
        if i + 10 < num_elements and i > 10:
            rpm_window = depth_data['Top Drive RPM (RPM)'][i:i+10].values
            torque_window = depth_data['Top Drive Torque (ft·lbf)'][i:i+10].values
            sub_ten = rpm_window < 9
            count_sub = np.sum(sub_ten)
            torque_mean = np.mean(torque_window)
            upper_torque_quartile = np.percentile(torque_window, 75)
            rpm_ratio = (np.max(rpm_window) - np.min(rpm_window)) / np.max(rpm_window) > 0.1
            ratio = (2 * torque_mean - upper_torque_quartile) / torque_mean
            ratio_array.append(ratio)
            sub_ratio = np.array(ratio_array[i-10:i]) < 0.7
            count_ratio = np.sum(sub_ratio)
            if ratio < 0.7 or count_sub > 2 or count_ratio > 2:
                sliding_now = 1
            else:
                sliding_now = 0
        else:
            ratio_array.append(1)
            sliding_now = 0

        # Update the Sliding column
        depth_data.at[i, 'Sliding'] = sliding_now

    return depth_data

if __name__ == "__main__":
    main()
