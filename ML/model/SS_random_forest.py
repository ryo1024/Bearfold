import tensorflow as tf

if __name__ == "__main__":
    params = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
  num_classes=3, num_features=10, regression=False,
  num_trees=50, max_nodes=1000)

    classifier = tf.contrib.tensor_forest.client.random_forest.TensorForestEstimator(params)
