
# Frailty-Data-Analysis-and-Visualization

This repository holds codes and documents pertaining to my UGP Project of analysing frailty data and building a visualization tool to better understand frailty, healthy aging and its factors of influence. The primary variables of interest are "Grip Test," "Timed Walk," and "Balance Test."



## Folder Structure

The repository is structured as follows:

- **Preliminary Analysis**: This folder contains initial assessments on the dataset, specifically targeting the variables related to frailty: Grip Test, Timed Walk, and Balance Test.
  - **Histograms**: Visual representations showing the frequency distribution of the three variables.
  - **Interdependence**: Exploration of potential dependency patterns within the variables.
  - **Plots Against Earnings**: Basic trend analysis by comparing variables against earnings.

Additionally, a report on the LASI survey is provided, giving an overview of the dataset formats and sizes.


## Format of the dataset

The LASI dataset can be accessed through the [Gateway to Global Aging website](https://g2aging.org/?section=lasi-downloads). Read a brief overview about the LASI survey [here](https://g2aging.org/survey-overview).

The downloadable data is available in the Stata, SAS, SPSS and R formats. You are expected to convert the data to a pickled dataset called 'dataframe' and store it in the same folder as the python codes to run it.
## Run Locally

Clone the project

```bash
  git clone https://github.com/rashmigr01/Frailty-Data-Analysis-and-Visualization.git
```

Go to the project directory

```bash
  cd Frailty-Data-Analysis-and-Visualization
```

Using a virtual environment is recommended, to manage project dependencies and ensure a clean environment for your analysis. If you don't have `virtualenv` installed, you can install it using:

Install dependencies

```bash
  pip install virtualenv
```
Create a new virtual environment 'venv'

```bash
    virtualenv venv
```

Activate the virtual environment

On Windows

```bash
    venv\Scripts\activate
```

On macOS/Linux

```bash
    source venv/bin/activate
```

Install dependencies

```bash
    pip install -r requirements.txt
```

Navigate to a folder and run the python code

On Windows

```bash
  python filename.py
```

On macOS/Linux

```bash
    python3 filename.py
```

Deactivate the virtual environment after use

```bash
    deactivate
```


## Future of the project

This project is currently ongoing and only contains preliminary analysis information. With a research-oriented approach, further analysis will not be made public until documentable progress is made.

The project's goal is to build a visuaization tool which will be uploaded to this repository as the project progresses.