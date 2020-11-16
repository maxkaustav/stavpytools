import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

def plot_images(image,label,cmap=None,save=False,destination="/",name="fig"):
        """
        Args : 
        image: image array
        label: label of image
        cmap: None if color else gray for b/w.Default none
        save: Bool save or not(False)
        destination: Default root.Else pass a string.
        """
        plt.imshow(image,cmap="gray")
        plt.title("Label:{}".format(label))
        if save:
            plt.savefig(destination)

def plot_inference_graph(data,labelx="",labely="",title_name="",c="blue",save=False, destin="fig"):
    """
    Args:
    data: data to be send in the form of array
    labelx: X axis label
    labely: Y axis label
    title_name: tile of graph
    c: color of the plot.Default blue 
    save: Boolean
    destin: destination and name ex: destination/destination/name
    """
    plt.plot(data, c=c)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title_name)
    if save:
      plt.savefig(destin)

def montecarloplot(sample,n_class,no_sample=3,save=False,destin="fig"):
  """
  Args:
  sample: data in format array([number of monte carlo,no of prediction,no of classes])
  n_class:  no of classes
  no_samples: number of samples to be plotted
  """
  q=np.ceil(no_sample/5)
  plt.figure(figsize=(20,5*q))
  r=np.ceil(no_sample/4)
  for i in range(no_sample):
    plt.subplot(r,4,i+1)
    for j in range(n_class):
      sns.kdeplot(sample[:,i,j],label=j)
    plt.legend()
    plt.xlabel("probability")
    plt.ylabel("monte carlo density")
  if save:
    plt.savefig(destin)



