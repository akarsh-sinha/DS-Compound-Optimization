# DS Compound Optimization

## Project Overview

The DS Compound Optimization project aims to develop a predictive model for the desulphurization (DS) process in steelmaking. The objective is to predict the sulphur content at the DS unit exit (DS_S) based on various input variables. This prediction is critical to ensure that the sulphur content is reduced from high levels (0.02-0.1%) to desired levels (0.002-0.015%) before further processing in the LD converter.

## Process Description

In the steelmaking process, hot metal with high sulphur content is treated in a desulphurization (DS) unit. The DS unit receives hot metal from blast furnaces and applies treatment to reduce the sulphur content to a specified range. The effectiveness of this process is crucial for maintaining the quality of the steel product.

## Task

The main task is to develop a machine learning model to predict the sulphur content at the DS unit exit (DS_S) based on the following input variables:

## Data Description

| Variables        | Description                          |
|-----------------|--------------------------------------|
| **CASTNO**       | Unique identification of batch/heat  |
| **HM_WT**       | Size of batch - tons of hot metal     |
| **AIM_S**       | Aim Sulphur for that batch             |
| **HM_S**        | Input Hot Metal Sulphur                     |
| **HM_C**        | Input Hot Metal Carbon                      |
| **HM_SI**       | Input Hot Metal Silicon                     |
| **HM_TI**       | Input Hot Metal Titanium                    |
| **HM_MN**       | Input Hot Metal Manganese                   |
| **CAC2**        | CaC2 added quantity                       |
| **MG**          | Mg added quantity                   |
| **HM_TEMP**     | Hot Metal Temperature                 |
| **CAC2_INJ_TIME** | Calcium Carbide Injection Time      |
| **MG_INJ_TIME** | Magnesium Injection Time              |
| **DS_S**        | Output Sulphur achieved                |

## Award Criteria

The success of the model will be evaluated based on the **Model Hit Rate**, defined as the percentage of data points where the difference between predicted and actual DS_S values is within ±0.002%. This criterion ensures that the model provides accurate predictions suitable for industrial applications.
                                           

## Getting Started

### Dependencies

Ensure you have the following Python packages installed:
- `pandas`
- `numpy`
- `scikit-learn`

You can install the required packages using pip:
```bash
pip install pandas numpy scikit-learn 
