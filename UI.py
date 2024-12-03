import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

def normalize_column_names(depth_data):
    depth_data.rename(columns={
        'Top Drive RPM(RPM)': 'Top Drive RPM (RPM)',
        'Top Drive Torque(ft·lbf)': 'Top Drive Torque (ft·lbf)',
        'Flow In Rate(galUS/min)': 'Flow In Rate (galUS/min)',
        'Pump Pressure(psi)': 'Pump Pressure (psi)',
        'Diff Press(psi)': 'Diff Press (psi)',
        'ROP - Average(ft/hr)': 'ROP - Average (ft/hr)',
        'Bit Weight(klb)': 'Bit Weight (klb)',
        'Block Height(ft)': 'Block Height (ft)',
        'Hook Load(klb)': 'Hook Load (klb)'
    }, inplace=True)
    return depth_data

def detect_sliding(depth_data):
    depth_data = normalize_column_names(depth_data)
    num_elements = len(depth_data)
    depth_data['Sliding'] = 0

    for i in range(num_elements):
        if i + 10 < num_elements and i > 10:
            rpm_window = depth_data['Top Drive RPM (RPM)'][i:i+10].values
            torque_window = depth_data['Top Drive Torque (ft·lbf)'][i:i+10].values
            torque_mean = np.mean(torque_window)
            upper_torque_quartile = np.percentile(torque_window, 75)
            ratio = (2 * torque_mean - upper_torque_quartile) / torque_mean
            if ratio < 0.7 or np.sum(rpm_window < 9) > 2 or np.sum(np.array([ratio]) < 0.7) > 2:
                depth_data.at[i, 'Sliding'] = 1
    return depth_data

def load_data():
    if not os.path.exists("resources/DrillingData.csv"):
        export_data = pd.ExcelFile("resources/DrillingData.xlsx").parse("Export Data")
        export_data.rename(columns={
            'Flow In Rate(galUS/min)': 'Flow In Rate (galUS/min)',
            'Pump Pressure(psi)': 'Pump Pressure (psi)',
            'Diff Press(psi)': 'Diff Press (psi)',
            'Top Drive RPM(RPM)': 'Top Drive RPM (RPM)',
            'ROP - Average(ft/hr)': 'ROP - Average (ft/hr)',
            'Bit Weight(klb)': 'Bit Weight (klb)',
            'Top Drive Torque(ft·lbf)': 'Top Drive Torque (ft·lbf)',
            'Block Height(ft)': 'Block Height (ft)',
            'Hook Load(klb)': 'Hook Load (klb)'
        }, inplace=True)
        export_data.to_csv("resources/DrillingData.csv", index=False)

    return pd.read_csv("resources/DrillingData.csv")

def create_plots(data):
    data = detect_sliding(data)
    columns = [
        ("Flow In Rate (galUS/min)", "Flow In Rate"),
        ("Pump Pressure (psi)", "Pump Pressure"),
        ("Diff Press (psi)", "Differential Pressure"),
        ("Top Drive RPM (RPM)", "Top Drive RPM"),
        ("ROP - Average (ft/hr)", "ROP - Average"),
        ("Bit Weight (klb)", "Bit Weight"),
        ("Top Drive Torque (ft·lbf)", "Top Drive Torque"),
        ("Block Height (ft)", "Block Height"),
        ("Hook Load (klb)", "Hook Load"),
        ("Sliding", "Sliding Detection")
    ]
    figures = []
    for column, title in columns:
        fig, ax = plt.subplots(figsize=(10, 5))
        data.plot(x="Depth", y=column, ax=ax, color="red" if column == "Sliding" else "blue", legend=False)
        ax.set_title(title)
        ax.set_xlabel("Depth (ft)")
        ax.set_ylabel(column if column != "Sliding" else "Sliding (1=True, 0=False)")
        ax.grid(visible=True, linestyle='--', alpha=0.7)
        figures.append(fig)
    return figures

def display_plot(figures, index):
    for widget in content_frame.winfo_children():
        widget.destroy()
    tk.Label(content_frame, text=f"Data Plot #{index + 1}", font=("Helvetica", 16, "bold")).pack(pady=10)
    canvas = FigureCanvasTkAgg(figures[index], master=content_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    canvas.draw()

def navigate(direction):
    global current_index
    if direction == "prev" and current_index > 0:
        current_index -= 1
    elif direction == "next" and current_index < len(figures) - 1:
        current_index += 1
    display_plot(figures, current_index)

window = tk.Tk()
window.title("Drilling Data Visualization")

nav_frame = ttk.Frame(window)
nav_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

ttk.Button(nav_frame, text="Previous", command=lambda: navigate("prev")).pack(side=tk.LEFT, padx=5)
ttk.Button(nav_frame, text="Next", command=lambda: navigate("next")).pack(side=tk.RIGHT, padx=5)

content_frame = ttk.Frame(window)
content_frame.pack(fill=tk.BOTH, expand=True)

data = load_data()
figures = create_plots(data)
current_index = 0
display_plot(figures, current_index)

window.mainloop()
