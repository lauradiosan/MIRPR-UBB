
# Proiecte MIRPR 2024-2025


<!-- <details>
    <summary> 1. Title </summary>
### Scop
### Ideea de baza
### TODOlist
1. Iteratia1
2. Iteratia2
### Data
### Bibliografie
</details> -->



<details>
    <summary> <img style="vertical-align:middle"  src="images\indoor.jpeg" alt="networks" width="100"/> Indoor Room Generation using Stable Diffusion (Owner: Alexandru Manole) </summary>

### Scop 
Generate Realistic Synthetic Images of Indoor Scenes – To improve the performance of data-hungry AI models which require large datasets in order to reach their full potential. 

### Ideea de baza
In order to improve the performance of indoor room semantic segmentation and\or depth estimation, develop a Stable Diffusion-based model (i.e. ControlNet) for realistic image generation. Evaluate the quality of the generated samples.

### TODOlist
1. Train ControlNet on Toy Dataset (Circles)
2. Test pre-trained ControlNet
3. Fine-tune ControlNet on NYU Depth DatasetV2
4. Evaluate quality of generated images
- Visual inspection
- Metrics (i.e Fréchet Inception Distance)
- Impact in semantic segmentation training
    - Train semantic segmentation model with real data
    - Train model with both real and synthetic data
    - Compare performance of the two models

### Data

### Bibliografie

Data [NYU Depth Dataset V2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html)
- [NYU Dataset](https://cs.nyu.edu/~fergus/datasets/indoor_seg_support.pdf)

ControlNet 
- article Zhang, L., Rao, A., & Agrawala, M. (2023). Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 3836-3847) [link](https://arxiv.org/pdf/2302.05543)
- code [link](https://github.com/lllyasviel/ControlNet)

Generative Library [link](https://github.com/stability-ai/generative-models)

Stable Diffusion 
- article Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2022). High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 10684-10695) [link](https://arxiv.org/pdf/2112.10752)

U-Net 
- article Ronneberger, O., Fischer, P., & Brox, T. (2015). U-net: Convolutional networks for biomedical image segmentation. In Medical image computing and computer-assisted intervention–MICCAI 2015: 18th international conference, Munich, Germany, October 5-9, 2015, proceedings, part III 18 (pp. 234-241). Springer International Publishing [link](https://arxiv.org/pdf/1505.04597)

Fréchet Inception Distance 
- article Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., & Hochreiter, S. (2017). Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing systems, 30. [link](https://arxiv.org/pdf/1706.08500)

</details>


<details>
    <summary>   Optimal therapeutic plan for implants (owner: dna. dr. Mihaela Hedesiu) <img style="vertical-align:middle"  src="images\implantPlan.jpeg" alt="networks" width="100"/> </summary>

### Scop
Dezvoltarea   unor algoritmi AI pentru predictia unui plan therapeutic implantar optim si personalizat adaptat situatiei anatomice a pacientului.  [link](2024-2025\Projects\Implant planning-articole.pptx)


### Ideea de baza
- Identificarea zonelor edentate: maxilla, mandibular (reconstructive OPT) 
- Densitatea osoasa (cross-section) 
- Inaltimea crestei (cross-section) 
- Diametrul crestei (cross-section) 

Rezulate cu AI  
- Numar implante  
- Pozitia pe arcada 
- Numar implante  
- Inaltimea implantului  
- Diametrul implantului 

### TODOlist
1. se pleaca de la o imagine CBCT (un dicom 3D) si se segmenteaza (in format 3D) dintii, mandibula, canale mandibulare, sinusuri maxilare) - folosind un algoritm de segmentare in imagine (de ex DentalSegmentator, nnU-Net, 3D U-Net)
2. se identifica zonele fara dinti (edentate) in imaginea 3D 
3. se transforma totul in 2D = view panoramic (adica reconstructie panoramica/reconstructie OPT
4. se realizeaza reconstructii cross-section cu masuratori ale crestei edentate


### Data
- Examinari CBCT – format DICOM 
[link](https://github.com/IvisionLab/OdontoAI-Open-Panoramic-Radiographs/blob/main/README.md) 
<!-- - Reconstructii panoramice - identificarea zonelor edentate  pentru plasarea implantelor  
- Recosntructie OPT 
- Reconstructii cross-section cu Masuratori ale crestei edentate   -->

### Bibliografie
Flow general: 
- Kurt Bayrakdar, S., Orhan, K., Bayrakdar, I.S. et al. A deep learning approach for dental implant planning in cone-beam computed tomography images. BMC Med Imaging 21, 86 (2021). doi:10.1186/s12880-021-00618-z [link](https://bmcmedimaging.biomedcentral.com/articles/10.1186/s12880-021-00618-z)

DentalSegmentator 
- article: Dot G, et al. DentalSegmentator: robust open source deep learning-based CT and CBCT image segmentation. Journal of Dentistry (2024) doi:10.1016/j.jdent.2024.105130 [link](https://www.sciencedirect.com/science/article/pii/S0300571224002999?via%3Dihub)
- code [link](https://github.com/gaudot/SlicerDentalSegmentator)

nnU-Net
- article: Isensee F, et al. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nat Methods. 2021;18(2):203-211. doi:10.1038/s41592-020-01008-z [link](https://www.nature.com/articles/s41592-020-01008-z)
- code [link](https://github.com/mic-dkfz/nnunet)

3D U-Net 
- article: Melerowitz, L., Sreenivasa, S., Nachbar, M., Stsefanenka, A., Beck, M., Senger, C., ... & Stromberger, C. (2024). Design and evaluation of a deep learning-based automatic segmentation of maxillary and mandibular substructures using a 3D U-Net. Clinical and Translational Radiation Oncology, 47, 100780. [link](https://www.ctro.science/article/S2405-6308(24)00057-0/fulltext)
- code [link1](https://github.com/Maxlo24/AMASSS_CBCT) [link2](https://github.com/ellisdg/3DUnetCNN)
</details>


<details>
    <summary> <img style="vertical-align:middle" src="images\periimplantitis.jpeg" alt="networks" width="100"/> Automatic model for risk estimation of peri-implantitis (owner: dna. dr. Mihaela Hedesiu)    </summary>

### Scop
Modele AI pentru evaluarea riscului de aparitie  a periimplantitei  [link](2024-2025\Projects\Implant planning-articole.pptx)

### Ideea de baza
- algoritmi AI de identificare a factorilor asociati cu dezvolatrea periimplantitei  
- acordarea unui scor de risc in functie de datele gasite in literatura 
- dezvoltaea unui algoritm AI de calcul a riscului 
- Validarea algoritmului dezvolatat  pe cazuri clinice  - calculul performantei predictiei riscului de esec implantar  


### TODOlist
1. Dandu-se o colectie de documente text (articles, case reports, reviews, etc.), se inspecteaza colectia si se cauta factorii care au determinat esecul tratamentului implantar
2. In functie de anumite criterii (frecventa = in cate articole apare acel factor, intensitate = daca s-a cuantificat cumva influenta acelui factor) se da un scor de risc fiecarui factor
3. se creaza 1 chestionar cu acest sistem de scoring care se va valida clinic

### Data
- Date din literatura - 3 baze de date PubMed, Embase , Google scholar - model de cautare si identificare a esecului implantar – un fel de review dar realizat prin AI 
- cateva exemple cu documente [link](2024-2025\Projects\Articole implat failure.zip)

### Bibliografie

</details>
 
<details>
    <summary> Estimation of Land Surface Temperature (owner: dna. prof.Adina Croitoru & Adriana Coroiu) <img style="vertical-align:middle" src="images\lst.png" alt="networks" width="100"/> </summary>

### Scop
Cresterea de rezolutie a informatilor de pe imaginile satelitare [link](2024-2025\Projects\Challenges_Hackaton_Info_UBB-FAG.pptx)

### Ideea de baza
Estimarea temperaturii aerului la nivelul străzilor este o sarcină dificilă din cauza suprafețelor urbane foarte eterogene, a morfologiei străzilor asemănătoare unor canioane și a diverselor procese fizice din mediul construit. Deși studiile de pionierat s-au angajat în investigații prin abordări bazate pe date, multe întrebări rămân inca fara răspuns. Problema de estimare a temperaturii la nivelul străzilor se poate rezolva cu ajutorul rețelele neuronale bazate pe grafe (GNN) si cu tehnici de reprezentare spațială a informatiilor (embeddings). În mod colectiv, acest studiu contribuie, de asemenea, la planificarea și politica urbană, oferind căi de îmbunătățire a rezistenței orașului la schimbările climatice, promovând astfel agenda pentru gestionarea mediului și sustenabilitatea urbană.

### TODOlist
1. Exersare antrenare&validare model de ML bazat pe GNN
2. Antrenare si validare model de estimare a temperaturii plecand de la imagini de o anumita resolutie (de ex resolutie de 30m) pe baza unor imagini inregistrate (unde pentru fiecare pixel se cunoaste temperatura reala)
3. Estimare temepratura in imagini de o alta rezolutie (de ex resolutie 10m) pe baza modelului anterior antrenat (pentru ca imaginile de 10m nu au temperatura reala pentru fiecare pixel)


### Data

### Bibliografie

Metodologie
- Yu, Y., Li, P., Huang, D., & Sharma, A. (2024). Street-level temperature estimation using Graph Neural Networks: Performance, feature embedding and interpretability. Urban Climate, 56, 102003. [link](https://www.sciencedirect.com/science/article/pii/S2212095524001998#bi0005)
- Onačillová, K., Gallay, M., Paluba, D., Péliová, A., Tokarčík, O., & Laubertová, D. (2022). Combining landsat 8 and sentinel-2 data in google earth engine to derive higher resolution land surface temperature maps in urban environment. Remote Sensing, 14(16), 4076 [link](https://www.mdpi.com/2072-4292/14/16/4076)
- Li, P., & Sharma, A. (2024). Hyper‐local temperature prediction using detailed urban climate informatics. Journal of Advances in Modeling Earth Systems, 16(3), e2023MS003943. [link](https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2023MS003943) - they provide access to the data!


Graph Neural Networks 
- Jure Leskovec's lecture [link](https://web.stanford.edu/class/cs224w/index.html#schedule) and [package](https://www.pyg.org/)
- PyTorch geometric [library](https://pytorch-geometric.readthedocs.io/en/latest/) [docs1](https://arxiv.org/pdf/1903.02428) [docs2](https://proceedings.neurips.cc/paper_files/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf)


</details>
<!-- 
<details>
    <summary><img style="vertical-align:middle" src="images\extremeEvents.jpeg" alt="networks" width="100"/>  Prediction of extreme events (owner: dna prof. Adina Croitoru & Adriana Coroiu) </summary>

### Scop
Imbunatatirea prognozelor pentru fenomene extreme [link](2024-2025\Projects\Challenges_Hackaton_Info_UBB-FAG.pptx)

### Ideea de baza
Evenimentele atmosferice extreme provoacă daune grave societăților umane și ecosistemelor. Frecvența și intensitatea evenimentelor extreme și a altor evenimente asociate cresc continuu din cauza schimbărilor climatice și a încălzirii globale. Predicția si caracterizarea cu precizie a evenimentelor extreme atmosferice este, prin urmare, un domeniu cheie de cercetare în care multe grupuri lucrează în prezent prin aplicarea diferitelor metodologii și instrumente de calcul. Metodele de învățare automată și de învățare profundă au apărut în ultimii ani ca tehnici puternice pentru a aborda multe dintre problemele legate de evenimentele atmosferice extreme. 

### TODOlist
1. Identify a challenge related to data-generation - check this [paper](https://link.springer.com/content/pdf/10.1007/s10462-024-10764-9.pdf)
2. replicate one of the models presented in the paper [link](https://journals.ametsoc.org/configurable/content/journals$002faies$002f2$002f1$002fAIES-D-22-0035.1.xml?t:ac=journals%24002faies%24002f2%24002f1%24002fAIES-D-22-0035.1.xml)
3. develop an approach based on difussion models and compare the results with those obtained by the replicated model

### Data
- [link](https://github.com/google-research/heatnet)


### Bibliografie

Useful research project - [link](https://climateintelligence.eu/outcomes/#1725010984824-7d0d0503-8097)

Articole survey 
- Bond-Taylor, S., Leach, A., Long, Y., & Willcocks, C. G. (2021). Deep generative modelling: A comparative review of vaes, gans, normalizing flows, energy-based and autoregressive models. IEEE transactions on pattern analysis and machine intelligence, 44(11), 7327-7347 [link](https://link.springer.com/content/pdf/10.1007/s10462-024-10764-9.pdfhttps://link.springer.com/content/pdf/10.1007/s10462-024-10764-9.pdf)
- Materia, S., García, L. P., van Straaten, C., O, S., Mamalakis, A., Cavicchia, L., ... & Donat, M. (2024). Artificial intelligence for climate prediction of extremes: State of the art, challenges, and future perspectives. Wiley Interdisciplinary Reviews: Climate Change, e914. [link](https://wires.onlinelibrary.wiley.com/doi/epdf/10.1002/wcc.914)
- Salcedo-Sanz, S., Pérez-Aracil, J., Ascenso, G., Del Ser, J., Casillas-Pérez, D., Kadow, C., ... & Castelletti, A. (2024). Analysis, characterization, prediction, and attribution of extreme atmospheric events with machine learning and deep learning techniques: a review. Theoretical and Applied Climatology, 155(1), 1-44. [link](https://link.springer.com/article/10.1007/s00704-023-04571-5)

Artciol cu CNN si date 
- Lopez-Gomez, I., McGovern, A., Agrawal, S., & Hickey, J. (2023). Global extreme heat forecasting using neural weather models. Artificial Intelligence for the Earth Systems, 2(1). [link](https://journals.ametsoc.org/configurable/content/journals$002faies$002f2$002f1$002fAIES-D-22-0035.1.xml?t:ac=journals%24002faies%24002f2%24002f1%24002fAIES-D-22-0035.1.xml) [code](https://github.com/google-research/heatnet)



</details> -->


<details>
    <summary><img style="vertical-align:middle" src="images\extremeEvents.jpeg" alt="networks" width="100"/>  Identify the interactions between SDG targets/indices for maximizing the investment impact (owner: dna prof. Adina Croitoru & Adriana Coroiu) </summary>

### Scop
Imbunatatirea prognozelor pentru fenomene extreme [link](2024-2025\Projects\Challenges_Hackaton_Info_UBB-FAG.pptx)

### Ideea de baza

Sustainable development is an approach that attempts to balance the social and economic needs of present and future human generations with the imperative of preserving or preventing undue damage to the natural environment  long-term planning. 

The 2030 Agenda for Sustainable Development is a global framework adopted by UN, a core guiding document and a global framework adopted by all United Nations members in 2015. 
- Agenda 2030 (Romania)

Structure of goals, targets and indicators:
- 17 SDGs - UN resolution.
- Each goal typically has 8-12 targets;
- Each target has 1-4 indicators used to measure progress toward reaching the targets, They are: 
    - outcome targets (circumstances to be attained) or
    - means of implementation targets.

### TODOlist
To develop a model aiming to prioritize intervention (investments) in a territorial unit to maximize the impact.
For each target/indicator  a map of interactions (a tree).

Ex: educational efforts for girls (goal 4) would enhance maternal health outcomes (part of goal 3), and contribute to poverty eradication (goal 1), gender equality (goal 5) and economic growth (goal 8).

Why? All types of organizations must report financially and non-financially based on SDGs !!!  This type of analysis could improve the efficacity of the investments!


### Data

Database - Eurostat (europa.eu) [link](https://ec.europa.eu/eurostat/web/sdi/database)


### Bibliografie
- Nilsson M, Griggs D, Visbeck M (2016) Map the interactions between Sustainable Development Goals. NATURE | VOL 534 |
- Rezultate | România Durabilă (gov.ro)
- Romania Durabila 2030 (gov.ro)
- [link](https://unstats.un.org/sdgs/indicators/indicators-list)
- [link](https://ec.europa.eu/eurostat/web/sdi/indicators)
- [link](http://romania-durabila.gov.ro/wp-content/uploads/2022/02/INDD_tin te2030_14febr2022.pdf()


</details>

<details>
    <summary> Causality identification (owner: dl. dr. Dan Blendea)  <img  style="vertical-align:middle" src="images\causality.jpeg" alt="networks" width="100"/></summary>

### Scop
Identificarea cauzelor insuficientei mitrale [link](2024-2025\Projects\variabilitate.pdf)

### Ideea de baza

Plecand de la o ecografie cardiaca (in format DICOM) se doreste identificarea cauzelor insuficientei mitrale (Mitral Regurgitation - MR). Se va folosi un model AI bazat pe Graph-based CNN care va analiza ecografia, iar pe baza masuratorilor (volumul MR, volumul ventriculului stang, volumul atriului stang, volumul inelului mitral, etc) si vor identifica interdependentele existente intre aceste masuratori (efectuate de-a lungul a mai multe cicluri cardiace). [more details](variabilitate.pdf)



### TODOlist
1. Se va analiza evolutia individuala a masuratorilor in timp (pe parcursul mai multor cicluri cardiace) 
2. se va identifica interdependentele existente intre aceste masuratori
3. Se va dezvolta un model de estimare a cauzelor insuficientei mitrale pe baza masuratorilor ecografice si a interdependentelelor identificate


### Data
- tiny dataset [link](2024-2025\Projects\pacienti.xlsx)


### Bibliografie
Graph Neural Networks 
- Jure Leskovec's lecture [link](https://web.stanford.edu/class/cs224w/index.html#schedule) and [package](https://www.pyg.org/)
- PyTorch geometric [library](https://pytorch-geometric.readthedocs.io/en/latest/) [docs1](https://arxiv.org/pdf/1903.02428) [docs2](https://proceedings.neurips.cc/paper_files/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf)

Causality inspired GNNs [link](https://github.com/usail-hkust/Awesome-Causality-Inspired-GNNs)

Wang, L., Adiga, A., Chen, J., Sadilek, A., Venkatramanan, S., & Marathe, M. (2022, June). Causalgnn: Causal-based graph neural networks for spatio-temporal epidemic forecasting. In Proceedings of the AAAI conference on artificial intelligence (Vol. 36, No. 11, pp. 12191-12199). [link](https://arxiv.org/pdf/2312.12477)

</details>



<details>
    <summary> <img  style="vertical-align:middle"  src="images\cancer.jpeg" alt="networks" width="100"/> Localizarea cancerului de col uterin (owner: dl. dr. Andrei Roman) </summary>
### Scop
Identificarea automata a leziunilor in cancerul de col uterin in imagini de tip RMN [link](2024-2025\Projects\Cancer de col uterin-1.pptx)

### Ideea de baza
### TODOlist
1. Iteratia1
2. Iteratia2
### Data
- dataset1 [link](https://synthrad2023.grand-challenge.org/)
- dataset2 [link](https://github.com/SynthRAD2023/preprocessing)

### Bibliografie
- Bourgioti, C., Chatoupis, K., & Moulopoulos, L. A. (2016). Current imaging strategies for the evaluation of uterine cervical cancer. World journal of radiology, 8(4), 342. [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4840192/)
- Zaki, N., Qin, W., & Krishnan, A. (2023). Graph-based methods for cervical cancer segmentation: Advancements, limitations, and future directions. AI Open. [link](https://www.sciencedirect.com/science/article/pii/S2666651023000086)
- Kurata, Y., Nishio, M., Moribata, Y., Kido, A., Himoto, Y., Otani, S., ... & Nakamoto, Y. (2021). Automatic segmentation of uterine endometrial cancer on multi-sequence MRI using a convolutional neural network. Scientific Reports, 11(1), 14440.[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8280152/#MOESM1)
- Lin, Y. C., Lin, Y., Huang, Y. L., Ho, C. Y., Chiang, H. J., Lu, H. Y., ... & Lin, G. (2023). Generalizable transfer learning of automated tumor segmentation from cervical cancers toward a universal model for uterine malignancies in diffusion-weighted MRI. Insights into Imaging, 14(1), 14. [link](https://insightsimaging.springeropen.com/articles/10.1186/s13244-022-01356-8)
- Afshar, P., Mohammadi, A., Plataniotis, K. N., Oikonomou, A., & Benali, H. (2019). From handcrafted to deep-learning-based cancer radiomics: challenges and opportunities. IEEE Signal Processing Magazine, 36(4), 132-160. [link](https://arxiv.org/pdf/1808.07954.pdf)

</details>



<details>
    <summary> Evolutia gripei (owner: dl. prof. Zoltan Balint) <img style="vertical-align:middle" src="images\influenza.jpeg" alt="networks" width="100"/>  </summary>

### Scop
Identificarea predictorilor imunitari de bază care pot discrimina între persoanele cu răspuns ridicat sau scăzut după vaccinarea antigripală [link](2024-2025\Projects\BalintZ_FluPRINT_04102024.pptx)

### Ideea de baza
Sistemul imunitar cuprinde mai multe tipuri de celule care lucrează împreună pentru a dezvolta un răspuns eficient la un anumit agent patogen. Cu toate acestea, care dintre aceste nenumărate tipuri de celule sunt importante într-un anumit răspuns nu este bine înțeles. Abordarea imunologică își propune să măsoare impactul expresiei genelor și diferitelor celule și molecule din sistemul imunitar în timpul unei infecții sau vaccinări și utilizează metodelor de Machine Learning pentru a discerne care componente sunt cele mai importante. Aceste studii au scopul practic de a determina ce face o formulare de vaccin mai bună decât alta sau modul în care indivizii variază. Pentru a realiza acest lucru, este crucială o modelare precisă a proceselor complexe care duc la un rezultat de succes.

### TODOlist

1. Definirea problemei (ce se da si ce se cere):
- Pornind de la un set de date de tip tabelar, sa se prelucreze datele si sa se antreneze un model AI de clasificare. 
2. Analiza datelor de intrare:
- Descarcarea unui set de date [link](https://zenodo.org/records/3222451). 
- analiza exploratorie a datelor
3. Dezvoltarea unui model de AI si evaluarea performantei; stabilirea celor mai importante atribute din model
4. Propuneri de imbunatatiri

### Data
1. FluPRINT database [link](https://zenodo.org/records/3222451). 
2. A small dataset [link](https://journals.aai.org/jimmunol/article-supplement/107431/xlsx/ji_1900033_supplemental_table_14/)
2. Another tiny dataset [link](https://journals.aai.org/jimmunol/article-supplement/107431/xlsx/ji_1900033_supplemental_table_18/)

### Bibliografie
1. Tomic, A., Tomic, I., Rosenberg-Hasson, Y., Dekker, C. L., Maecker, H. T., & Davis, M. M. (2019). SIMON, an automated machine learning system, reveals immune signatures of influenza vaccine responses. The Journal of Immunology, 203(3), 749-759. [link](https://journals.aai.org/jimmunol/article/203/3/749/107431)
2. Tomic, A., Tomic, I., Dekker, C. L., Maecker, H. T., & Davis, M. M. (2019). The FluPRINT dataset, a multidimensional analysis of the influenza vaccine imprint on the immune system. Scientific data, 6(1), 214. [link](https://www.nature.com/articles/s41597-019-0213-4)
3. Weissler, E. H., Naumann, T., Andersson, T., Ranganath, R., Elemento, O., Luo, Y., ... & Ghassemi, M. (2021). The role of machine learning in clinical research: transforming the future of evidence generation. Trials, 22, 1-15. [link](https://link.springer.com/content/pdf/10.1186/s13063-021-05489-x.pdf)
</details>


<details>
    <summary> <img style="vertical-align:middle" src="images\anxiety.jpeg" alt="networks" width="100"/> Early Discovery of Anxiety/Depression in Teenagers Using Digital Tools (Owner: Cristiana Bogateanu si Vlad Neste)  </summary>

### Scop
Anxiety/Depression for teenagers - To enhance mental health support for teenagers by developing digital tools that can proactively identify signs of anxiety and depression. These tools aim to engage with adolescents in their digital environments—whether through chatbots, social media, video games, or other innovative platforms—to provide early intervention and emotional support. 

### Ideea de baza
The Early Discovery of Anxiety/Depression in Teenagers solution leverages digital platforms to identify and monitor mental health challenges among adolescents. The system combines multiple approaches, including AI-powered chatbots capable of conversational analysis, sentiment evaluation through social media interactions, and mental health assessments embedded in video game experiences. By engaging teenagers where they spend most of their time—whether online or gaming—the system aims to provide real-time insights and early warnings of anxiety or depression. This integrated solution offers a holistic approach, blending digital engagement with predictive analytics and personalized intervention strategies. 

<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data
### Bibliografie

- [link](https://arxiv.org/abs/2402.16182)
- [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11025697/)
- [link](https://home.dartmouth.edu/news/2024/02/phone-app-uses-ai-detect-depression-facial-cues)
- [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9461333)
- [link](https://chatgpt.com/g/g-IMV77BDMO-depression)
- [link](https://www.sciencedirect.com/science/article/pii/S0001691824002877)
- [link](https://www.mdpi.com/1999-4893/16/12/543)
- DeepWell DTx - ideea of implementation ;) [link](https://www.deepwelldtx.com/)
</details>


<details>
    <summary> Predictive Mental Health Monitoring System  (Owner: Cristiana Bogateanu si Vlad Neste) <img style="vertical-align:middle" src="images\mentalHealth.jpeg" alt="networks" width="100"/></summary>

### Scop
Mental Health - To empower individuals and healthcare providers by offering a predictive mental health monitoring system that proactively identifies and mitigates the risk of suicidal actions through the continuous and intelligent analysis of health data collected from wearable devices.  

### Ideea de baza
The Predictive Mental Health Monitoring System is a cutting-edge solution designed to leverage the capabilities of wearable devices, such as those similar to the Oura Ring, to monitor key health indicators and provide real-time insights into an individual's mental health. By combining advanced machine learning algorithms, GenAI, and innovative data analytics, the system aims to predict and prevent suicidal actions, offering timely interventions and personalised support. 

<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data
### Bibliografie
- [link](https://pubmed.ncbi.nlm.nih.gov/25398168/)
- [link](https://pubmed.ncbi.nlm.nih.gov/26875620/)
- [link](https://pubmed.ncbi.nlm.nih.gov/17805308/)
- [link](https://pubmed.ncbi.nlm.nih.gov/25628520/)
- [link](https://pubmed.ncbi.nlm.nih.gov/29386207/)
- [link](https://pubmed.ncbi.nlm.nih.gov/16033674/)
- [link](https://pubmed.ncbi.nlm.nih.gov/29240871/)
- [link](https://pubmed.ncbi.nlm.nih.gov/23685197/)
- [link](https://pubmed.ncbi.nlm.nih.gov/21658563/)
- [link](https://pubmed.ncbi.nlm.nih.gov/31236817/)
- [link](https://pubmed.ncbi.nlm.nih.gov/29727550/)


</details>


<details>
    <summary>   <img style="vertical-align:middle" src="images\triage.jpeg" alt="networks" width="100"/> Digital Triage System (Owner: Cristiana Bogateanu si Vlad Neste) </summary>

### Scop
Digital Triage - To support individuals and healthcare providers by offering a smart system that helps identify the most appropriate healthcare professional based on an individual's symptoms, ensuring faster and more accurate access to the right medical care. 

### Ideea de baza
The Digital Triage System is designed to function as a companion that uses advanced AI-driven technologies to guide individuals through a series of questions regarding their symptoms and health concerns. By intelligently assessing the input, the system can accurately indicate potential conditions and recommend the appropriate type of healthcare provider, such as a specialist, general practitioner, or mental health professional. Leveraging machine learning algorithms and symptom databases, this solution optimizes the pathway to care, reducing diagnostic delays and improving health outcomes. 

 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data
### Bibliografie
- [link](https://go.jamasoftware.com/the-rapid-rise-of-digital-health-technology.html?kw=digital%20technology%20in%20healthcare&cpn=11827675850&utm_source=google&utm_medium=cpc&utm_campaign=emea-search-medical-nonb&utm_adgroup=digital-health&utm_term=digital%20technology%20in%20healthcare&utm_content=582244983547&_bm=11827675850136122053649&gad_source=1&gclid=EAIaIQobChMIvNCu-u7piAMV0aqDBx0RsCSsEAAYAiAAEgIH1fD_BwE)
- [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9794085/)
- [link](https://infermedica.com/solutions/triage)
- [link](https://transform.england.nhs.uk/key-tools-and-info/digital-playbooks/gastroenterology-digital-playbook/using-intelligent-automation-to-improve-the-triage-and-referral-management-pathway/)
- [link](https://www.sciencedirect.com/science/article/abs/pii/S0738399123004573)
- [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11158416/)
- [link](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1297073/full)
- [link](https://xby2.com/case-studies/next-gen-ai-powered-emergency-triage/)
- [link](https://aws.amazon.com/ai/generative-ai/?gclid=EAIaIQobChMI7eOCjO_piAMVtpCDBx21lxHOEAAYASAAEgL_f_D_BwE&trk=718bb85a-f217-4294-bf55-ee86400cb863&sc_channel=ps&ef_id=EAIaIQobChMI7eOCjO_piAMVtpCDBx21lxHOEAAYASAAEgL_f_D_BwE:G:s&s_kwcid=AL!4422!3!686079230781!p!!g!!generative%20ai%20applications!20901655430!157427215859)
- [link](https://www.youtube.com/watch?v=S1E8jQofS_Y)
- [link](https://www.youtube.com/watch?v=yaTg9bNUeE8)
- [link](https://www.youtube.com/watch?v=c9hThlZNU0o)
- [link](https://www.clearstep.health/blog/generative-ai-in-healthcare-safely-harness-its-power-with-clinically-validated-virtual-triage)
- [link](https://medium.com/columbia-journal-of-science-tech-ethics-and-policy/harnessing-the-power-of-ai-in-emergency-triage-a-paradigm-shift-0af7786948bd_
- [link](https://618media.com/en/blog/claude-ai-in-healthcare-applications/)
- [link](https://www.sciencedirect.com/science/article/pii/S2589750024000979)

</details>

<details>
    <summary> Support in the drug development (Owner: Cristiana Bogateanu si Vlad Neste) <img  style="vertical-align:middle" src="images\drugs.jpeg" alt="networks" width="100"/></summary>

### Scop
Predict the Actions of Substances on the Human Body - To develop a high-fidelity system capable of accurately predicting the actions and reactions of substances within the human body, starting with their interactions with proteins, ultimately advancing drug discovery and personalized medicine. 

### Ideea de baza
The Predict the Actions of Substances system aims to use computational biology and machine learning to model and predict the behavior of various substances at the molecular level. By focusing initially on how these substances interact with proteins, the system will provide insights into potential therapeutic or harmful effects, facilitating early-stage drug discovery and safety testing. Leveraging vast datasets of molecular structures and biological reactions, the solution will deliver predictive simulations and data analytics, helping researchers and healthcare providers understand substance-protein interactions before human trials or clinical use. 

 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data
### Bibliografie

- [link](https://www.gc.cuny.edu/news/new-ai-model-can-accurately-predict-human-response-novel-drug-compounds)
- [link](https://theconversation.com/ai-system-can-predict-the-structures-of-lifes-molecules-with-stunning-accuracy-helping-to-solve-one-of-biologys-biggest-problems-229745)
- [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10143484/)
- [link](https://www.nature.com/articles/s42256-022-00541-0)
- [link](https://www.researchgate.net/figure/Overview-of-CODE-AE-a-Rationale-of-CODE-AE-Mechanistically-drug-response-biomarkers_fig1_364350188)
- [link](https://www.researchgate.net/publication/348958834_CODE-AE_A_Coherent_De-confounding_Autoencoder_for_Predicting_Patient-Specific_Drug_Response_From_Cell_Line_Transcriptomics)
- [link](https://deepmind.google/technologies/alphafold/)
- [link](https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/)
- [link](https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/)

</details>

<details>
    <summary> <img  style="vertical-align:middle" src="images\elderly.jpeg" alt="networks" width="100"/> Elderly People Caring Platform (Owner: Cristiana Bogateanu si Vlad Neste)  </summary>

### Scop
Elderly People Support - To provide a comprehensive and user-friendly platform that integrates data from various health conditions affecting the elderly, offering personalized recommendations, health status insights, and gamified elements to encourage healthy behaviors and proactive care. 

### Ideea de baza
The Elderly People Caring Platform is designed to support the aging population by consolidating data from multiple health conditions, such as cardiovascular disease, diabetes, and cognitive decline. The platform uses this data to provide actionable health recommendations and guidance on the appropriate healthcare pathways. Additionally, the system offers real-time insights into the user’s health status, making it easier to track changes and improvements over time. By incorporating gamification elements, such as health challenges, milestones, and rewards, the platform aims to engage elderly users in maintaining and improving their health in an enjoyable and motivating way. 
 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data
### Bibliografie
- [link](https://healthtechmagazine.net/article/2024/04/embracing-generative-ai-and-large-language-models-senior-care)
- [link](https://www.linkedin.com/pulse/harnessing-generative-ai-revolutionize-senior-care-future-skaria-vfckc/)
- [link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10534283/)
- [link](https://celiatecuida.com/en/home_en/) - GOOOD EXAMPLE
- [link](https://www.matellio.com/blog/ai-companion-for-elderly/)
- [link](https://www.ageinplacetech.com/blog/five-examples-use-ai-care-older-adults)
- [link](https://witlingo.com/gen-ai-senior-living/)
- [link](https://automationedge.com/blogs/generative-ai-in-home-care/)

</details>




<details>
    <summary> SimQuery (Owner: dl. Lucian Munteanu) <img style="vertical-align:middle"  src="images\news.jpg" alt="networks" width="100"/></summary>

### Scop
Journalists and content creators need a system to verify the accuracy of information before publishing. The system should check if the content is supported by the already validated data (Ground Truth).
- To query a ground truth database (in order to retrieve information using natural language The result of the query can be actual relevant data stored in the GT or it can be generated content using data summarization or other techniques. 
- To identify if a piece of information is supported by the GT The support detection process should allow for the system to automatically detect ground truth information which supports a certain piece of information [link](2024-2025\Projects\HCOE_Challenge_SimQuery.pdf)

### Ideea de baza
Improve operational efficiency, fosters innovation, strengthens decision making and gives organization a powerful tool for gaining insights from its data 

Facilitate collaboration between different domains by highlighting how ideas in one area may apply to another, fostering cross functional innovation 

Ground Truth represents a public data considered as being the correct and comprehensive representation of a certain reality 

Piece of information is defined as a generic information ( with no definite size and no 

definite content or ideas It can be a fragment of a page, a page, a document or a collection of documents 

Support  -definition- an information supports another information if there is a certain semantically similarity (topic similarity) and both information express the same idea(s) 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data

### Bibliografie
</details>


 <details>
    <summary> <img style="vertical-align:middle"  src="images\tst.jpeg" alt="networks" width="100"/> TSQS (Text Style Query System) (Owner: dl. Lucian Munteanu)  </summary>

### Scop
Personalized Learning Assistant - Students need to ask questions and receive answers in a style that matches their preferred learning method. Such a system should also analyze their writing style and provide feedback to improve their academic writing. [link](2024-2025\Projects\HCOE_Challenge_TSQS.pdf)

- To query a ground truth database (in order to retrieve information using natural language) The result of the query can be actual relevant data stored in the GT or it can be generated content using data summarization or other techniques. 
- To identify and analyze the style of a piece of information by itself and comparing with GT style(s) The style detection process should allow for the system to automatically detect ground truth information which has similar style with the piece of information  

### Ideea de baza

Style - refers to the distinctive linguistic patterns or characteristics that define how a text is written, as opposed to what is written (the content/ideas) 

<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data

### Bibliografie

Handcrafted Features in Computational Linguistics 
- article: Lee, B. W., & Lee, J. H. J. (2023). LFTK: Handcrafted features in computational linguistics. arXiv preprint arXiv:2305.15878. [link](https://aclanthology.org/2023.bea-1.1/)
- python package: [link](https://github.com/brucewlee/lftk)

Review TST: 
- Jin, D., Jin, Z., Hu, Z., Vechtomova, O., & Mihalcea, R. (2022). Deep learning for text style transfer: A survey. Computational Linguistics, 48(1), 155-205. [link](https://aclanthology.org/2022.cl-1.6/)
- Lyu, Y., Luo, T., Shi, J., Hollon, T. C., & Lee, H. (2023). Fine-grained text style transfer with diffusion-based language models. arXiv preprint arXiv:2305.19512. [link](https://aclanthology.org/2023.repl4nlp-1.6/)


</details>
