
# Asistent Automat pentru un student la medicina  <img src="heartSmall.png" alt="A cool heart"/>

## Obiective
Dezvoltarea unei aplicatii didactice care sa ajute studentii la medicina sa invete.


## Ideea de baza
In procesul de invatare desfasurat de un student la medicina ar fi utila o aplicatie (mobila) care sa ii prezinte vizual informatii relevante despre organele si bolile investigate. Astfel se doreste o aplicatie care, plecand de la informatii preluate in format RMN, sa permita vizualizarea 3D a unui organ (in intregime sau partial, din diferite unghiuri, reliefand anumite detalii – de ex vizualizarea vezicii urinare si a peretelui, cu straturile corespunzatoare, etc.), precum si a unor leziuni posibile (identificarea automata a acestor leziuni si vizualizarea lor – de ex. tumori in vezica). 


## TO DO List
1. Dezvoltare flow principal pentru aplicatie 
- Incarcare si vizualizare imagine medicala (variate modalitati medicale – de ex. RMN, CT, imagini 2D sau 3D)
2. Dezvoltare componente inteligente
- Antrenarea si validarea unui model de localizare a vezicii/prostatei (localizare ROI)
- Antrenarea si validarea unui model de segmentare a vezicii/prostatei (in interiorul ROI identificarea peretelui, respectiv a cavitatii vezicii/prostatei, identificarea tumorii)
- Antrenarea si validarea unui model de stadializare a tumorii identificate (analiza structurii tesuturilor din cadrul leziunii)
- Testarea modelului/modelelor pe imagini noi - integrarea modelelor inteligente in aplicatie
3. Imbunatatire componenta inteligenta
- Din perspectiva calitatii procesului de invatare automata
- Din perspectiva complexitatii temporale si spatiale aferenta clasificatorului
- Din perspectiva clientului (utilizarii aplicatiei de catre student/medic)


## Date si referinte

**Cateva exemple**
1. https://github.com/deepmedic/deepmedic 
2. https://github.com/christianpayer/MedicalDataAugmentationTool-MMWHS
3. https://github.com/RonaldGalea/imATFIB 
**Imagini**
1. http://segchd.csail.mit.edu/data.html
2. https://grand-challenge.org/challenges/

**Evaluare**
1. VISCERAL tool http://www.visceral.eu/resources/evaluatesegmentation-software/
2. Descriere metrici https://bmcmedimaging.biomedcentral.com/articles/10.1186/s12880-015-0068-x


**Metode de lucru**

Prostata
- lucrari:
    * lucrare recenta https://www.nature.com/articles/s41598-020-71080-0
- databases: 
    * 26 MR datasets - https://wiki.cancerimagingarchive.net/display/Public/PROSTATE-MRI#327726088352fbd47ff4147b574d72f5b596e4a
    * https://promise12.grand-challenge.org/ - great challenge, one can check methods, articles
    * https://zenodo.org/record/16396#.X57-1IgzaM9 - 3 patients MR and ultrasound
    * https://prostatemrimagedatabase.com/ - 230 datasets - I have no info about quality
- theory - prostate imaging -
    * https://www.slideshare.net/abd_ellah_nazeer/presentation1-mri-imaging-of-the-prostate
    * https://www.slideshare.net/abd_ellah_nazeer/presentation1pptx-radiological-imaging-of-prostatic-diseases - sl48/49  
    * Kato Zoltan - linear registration of medical data - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbinregdemo
    * 3D -  http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbin3dregdemo

Vezica urinară
- lucrari
    * recent review paper - MRI meta analysis: - https://euoncology.europeanurology.com/article/S2588-9311(20)30032-8/fulltext
    * paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6690492/ - 2019 - VI-RADS
    * M. G. Bandyk et al., MRI and CT bladder segmentation from classical to deep learning based approaches: Current limitations and lessons, Computers in Biology and Medicine, 104472 (2021)
    * R. Carando et al, The effectiveness of multiparametric magnetic resonance imaging in bladder cancer (Vesical Imaging-Reporting and Data System): A systematic review. Arab Journal of Urology, 2020,18(2):67-71 (2020)
    * X. Dolz et al., Multiregion segmentation of bladder cancer structures in MRI with progressive dilated convolutional networks, Med. Phys. 45 (12):5482–5493 (2018)
    * K. Hammouda et al., A deep learning-based approach for accurate segmentation of bladder wall using mr images, 2019 IEEE International Conference on Imaging, pp. 1-6 (2019)
    * L. Jing, Y. Tian, Self-supervised visual feature learning with deep neural networks: A survey, IEEE Transactions on pattern analysis and machine intelligence (2020)
    * S. H. Kim, Validation of vesical imaging reporting and data system for assessing muscle invasion in bladder tumor. Abdominal Radiology, 45(2):491-498 (2020)
    * L. Liu, L Liu, B. Xu, et al., Bladder cancer multi-class segmentation in MRI with Pyramid-In-Pyramid network, 2019 IEEE 16th International Symposium on Biomedical Imaging (ISBI 2019), pp. 28–31 (2019)
    * M. I. Metwally et al, The validity, reliability, and reviewer acceptance of VI-RADS in assessing muscle invasion by bladder cancer: a multicenter prospective study. European Radiology, 1-13 (2021)
    * Panebianco et al., Multiparametric magnetic resonance imaging for bladder cancer: development of VI-RADS (Vesical Imaging-Reporting And Data System), European urology, 74(3):294-306 (2018)
    * Panebianco, V et al., An evaluation of morphological and functional multi-parametric MRI sequences in classifying non-muscle and muscle invasive bladder cancer, Eur Radiol., 27(9):3759–66 (2017)
    * D. Xiao, G. Zhang, Y. Liu, 3D detection and extraction of bladder tumors via MR virtual cystoscopy, International journal of computer assisted radiology and surgery 11 (1):89–97 (2016)
    * X. Xu, Y. Liu, Y. Liu, Preoperative prediction of muscular invasiveness of bladder cancer with radiomic features on conventional MRI and its high-order derivative maps, Abdom Radiol (NY). 42(7):1896–905 (2017)
    * X. Xu et al, Three-dimensional texture features from intensity and high-order derivative maps for the discrimination between bladder tumors and wall tissues via MRI, International journal of computer assisted radiology and surgery, 12(4):645-656 (2017)
   
- databases 
    * http://www.visceral.eu/
    * bladder
        - 19 MRI - mouse, xenograft model - 2019 - https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=52757379120 
        - human participants - multimodal imaging - https://wiki.cancerimagingarchive.net/display/Public/TCGA-BLCA#1605636778b0bc3193ac47e9a70f2dcc3b72b99e
- medical hints 
    * urinary stone detection - https://pubs.rsna.org/doi/10.1148/ryai.2019180066 - 2019
    * MRI kidney/urinary tract - https://onlinelibrary.wiley.com/doi/pdf/10.1002/jmri.20700





**Tehnici de AI**
1. Vezhnevets, Vladimir, and Vadim Konouchine. "GrowCut: Interactive multi-label ND image segmentation by cellular automata." proc. of Graphicon. Vol. 1. No. 4. 2005.
2. Kauffmann, Claude, and Nicolas Piché. "Seeded ND medical image segmentation by cellular automaton on GPU." International journal of computer assisted radiology and surgery 5.3 (2010): 251-262.
3. T. Wu et al, Leveraging graph-based hierarchical medical entity embedding for healthcare applications, Scientific reports, 11(1):pp. 1-13 (2021)
4. J. Zhou et al., Graph neural networks: A review of methods and applications, AI Open 1:57-81 (2020)
5. L. Jing, Y. Tian, Self-supervised visual feature learning with deep neural networks: A survey, IEEE Transactions on pattern analysis and machine intelligence (2020)




