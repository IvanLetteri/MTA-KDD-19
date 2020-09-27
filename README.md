## Daily Updated Optimized version of MTA-KDD dataset can be found [HERE](https://www.ivanletteri.it/optmtakdd/)
You can read publication about Optimized MTA-KDD version [here](https://arxiv.org/abs/2009.11347) 

# MTA-KDD'19
This repository contains additional material for the paper "MTA-KDD'19: A Dataset for Malware Traffic Detection".

## Additional material
The additional material for the paper can be found [here](ITASEC2020.pdf).
More details about MTA-KDD'19 can be found [here](https://www.ivanletteri.it/2020/01/31/itasec2020/).

## Merging Malware and Legitimate classes

```python
url = 'http://https://github.com/IvanLetteri/MTA-KDD-19/blob/master/'

dfMTA = pd.read_csv(url+'datasetLegitimate33featues.csv')
dfLEG = pd.read_csv(url+'datasetMalware33featues.csv')
dfComplete = pd.concat([dfMTA, dfLEG])
dfComplete.describe()
```

To enhance performance, it is recommendable to use a more complete scikit-learn pipe that implements normalization and feature selection.

```python
import pandas as pd
import pandas_profiling as pp
import IPython
import scipy.io
import numpy as np
#from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
from sklearn import svm
from sklearn.feature_selection import f_regression, mutual_info_regression

# visual libraries
from matplotlib import pyplot as plt
from matplotlib import gridspec

import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D 
plt.style.use('ggplot')

from keras.models import model_from_json
from keras import backend as K
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from keras.optimizers import Adam, SGD
from keras.utils.vis_utils import plot_model
from sklearn import metrics
from sklearn.metrics import roc_curve, auc, confusion_matrix
from sklearn.model_selection import train_test_split
```

## Cite

If you use this work, please cite the following paper:
I. Letteri, G.D. Penna, L.D. Vita, M.T. Grifa.
"MTA-KDD'19: A Dataset for Malware Traffic Detection.",
2020,
Keywords: Malware analysis, Network Traffic, Machine Learning, Malware Detection
```
@inproceedings{itasec2020,
  author    = {Ivan Letteri and Giuseppe {Della Penna} and Luca Di Vita and Maria Teresa Grifa},
  editor    = {Michele Loreti and Luca Spalazzi},
  title     = {MTA-KDD'19: {A} Dataset for Malware Traffic Detection},
  booktitle = {Proceedings of the Fourth Italian Conference on Cyber Security, Ancona, Italy, February 4th to 7th, 2020},
  series    = {{CEUR} Workshop Proceedings},
  volume    = {2597},
  pages     = {153--165},
  publisher = {CEUR-WS.org},
  year      = {2020},
  url       = {http://ceur-ws.org/Vol-2597/paper-14.pdf},
  timestamp = {Mon, 27 Apr 2020 16:53:46 +0200},
  biburl    = {https://dblp.org/rec/conf/itasec/LetteriPVG20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
