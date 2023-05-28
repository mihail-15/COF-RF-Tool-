# import the necessary packages
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
from matplotlib import patheffects

# load the data from the 'xlsx' file and include your path
data = pd.read_excel("C:/Users//pin-on-disk/data_AlSi10Mg-SiC.xlsx")
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# split the data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)

# define a function to perform hyperparameter tuning using GridSearchCV
def rf_gridsearch(X_train, y_train, X_val, y_val):
    rf = RandomForestRegressor(random_state=42)
    param_grid = {
        'max_features': [2, 3],
        'min_samples_leaf': [3, 4, 5],
        'n_estimators': [10, 20, 50, 100]
    }
    gs = GridSearchCV(rf, param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
    gs.fit(X_train, y_train)
    rf_best = gs.best_estimator_
    y_val_pred = rf_best.predict(X_val)
    r2 = r2_score(y_val, y_val_pred)
    rmse = np.sqrt(mean_squared_error(y_val, y_val_pred))
    mse = mean_squared_error(y_val, y_val_pred)
    mae = mean_absolute_error(y_val, y_val_pred)
    print("Best parameters: ", gs.best_params_)
    print("R2 score: {:.4f}".format(r2))
    print("RMSE: {:.4f}".format(rmse))
    print("MSE: {:.4f}".format(mse))
    print("MAE: {:.4f}".format(mae))
    return rf_best

# perform hyperparameter tuning on the training and validation sets
rf_best = rf_gridsearch(X_train, y_train, X_val, y_val)

# train the random forest model on the entire training set using the best hyperparameters
rf = RandomForestRegressor(max_features=rf_best.max_features, min_samples_leaf=rf_best.min_samples_leaf, n_estimators=rf_best.n_estimators, random_state=42)
rf.fit(X_train, y_train)

# predict the coefficient of friction for the test set
y_pred = rf.predict(X_test)

# predict the coefficient of friction for the validation set
y_val_pred = rf.predict(X_val)

# calculate the R2, RMSE, MSE, and MAE
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# calculate and store the performance metrics for the test set
r2_test = r2_score(y_test,y_pred)
rmse_test = np.sqrt(mean_squared_error(y_test,y_pred))
mse_test = mean_squared_error(y_test,y_pred)
mae_test = mean_absolute_error(y_test,y_pred)

# calculate and store the performance metrics for the validation set
r2_val = r2_score(y_val, y_val_pred)
rmse_val = np.sqrt(mean_squared_error(y_val, y_val_pred))
mse_val = mean_squared_error(y_val, y_val_pred)
mae_val = mean_absolute_error(y_val, y_val_pred)


# Shadow effect objects with different transparency, blur, angle and distance and smaller linewidth
pe1 = [patheffects.SimpleLineShadow(offset=(0.5, -0.5), alpha=0.4, linewidth=1), patheffects.Normal()]

# Plot of the actual vs predicted coefficient of friction as a function of sliding distance
plt.scatter(X_test[:, 0], y_test,color='cyan',label='Actual test', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.scatter(X_test[:, 0], y_pred,color='orange',label='Predicted test', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.scatter(X_val[:, 0], y_val,color='green',label='Actual val', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.scatter(X_val[:, 0], y_val_pred,color='magenta',label='Predicted val', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.xlabel('Sliding distance, m', fontsize='15', fontweight='bold')
plt.ylabel('Coefficient of friction, -', fontsize='15', fontweight='bold')
plt.legend()

# x axis limit to 60
plt.xlim(0, 450)

# y axis limit to 40
plt.ylim(0, 0.6)

# gridlines to the plot
plt.grid(True)

plt.show()

fig = plt.figure() 
plt.plot(X,y)
plt.xlim(0, 450)
plt.ylim(0, 0.6)
plt.grid(True)

# Plot of the actual vs predicted coefficient of friction as a function of sliding distance
plt.scatter(X_test[:, 0], y_test,color='cyan',label='Actual test', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.scatter(X_test[:, 0], y_pred,color='orange',label='Predicted test', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.scatter(X_val[:, 0], y_val,color='green',label='Actual val', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.scatter(X_val[:, 0], y_val_pred,color='magenta',label='Predicted val', linewidth=1, alpha=0.9, zorder=1, marker=None, path_effects=pe1)
plt.xlabel('Sliding distance, m', fontsize='15', fontweight='bold')
plt.ylabel('Coefficient of friction, -', fontsize='15', fontweight='bold')
plt.legend()


# Save the plot with dpi=500 in 'png'
fig.savefig('cof_plot.png', dpi=500)


# write the performance metrics for both sets in a file
with open('performance_metrics.txt','w') as f:
    f.write('Test set performance metrics:\n')
    f.write('R2 score: {:.4f}\n'.format(r2_test))
    f.write('RMSE: {:.4f}\n'.format(rmse_test))
    f.write('MSE: {:.4f}\n'.format(mse_test))
    f.write('MAE: {:.4f}\n'.format(mae_test))
    f.write('Validation set performance metrics:\n')
    f.write('R2 score: {:.4f}\n'.format(r2_val))
    f.write('RMSE: {:.4f}\n'.format(rmse_val))
    f.write('MSE: {:.4f}\n'.format(mse_val))
    f.write('MAE: {:.4f}\n'.format(mae_val))
    f.close()

