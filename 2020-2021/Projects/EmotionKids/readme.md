# Detectia emotiilor in comportamentul prescolarilor  	 <img src="emotionsSmall.png" alt="A cool kid"/>

## Obiective
Identificarea emotiilor pe care le traiesc prescolarii in timp ce folosesc aplicatii educative 


## Ideea de baza
Succesul sau esecul unei aplicatii interactive este determinata de utilizabilitatea produsului. Una din componentele utilizabilitatii este satisfactia utilizatorului. Evaluarea satisfactiei pentru utilizatorii adulti se realizeaza prin observatie, interviuri post-interactiune sau metode cantitative (chestionare) care insa nu pot fi aplicate copiilor prescolari, care au capacitate limitata de autoanaliza si  de comunicare, nu pot citi si nu pot scrie.  Astfel, pe langa observatie (care poate fi subiectiva, depinzand de modul de interpretare a reactiilor prescolarului de catre expertul care realizeaza aplicatia), se doreste o masurare obiectiva a emotiilor pe care le traiesc copiii in timpul interactiunii. Pentru aceasta este nevoie de dezvoltarea unei aplicatii care sa permita identificarea starilor emotionale ale unui prescolar in timpul derularii unei activitati (de ex. 30% din timp a zambit sau asocieri intre sarcini pe care le fac copiii si frecventa unei emotii).


## TO DO list
1. Autentificare utilizator prescolar – pentru ca ei nu stiu sa scrie si sa citeasca este nevoie de un alt mecanism de autentificare (de ex unul bazat pe recunoasterea faciala)
- Antrenarea si validarea unui model de recunoastere facial general (pe o baza de date de tip benchmark)
- Inregistrarea tuturor utilizatorilor/prescolarilor si stocarea imaginilor faciale ale acestora
- Folosirea modelului de recunoastere pentru autentificarea unui prescolar 
2. Inregistrare activitate (prescolar interactioneaza cu calculatorul in timpul activitatii, deci poate fi „urmarit” folosind camera calculatorului) si etichetarea acesteia cu una sau mai multe stari emotionale
- Antrenarea si validarea unui model de recunoastere a emotiilor in imagini/video (pe o baza de date de tip benchmark)
- Antrenarea si validarea unui model de recunoastere a emotiilor in semnale audio (pe o baza de date de tip benchmark)
- Inregistrarea si stocarea activitatii unui prescolar
- Folosirea modelelor de recunoastere a emotiilor pentru etichetarea activitatii inregistrate pentru un anumit prescolar si pentru un grup de prescolari
3. Imbunatatire componente inteligente
- Din perspectiva calitatii procesului de invatare automata
- Din perspectiva complexitatii temporale si spatiale aferenta clasificatorului
- Din perspectiva clientului (utilizarii aplicatiei de catre prescolar in colaborare cu educatoarea/psihologul)

## Date si referinte
**Imagini**
1. Emotii faciale 
- Cohn-Kanade http://www.consortium.ri.cmu.edu/ckagree/
- FER https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview
- CAFE (for kids) link](http://databrary.org/volume/30) https://www.childstudycenter-rutgers.com/the-child-affective-facial-expression-se
- EmoReact (for kids)  [link spre date](http://www.cs.ubbcluj.ro/~lauras/test/docs/school/MIRPR/2019-2020/emoReact.zip) detalii despre date: Nojavanasghari, Behnaz, et al. "EmoReact: a multimodal approach and dataset for recognizing emotional responses in children." Proceedings of the 18th acm international conference on multimodal interaction. ACM, 2016 [link](https://www.behnaznojavan.com/data)
- UBB database [link spre date](http://www.cs.ubbcluj.ro/~lauras/test/docs/school/MIRPR/2019-2020/ubbKids.zip) [date noi](https://photos.app.goo.gl/sSPzhoBQF9n3Nm7cA)


2. Recunoasterea fetei si emotii faciale 
- http://www.consortium.ri.cmu.edu/index.php#projects
3. Emotii in vorbire
- https://zenodo.org/record/1188976#.XYnKuigzY2x

**Metode de lucru**
1. Tarnowski, Paweł, et al. ”Emotion recognition using facial expressions.” Procedia Computer Science 108 (2017): 1175-1184.
Matsuda, Yuki, et al. "Emotour: Estimating emotion and satisfaction of users based on behavioral cues and audiovisual data." Sensors 18.11 (2018): 3978.
2. Singh, Shilpi, and S. V. A. V. Prasad. "Techniques and Challenges of Face Recognition: A Critical Review." Procedia computer science 143 (2018): 536-543.
3. Samadiani, Najmeh, et al. "A review on automatic facial expression recognition systems assisted by multimodal sensor data." Sensors 19.8 (2019): 1863.
4. Singh, Shilpi, and S. V. A. V. Prasad. "Techniques and Challenges of Face Recognition: A Critical Review." Procedia computer science 143 (2018): 536-543.
5. Lu, Chaochao, and Xiaoou Tang. "Surpassing human-level face verification performance on LFW with GaussianFace." Twenty-ninth AAAI conference on artificial intelligence. 2015.
6. Taigman, Yaniv, et al. "Deepface: Closing the gap to human-level performance in face verification." Proceedings of the IEEE conference on computer vision and pattern recognition. 2014.
7. Schroff, Florian, Dmitry Kalenichenko, and James Philbin. "Facenet: A unified embedding for face recognition and clustering." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015.
https://www.faceplusplus.com/
8. El Ayadi, Moataz, Mohamed S. Kamel, and Fakhri Karray. "Survey on speech emotion recognition: Features, classification schemes, and databases." Pattern Recognition 44.3 (2011): 572-587.
9. Kerkeni, Leila, et al. "Automatic Speech Emotion Recognition Using Machine Learning." Social Media and Machine Learning. IntechOpen, 2019.
10. LoBue, Vanessa, and Cat Thrasher. "The Child Affective Facial Expression (CAFE) set: Validity and reliability from untrained adults." Frontiers in psychology 5 (2015): 1532.
11. Lassalle, Amandine, et al. "The EU-Emotion Voice Database." Behavior research methods 51.2 (2019): 493-506.
