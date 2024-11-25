from data_loader import (
    fetch_data_with_pymongo, 
    create_spark_session, 
    convert_to_spark_dataframe
)
from data_transformer import transform_data, prepare_data_for_modeling
from model_trainer import train_and_evaluate_models
from visualization import plot_results, plot_feature_importance

def main():
    print("Starting main process...")
    
    # Data loading
    data = fetch_data_with_pymongo()
    spark = create_spark_session()
    df = convert_to_spark_dataframe(spark, data)
    
    # Data transformation
    df_transformed = transform_data(df)
    df_preprocessed = prepare_data_for_modeling(df_transformed)
    
    # Model training and evaluation
    results, feature_importance = train_and_evaluate_models(df_preprocessed)
    
    # Visualization
    plot_results(results)
    if feature_importance is not None:
        feature_names = df_preprocessed.columns
        plot_feature_importance(feature_importance, feature_names)
    
    print("Main process completed.")

if __name__ == "__main__":
    main()