# Summary of 54_CatBoost_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 8
- **rsm**: 0.7
- **loss_function**: RMSE
- **eval_metric**: RMSE
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.8
 - **shuffle**: False

## Optimized metric
rmse

## Training time

106.8 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 12087.7         |
| MSE      |     3.00197e+08 |
| RMSE     | 17326.2         |
| R2       |     0.99404     |
| MAPE     |     0.0439434   |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
