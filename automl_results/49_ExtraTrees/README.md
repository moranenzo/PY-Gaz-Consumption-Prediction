# Summary of 49_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: squared_error
- **max_features**: 0.7
- **min_samples_split**: 50
- **max_depth**: 4
- **eval_metric_name**: rmse
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.8
 - **shuffle**: False

## Optimized metric
rmse

## Training time

3.5 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 22542.2         |
| MSE      |     9.54538e+08 |
| RMSE     | 30895.6         |
| R2       |     0.981048    |
| MAPE     |     0.102921    |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
