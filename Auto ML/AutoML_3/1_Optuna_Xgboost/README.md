# Summary of 1_Optuna_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: reg:squarederror
- **eta**: 0.05
- **max_depth**: 12
- **min_child_weight**: 13
- **subsample**: 0.7519887123246279
- **colsample_bytree**: 0.3124407656964223
- **eval_metric**: rmse
- **lambda**: 1.320949656036725
- **alpha**: 6.607298489806165
- **max_rounds**: 1000
- **early_stopping_rounds**: 50
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 10
 - **shuffle**: True

## Optimized metric
rmse

## Training time

2018.4 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      | 1.43294   |
| MSE      | 3.36734   |
| RMSE     | 1.83503   |
| R2       | 0.649731  |
| MAPE     | 0.0162406 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)
### Dependence (Fold 2)
![SHAP Dependence from Fold 2](learner_fold_1_shap_dependence.png)
### Dependence (Fold 3)
![SHAP Dependence from Fold 3](learner_fold_2_shap_dependence.png)
### Dependence (Fold 4)
![SHAP Dependence from Fold 4](learner_fold_3_shap_dependence.png)
### Dependence (Fold 5)
![SHAP Dependence from Fold 5](learner_fold_4_shap_dependence.png)
### Dependence (Fold 6)
![SHAP Dependence from Fold 6](learner_fold_5_shap_dependence.png)
### Dependence (Fold 7)
![SHAP Dependence from Fold 7](learner_fold_6_shap_dependence.png)
### Dependence (Fold 8)
![SHAP Dependence from Fold 8](learner_fold_7_shap_dependence.png)
### Dependence (Fold 9)
![SHAP Dependence from Fold 9](learner_fold_8_shap_dependence.png)
### Dependence (Fold 10)
![SHAP Dependence from Fold 10](learner_fold_9_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 2)
![SHAP worst decisions from fold 2](learner_fold_1_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 3)
![SHAP worst decisions from fold 3](learner_fold_2_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 4)
![SHAP worst decisions from fold 4](learner_fold_3_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 5)
![SHAP worst decisions from fold 5](learner_fold_4_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 6)
![SHAP worst decisions from fold 6](learner_fold_5_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 7)
![SHAP worst decisions from fold 7](learner_fold_6_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 8)
![SHAP worst decisions from fold 8](learner_fold_7_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 9)
![SHAP worst decisions from fold 9](learner_fold_8_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 10)
![SHAP worst decisions from fold 10](learner_fold_9_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)
### Top-10 Best decisions (Fold 2)
![SHAP best decisions from fold 2](learner_fold_1_shap_best_decisions.png)
### Top-10 Best decisions (Fold 3)
![SHAP best decisions from fold 3](learner_fold_2_shap_best_decisions.png)
### Top-10 Best decisions (Fold 4)
![SHAP best decisions from fold 4](learner_fold_3_shap_best_decisions.png)
### Top-10 Best decisions (Fold 5)
![SHAP best decisions from fold 5](learner_fold_4_shap_best_decisions.png)
### Top-10 Best decisions (Fold 6)
![SHAP best decisions from fold 6](learner_fold_5_shap_best_decisions.png)
### Top-10 Best decisions (Fold 7)
![SHAP best decisions from fold 7](learner_fold_6_shap_best_decisions.png)
### Top-10 Best decisions (Fold 8)
![SHAP best decisions from fold 8](learner_fold_7_shap_best_decisions.png)
### Top-10 Best decisions (Fold 9)
![SHAP best decisions from fold 9](learner_fold_8_shap_best_decisions.png)
### Top-10 Best decisions (Fold 10)
![SHAP best decisions from fold 10](learner_fold_9_shap_best_decisions.png)

[<< Go back](../README.md)
