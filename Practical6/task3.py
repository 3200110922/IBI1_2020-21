gene_lengths = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]

import numpy as np
import matplotlib.pyplot as plt

a = np.array(gene_lengths)
b = np.array(exon_counts)
c = a/b
#make lists a and b into ndarry so it's easy to process data
c.sort()
# sort new ndarry c.
plt.boxplot(c,
    vert=True,
    whis=1.5,
    patch_artist=True,
    meanline=False,
    showbox=True,
    showcaps=True,
    showfliers=True,
    notch=False
    )
#set up a new boxplot
print(c)
plt.show()
