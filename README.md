# CS4273-GroupProject

We will be utilizing 10,000’ of drilling data to implement an algorithm that will detect whether the mode of drilling is sliding or rotating. In order to do this we will be ingesting data from excel that will be categorized into the different drilling parameters utilizing python data frames. We will then pass the data through our algorithm to determine the drilling mode being performed and then display that data on a custom UI. This will be a more basic version of the algorithm that is being designed by the company as it is not utilizing machine learning, but it will still demonstrate the end goal of detection and display of the rig state.

## Requirements

The project requires Python 3.8 or higher. The following Python libraries are used:
- `pandas`
- `numpy`
- `matplotlib`
- `openpyxl` (for working with Excel files)

## Setup Instructions

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/wellatleastitried/CS4273-GroupProject
   cd CS4273-GroupProject
   ```

2. Install the dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: It's recommended to use a Python virtual environment to avoid conflicts:
   > ```bash
   > python -m venv venv
   > source venv/bin/activate  # On Windows: venv\Scripts\activate
   > pip install -r requirements.txt
   > ```
