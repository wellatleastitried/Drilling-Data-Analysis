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
