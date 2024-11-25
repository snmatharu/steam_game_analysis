from pyspark.ml.regression import LinearRegression, DecisionTreeRegressor, RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

def train_and_evaluate_models(df_preprocessed):
    print("Training and evaluating models...")
    train, test = df_preprocessed.randomSplit([0.8, 0.2], seed=42)
    
    models = {
        "Linear Regression": LinearRegression(featuresCol="scaled_features", labelCol="peak_ccu"),
        "Decision Tree": DecisionTreeRegressor(featuresCol="scaled_features", labelCol="peak_ccu"),
        "Random Forest": RandomForestRegressor(featuresCol="scaled_features", labelCol="peak_ccu", numTrees=100)
    }
    
    results = {}
    feature_importance = None
    
    evaluator = RegressionEvaluator(labelCol="peak_ccu", predictionCol="prediction", metricName="mae")
    rmse_evaluator = RegressionEvaluator(labelCol="peak_ccu", predictionCol="prediction", metricName="rmse")
    r2_evaluator = RegressionEvaluator(labelCol="peak_ccu", predictionCol="prediction", metricName="r2")
    
    for model_name, model in models.items():
        print(f"Training {model_name}...")
        fitted_model = model.fit(train)
        predictions = fitted_model.transform(test)
        
        mae = evaluator.evaluate(predictions)
        rmse = rmse_evaluator.evaluate(predictions)
        r2 = r2_evaluator.evaluate(predictions)
        
        results[model_name] = {"MAE": mae, "RMSE": rmse, "R2": r2}
        
        if model_name == "Random Forest":
            feature_importance = fitted_model.featureImportances
        
        print(f"{model_name} completed. MAE: {mae}, RMSE: {rmse}, R2: {r2}")
    
    print("Model training and evaluation completed.")
    return results, feature_importance
