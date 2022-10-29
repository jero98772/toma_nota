import tensorflow as tf
import pandas as pd
import matplotlib as plt
#imports
#variables
#function
def buildModel(lr):
	model=tf.keras.models.Sequential()
	model.add(tf.keras.layers.Dense(units=1,input_shape=(1,1)))
	model.compile(tf.optimizers.RMSprop(lr=lr,loss="mean_squared_error",metrics=[tf.keras.metrics.RootMeanSquaredError()]))
	return model
def trainModel(model, df, feature, label, epochs, batch_size):
	history = model.fit(x=df[feature],y=df[label],batch_size=batch_size,epochs=epochs)
	trained_weight = model.get_weights()[0]
	trained_bias = model.get_weights()[1]
def predict(n,feature,labels):
	df[feature][1000:10000+n]
def predict_house_values(n, feature, label):
  batch = training_df[feature][10000:10000 + n]
  predicted_values = my_model.predict_on_batch(x=batch)

  print("feature   label          predicted")
  print("  value   value          value")
  print("--------------------------------------")
  for i in range(n):
    print ("%5.0f %6.0f %15.0f" % (training_df[feature][10000 + i],
                                   training_df[label][10000 + i],
                                   predicted_values[i][0] ))	

#def main():
df=pd.read_csv("aqa.csv")
df.describe()
#main()