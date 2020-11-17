import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf


def MonteCarlo(no_ofmc,model,dataset,batch_size=0):
  """
  no_of_mc: Number of Monte Carlo
  model: tf model
  dataset: tf.data.Dataset
  batch_size: batch size of the data,if not batch keep zero
  """
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
      if batch_size==0:
        y_=model.predict(tf.expand_dims(x,axis=0))
        y_=tf.squeeze(y_,axis=0)
      else :
        y_=model.predict(x)
      stackin.append(y_)
      if i>(percent_complete*(count+1)):
        count=count+1
      x=dot.replace(".","=",count)
      print("\r[{}] {:.2f} % complete".format(x,((i+1)/total_loops)*100),end="")
    stack.append(stackin)
    print()
  return np.array(stack)

def MonteCarloDataReturn(no_ofmc,model,dataset,batch_size=0):
  """
  no_of_mc: Number of Monte Carlo
  model: tf model
  dataset: tf.data.Dataset
  batch_size: batch size of the data,if not batch keep zero
  """
  stackp=[]
  stackd=[]
  stackl=[]
  total_loops=0
  print("Initializing....")
  for i,(x,y) in enumerate(dataset):
    total_loops=total_loops+1
    percent_complete=total_loops/40
  for j in range(no_ofmc):
    dot="......................................."
    count=0
    stackinp=[]
    stackind=[]
    stackinl=[]
    print("Monte Carlo {}/{}".format(j+1,no_ofmc))
    for i,(x,y) in enumerate(dataset):
      if batch_size==0:
        y_=model.predict(tf.expand_dims(x,axis=0))
        y_=tf.squeeze(y_,axis=0)
      else :
        y_=model.predict(x)
      stackinp.append(y_)
      stackind.append(x)
      stackinl.append(y)
      if i>(percent_complete*(count+1)):
        count=count+1
      x=dot.replace(".","=",count)
      print("\r[{}] {:.2f} % complete".format(x,((i+1)/total_loops)*100),end="")
    stackp.append(np.array(stackinp))
    if j<1:
      stackd.append(np.array(stackind))
      stackl.append(np.array(stackinl))
    print()
  return {"predict":np.array(stackp),"data":np.array(stackd),"label":np.array(stackl)}