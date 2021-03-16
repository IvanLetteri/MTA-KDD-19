## Daily Updated Optimized version of MTA-KDD dataset can be found [HERE](https://www.ivanletteri.it/optmtakdd/)
You can read publication about Optimized MTA-KDD version [here](https://arxiv.org/abs/2009.11347)
You can read publication about Balancing of Optimized MTA-KDD version with SMOTE, ADASYN, G1No and G1No Gourmet algorithms[here](https://arxiv.org/abs/2012.15231) 

## Additional material
The additional material for the paper can be found [here](https://www.ivanletteri.it/2021/03/16/a-novel-resampling-technique-for-imbalanced-dataset-optimization/).

## Merging Malware and Legitimate classes

```python
url = 'https://github.com/IvanLetteri/MTA-KDD-19/tree/master/G1NoGourmetDataset/RRwOptMTAKDD.csv'

Samples percentage Malware : 72.12283044058745 % - tot. num. of Malware samples:  35113
Samples percentage Legitimate : 27.87716955941255 % - tot. num. of Legitimate samples:  13572
```

# **Step 1.** 

weight for all samples Silhouette based

$w_i = \frac{(silh_{max} - silh_i)}{(silh_{max} - silh_{min})}$

Sum of instance weights

**wSUM** is  $\sum_i w_i$

$S_i$ is the silhouette of sample $i$

where [ProbWi] is $p_i = \frac{W_i}{\sum(W_i)}$

**Step 2.**

Mean of instance weights for each features

$$\mu_{f_i} = \frac{\sum s_i * w_i}{\sum w_i}$$

# **Variance**

Part 1.

$$\sigma^2 = ((s_i * w_i) - \mu_{f_i})^2$$

where $s_i$ is a row of dataset (sample)

```python
df['WiSilhouette']=(df['silhouette'].max() - df['silhouette'])/(df['silhouette'].max() - df['silhouette'].min())

wSUM = np.sum(df['WiSilhouette'])

Smax = df['silhouette'].max()
df["ProbWi"] = df["WiSilhouette"] / wSUM

# **Standard Deviation**

Part 2.

$\sigma_i = \sqrt{((s_i * w_i)- \mu_i)^2}$

#titles=['StartFlow','NumIPdst','NumCon','NumPorts','MinLenrx','FirstPktLen','TCPoverIP','MinLen','UDPoverIP','DNSoverIP','RstFlagDist']
#titles = list(df.columns).remove('label','WiSilhouette','ProbWi') 
for title in titles:
  df['MuWi'+title] = np.dot(df[title], df['WiSilhouette']).sum() / wSUM
#for title in titles:
  df['SigmaWi'+title] = np.sqrt(np.dot((df[title]-df['MuWi'+title])**2, df['WiSilhouette']).sum() /  wSUM)
  
```
