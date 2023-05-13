COF-RF-Tool

COF-RF-Tool is a software that predicts the coefficient of friction (COF) of open-cell AlSi10Mg-SiC composites under dry sliding conditions using a Random Forest (RF) model. The software addresses the research challenge of designing and optimizing materials that have low friction and high wear resistance, which are important for various engineering applications. The software has an impact on the field of tribology, as it can provide reliable predictions of the COF based on experimental data, using a machine learning technique that has high accuracy and generalization ability.

Installation

The software requires python 3.7 or higher to run. The software also depends on several packages for data analysis, machine learning, and visualization, such as pandas, numpy, sklearn, matplotlib, and patheffects. These packages can be installed using pip or conda commands.

To install the software, users can download or clone the source code from GitHub:

git clone https://github.com/COF-RF-Tool/COF-RF-Tool.git

Usage

To use the software, users can follow these steps:

1. Open a terminal or any IDE (such as Visual Studio Code) and navigate to or open the folder where the source code is located.

2. Open the cof_rf_tool.py file and edit the file path of the data file if needed.

3. Run the code by using the appropriate command or button for your terminal or IDE.

4. Wait for the code to finish and check the output folder for the results.

The software will output the following:

* A plot of the actual vs predicted COF as a function of sliding distance for both the test set and the validation set.

* A text file with the performance metrics for both sets, such as R2, RMSE, MSE, and MAE.

Support

If you have any questions or issues with the software, please open an issue on GitHub or contact me at mihail1kolev@gmail.com.

License

The software is licensed under the MIT License. See LICENSE for more details.
