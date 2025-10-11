
# Teme de proiect MIRPR 2025-2026


## Project 1 
<details>
    <summary> Conversational Avatar Production (owner: Alexandru Manole, alexandru.manole@ubbcluj.ro) 
    <img src="projects\avatar.webp" width="100">
    </summary>

### Conversational Avatar Production

#### Scop
Dezvoltarea unui sistem conversațional, care răspunde la întrebări textuale în mod vocal prin intermediul unui avatar. De ex.:
- UBB-bot care răspunde la întrebări despre UBB si are ca avatar imaginea lui Janos Bolyai
- Turing-bot care răspunde la întrebări despre AI si are ca avatar imaginea lui Alan Turing



#### Ideea de baza
În lumea digitală, interacțiunea cu avatare animate devine din ce în ce mai importantă, fie că vorbim despre asistenți virtuali, personaje din jocuri, educație interactivă sau prezentatori AI pentru conținut video generat automat. Totuși, crearea animațiilor realiste pentru vorbire și expresii faciale implică, de obicei, procese complexe și costisitoare, necesitând resurse considerabile. 
Folosind tehnici de Machine Learning, acest proces poate fi automatizat, permițând avatarelor să reproducă mișcările buzelor și expresiile faciale în timp real, pe baza unui input audio sau text. O astfel de tehnologie ar putea fi utilizată în crearea de consilieri virtuali  pentru procedura de admitere pentru cursuri online, ghidurilor interactive pentru muzee sau aplicații turistice, asistenților personalizați pentru servicii bancare și customer support, dar și în industria filmelor și jocurilor pentru generarea rapidă de personaje animate. Scopul este de a dezvolta și antrena un model AI capabil să genereze animații fluide și naturale, transformând interacțiunile virtuale într-o experiență mai autentică și captivantă. 

#### Bibliografie

În funcție de soluția elaborată, câteva cerințe parțiale ar fi utilizarea corectă a următoarelor:
- generarea de imagini folosind modele de tip Stable Diffusion, precum Flash Diffusion [paper](https://arxiv.org/pdf/2406.02347), [git](https://github.com/gojasper/flash-diffusion). Task-uri posibile:
    - utilizare model pre-antrenat cu aceasta arhitectura si comparare cu alte modele de Stable Diffusion.
    - antrenare de la 0 a unui model Flash Diffusion pe un set de date mic (e.g. cateva sute de imagini)
    - fine-tuning folosind LoRA
    - antrenarea Flash Diffuision pentru o retea care nu e prezentata pe git (e.g. ControlNet)

- recomandarile de la versiunea precedenta a bot-ului [link](https://github.com/lauradiosan/AI-UBB/blob/main/2024-2025/labs/projects.md)

</details>



## Project 2

<details>
    <summary> Identificarea defectelor software (owner: Laura Cernau, laura.cernau@ubbcluj.ro) <img src="projects\code.jpg" width="100"> </summary>

### Identificarea defectelor software

#### Scop

Instrumentele AI îmbunătățesc productivitatea, dar degradează calitatea codului. 
Ultima analiză a [GitClear](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality?utm_source=substack&utm_medium=email) asupra a 211 milioane de linii de cod a constatat că asistenții AI (cum ar fi Copilot) pot spori productivitatea, dar înrăutățesc calitatea codului. Aceasta arată un compromis clar: producem mai mult cod, dar bazele noastre de cod au mult mai multe duplicate și mai puține refactorizări.

#### Ideea de baza

Se va considera o baza de date cu mai multe proiecte software. Se va dezvolta un model de AI bazat pe LLM care sa identifice defectele software in codul sursa pe baza codului sursa si al metricilor de complexitate. 

Posibile versiuni de input pentru LLM (prin intermediul prompt-ului): 
- doar codul sursa al clasei curente, 
- codul sursa al clasei curente si codul sursa al claselor "parinte", 
- codul sursa al clasei curente si codul sursa al claselor "parinte", precum si metrici de complexitate asociate codului sursa (metrici precum complexitatea ciclomatica [link](https://d1wqtxts1xzle7.cloudfront.net/48213691/tse.1976.23383720160821-12832-sniirk-libre.pdf?1471767990=&response-content-disposition=inline%3B+filename%3DA_Complexity_Measure.pdf&Expires=1743369021&Signature=FrLxyskf0pTFRiM~Q30qykafb4a-m071sO87klcxqXqJBcRJGOYOZ5CY94KFjsADNciMoVd4CNwPVHiVkgcACxxV-V~Bod8D8eI1gP7q8sHR0a5qhrIhpfePgf54kCvxGbTP-dFu9YItw~E2FXb~PQRIfzL9BmczizOXSASL1To9qFYCVhJv9MT-CoTABaSPQ8T4-9ZFVzdPwgXFX3e3oRYjotU3EWC6HkdWUG0gRvmMqONAyLWrxY8xFU4m7PkVnmAasyN7G9L38-DBsF8AUJT6CpjFfvAaAigK0iv8TkFYzyfbR5pu97LLH5w622qHtRc9tuo~3Qu2J9SPO0JGSA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA), 
complexitatea cognitiva [link](https://www.researchgate.net/publication/313803215_Automated_tool_for_the_calculation_of_cognitive_complexity_of_a_software), Weighted methods per Class [link](https://www.researchgate.net/publication/313803215_Automated_tool_for_the_calculation_of_cognitive_complexity_of_a_software), Lack of Cohesion in Methods [link](https://www.researchgate.net/publication/313803215_Automated_tool_for_the_calculation_of_cognitive_complexity_of_a_software), Depth of inheritance tree [link](https://www.researchgate.net/publication/313803215_Automated_tool_for_the_calculation_of_cognitive_complexity_of_a_software), Halstead’s Metrics [link](https://books.google.ro/books/about/Elements_of_Software_Science.html?id=zPcmAAAAMAAJ&redir_esc=y), 
Size metrics - Lines of Code [link](https://www.researchgate.net/publication/328646564_On_the_correlation_between_testing_effort_and_software_complexity_metrics)) 


Output asteptat: defectele software identificate in codul sursa (daca clasa contine sau nu contine bug-uri, ce fel de bug contine)


#### Data
- Data [link](https://www.inf.szte.hu/~ferenc/pdf/FTL18-PROMISE-A%20public%20unified%20bug%20dataset%20for%20Java.pdf)


#### Bibliografie

- List of research papers focused on Large Language Models [link](https://github.com/PurCL/CodeLLMPaper/tree/main)

- Simões, I. R. D. S., & Venson, E. (2024, November). Evaluating Source Code Quality with Large Language Models: a comparative study. In Proceedings of the XXIII Brazilian Symposium on Software Quality (pp. 103-113).
[link](https://www.researchgate.net/publication/383119379_Evaluating_Source_Code_Quality_with_Large_Languagem_Models_a_comparative_study)

- Wadhwa, N., Pradhan, J., Sonwane, A., Sahu, S. P., Natarajan, N., Kanade, A., ... & Rajamani, S. (2024). Core: Resolving code quality issues using llms. Proceedings of the ACM on Software Engineering, 1(FSE), 789-811 [link](https://dl.acm.org/doi/pdf/10.1145/3643762)

- Jelodar, H., Meymani, M., & Razavi-Far, R. (2025). Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets. arXiv preprint arXiv:2503.17502 [link](https://www.researchgate.net/publication/390143194_Large_Language_Models_LLMs_for_Source_Code_Analysis_applications_models_and_datasets)

- Fang, C., Miao, N., Srivastav, S., Liu, J., Zhang, R., Fang, R., ... & Homayoun, H. (2024). Large language models for code analysis: Do {LLMs} really do their job?. In 33rd USENIX Security Symposium (USENIX Security 24) (pp. 829-846) [link](https://www.usenix.org/system/files/sec24fall-prepub-2205-fang.pdf)

- Backström, O., & Kihlert, A. (2023). Code Quality and Large Language Models in Computer Science Education: Enhancing student-written code through ChatGPT [link](https://www.diva-portal.org/smash/get/diva2:1779791/FULLTEXT01.pdf)

</details>




## Project 3

<details>
    <summary> Helpdesk bazat pe LLM personalizate pentru MateInfo-UBB ()
<img src="projects/RAG.png" width="120"> </summary>

### Sistem automat pentru helpdesk bazat pe LLM

#### Scop
Dezvoltarea unui sistem inteligent care să poată să răspundă la întrebări folosind un LLM și o colecție de documente. 
Se doreste "specializarea" sistemului pentru intrebari din lumea informaticii/financiara.  

#### Ideea de baza

Dezvoltarea unui sistem de tip Retrieval-Augmented Generation (RAG) care să poată să răspundă la întrebări folosind un LLM și o colecție de documente. Sistemul va folosi un model de tip RAG pentru a căuta în colecția de documente și a genera răspunsuri la întrebările utilizatorilor. Se vor compara mai multe strategii de indexare/vectorizare (TF-IDF, embeddings, etc.), mai multe modele de LLMs (pre-trained si fine-tuned), mai multe metode de re-ranking pentru selectia documentelor,  mai multe metode de evaluare a raspunsurilor (evaluare umana si evaluare automata).


#### Data

- Public data [link](https://github.com/MoritzLaurer/rag-demo/tree/master)
- Private data - by request


#### Bibliografie

RAG backgrounds
- RAG demo [link](https://github.com/MoritzLaurer/rag-demo/tree/master)
- Example of building a RAG with LangChain [link](https://python.langchain.com/docs/tutorials/rag/)
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in neural information processing systems, 33, 9459-9474 [link](https://arxiv.org/pdf/2005.11401)
- Better Customer Support Using Retrieval-Augmented Generation (RAG) at Thomson Reuters [link](https://medium.com/tr-labs-ml-engineering-blog/better-customer-support-using-retrieval-augmented-generation-rag-at-thomson-reuters-4d140a6044c3)
- Survey of different RAG systems [link](https://www.youtube.com/watch?v=mE7IDf2SmJg)
- RAG from scratch [link](https://www.freecodecamp.org/news/mastering-rag-from-scratch/)

Re-ranking: cross-ncoders, bi-encoders, multi-vector models, transformer-based rerankers (TinyBERT), graph-based rerankers (Graph Neural Networks)
- Lee, J., Bernier-Colborne, G., Maharaj, T., & Vajjala, S. (2024, June). Methods, Applications, and Directions of Learning-to-Rank in NLP Research. In Findings of the Association for Computational Linguistics: NAACL 2024 (pp. 1900-1917) [link](https://aclanthology.org/2024.findings-naacl.123.pdf)
- Abdallah, A., Piryani, B., Mozafari, J., Ali, M., & Jatowt, A. (2025). How Good are LLM-based Rerankers? An Empirical Analysis of State-of-the-Art Reranking Models. arXiv preprint arXiv:2508.16757 [link](https://arxiv.org/abs/2508.16757)
- Déjean, H., Clinchant, S., & Formal, T. (2024). A thorough comparison of cross-encoders and LLMs for reranking SPLADE. arXiv preprint arXiv:2403.10407 [link](https://arxiv.org/html/2403.10407v1)

LLM-based evaluation
- Liu, Y., Iter, D., Xu, Y., Wang, S., Xu, R., & Zhu, C. (2023). G-eval: NLG evaluation using gpt-4 with better human alignment. arXiv preprint arXiv:2303.16634 [link](https://arxiv.org/abs/2303.16634)
- Shen, C., Cheng, L., Nguyen, X. P., You, Y., & Bing, L. (2023). Large language models are not yet human-level evaluators for abstractive summarization. arXiv preprint arXiv:2305.13091 [link](https://arxiv.org/abs/2305.13091)

</details>

## Project 4

<details>
    <summary> Identificarea cancerului de plaman  (owner: dl. dr. Andrei Roman, Nicolas Musat, nicolasmusat12@hotmail.com) 
    <img src="projects\lungCancer.jpeg" width="100">
    </summary>

### Identificarea cancerului de plaman

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de plămân.

#### Ideea de baza

Deși cancerul pulmonar este recunoscut ca fiind cel mai mortal tip de cancer, un prognostic bun și un tratament eficient depind de detectarea timpurie a acestuia. Povara medicilor poate fi redusa cu ajutorul tehnicilor de AI care sunt esențiale în automatizarea diagnosticului și clasificării bolilor. De aceea, se dorește dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de plămân. 

Se va urmari dezvoltarea unor modele inteligente capabine sa analizeze scanarile CT/PET si sa prezica diferiti biomarkeri tumorali folosind doar:
- 3D Segmented CT scans (maybe PET)
- Biopsy confirmed IHC markers (maybe genomic too)
- Age
- Gender
Scopul este construirea unei "biopsii virtuale" care să sprijine radiologii în timpul diagnosticului. 

Problema poate fi abordata ca o problema de clasificare multi-label. 



#### Data

- Chest CT-scane images [link](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images/data)
- Lung Image Database Consortium image collection (LIDC-IDRI) [link](https://www.cancerimagingarchive.net/collection/lidc-idri/)

#### Bibliografie

- Shao J, Ma J, Zhang S, Li J, Dai H, Liang S, Yu Y, Li W, Wang C. Radiogenomic System for Non-Invasive Identification of Multiple Actionable Mutations and PD-L1 Expression in Non-Small Cell Lung Cancer Based on CT Images. Cancers. 2022; 14(19):4823 [link](https://doi.org/10.3390/cancers14194823)
- Owens CA, Peterson CB, Tang C, Koay EJ, Yu W, et al. (2018) Lung tumor segmentation methods: Impact on the uncertainty of radiomics features for non-small cell lung cancer. PLOS ONE 13(10): e0205003 [link](https://doi.org/10.1371/journal.pone.0205003)
- Majumder S, Katz S, Kontos D, Roshkovan L. State of the art: radiomics and radiomics-related artificial intelligence on the road to clinical translation. BJR Open. 2023 Dec 12;6(1):tzad004. doi: 10.1093/bjro/tzad004. PMID: 38352179; PMCID: PMC10860524.
- Liu, J. A., Yang, I. Y., & Tsai, E. B. (2022). Artificial intelligence (AI) for lung nodules, from the AJR special series on AI applications. American Journal of Roentgenology, 219(5), 703-712. [link](https://ajronline.org/doi/10.2214/AJR.22.27487) 
- Gu, Y., Chi, J., Liu, J., Yang, L., Zhang, B., Yu, D., ... & Lu, X. (2021). A survey of computer-aided diagnosis of lung nodules from CT scans using deep learning. Computers in biology and medicine, 137, 104806. [link](https://www.sciencedirect.com/science/article/pii/S0010482521006004?casa_token=qhi8cSHcd5UAAAAA:iUwm4l441GNq0Ph2QQ8gW5tConmiyHUtm6ynRLEi1b7Io2HdL6qI0hSggNQPfHWn16XeO4FDNQ#sec4)
- Javed, R., Abbas, T., Khan, A. H., Daud, A., Bukhari, A., & Alharbey, R. (2024). Deep learning for lungs cancer detection: a review. Artificial Intelligence Review, 57(8), 197. [link](https://link.springer.com/article/10.1007/s10462-024-10807-1)
- Shatnawi, M. Q., Abuein, Q., & Al-Quraan, R. (2025). Deep learning-based approach to diagnose lung cancer using CT-scan images. Intelligence-Based Medicine, 11, 100188. [link](https://www.sciencedirect.com/science/article/pii/S2666521224000553#bib41)
- Hiraman, A., Viriri, S., & Gwetu, M. (2024). Lung tumor segmentation: a review of the state of the art. Frontiers in Computer Science, 6, 1423693. [link](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1423693/full)
- Jayaram, J., Haw, S. C., Palanichamy, N., Anaam, E., & Kumar, S. (2025). A Systematic Review on Effectiveness and Contributions of Machine Learning and Deep Learning Methods in Lung Cancer Diagnosis and Classifications. International Journal of Computing, 17(1), 1-12. [link](https://iiict.uob.edu.bh/IJCDS/papers/1571032811.pdf)


</details>

## Project 5
<details>
    <summary> Identificarea cancerului de san  (owner: dl. dr. Andrei Roman, dr. Cristiana Moroz-Dubenco, cristiana.moroz@ubbcluj.ro) 
        <img src="projects\breastCancer.jpeg" width="100">
    </summary>

### Identificarea cancerului de san

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de san.

#### Ideea de baza
Detectarea cancerului de sân în mamografii este o problemă critică în imagistica medicală și diagnostic. Interpretarea mamografiilor este provocatoare din cauza variațiilor în densitatea țesuturilor, a structurilor suprapuse și a diferențelor subtile dintre tumorile benigne și maligne. 
Această problemă trebuie rezolvată folosind un algoritm inteligent, deoarece examinarea manuală tradițională de către radiologi este consumatoare de timp și predispusă la erori umane. 

Plecand de la seturile de date cu mamografii, se vor folosii modele de AI bazate pe arhitecturi de tip Transformer/GNN pentru a identifica tumori maligne si benigne in imagini. Modelele folosite pot fi pre-antrenate pe alte seturi de date si fine-tunate pe setul de date cu mamografii.


#### Data
- MIAS [link](http://peipa.essex.ac.uk/info/mias.html)
- DDSM [link](http://www.eng.usf.edu/cvprg/Mammography/Database.html) or [link](https://www.cancerimagingarchive.net/collection/cbis-ddsm/)
- INbreast  [link](https://www.kaggle.com/datasets/tommyngx/inbreast2012)
- DBT - [link](https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/)

#### Bibliografie

- Graph CNNs 
    - PyG [link](https://github.com/pyg-team/pytorch_geometric) 
    - Graph Learning resources [link](https://snap.stanford.edu/graphlearning-workshop/)
    - GNNs for breast cancer - Chowa, S. S., Azam, S., Montaha, S., Payel, I. J., Bhuiyan, M. R. I., Hasan, M. Z., & Jonkman, M. (2023). Graph neural network-based breast cancer diagnosis using ultrasound images with optimized graph construction integrating the medically significant features. Journal of Cancer Research and Clinical Oncology, 149(20), 18039-18064. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC10725367/)
    - GNNs for breast cancer -  Agyekum, E. A., Kong, W., Ren, Y. Z., Issaka, E., Baffoe, J., Xian, W., ... & Shen, X. (2025). A comparative analysis of three graph neural network models for predicting axillary lymph node metastasis in early-stage breast cancer. Scientific Reports, 15(1), 13918. [link](https://www.nature.com/articles/s41598-025-97257-z)
- Transformers
    - Vit - Dosovitskiy, A. (2020). An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929.
        [link](https://arxiv.org/pdf/2010.11929)
        - Code [link](https://github.com/google-research/vision_transformer) or HuggingFace models [link](https://huggingface.co/docs/transformers/en/model_doc/vit)
    - CrossViT - Chen, C. F. R., Fan, Q., & Panda, R. (2021). Crossvit: Cross-attention multi-scale vision transformer for image classification. In Proceedings of the IEEE/CVF international conference on computer vision (pp. 357-366). [link](https://openaccess.thecvf.com/content/ICCV2021/papers/Chen_CrossViT_Cross-Attention_Multi-Scale_Vision_Transformer_for_Image_Classification_ICCV_2021_paper.pdf)
        - Code [link](https://github.com/IBM/CrossViT)
    - DeiT - Touvron, H., Cord, M., Douze, M., Massa, F., Sablayrolles, A., & Jégou, H. (2020). Training data-efficient image transformers & distillation through attention. arXiv 2020. arXiv preprint arXiv:2012.12877, 2(3). \href{https://arxiv.org/abs/2012.12877v2}{link}
        - Code [link](https://github.com/facebookresearch/deit/tree/2aefd8fc8634d099c1495ce9dba2b6c6a921d611)
    - MammoViT - Al Mansour, A. G., Alshomrani, F., Alfahaid, A., & Almutairi, A. T. (2025). MammoViT: A Custom Vision Transformer Architecture for Accurate BIRADS Classification in Mammogram Analysis. Diagnostics, 15(3), 285 [link](https://www.mdpi.com/2075-4418/15/3/285)
    - Gutierrez-Cardenas, J. (2024). Breast Cancer Classification Through Transfer Learning with Vision Transformer, PCA, and Machine Learning Models. International Journal of Advanced Computer Science & Applications, 15(4). [link](https://www.proquest.com/docview/3060148581?fromopenview=true&pq-origsite=gscholar&sourcetype=Scholarly%20Journals)

</details>




## Project 6
<details>
    <summary> Voice to text  (owner: dna. dr. Alina Baciu) 
    <img src="projects\voice.avif" width="150">
    </summary>

### Automatizarea intocmirii fisei pacientului

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii pentru a completa in mod automat fisa pacientului.

#### Ideea de baza

Munca medicilor este plina de provocari. Mai ales cand trebuie sa faca multe task-uri, uneori simultan, precum realizarea si citirea unei ecografii si inregistrarea observatiilor facute. De aceea este nevoie de un sistem inteligent care sa transforme informatia audio inregistrata de catre un medic in format text si sa completeze in mod automat rubricile dedicate din fisa pacientului.
Se va pleca de la inregistrari audio precum [aceasta](projects/voice2text/test1.ogg), se vor converti in format text si se va compelta automat partea evidentiata cu galben din fisa pacientului, precum [aceasta](projects/voice2text/patient1.odt) (informatiile respective se vor salva intr-un tabel/jason si apoi se vor exporta intr-un document word)



#### Data

- inregistrari audio [link](projects/voice2text/test1.ogg) [link](projects/voice2text/test2.ogg) [link](projects/voice2text/test3.ogg)
- fisa pacientului [link](projects/voice2text/patient1.odt)
 
#### Bibliografie

- [Whisper](https://openai.com/index/whisper/)
- [DeepSpeech](https://github.com/mozilla/DeepSpeech)
- [RobinASR](https://github.com/racai-ai/RobinASR) - for romanian
- [speech2text](https://huggingface.co/docs/transformers/model_doc/speech_to_text)
- [wav2vec](https://ai.meta.com/research/impact/wav2vec/)
- [wav2vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2)
- [romanian wav2vec2](https://huggingface.co/gigant/romanian-wav2vec2)
- [wavLM](https://huggingface.co/docs/transformers/model_doc/wavlm)



</details>

## Project 7
<details>
    <summary> Estimarea dificultatii cazurilor stomatologice (owner: dna. dr. Mihaela Hedesiu) 
    <img src="projects\endodontie.webp" width="100"> </summary>

### Identificarea dificultatii cazului de endodontie

#### Scop
Dezvoltarea unui sistem inteligent care sa estimeze dificultatea cazului de endodontie (daca trebuie trimis spre specialist sau nu). Diferentierea intre un tratament endodontic corect si unul incorect. Oferirea unui scor de corectitudine al tratamentului. 

#### Ideea de baza
Tratamentul endodontic presupune curățarea, modelarea și obturarea canalelor radiculare pentru prevenirea sau tratarea parodontitei apicale. Deși are o rată de succes ridicată (82–92%), pot apărea eșecuri cauzate de erori procedurale precum perforații apicale, blocaje sau obturații incorecte, care pot duce la complicații postoperatorii și pierderea dintelui. 
Complexitatea anatomică a coroanei și a canalelor radiculare crește riscul acestor erori, motiv pentru care evaluarea preoperatorie corectă și trimiterea cazurilor dificile către specialiști sunt esențiale. Ghidurile AAE oferă criterii standardizate pentru evaluarea dificultății, dar aplicarea lor manuală este consumatoare de timp și subiectivă.

Inteligența artificială promite automatizarea acestor evaluări. Studiul propus urmărește dezvoltarea unui instrument de diagnostic bazat pe radiografii periapicale, folosind deep learning pentru evaluarea standardizată a dificultății cazurilor endodontice.



#### Data

 
#### Bibliografie



</details>

## Project 8


<details>
    <summary> Causality identification (owner: dl. dr. Dan Blendea, dblendea1@gmail.com)  <img  style="vertical-align:middle" src="projects\causality.jpeg" alt="networks" width="100"/></summary>

### Scop
Identificarea cauzelor insuficientei mitrale [link](../../2024-2025/Projects/variabilitate.pdf)


### Ideea de baza

Plecand de la o ecografie cardiaca (in format DICOM) se doreste identificarea cauzelor insuficientei mitrale (Mitral Regurgitation - MR). Se va folosi un model AI bazat pe Graph-based CNN care va analiza ecografia, iar pe baza masuratorilor (volumul MR, volumul ventriculului stang, volumul atriului stang, volumul inelului mitral, etc) si vor identifica interdependentele existente intre aceste masuratori (efectuate de-a lungul a mai multe cicluri cardiace). [more details](variabilitate.pdf)



### TODOlist
1. Se va analiza evolutia individuala a masuratorilor in timp (pe parcursul mai multor cicluri cardiace) 
2. se va identifica interdependentele existente intre aceste masuratori
3. Se va dezvolta un model de estimare a cauzelor insuficientei mitrale pe baza masuratorilor ecografice si a interdependentelelor identificate


### Data
- tiny dataset [link](../../2025-2026/Projects/pacienti.xlsx)


### Bibliografie

- Jure Leskovec's lecture [link](https://web.stanford.edu/class/cs224w/index.html#schedule) and [package](https://www.pyg.org/)
- PyTorch geometric [library](https://pytorch-geometric.readthedocs.io/en/latest/) [docs1](https://arxiv.org/pdf/1903.02428) [docs2](https://proceedings.neurips.cc/paper_files/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf)
- Neural Granger Causality [link](https://github.com/harpoonix/GC-xLSTM)
- Causality inspired GNNs [link](https://github.com/usail-hkust/Awesome-Causality-Inspired-GNNs)
- GNN for causality [link](https://arxiv.org/abs/2407.09378)
- Wang, L., Adiga, A., Chen, J., Sadilek, A., Venkatramanan, S., & Marathe, M. (2022, June). Causalgnn: Causal-based graph neural networks for spatio-temporal epidemic forecasting. In Proceedings of the AAAI conference on artificial intelligence (Vol. 36, No. 11, pp. 12191-12199). [link](https://arxiv.org/pdf/2312.12477)

</details>



## Project 9

<details>
    <summary> Medical dataset generation (owner: Mihai Nadas, mihai.nadas@ubbcluj.ro)  <img  style="vertical-align:middle" src="projects\medicalData.jpg" alt="networks" width="100"/></summary>

### Scop
Dezvoltarea unui corpus medical în limba română 

### Ideea de baza

Dezvoltarea unui corpus medical în limba română poate susține cercetarea în domeniul NLP medical. Se vor colecta, genera și structura date, apoi se vor testa modele de inteligență artificială pe sarcini precum extragerea simptomelor sau codificarea ICD-10. Proiectul se bazează pe o metodologie recentă aplicată în generarea de fabule [link](https://arxiv.org/pdf/2504.20605?), adaptată pentru domeniul medical.



### TODOlist
1. Colectare și curățare date reale
- Surse: articole științifice, ghiduri clinice, materiale educaționale, rapoarte publice.
- Activități: scraping, OCR (dacă e cazul), curățare lingvistică, anonimizare.

2. Definirea schemelor de reprezentare
- Structuri pentru note clinice, conversații, rezumate.
- Exemple: [Pacient] are simptome de ..., [Doctor] recomandă tratament cu ..., etc.

3. Generare sintetică (prompt engineering + LLM)
- Crearea de prompturi pentru generarea de texte medicale realiste.
- Validarea calității și diversității textelor generate.
- Posibilă utilizare de modele open-source (ex: LLaMA, Mistral) sau API-uri comerciale.

4. Structurare corpus final
- Organizare pe tipuri de documente.
- Etichetare (manuală sau automată) pentru sarcini NLP.

5. Aplicații NLP
- Extragere de simptome: NER medical.
- Codificare ICD-10: clasificare text.
- Sumarizare tratamente: modele de sumarizare extractivă/abstractivă.

### Data
- A list of Romanian NLP Datasets [link](https://github.com/AndyTheFactory/romanian-nlp-datasets)

- English-Romanian Medical Domain Parallel Corpora [link](https://www.futurebeeai.com/dataset/text-dataset/romanian-english-translated-parallel-corpus-for-medical-domain)

- Li, Y., Wu, S., Smith, C., Lo, T., & Liu, B. (2025, June). Improving clinical note generation from complex doctor-patient conversation. In Pacific-Asia Conference on Knowledge Discovery and Data Mining (pp. 209-221). Singapore: Springer Nature Singapore [link](https://arxiv.org/html/2408.14568v1)

### Bibliografie

Laparra, E., Mascio, A., Velupillai, S., & Miller, T. (2021). A review of recent work in transfer learning and domain adaptation for natural language processing of electronic health records. Yearbook of medical informatics, 30(01), 239-244 [link](https://www.thieme-connect.com/products/ejournals/pdf/10.1055/s-0041-1726522.pdf)

Mitrofan, M., & Tufiş, D. (2018, May). Bioro: The biomedical corpus for the romanian language. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018) [link](https://aclanthology.org/anthology-files/pdf/L/L18/L18-1191.pdf)

Mitrofan, M., Mititelu, V. B., & Mitrofan, G. (2019, August). Monero: a biomedical gold standard corpus for the romanian language. In Proceedings of the 18th BioNLP Workshop and Shared Task (pp. 71-79) [link](https://aclanthology.org/W19-5008.pdf)

Midrigan-Ciochina, L., Boyd, V., Sanchez-Ortega, L., Malancea_Malac, D., Midrigan, D., & Corina, D. P. (2020, May). Resources in underrepresented languages: Building a representative romanian corpus. In Proceedings of the Twelfth Language Resources and Evaluation Conference (pp. 3291-3296) [link](https://aclanthology.org/2020.lrec-1.402.pdf)

Nitu, M., & Dascălu, M. (2022). Natural Language Processing Tools for Romanian–Going Beyond a Low‑Resource Language. Interaction Design & Architecture (s), special issue. DOI, 10 [link](https://ixdea.org/wp-content/uploads/IxDEA_art/60/60_SP_1.pdf)

OpenLLM-Ro [link](https://openllm.ro/)

</details>


## Project 10

<details>
    <summary> Legal dataset generation (owner: Mihai Nadas, mihai.nadas@ubbcluj.ro)  <img  style="vertical-align:middle" src="projects\medicalData.jpg" alt="networks" width="100"/></summary>

### Scop
Dezvoltarea unui corpus de documente juridice 

### Ideea de baza

Construirea celui mai mare corpus de documente juridice românești (legi, hotărâri judecătorești, contracte, documente notariale), completat cu date sintetice. Pe baza acestuia, se pot antrena și evalua modele de limbaj de dimensiuni mici/medii, cu aplicații în clasificarea clauzelor contractuale, extragerea de entități sau sumarizare juridică.


### TODOlist
1. Colectare și curățare date reale

2. Definirea schemelor de reprezentare

3. Generare sintetică (prompt engineering + LLM)

4. Structurare corpus final

5. Aplicații NLP


### Data
- A list of Romanian NLP Datasets [link](https://github.com/AndyTheFactory/romanian-nlp-datasets)



### Bibliografie

motor de cautare juridic [link](https://www.wolterskluwer.com/ro-ro/solutions/sintact/Jurisprudenta-Hotarari-Judecatoresti)

portal legislativ [link](https://legislatie.just.ro/)

OpenLLM-Ro [link](https://openllm.ro/)

Midrigan-Ciochina, L., Boyd, V., Sanchez-Ortega, L., Malancea_Malac, D., Midrigan, D., & Corina, D. P. (2020, May). Resources in underrepresented languages: Building a representative romanian corpus. In Proceedings of the Twelfth Language Resources and Evaluation Conference (pp. 3291-3296) [link](https://aclanthology.org/2020.lrec-1.402.pdf)

Nitu, M., & Dascălu, M. (2022). Natural Language Processing Tools for Romanian–Going Beyond a Low‑Resource Language. Interaction Design & Architecture (s), special issue. DOI, 10 [link](https://ixdea.org/wp-content/uploads/IxDEA_art/60/60_SP_1.pdf)


</details>

## Project 11

<details>
    <summary> Early Discovery of Anxiety/Depression in Teenagers Using Digital Tools (Owner: Cristiana Bogateanu, cristiana.bogateanu@nagarro.com)  <img style="vertical-align:middle" src="images\anxiety.jpeg" alt="networks" width="100"/> </summary>

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


## Project 12

<details>
    <summary>   Digital Triage System (Owner: Cristiana Bogateanu, cristiana.bogateanu@nagarro.com) <img style="vertical-align:middle" src="images\triage.jpeg" alt="networks" width="100"/> </summary>

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




## Project 13
<details>
    <summary>  Real-Time Scene-Aware Assistant for Blind People using TinyVLM  (Owner: Mohamed Hassan, Bosch, Hassan.Mohamed@ro.bosch.com)  <img  style="vertical-align:middle" src="images\elderly.jpeg" alt="networks" width="100"/> </summary>

### Scop

Asistent conștient de scenă în timp real pentru persoanele nevăzătoare, utilizând TinyVLM – sau cazuri de utilizare și soluții adiacente

Acesta oferă asistență prin generarea de descrieri ale scenei, inclusiv elemente dinamice și scenarii complexe, ajutând persoanele nevăzătoare să interacționeze mai complet cu mediul înconjurător.

 

### Ideea de baza
Proiectul propune dezvoltarea unui sistem inteligent de asistență vizuală destinat persoanelor nevăzătoare, utilizând TinyVLM – un model eficient de tip Vision-Language, optimizat pentru dispozitive cu resurse limitate. Sistemul are capacitatea de a analiza în timp real mediul înconjurător și de a genera descrieri detaliate și relevante în limbaj natural, facilitând astfel o interacțiune mai sigură și mai autonomă cu spațiul din jur. 
Modelul este capabil să interpreteze scene complexe, să identifice elemente dinamice și să răspundă la întrebări vizuale, oferind suport în activități precum navigarea urbană, orientarea în spații necunoscute sau evitarea obstacolelor. 

Soluția propusă valorifică avantajele TinyVLM – dimensiune redusă, eficiență computațională și capacitate de raționament vizual – pentru a crea un instrument accesibil, scalabil și ușor de integrat în viața de zi cu zi a persoanelor cu deficiențe de vedere. Proiectul are un puternic impact social, contribuind la incluziunea digitală și la îmbunătățirea calității vieții prin tehnologii AI de ultimă generație.
 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data

- SANPO [link](https://research.google/blog/sanpo-a-scene-understanding-accessibility-navigation-pathfinding-obstacle-avoidance-dataset/)

- merged dataset [link](https://huggingface.co/datasets/mlevytskyi/blind-people-scene-descriptions)


### Bibliografie
- Vision Language Models (VLMs) [link1](https://www.nvidia.com/en-us/glossary/vision-language-models/) [link2](https://huggingface.co/blog/vlms) [link3](https://huggingface.co/blog/vlms-2025)
- Tiny VLM [paper(https://openreview.net/pdf?id=lVIkk8p6RN) [code](https://github.com/anananan116/TinyVLM)



</details>


## Project 14
<details>
    <summary>  Monitorizarea stării de sănătate cu ajutorul SmartWatch (Owner: Zoltan Balint, zoltan.balint@ubbcluj.ro) <img  style="vertical-align:middle" src="images\smartWatch.png" alt="networks" width="100"/> </summary>

### Scop

Brățările de fitness și ceasurile inteligente purtate la încheietură, bazate pe accelerometru, au apărut pe piața de consum în 2011. De atunci, au fost lansate numeroase dispozitive purtabile. Pe lângă utilizarea lor pentru monitorizarea activității fizice personale, aceste dispozitive sunt tot mai des folosite în cercetare pentru colectarea de date de sănătate. Sunt concepute pentru utilizare pe termen lung, ceea ce permite înregistrarea continuă cu un efort minim din partea participanților. Proiectul urmărește explorarea potențialului datelor colectate de ceasuri inteligente și dispozitive purtabile în domeniul sănătății, prin aplicarea tehnicilor de Business Intelligence (BI).

### Ideea de baza
Proiectul urmărește utilizarea tehnicilor de Business Intelligence (BI) pentru analiza datelor colectate de dispozitive purtabile (ex. ceasuri inteligente). Scopul este extragerea de informații relevante pentru sănătatea utilizatorului, precum nivelul de activitate fizică, calitatea somnului, ritmul cardiac și localizarea, și transformarea acestora în insight-uri utile pentru intervenții personalizate.
 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data

- [link](https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-022-06146-5
https://www.researchgate.net/publication/378021834_Analysis_of_Fitness_Based_on_Smart_Watch_Data)

- [link](https://ceur-ws.org/Vol-3514/paper73.pdf)


### Bibliografie

Mogra, A., Pandey, P. K., & Panwar, R. S. (2024, December). Artificial Intelligence Enabled Sleep Health Dashboards: Power BI Integration for Data-Driven Lifestyle Modifications. In 2024 Eighth International Conference on Parallel, Distributed and Grid Computing (PDGC) (pp. 535-539). IEEE [link](https://ieeexplore.ieee.org/abstract/document/10984363)

Reddy, N. C. N., Ramesh, A., Rajasekaran, R., & Masih, J. (2020, May). Ritchie’s Smart Watch Data Analytics and Visualization. In International Conference on Image Processing and Capsule Networks (pp. 776-784). Cham: Springer International Publishing.[link](https://d1wqtxts1xzle7.cloudfront.net/96645011/978-3-030-51859-2_70-libre.pdf?1672579590=&response-content-disposition=inline%3B+filename%3DRitchie_s_Smart_Watch_Data_Analytics_and.pdf&Expires=1759213247&Signature=QSkC1ZZ1hezkhPx2bnqrWfikyhAPRw8R83lYHOrsKW2GA4nfVd~kOZ-RvFPbNCPPnK9x6b66MnJYvnR1VElnEt~Nn8dsjHjiR4WpKMJ8KhfpSqKeoPoEmTSPtTo57lcLSAyLr7XL0tbdk5YpxUrrK6GcHpG7YTfUrOu9Xh2lxi~-V1DOXFkhtHqw9wtWGoniLusVXsLuGaGdQibTMUCEUmV5Cw-fISVvv170AiNH-Lb5z4yZqaunHabVBOBWQ~dhzedn~7G7PPQEdWcIBSXf~uxQDpCfXlzRQ1F-Xh2dBDZFyOru9AxMKgElC6a6f5jMIn6YLQwPTpZBiSgW~YZYEQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

Bhavsar, K., Singhal, S., Chandel, V., Samal, A., Khandelwal, S., Ahmed, N., & Ghose, A. (2021, March). Digital biomarkers: Using smartwatch data for clinically relevant outcomes. In 2021 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops) (pp. 630-635). IEEE. [link](https://ieeexplore.ieee.org/abstract/document/9431000)

Del-Valle-Soto, C., Briseño, R. A., Valdivia, L. J., & Nolazco-Flores, J. A. (2024). Unveiling wearables: exploring the global landscape of biometric applications and vital signs and behavioral impact. BioData Mining, 17(1), 15. [link](https://link.springer.com/content/pdf/10.1186/s13040-024-00368-y.pdf)

</details>
