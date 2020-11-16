import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visual():

    def plot_images(self,image,label,cmap=None,save=False,destination="/"):
        """
        Args : 
        image: image array
        label: label of image
        cmap: None if color else gray for b/w.Default none
        save: Bool save or not(False)
        destination: Default root.Else pass a string
        """
        plt.imshow(image,cmap="gray")
        plt.title("Label:{}".format(label))
        if save:
            plt.savefig(destination)