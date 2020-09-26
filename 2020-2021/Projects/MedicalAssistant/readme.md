
# Asistent Automat pentru un student la medicina  <img src="heartSmall.png" alt="A cool heart"/>

## Obiective
Dezvoltarea unei aplicatii didactice care sa ajute studentii la medicina sa invete.


## Ideea de baza
In procesul de invatare desfasurat de un student la medicina ar fi utila o aplicatie (mobila) care sa ii prezinte vizual informatii relevante despre organele si bolile investigate. Astfel se doreste o aplicatie care, plecand de la informatii preluate in format RMN sau CT, sa permita vizualizarea 3D a unui organ (in intregime sau partial, din diferite unghiuri, reliefand anumite detalii – de ex vizualizarea inimii cu camerele ei sau doar a unei camere, sistemul vascular din inima, etc.), precum si a unor defecte posibile (identificarea automata a acestor defecte si vizualizarea lor – de ex. Fibroza atriala). 


## TO DO List
1. Dezvoltare flow principal pentru aplicatie 
- Incarcare si vizualizare imagine medicala (variate modalitati medicale – de ex. RMN, CT, imagini 2D sau 3D)
2. Dezvoltare componenta inteligenta
- Antrenarea si validarea unui model (sau a 2 modele) de identificare automata a defectelor (semnalate prin conturul si prin textura regiunii respective)
- Testarea modelului/modelelor pe imagini noi - integrarea modelului (clasificatorului) in aplicatie
3. Imbunatatire componenta inteligenta
- Din perspectiva calitatii procesului de invatare automata
- Din perspectiva complexitatii temporale si spatiale aferenta clasificatorului
- Din perspectiva clientului (utilizarii aplicatiei de catre student/medic)

## Date si referinte
**Imagini**
1. http://segchd.csail.mit.edu/data.html
2. https://grand-challenge.org/challenges/

**Evaluare**
1. VISCERAL tool http://www.visceral.eu/resources/evaluatesegmentation-software/
2. Descriere metrici https://bmcmedimaging.biomedcentral.com/articles/10.1186/s12880-015-0068-x

**Metode de lucru**
1. Vezhnevets, Vladimir, and Vadim Konouchine. "GrowCut: Interactive multi-label ND image segmentation by cellular automata." proc. of Graphicon. Vol. 1. No. 4. 2005.
2. Kauffmann, Claude, and Nicolas Piché. "Seeded ND medical image segmentation by cellular automaton on GPU." International journal of computer assisted radiology and surgery 5.3 (2010): 251-262.
3. Peng Peng, Karim Lekadir,  Ali Gooya, Ling Shao, Steffen E. Petersen, Alejandro F. Frangi, A review of heart chamber segmentation for  structural and functional analysis using cardiac magnetic resonance imaging, Magn Reson Mater Phy (2016) 29:155–195
4. Catalina Tobon-Gomez, Jochen Peters, Juergen Weese, Karen Pinto, Rashed Karim, Tobias Schaeffter, Reza Razavi, and Kawal S. Rhode, Left Atrial Segmentation Challenge: A Unified Benchmarking Framework, STACOM 2013, LNCS 8330, pp. 1–13, 2014
5. Catalina Tobon-Gomez et al., Benchmark for algorithms segmenting the left
atrium from 3D CT and MRI datasets, IEEE Transactions on Medical Imaging, 2015
6. Bram van Ginneken, Fifty years of computer analysis in chest imaging: rule-based, Radiol Phys Technol, 2017
7. Lequan Yu, Xin Yang, Jing Qin and Pheng-Ann Heng 
3D FractalNet: Dense volumetric segmentation for cardiovascular MRI volumes, 2017 
8. Jelmer M. Wolterink, Tim Leiner, Max A. Viergever and Ivana Isgum 
Dilated convolutional neural networks for cardiovascular MR segmentation in congenital heart disease, 2017
9. Rahil Shahzad, Shan Gao, Qian Tao, Oleh Dzyubachyk and Rob van der Geest, Automated cardiovascular segmentation in patients with congenital heart disease from 3D CMR scans: Combining multi-atlases and level-sets, 2017 
10. Rezaei, Mina, Haojin Yang, and Christoph Meinel. "Whole heart and great vessel segmentation with context-aware of generative adversarial networks." Bildverarbeitung für die Medizin 2018. Springer Vieweg, Berlin, Heidelberg, 2018. 353-358.
11. Yu, Lequan, et al. "Automatic 3D cardiovascular MR segmentation with densely-connected volumetric convnets." International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, Cham, 2017.
12. Payer, Christian, et al. "Multi-label whole heart segmentation using CNNs and anatomical label configurations." International Workshop on Statistical Atlases and Computational Models of the Heart. Springer, Cham, 2017.
13. Yang, Guang, et al. "Multiview Sequential Learning and Dilated Residual Learning for a Fully Automatic Delineation of the Left Atrium and Pulmonary Veins from Late Gadolinium-Enhanced Cardiac MRI Images." 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). IEEE, 2018.
14. Zhang, Tinghong, et al. "Multiple Attention Fully Convolutional Network for Automated Ventricle Segmentation in Cardiac Magnetic Resonance Imaging." Journal of Medical Imaging and Health Informatics 9.5 (2019): 1037-1045.
15. Zhang, Dong, et al. "Direct Quantification for Coronary Artery Stenosis Using Multiview Learning." International Conference on Medical Image Computing and Computer-Assisted Intervention. Springer, Cham, 2019.
16. Zhuang, Xiahai, et al. "Evaluation of Algorithms for Multi-Modality Whole Heart Segmentation: An Open-Access Grand Challenge." arXiv preprint arXiv:1902.07880 (2019).



