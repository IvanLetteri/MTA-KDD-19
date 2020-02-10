# MTA-KDD'19
This repository contains additional material for the paper "MTA-KDD'19: A Dataset for Malware Traffic Detection".

## Additional material
The additional material for the paper can be found [here](ITASEC2020.pdf).
It contains the results on all the datasets for the different WordNet-based similarity metrics considered.

## Implementation

The implementation of MTAKDD'19 will be share on googleColab to the url [gColab mtakdd19](https://toDefineWorkInProgress).

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
Keywords: Sentiment analysis; Sentiment lexicon; Semantic similarity; Word embeddings

```
@article{LETTERI2020,
title = "MTA-KDD'19: A Dataset for Malware Traffic Detection",
journal = "---",
volume = "---",
pages = "__ - __",
year = "2020",
issn = "__-__",
doi = "---",
url = "---",
author = "I. Letteri, G.D. Penna, L.D. Vita, M.T. Grifa.",
keywords = "Malware analysis, Network Traffic, Machine Learning, Malware Detection",
}
```
