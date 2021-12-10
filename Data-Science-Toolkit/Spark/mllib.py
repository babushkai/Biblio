from pyspark.ml.regression import LinearRegression
regressor = LinearRegression(featuresCol="features", labelCol="price")

#model = regressor.fit