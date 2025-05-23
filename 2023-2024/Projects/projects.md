
# Proiecte MIRPR 2023-2024

<details>
    <summary> 1. Project Image processing for prostate cancer </summary>

### Scop
Caracterizarea tumorilor de prostata in imagini de tip RMN cu ajutorul atributelor de textura (radiomice)

### Ideea de baza
Caracterizarea tesuturilor canceroase la nivelul prostatei (prin metode automate neinvazive) contribuie la stabilirea unui tratament personalizat si la o mai buna recuperare a pacientului. Problema algoritmica este aceea de clasificare a diferitelor leziuni pe baza caracteristicilor radiomice extrase din RMN-urile de prostată. Caracteristicile radiomice se referă la modul în care anumiți parametri reproduc eterogenitatea sau complexitatea texturii. Cu cât scorul Gleason/ISUP pentru un nodul este mai mare, cu atât aspectul pe imagine va fi mai eterogen, cu diferențe mari de contrast între pixelii vecini și între texturile subregiunilor învecinate din acel nodul, diferențe uneori chiar vizibile cu ochiul liber. Cele mai utilizate caracteristici radiomice sunt matricele GLCM, GLRLM secundare și GLSZM.

### TODOlist
1. Iteratia1
- considerarea setului de atribute radiomice extrase si analiza acestor atribute
- clasificarea binara a leziunilor (ISUP-1 vs. others sau ISUP-1 vs. normal) cu un algoritm de ML
    - Evolutionary algorithms (e.g. [Multi Expression Programming](http://mepx.org/))
    - Decision Trees
    - Support Vector Machine
    - Artificial Neural Networks
    - other ML algorithms
- evaluarea predictiilor realziate de clasificatorul binar

2. Iteratia2
- extragerea atributelor radiomice din imagini RMN si analiza acestor atribute
- clasificarea multi-clasa a leziunilor (ISUP-1 vs. ISUP-2 vs. ISUP-3 vs. ISUP-4 vs. ISUP-5) cu un algoritm de ML
- evaluarea predictiilor 

### Data
- Cluj Hospital dataset of radiomic features extracted from 35 MRI images [link](ProjectsData/radiomicFeatsCluj35.zip)
- 26 MR datasets - https://wiki.cancerimagingarchive.net/display/Public/PROSTATE-MRI#327726088352fbd47ff4147b574d72f5b596e4a
- https://promise12.grand-challenge.org/ - great challenge, one can check methods, articles
- https://prostatemrimagedatabase.com/ - 230 datasets - I have no info about quality

### Bibliografie
- Oltean, M. (2022). Multi Expression Programming for solving classification problems [link](https://www.researchgate.net/publication/359261779_Multi_Expression_Programming_for_solving_classification_problems)
- Afshar, P., Mohammadi, A., Plataniotis, K. N., Oikonomou, A., & Benali, H. (2019). From handcrafted to deep-learning-based cancer radiomics: challenges and opportunities. IEEE Signal Processing Magazine, 36(4), 132-160.
- L. Jing, Y. Tian, Self-supervised visual feature learning with deep neural networks: A survey, IEEE Transactions on pattern analysis and machine intelligence (2020)
- theory -> prostate imaging
    - https://www.slideshare.net/abd_ellah_nazeer/presentation1-mri-imaging-of-the-prostate
    - https://www.slideshare.net/abd_ellah_nazeer/presentation1pptx-radiological-imaging-of-prostatic-diseases - sl48/49
    - Kato Zoltan - linear registration of medical data - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbinregdemo
    - 3D - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbin3dregdemo

</details>

<details>
    <summary> 2. Project Classification of prostate biopsy</summary>

### Aim
Caracterizarea cancerului de prostata in imagini de microscop (histopatologice)

### Main idea
Diagnosticul cancerului de prostată (PCa) se bazează pe stadializarea biopsiilor de țesut de prostată. Aceste mostre de țesut sunt examinate de un patolog și punctate conform sistemului de clasificare Gleason. Procesul de clasificare constă în găsirea și clasificarea țesutului canceros în așa-numitele modele Gleason (3, 4 sau 5) pe baza modelelor arhitecturale de creștere a tumorii. După ce biopsiei i se atribuie un scor Gleason, acesta este convertit într-un grad ISUP pe o scară de la 1 la 5. Sistemul de clasificare Gleason este cel mai important marker de prognostic pentru PCa, iar gradul ISUP are un rol crucial atunci când se decide cum trebuie tratat un pacient. Există atât riscul de a lipsi cancerul, cât și un risc mare de supraevaluare, ceea ce duce la un tratament inutil. Cu toate acestea, sistemul suferă de o variabilitate semnificativă între observatori între patologi, limitându-și utilitatea pentru pacienții individuali. Această variabilitate a evaluărilor ar putea duce la un tratament inutil sau, mai rău, la lipsa unui diagnostic sever.

### TODOlist
1. Iteratia1
- formarea patch-urilor - abordarea bazata pe grid sampling - si analiza datelor
- clasificarea patch-urilor (binara - ISUP-1 vs. others, ISUP-1 vs. normal - sau multi-clasa) cu un algoritm de ML
- evaluarea predictiilor facute de clasificator (prin vot majoritar)

2. Iteratia2
- formarea patch-urilor - abordarea bazata pe segmentation-driven sampling (kMeans sau UNet) - si analiza datelor 
- clasificarea patch-urilor (binara - ISUP-1 vs. others, ISUP-1 vs. normal - sau multi-clasa) cu un algoritm de ML
- evaluarea predictiilor facute de clasificator (prin vot majoritar)

3. Iteratia3
- formarea patch-urilor - abordarea bazata pe segmentation-driven sampling (Graph-based NNs - similar cu [link](https://arxiv.org/pdf/1910.13328.pdf)) - si analiza datelor 
- clasificarea patch-urilor (binara - ISUP-1 vs. others, ISUP-1 vs. normal - sau multi-clasa) cu un algoritm de ML
- evaluarea predictiilor facute de clasificator (prin vot majoritar)

### Data
- Grand Challenge Data [link](https://www.kaggle.com/competitions/prostate-cancer-grade-assessment/data)

### Bibliografie
- Bulten, W., Kartasalo, K., Chen, P. H. C., Ström, P., Pinckaers, H., Nagpal, K., ... & Eklund, M. (2022). Artificial intelligence for diagnosis and Gleason grading of prostate cancer: the PANDA challenge. Nature medicine, 28(1), 154-163. [link](https://www.nature.com/articles/s41591-021-01620-2#Abs1)
- Lazar, A. J., & Demicco, E. G. (2022). Human and machine: Better at pathology together?. Cancer cell, 40(8), 806-808. 
- Linkon, A. H. M., Labib, M. M., Hasan, T., & Hossain, M. (2021). Deep learning in prostate cancer diagnosis and Gleason grading in histopathology images: An extensive study. Informatics in Medicine Unlocked, 24, 100582. [link](https://www.sciencedirect.com/science/article/pii/S2352914821000721#bib107)
- Salvi, M., Acharya, U. R., Molinari, F., & Meiburger, K. M. (2021). The impact of pre-and post-image processing techniques on deep learning frameworks: A comprehensive review for digital pathology image analysis. Computers in Biology and Medicine, 128, 104129 [link](https://www.sciencedirect.com/science/article/pii/S0010482520304601)
- Graph Neural Networks documentation [link](https://cs.stanford.edu/people/jure/) 
- theory -> prostate imaging
    - https://www.slideshare.net/abd_ellah_nazeer/presentation1-mri-imaging-of-the-prostate
    - https://www.slideshare.net/abd_ellah_nazeer/presentation1pptx-radiological-imaging-of-prostatic-diseases - sl48/49
    - Kato Zoltan - linear registration of medical data - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbinregdemo
    - 3D - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbin3dregdemo

</details>

<details>
    <summary> 3. Project Image processing for breast cancer </summary>

### Scop
Caracterizarea tumorilor de san in imagini de tip tomosinteza


### Ideea de baza
Tomosinteza digitală a sânului (DBT) este o tehnologie avansată de screening pentru cancerul de sân, aprobată de FDA în 2011. DBT este adesea denumită mamografie 3D, deoarece produce imagini cvasi-tridimensionale (3D) ale sânului. În DBT, un aparat cu raze X este rotit pentru a captura imagini ale țesutului mamar din unghiuri diferite. Aceste imagini sunt reconstruite pentru a produce secțiuni subțiri ale sânului, care au detalii îmbunătățite în comparație cu mamografia tradițională 2D. Mai exact, rezoluția mai mare în afara planului în DBT permite o mai bună vizualizare a maselor și a distorsiunilor arhitecturale [link](https://pubs.rsna.org/doi/pdf/10.1148/rg.2019180046). Beneficiile DBT ca instrument de screening sunt demonstrate în mai multe studii prospective [ref](https://pubs.rsna.org/doi/full/10.1148/radiol.2015141303) în ultimul deceniu.


### TODOlist
1. Iteratia1
- considerarea setului de imagini de tip tomosinteza si analiza acestuia 
- clasificarea imaginilor prin folosirea unui algoritm de ML
- evaluarea predictilor facute de clasificator
 
2. Iteratia2
- considerarea setului de imagini de tip tomosinteza si analiza acestuia 
- localizarea tumorilor in imagini prin folosirea unui algoritm de ML (fie detectie, fie segmentare) - se poate porni de la exemplul de segmentare a tumorilor [link](https://github.com/MaciejMazurowski/mri-breast-tumor-segmentation)  in imagini MRI [link](https://github.com/mazurowski-lab/MRI-deeplearning-tutorial)
- evaluarea predictilor facute automat

3. Iteratia3
- considerarea setului de imagini de tip tomosinteza si analiza acestuia 
- identificarea cancerului de san in imagini prin folosirea unui algoritm de ML bazat pe grafe [link](https://dl.acm.org/doi/pdf/10.1145/3535508.3545549?casa_token=5wUH0sLz0Y0AAAAA:lFuFZ49UTvo1PcmtNLVUYsUlncgRiH3zUsYWO2JBBTReebYSuWeGZRp0xBVLGnhAcMscbkv5G_Dm)
- evaluarea predictilor facute automat

### Data
- DBT dataset [link](https://sites.duke.edu/mazurowski/resources/digital-breast-tomosynthesis-database/)); about used algorithms [link](https://github.com/mazurowski-lab/DBT-cancer-detection-algorithms) more details are available [here](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2801740)


### Bibliografie
- Geras, K. J., Mann, R. M., & Moy, L. (2019). Artificial intelligence for mammography and digital breast tomosynthesis: current concepts and future perspectives. Radiology, 293(2), 246-259. [link](https://pubs.rsna.org/doi/10.1148/radiol.2019182627)
- Bai, J., Posner, R., Wang, T., Yang, C., & Nabavi, S. (2021). Applying deep learning in digital breast tomosynthesis for automatic breast cancer detection: A review. Medical image analysis, 71, 102049.[link](https://www.sciencedirect.com/science/article/pii/S1361841521000955)
- Fan, M., Zheng, H., Zheng, S., You, C., Gu, Y., Gao, X., ... & Li, L. (2020). Mass detection and segmentation in digital breast tomosynthesis using 3D-mask region-based convolutional neural network: a comparative analysis. Frontiers in molecular biosciences, 7, 599333. [link](https://www.frontiersin.org/articles/10.3389/fmolb.2020.599333/full)
- Graph Neural Networks documentation [link](https://cs.stanford.edu/people/jure/) 
- Buda, M., Saha, A., Walsh, R., Ghate, S., Li, N., Święcicki, A., ... & Mazurowski, M. A. (2021). A data set and deep learning algorithm for the detection of masses and architectural distortions in digital breast tomosynthesis images. JAMA network open, 4(8), e2119100-e2119100. [link](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2783046?utm_campaign=articlePDF&utm_medium=articlePDFlink&utm_source=articlePDF&utm_content=jamanetworkopen.2023.0524)

</details>

<details>
    <summary> 4. Project Image processing for bladder cancer </summary>

### Scop
- stadializarea tumorilor in imagini medicale ale vezicii

### Ideea de baza

- identificarea tumorilor in vezica si gradul lor de infiltrare in peretele vezicii cu ajutorul tehnicilor automate (prin metode non-invazive) se poate dovedi a fi un real sprijin in stadializarea cancerului de vezica 

### TODOlist
1. Iteratia 1
- analiza datelor
- segmentarea zonelor de interes (perete, interior, tumora, background) cu ajutorul unor modele bazate pe CNN [DeepMedic](https://github.com/deepmedic/deepmedic), [U2net](https://github.com/xuebinqin/U-2-Net), [DeepLab](https://github.com/tensorflow/models/tree/master/research/deeplab)
- evaluarea segmentarilor

2. Iteratia 2
- clasificarea leziunilor anterior segmentate in functie de gradul lor de penetrare a peretelui vezicii
- evaluarea performantei

### Data
- 19 MRI - mouse, xenograft model - 2019 - https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=52757379120
- human participants - multimodal imaging - https://wiki.cancerimagingarchive.net/display/Public/TCGA-BLCA#1605636778b0bc3193ac47e9a70f2dcc3b72b99e


### Bibliografie
- M. I. Metwally et al, The validity, reliability, and reviewer acceptance of VI-RADS in assessing muscle invasion by bladder cancer: a multicenter prospective study. European Radiology, 1-13 (2021)
- S. H. Kim, Validation of vesical imaging reporting and data system for assessing muscle invasion in bladder tumor. Abdominal Radiology, 45(2):491-498 (2020)
- Tian, Z., Li, X., Zheng, Y., Chen, Z., Shi, Z., Liu, L., & Fei, B. (2020). Graph‐convolutional‐network‐based interactive prostate segmentation in MR images. Medical physics, 47(9), 4164-4176.
- X. Dolz et al., Multiregion segmentation of bladder cancer structures in MRI with progressive dilated convolutional networks, Med. Phys. 45 (12):5482–5493 (2018)
- K. Hammouda et al., A deep learning-based approach for accurate segmentation of bladder wall using mr images, 2019 IEEE International Conference on Imaging, pp. 1-6 (2019)

</details>

<details>
    <summary> 5. Project Image processing for dental data </summary>

### Scop
Identificarea dintilor si leziunilor in imagini dentare

### Ideea de baza
- procesarea automata a imaginilor medicale dentare poate fi foarte utila atat medicilor, cat si pacientilor. Identificarea dintilor si a leziunilro in aceste imagini reprezinta baza dezvoltarii unor aplicatii de screening automat a starii de sanatate a dintilor.

### TODOlist
1. Iteratia 1
- analiza datelor
- segmentarea zonelor de interes (mandibula, dinti) cu ajutorul unor modele preantrenate [DeepMedic](https://github.com/deepmedic/deepmedic), [U2net](https://github.com/xuebinqin/U-2-Net), [DeepLab](https://github.com/tensorflow/models/tree/master/research/deeplab)
- evaluarea segmentarilor

2. Iteratia 2
- antrenarea unor modele de segmentare bazate pe CNN si grafe [link](Lu, Y., Chen, Y., Zhao, D., Liu, B., Lai, Z., & Chen, J. (2020). CNN-G: Convolutional neural network combined with graph for image segmentation with theoretical analysis. IEEE Transactions on Cognitive and Developmental Systems, 13(3), 631-644.) a zonelor de interes specifice datelor medicale stomatologice [exemplu](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net) si studiul diferitelor functii de loss [link](https://github.com/JunMa11/SegLoss)
- evaluarea segmentarilor
- compararea abordarii din iteratia 1 cu abordarea din iteratia 2

### Data
- images with segmented [mandible](https://data.mendeley.com/datasets/hxt48yk462/1) and [tooth](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net)
- spectral images and their masks [here](https://sites.uef.fi/spectral/odsi-db/)

### Bibliografie
- Jader, G., Fontineli, J., Ruiz, M., Abdalla, K., Pithon, M., & Oliveira, L. (2018, October). Deep instance segmentation of teeth in panoramic X-ray images. In 2018 31st SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI) (pp. 400-407). IEEE.
- Leite, A. F., Gerven, A. V., Willems, H., Beznik, T., Lahoud, P., Gaêta-Araujo, H., ... & Jacobs, R. (2021). Artificial intelligence-driven novel tool for tooth detection and segmentation on panoramic radiographs. Clinical oral investigations, 25(4), 2257-2267.
- Lu, Y., Chen, Y., Zhao, D., Liu, B., Lai, Z., & Chen, J. (2020). CNN-G: Convolutional neural network combined with graph for image segmentation with theoretical analysis. IEEE Transactions on Cognitive and Developmental Systems, 13(3), 631-644.



</details>


<details>
    <summary> 6. Project Image processing for Emergency Room </summary>

### Scop
Identificarea problemelor medicale ale plamanilor in ecografii

### Ideea de baza
- procesarea automata a imaginilor medicale de tip ecografii este foarte utila in medicina de urgenta. Clasificarea automata a acestor imagini in imagini sanatoase sau patologice poate sprijini procesul de diagnosticare. 
Răspândirea rapidă a SARS-CoV-2 (COVID-19) din decembrie 2019 a forțat Unitățile de Terapie Intensivă să facă față unui număr mare de pacienți internați simultan cu resurse limitate. Pacienții grav bolnavi de COVID-19, în special cei cu ventilatoare mecanice, necesită o atenție specială, deoarece pot dezvolta complicații potențiale cu consecințe hemodinamice și respiratorii critice. Ultrasunetele la punctul de îngrijire (POCUS) ar putea avea un rol important în evaluarea pacientului cu SARS-CoV-2 în stare critică. În mare parte, ecografia pulmonară a fost prezentată ca având un rol în diagnostic și monitorizare, dar examinarea căilor respiratorii și evaluarea hemodinamică sunt de asemenea de interes.


### TODOlist
1. Iteratia 1
- analiza datelor
- clasificarea binara a imaginilor (normale vs. patologice)
- evaluarea clasificarii

2. Iteratia 2
- analiza datelor
- clasificarea multiclasa a imaginilor (normale vs. patologia1 vs. patologia2 vs. patologia3)
- evaluarea clasificarii
- compararea abordarii din iteratia 1 cu abordarea din iteratia 2

### Data
- imagini[link](https://drive.google.com/file/d/1KGIfChgskbB0H2FhPsMdebhllfcqMMkk/view?usp=sharing)


### Bibliografie
- Ghid imagini [link](GhidImaginiUS-AI.docx)
- Simon, R., Petrișor, C., Bodolea, C., Csipak, G., Oancea, C., & Golea, A. (2021). ABC approach proposal for POCUS in COVID-19 critically ill patients. Medical Ultrasonography, 23(1), 94-102. [link](https://eds.s.ebscohost.com/eds/pdfviewer/pdfviewer?vid=0&sid=b8705254-6e59-4baf-bd4b-8aca37d58999%40redis)
- Polyzogopoulou, E., Amoiridou, P., Abraham, T. P., & Ventoulis, I. (2022). Acute liver injury in COVID-19 patients hospitalized in the intensive care unit: Narrative review. World Journal of Gastroenterology, 28(47), 6662. [link](https://www.scienceopen.com/document_file/d2c6543c-9c93-4045-aed8-522af36a8a85/PubMedCentral/d2c6543c-9c93-4045-aed8-522af36a8a85.pdf)
</details>


<details>
    <summary> 7. Project Smart agriculture </summary>

### Scop
Cultivarea eficienta a plantelor

### Ideea de baza
Tot mai multe persoane sunt interesate de agricultura, produse cat mai naturale (eco, bio) si chiar cultivarea plantelor in gradina proprie. Dar multe dintre aceste persoane nu detin toate informatiile necesare cultivarii si ingrijirii plantelor (cand sa le semene/planteze, in ce sol se dezvolta optim, cand sa le ude, cat dureaza pana la maturizare, etc.). De aceea, ar fi util un sistem (o aplicatie) care sa permita oamenilor sa cultive legume intr-o anumita locatie avand in vedere factori de influenta precum: tipul de sol, temperatura, umiditatea, vantul, etc., dar si sfaturi utile pentru ingrijirea plantelor (cand sa le semene, cand sa le ude, etc.).

### TODOlist
1. Iteratia1
- identificarea culturii/culturilor cu potential maxim (productie maxima) care se poate cultiva pe o suprafata data avand in vedere specificul culturilor și specificul locatiei unde se face cultivarea (de ex carateristicile solului). Se pot lua in considerare si culturi succesive (ex. o cultura de salata verde sau de spanac urmata de o cultura de rosii sau de fasole verde). Info utile:
    - set care precizeaza ce sol prefera anumite culturi https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
    - un set care indica vecinatatile de plante https://www.kaggle.com/datasets/aramacus/companion-plants

2. Iteratia2
- identificarea bolilor în culturi pe baza procesării automate a imaginilor frunzelor. Info utile
    - set de imagini cu bolile plantelor [link1](https://www.kaggle.com/datasets/emmarex/plantdisease), [link2](https://www.kaggle.com/datasets/qramkrishna/corn-leaf-infection-dataset), [link3](https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases)

3. Iteratia3
- identificarea culturii potrivite si a cantitatii care poate fi posibil cultivata tinand cont de specificul culturii,  caracteristicile solului, coordonatele geografice ale locatiei, dimensiune parcelei, data plantarii, datele meteo aferente perioadei de cultivare. Datele de iesire se vor referi la cantitate din fiecare tip de leguma pentru parcela respectiva. Info utile:
    - dataset gata construit [link](https://www.nature.com/articles/s41597-021-00817-x#Sec4)
    - construire dataset cu informatiile necesare (caracteristicile culturilor, solului, etc.) extrase din "texte de specialitate" - se poate folosi un model de extragere a informatiilor utile din texte (de ex. transformerul BART de la HuggingFace [link](https://huggingface.co/facebook/bart-large-cnn?text=The+tower+is+324+metres+%281%2C063+ft%29+tall%2C+about+the+same+height+as+an+81-storey+building%2C+and+the+tallest+structure+in+Paris.+Its+base+is+square%2C+measuring+125+metres+%28410+ft%29+on+each+side.+During+its+construction%2C+the+Eiffel+Tower+surpassed+the+Washington+Monument+to+become+the+tallest+man-made+structure+in+the+world%2C+a+title+it+held+for+41+years+until+the+Chrysler+Building+in+New+York+City+was+finished+in+1930.+It+was+the+first+structure+to+reach+a+height+of+300+metres.+Due+to+the+addition+of+a+broadcasting+aerial+at+the+top+of+the+tower+in+1957%2C+it+is+now+taller+than+the+Chrysler+Building+by+5.2+metres+%2817+ft%29.+Excluding+transmitters%2C+the+Eiffel+Tower+is+the+second+tallest+free-standing+structure+in+France+after+the+Millau+Viaduct) sau altele [link](https://paperswithcode.com/task/reading-comprehension)) precum cele din folderul [ProjectsData/vegetables](ProjectsData\vegetables)

4. Iteratia4
- recomandari pt planul de cultivare (tinand cont de informatiile acumulate in functionalitatile precedente)
    - versiunea if - then
    - versiunea advanced

### Bibliographie
- Su, Y., Gabrielle, B., & Makowski, D. (2021). A global dataset for crop production under conventional tillage and no tillage systems. Scientific Data, 8(1), 33. [link](https://www.nature.com/articles/s41597-021-00817-x)
- Kluger, D. M., Owen, A. B., & Lobell, D. B. (2022). Combining randomized field experiments with observational satellite data to assess the benefits of crop rotations on yields. Environmental Research Letters, 17(4), 044066. [link](https://iopscience.iop.org/article/10.1088/1748-9326/ac6083)


</details>




<details>
    <summary> 8. Project Large Image processing for breast cancer </summary>

### Scop
Caracterizarea tumorilor de san in imagini de tip histopatologic


### Ideea de baza
Gradul tumorii cancerului de sân este puternic asociat cu supraviețuirea pacientului. În practica clinică actuală, patologii atribuie gradul tumorii după analiza vizuală a specimenelor de țesut. Cu toate acestea, studii diferite arată variații semnificative între observatori în gradul cancerului de sân. Au fost propuse metode de clasificare a cancerului de sân bazate pe computer, dar funcționează numai pe zone de țesut selectate în mod specific și/sau necesită adnotări care necesită forță de muncă pentru a fi aplicate noilor seturi de date. În acest proiect se urmareste antrenarea și evaluarea unui model de clasificare a cancerului de sân bazat pe învățarea profundă care funcționează pe imagini histopatologice cu diapozitive întregi. Clasificarea histologică a cancerului de sân implică revizuirea și notarea a trei caracteristici morfologice bine stabilite: numărul mitotic, pleomorfismul nuclear și formarea tubulilor. Luate împreună, aceste caracteristici formează baza sistemului de clasificare Nottingham, care este utilizat pentru a informa caracterizarea și prognoza cancerului de sân. Scopul proiectului este de a dezvolta modele de învățare profundă pentru a efectua notarea histologică a mostrelor de testut.


### TODOlist
1. Iteratia1
- considerarea setului de imagini de tip histo si analiza acestuia 
- clasificarea imaginilor prin folosirea unui algoritm de ML; se poate porni de la exemplul de aici [link](http://andrewjanowczyk.com/use-case-6-invasive-ductal-carcinoma-idc-segmentation/) si setul de date de aici [link](https://www.bracs.icar.cnr.it/)
- evaluarea predictilor facute de clasificator
 
2. Iteratia2
- considerarea setului de imagini de tip histo si analiza acestuia 
- localizarea tumorilor in imagini prin folosirea unui algoritm de ML (fie detectie, fie segmentare) - se poate porni de la exemplul de segmentare [link](https://github.com/AICAN-Research/H2G-Net) folosit in soft-ul [FastPathology](https://github.com/AICAN-Research/FAST-Pathology)
- evaluarea predictilor facute automat

3. Iteratia3
- considerarea setului de imagini de tip tomosinteza si analiza acestuia 
- identificarea cancerului de san in imagini prin folosirea unui algoritm de ML bazat pe grafe [link](https://kth.diva-portal.org/smash/get/diva2:1695468/FULLTEXT01.pdf) sau [link](https://drive.google.com/file/d/1sGHiDiZaLt5Yg1Pc1acxKwzHCXoXAFCy/view)
- evaluarea predictilor facute automat

### Data
- dataset1 [link](https://www.bracs.icar.cnr.it/)
- dataset2 - se va oferi direct celor interesati


### Bibliografie
- Jaroensri, R., Wulczyn, E., Hegde, N., Brown, T., Flament-Auvigne, I., Tan, F., ... & Chen, P. H. C. (2022). Deep learning models for histologic grading of breast cancer and association with disease prognosis. NPJ breast cancer, 8(1), 113. [link](https://www.nature.com/articles/s41523-022-00478-y)
- Wetstein, S. C., de Jong, V. M., Stathonikos, N., Opdam, M., Dackus, G. M., Pluim, J. P., ... & Veta, M. (2022). Deep learning-based breast cancer grading and survival analysis on whole-slide histopathology images. Scientific reports, 12(1), 15102.[link](https://www.nature.com/articles/s41598-022-19112-9)
- Niyas, S., Bygari, R., Naik, R., Viswanath, B., Ugwekar, D., Mathew, T., ... & Rajan, J. (2023). Automated Molecular Subtyping of Breast Carcinoma Using Deep Learning Techniques. IEEE Journal of Translational Engineering in Health and Medicine, 11, 161-169. [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9924555/)
- Hameed, Z., Garcia-Zapirain, B., Aguirre, J. J., & Isaza-Ruget, M. A. (2022). Multiclass classification of breast cancer histopathology images using multilevel features of deep convolutional neural network. Scientific Reports, 12(1), 15600. [link](https://www.nature.com/articles/s41598-022-19278-2)
</details>

<details>
    <summary> 9. Project Autonomated driving </summary>

More details [link](2023_04_03_SemesterProjects_Bosch.pdf)

</details>


<details>
    <summary> 10. Procesarea hartilor meteo </summary>

### Scop
Identificarea fronturilor atmosferice in imagini de tip "synoptic map"


### Ideea de baza
Identificarea in imagini a fronturilor atmosferice ;i corelarea lor cu incidentele de tip AVC. 
S-a constatat ca de-a lungul timpului distributia pe zile a accidentelor vasculare se poate corela cu anumit factori meteo precum frontul atmosferic, presiunea, temepratura, etc.
Primul pas ar fi identificarea acestor fronturi ]n imaginile de tip "synoptic map". 



### TODOlist
1. Colectarea de imagini de tip "synoptic map".
2. identificarea fronturilor in imagini si clasificarea fronturilor (reci, calde, mixte).
3. corelarea fronturilor cu alte variabile meteo (temperatura, presiunea)
4. corelarea datelor meteo cu date medicale

### Date si referinte
**Date si biblioteci**
- https://www.wetter3.de/archiv_dwd_dt.html
- https://danepubliczne.imgw.pl/datastore



**Metode de lucru**
- https://www.rmets.org/metmatters/how-interpret-weather-chart
- https://www.weather.gov/jetstream/wxmaps
- https://wcd.copernicus.org/articles/3/113/2022/wcd-3-113-2022.pdf