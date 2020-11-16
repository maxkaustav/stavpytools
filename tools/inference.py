import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf


def MonteCarlo(no_ofmc,dataset,model,batch_size=0):
  stack=[]
  total_loops=0
  print("Initializing....")
  for i,(x,y) in enumerate(dataset):
    total_loops=total_loops+1
    percent_complete=total_loops/40
  for i in range(no_ofmc):
    dot="......................................."
    count=0
    stackin=[]
    print("Monte Carlo {}/{}".format(i+1,no_ofmc))
    for i,(x,y) in enumerate(dataset):
      if batch_size>0:
        y_=model.predict(tf.expand_dims(x,axis=0))
      else :
        y_=model.predict(x,axis=0)
      stackin.append(y_)
      if i>(percent_complete*(count+1)):
        count=count+1
      x=dot.replace(".","=",count)
      print("\r[{}] {:.2f} % complete".format(x,((i+1)/total_loops)*100),end="")
    stack.append(stackin)
    print()
  return stack