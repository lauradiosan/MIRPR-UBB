


| Etapa |  Cerinta app | Punctaj app| Cerinta raport | Punctaj raport | Termen |
| :--- | :--- | :---: | :--- |:---: |:---: |
| 1 | flow-ul de baza   | 10    | descriere functionalitati  ale aplicatiei,  <br/>  descriere (plastica si formala) a problemei rezolvate cu ajutorul AI  <br/>  related work & useful tools and technologies | 5 | Lab 2 |
| 2 | algoritm inteligent + small data | 5 | descriere algoritm inteligent, descriere metodologie experimentala si rezultate obtinute	| 5 | Lab3 |	
| 3| algoritm inteligent + real data / benchmark data | 5 | descriere metodologie experimentala, rezultate obtinute, comparare cu SOTA	| 5 | Lab4 |	
| 4 | imbunatatirea algoritmului inteligent   | 10 | descrierea imbunatatirilor (metodologie si rezultate, analize comparative) | 10 | Lab 5 |
| 5 | integrare model inteligent in aplicatie (5p); <br/> noi imbunatatiri (...);<br/> teaser video de prezentare a proiectului (5p) | 10 |  descrierea si analiza (statistica a) rezultatelor obtinute (5p);  <br/> suport prezentare / slides - draft (5p)| 10 | Lab 6 |
| 6 | demo cu client(i) = pitch + demo app | 10 | analiza SWOT a proiectului realizat si concluzii; <br/> suport prezentare / slides - versiune finala | 10 | Lab7 |

Bonus: Concursuri sau articole stiintifice sau interventii notabile de-a lungul activitatii.


| Punctaj total | Nota |
| :--- | :---: | 
| >99 | 10 |
| [90, 99] |  9 |
| [70, 89] | 8 |
| [50, 69] | 7 |
| [40, 49] | 6 |
| [30, 39] | 5 |
| < 30 | 4 |

Nota: se accepta intarziere de maxim 2 saptamani in predarea temelor, caz in care se va aplica o penalizare de 20% din punctajul aferent temei.

Detalii etape:
<details>
    <summary> 1. Flow-ul de baza al aplicatiei </summary>

- Functionalitati de baza ale aplicatiei - o app simpla care va integra AI-ul; pentru moment "predictia facuta de AI" e hard-codata manual (la final se va inlocui cu cel mai bun model obtinut)
- Descrierea problemei rezolvate cu ajutorul AI (plastica si formala) - ce anume se rezolva, de ce e important, cine sunt utilizatorii, care sunt datele de intrare si iesire (ce tip de date se utilizeaza), cum se masoara performanta rezolvarii prolemei cu AI-ul
- Related work & useful tools and technologies - se vor descrie pe scurt cel putin 2 * n (n e nr de membrii ai echipei) lucrari relevante (articole, bloguri, proiecte open-source) care au legatura cu problema rezolvata: se vor urmari detalii precum: 
    - ce date s-au folosit, 
    - ce algoritmi de AI s-au folosit
    - ce performante s-au obtinut 
    - ce librarii/tehnologii s-au folosit si daca ofera Git-ul aferent abordarii propuse
</details>

<details>
    <summary> 2. Algoritm inteligent + small data </summary>

- se va cauta un set de date mic care sa fie relevant pentru problema propusa - de preferat un set de date real dar mic (ex: 100-200 de exemple); se va descrie sursa datelor si modul in care au fost colectate; daca se foloseste un set de date real, se vor respecta toate regulile etice si legale privind utilizarea datelor (ex: GDPR, drepturi de autor, etc.)
- se va alege un algoritm de AI (machine learning/deep learning) care sa rezolve problema propusa; se va implementa si antrena un model folosind un set mic de date (small data) - de exemplu, un set de date sintetic, sau un set de date real dar mic (ex: 100-200 de exemple); se poate porni antrenarea de la 0 sau se poate folosi transfer learning (pornind de la un model pre-antrenat pe un set de date similar cu cel folosit in proiect)
- descriere si scurta EDA a datelor
- Descriere algoritm inteligent - se va descrie pe scurt algoritmul ales, motivatia alegerii lui, librariile folosite, etc.
- Descriere metodologie experimentala si rezultate obtinute - se vor descrie detalii precum: 
    - cum s-a impartit setul mic de date (train/val/test), 
    - ce metrici s-au folosit pentru evaluare, 
    - ce hiperparametri s-au folosit, 
    - ce rezultate s-au obtinut (metrici + cateva exemple corect/gresit prezise)
</details>

<details>
    <summary> 3. Algoritm inteligent + real data / benchmark data </summary>

- se va re-folosi setul de date de la pasul2 (dar tot setul) sau se va cauta un set mare de date
- se va relua etapa 2, dar se va folosi un set de date real (de preferat benchmark) pentru antrenarea si testarea modelului; se poate porni antrenarea de la 0 sau se poate folosi transfer learning (pornind de la un model pre-antrenat pe un set de date similar cu cel folosit in proiect)
- descriere si scurta EDA a datelor
- Descriere si documentare metodologie experimentala si rezultate obtinute - se vor descrie detalii precum: 
    - cum s-a impartit setul real de date (train/val/test), 
    - ce metrici s-au folosit pentru evaluare, 
    - ce hiperparametri s-au folosit, 
    - ce rezultate s-au obtinut (metrici + cateva exemple corect/gresit prezise)
- Comparare cu SOTA - se vor compara rezultatele obtinute cu cele din lucrarile relevante descrise la pasul 1
</details>

<details>
    <summary>4. Imbunatatirea algoritmului inteligent </summary>

- se vor face imbunatatiri ale algoritmului inteligent, dpdv a calitatii procesului de rezolvare a problemei (optimizarea AI-ului) si/sau dpdv a complexitatii (complexitatea temporala/spatiala, portabilitatea, etc.); se pot incerca diferite abordari, precum: 
    - schimbarea arhitecturii modelului (ex: mai multe/mai putine straturi, alte tipuri de straturi, etc.)
    - schimbarea hiperparametrilor (ex: rata de invatare, dimensiunea batch-ului, etc.)
    - augmentarea datelor (ex: rotiri, translatii, etc. pentru imagini, SMOTE pentru date tabelare, etc.)
    - folosirea unor tehnici de regularizare (ex: dropout, weight decay, etc.)
    - folosirea unor tehnici de optimizare (ex: Adam, RMSprop, etc.)
    - folosirea unor tehnici de reducere a dimensionalitatii (ex: PCA, t-SNE, etc.)
    - folosirea unor tehnici de ensembling (ex: bagging, boosting, stacking, etc.)
- se vor analiza modelele obtinute pe baza a cel putin 3 criterii:
    - performanta (accuracy, IoU, eroare, loss, etc)
    - dimensiune / viteza 
    - transparenta / capacitate de explicare (explainability - folosind modele precum LIME, SHAP, GradCAM, ProtoNets, etc) 
si se va alege cel mai bun model pentru a fi integrat in aplicatie la pasul 5 
- Descrierea imbunatatirilor (metodologie si rezultate, analize comparative) - se vor descrie detalii precum:
    - ce imbunatatiri s-au facut,
    - cum s-a impartit setul real de date (train/val/test), 
    - ce metrici s-au folosit pentru evaluare, 
    - ce hiperparametri s-au folosit, 
    - ce rezultate s-au obtinut (metrici + cateva exemple corect/gresit prezise)
    - comparatie cu rezultatele obtinute la pasul 3
</details>

<details>
    <summary>5. Integrare model inteligent in aplicatie </summary>

- se va integra si testa cel mai bun model obtinut la pasul 4 in aplicatia dezvoltata la pasul 1 / aplicatia dezvoltata de colegii de la PPI 
- se va realiza un video scurt (1-2 minute) care sa prezinte pe scurt problema rezolvata, solutia propusa, si rezultatele obtinute; se va pune accent pe partea vizuala, astfel incat sa fie atractiv pentru potentiali utilizatori sau clienti
- se vor documenta si analiza noile rezultate obtinute (imbunatatiri)
- se va pregati suportul pentru prezentarea finala (draft); se vor include slide-uri care sa prezinte pe scurt: 
    - problema abordata si provocarile ei, 
    - solutia propusa,
    - rezultatele obtinute - se va pune accent pe partea vizuala, astfel incat sa fie atractiv pentru potentiali utilizatori sau clienti    
</details>

<details>
    <summary>6. Demo cu client(i) = pitch + demo app</summary>

- se va realiza o prezentare (pitch) de 5-10 minute in care se va prezenta pe scurt: 
    - problema abordata si provocarile ei, 
    - solutia propusa,
    - rezultatele obtinute - se va pune accent pe partea vizuala, astfel incat sa fie atractiv pentru potentiali utilizatori sau clienti    
- se va face un demo al aplicatiei dezvoltate, in care se va arata cum functioneaza aplicatia si cum se foloseste modelul inteligent integrat in ea
</details>