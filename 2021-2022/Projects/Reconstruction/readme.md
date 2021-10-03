
# Sistem suport pentru asistarea terapiei radiologice <img src="mask.jpg" alt="Thermoplastic mask"/>

## Obiective
Dezvoltarea dispozitivelor de imobilizare și materialelor compensatoare personalizate pentru radioterapie prin procesarea imaginilor și imprimare 3D 


## Ideea de baza
In terapia radiologica a diverselor boli este nevoie de construirea unor masti de protectie a anumitor parti ale corpului (de ex. protejarea fetei). Daca aceste masti respecta cat mai mult fizionomia unui pacient, ele se transforma in aliati siguri ai pacientului, dar si ai medicului in combaterea bolilor si cresterea gradului de securitate a organelor care nu trebuie iradiate. 

Constructia unei masti se poate adapta specificului unui pacient, respectand trasaturile fetei. In acest context se doreste dezvoltarea unei aplicatii care pe baza imaginii fetei unei persoane sa poata extrage caracteristicile faciale si sa frunizeze un model 3D a acestora.





## TO DO List
1. Dezvoltare flow principal pentru aplicatie 
- Incarcare si vizualizare imagine originala a unui pacient
- Incarcare si vizualizare masca faciala 
2. Dezvoltare componenta inteligenta
- Antrenarea si validarea unei metode inteligente de identificare automata a trasaturilor faciale 
- Dezvoltarea unui model 3D asociat mastii corespunzatoare trasaturilor faciale
- Imprimarea 3D a mastilor construite si validarea lor in laborator - studiu clinic
3. Imbunatatire componenta inteligenta
- Din perspectiva calitatii procesului de invatare automata
- Din perspectiva complexitatii temporale si spatiale aferenta clasificatorului
- Din perspectiva clientului (utilizarii aplicatiei de catre student/arheolog)


## Date si referinte
**Date si biblioteci**
1. DLib http://blog.dlib.net/2014/08/real-time-face-pose-estimation.html
2. MediaPipe https://google.github.io/mediapipe/solutions/face_mesh.html
3. 300-w https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/
4. HELEN http://www.ifp.illinois.edu/~vuongle2/helen/
5. https://paperswithcode.com/task/facial-landmark-detection


**Metode de lucru**
1. Michael K. Three-dimensional printing in radiation oncology: A systematic review of the literature 2020
2. Lattas, A., Moschoglou, S., Gecer, B., Ploumpis, S., Triantafyllou, V., Ghosh, A., & Zafeiriou, S. (2020). AvatarMe: Realistically Renderable 3D Facial Reconstruction" In-the-Wild". In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 760-769).
3. Guo, J., Zhu, X., Yang, Y., Yang, F., Lei, Z., & Li, S. Z. (2020). Towards fast, accurate and stable 3d dense face alignment. In Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XIX 16 (pp. 152-168). Springer International Publishing
4. Kazemi, V., & Sullivan, J. (2014). One millisecond face alignment with an ensemble of regression trees. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 1867-1874).



