import numpy as np
import pandas as pd

# Assuming depthData is a pandas DataFrame with columns 'BDEPTH_d', 'RPM_d', and 'TORQUE_d'
depthData = pd.DataFrame({
    'BDEPTH_d': np.random.rand(100),  # Example data
    'RPM_d': np.random.rand(100) * 20,
    'TORQUE_d': np.random.rand(100) * 100
})

num_elements = len(depthData['BDEPTH_d'])
Ratioarray = []
Slidingnow = 0

# Initialize Rig_States as a dictionary with lists
Rig_States = {'slide_ind': [False] * num_elements, 'rotate_ind': [False] * num_elements}

for i in range(num_elements):
    if i + 10 < num_elements and i > 10:
        rpmwindow = depthData['RPM_d'][i:i+10].values
        torquewindow = depthData['TORQUE_d'][i:i+10].values
        SubTen = rpmwindow < 9
        CountSub = np.sum(SubTen)
        torquemean = np.mean(torquewindow)
        uppertorquequartile = np.percentile(torquewindow, 75)
        RPMRatio = (np.max(rpmwindow) - np.min(rpmwindow)) / np.max(rpmwindow) > 0.1
        Ratio = (2 * torquemean - uppertorquequartile) / torquemean
        Ratioarray.append(Ratio)
        SubRatio = np.array(Ratioarray[i-10:i]) < 0.7
        CountRatio = np.sum(SubRatio)
        if Ratio < 0.7 or CountSub > 2 or CountRatio > 2:
            Slidingnow = 1
        else:
            Slidingnow = 0
    else:
        Ratioarray.append(1)
        Slidingnow = 0

    if Slidingnow == 0:
        Rig_States['slide_ind'][i] = False
        Rig_States['rotate_ind'][i] = True
    else:
        Rig_States['slide_ind'][i] = True
        Rig_States['rotate_ind'][i] = False

# Convert Rig_States to DataFrame if needed
Rig_States_df = pd.DataFrame(Rig_States)