
# Customer Segmentation  <img width="100" src="customerSegmentation.png" alt="A cool business" />

## Obiective
Dezvoltarea unui sistem de asistenta pentru segmentarea clientilor.


## Ideea de baza

V. Pareto: "80% of the land in Italy was owned by just 20% of the people" --> "20% of customers are responsible for 80% of profits"
Segmentarea clientilor reprezinta gruparea acestora astfel incat clientii din acelasi grup sunt foarte asemanatori dintr-un anumit punct de vedere (preferinte de plata, volum tranzactii, raspund similar la campaniile publicitare, etc.). 


## TO DO List
1. Identificarea caracteristicilor clientilor 
2. Pre-procesarea datelor (valori lipsa, valori extreme, valori nenumerice, normalizare - numerica si alfanumerica)
3. Clusterizarea datelor pentru identificarea segmentelor
- pre-fixarea sau calcularea nr de segmente
- folosirea unui algoritm de invatare nesupervizata, considerand toate datele si caracteristicile lor sau date micsorate
- evaluarea si validarea segmentelor identificate
4. Imbunatatire componenta inteligenta
- Din perspectiva calitatii procesului de invatare automata
- Din perspectiva complexitatii temporale si spatiale aferenta algoritmului de clusterizare
- Din perspectiva clientului (utilizarii aplicatiei)

## Date si referinte
1. Tiny dataset: Mall customers [link](https://github.com/SteffiPeTaffy/machineLearningAZ/blob/master/Machine%20Learning%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2025%20-%20Hierarchical%20Clustering/Mall_Customers.csv)
2. UCI dataset [link1](http://archive.ics.uci.edu/ml/datasets/online+retail), [link2](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
3. TBA soon ...

**Evaluare**


1. Vinh, N. X., Epps, J., & Bailey, J. (2010). Information theoretic measures for clusterings comparison: Variants, properties, normalization and correction for chance. The Journal of Machine Learning Research, 11, 2837-2854. [link](https://jmlr.csail.mit.edu/papers/volume11/vinh10a/vinh10a.pdf)
2. Halkidi, M., Batistakis, Y., & Vazirgiannis, M. (2001). On clustering validation techniques. Journal of intelligent information systems, 17(2-3), 107-145. [link](https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/content/pdf/10.1023/A:1012801612483.pdf&casa_token=uUoSeuN3yrcAAAAA:QeB32ZIHE0D5bjnF4RULslUQTmA8msl1Maz1WZ-0YHpX8GMNEsNW9NX42GuZgOp8BWd3epzs0uOGvPU4AQ)


**Metode de lucru**

1. Maulina, N. R., Surjandari, I., & Rus, A. M. M. (2019, July). Data Mining Approach for Customer Segmentation in B2B Settings using Centroid-Based Clustering. In 2019 16th International Conference on Service Systems and Service Management (ICSSSM) (pp. 1-6). IEEE. [link](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8887739&casa_token=CCryMfY8RU8AAAAA:pBcHWuNZjUTpiWAGDjd4h_-d4jRIlX7U6Xyx4iMKmfxLugvaB9Xno5Dmmvpe420JXI6pKiCvl2H8Tg&tag=1)

2. Halkidi, M., Batistakis, Y., & Vazirgiannis, M. (2001). On clustering validation techniques. Journal of intelligent information systems, 17(2-3), 107-145. [link](https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/content/pdf/10.1023/A:1012801612483.pdf&casa_token=uUoSeuN3yrcAAAAA:QeB32ZIHE0D5bjnF4RULslUQTmA8msl1Maz1WZ-0YHpX8GMNEsNW9NX42GuZgOp8BWd3epzs0uOGvPU4AQ)

3. Arthur, D., & Vassilvitskii, S. (2006). k-means++: The advantages of careful seeding. Stanford. [link](http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf)

4. Comaniciu, D., & Meer, P. (2002). Mean shift: A robust approach toward feature space analysis. IEEE Transactions on pattern analysis and machine intelligence, 24(5), 603-619.[link](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.76.8968&rep=rep1&type=pdf)

5. Von Luxburg, U. (2007). A tutorial on spectral clustering. Statistics and computing, 17(4), 395-416. [link](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=3E862EC16F46FE51C1869E5765FACE72?doi=10.1.1.165.9323&rep=rep1&type=pdf)

