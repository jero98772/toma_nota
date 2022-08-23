import tensorflow as tf
import numpy as np

datos_c=[-40,-10,0,8,15,22,38]
datos_fer=[-40,14,32,46,59,72,100]

capaOculta1=tf.layers.Dense(units=3,input_shape=[-1])
capaOculta2=tf.layers.Dense(units=3)
salida=tf.layers.Dense(units=1)