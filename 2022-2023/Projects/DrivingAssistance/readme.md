# Sistem automat de asistenta a traficului	<img src="driveSmall.png" alt="Drive!"/>

## Obiective
Dezvoltarea unui sistem automat de asistenta a conducatorilor auto

## Ideea de baza
Unora dintre conducatorii auto sau de trenuri le-ar prinde bine putin ajutor in trafic in activitati precum: detectia obstacolelor, adaptarea vitezei la conditiile meteo si rutiere, navigarea pe harta. Pentru aceasta este nevoie de o aplicatie inteligenta care, pe baza informatiilor curente captate din trafic si anumiti senzori (de ex GPS) sa recomande conducatorilor auto/feroviari anumite actiuni. 

## TO DO list
1. Recunoasterea 
- obstacolelor (pietoni, marcaje, alte masini, etc.)
- semnelor de circulatie si a marcajelor in trafic
- conditiilor meteo si rutiere curente 
2. Identificarea unui traseu optim (intre 2 locatii) 
3. Nota:
- In cazul recunoasterii unor anumite elemente, se vor antrena si valida modele de clasificare folosind informatii preluate din seturi de date de tip benchmark, iar clasificatorii rezultati vor fi testati folosind informatii noi preluate de diferiti senzori atasati autovehicului. 
- In cazul identificarii unui anumit traseu, se vor folosi informatii din harti (sub forma unor grafe) si algoritmi de optimizare corespunzatori.
4. Imbunatatire componente inteligente
-	Din perspectiva calitatii procesului de invatare automata
-	Din perspectiva complexitatii temporale si spatiale aferenta clasificatorului
-	Din perspectiva clientului prin considerarea si anticiparea comportamentului celorlalti participanti la trafic (pietoni, autovehicule) si prin scalarea sistemului automat in cazul unui grup de autovehicule (de ex reteaua de taxi-uri a unui oras)

## Date si referinte
**Pedestrians**
1. http://www.pedestrian-detection.com/
2. Franke, Uwe, et al. "From door to door—Principles and applications of computer vision for driver assistant systems." Intelligent Vehicle Technologies. Butterworth-Heinemann, 2001. 131-188.
3. Geronimo, David, et al. "Survey of pedestrian detection for advanced driver assistance systems." IEEE Transactions on Pattern Analysis & Machine Intelligence 7 (2009): 1239-1258. 
4. Dollar, Piotr, et al. "Pedestrian detection: An evaluation of the state of the art." IEEE transactions on pattern analysis and machine intelligence 34.4 (2011): 743-761. 
5. Paden, Brian, et al. "A survey of motion planning and control techniques for self-driving urban vehicles." IEEE Transactions on intelligent vehicles 1.1 (2016): 33-55. 
6. Rasouli, Amir, and John K. Tsotsos. "Autonomous vehicles that interact with pedestrians: A survey of theory and practice." IEEE Transactions on Intelligent Transportation Systems (2019).
7. Rasouli, Amir, Iuliia Kotseruba, and John K. Tsotsos. "Understanding pedestrian behavior in complex traffic scenes." IEEE Transactions on Intelligent Vehicles 3.1 (2017): 61-70.

**Routing**
1. http://neo.lcc.uma.es/vrp/vehicle-routing-problem/
2. Pillac, Victor, et al. "A review of dynamic vehicle routing problems." European Journal of Operational Research 225.1 (2013): 1-11.
3. Braekers, Kris, Katrien Ramaekers, and Inneke Van Nieuwenhuyse. "The vehicle routing problem: State of the art classification and review." Computers & Industrial Engineering 99 (2016): 300-313.
4. Goksal, Fatma Pinar, Ismail Karaoglan, and Fulya Altiparmak. "A hybrid discrete particle swarm optimization for vehicle routing problem with simultaneous pickup and delivery." Computers & Industrial Engineering 65.1 (2013): 39-53.
5. Marinakis, Yannis, and Magdalene Marinaki. "A hybrid genetic–Particle Swarm Optimization Algorithm for the vehicle routing problem." Expert Systems with Applications 37.2 (2010): 1446-1455.

Railways
1. Jahan, K., Niemeijer, J., Kornfeld, N., and Roth, M. (2021). Deep neural networks for railway switch detection and classification using onboard camera images. In 2021 IEEE Symposium Series on Computational Intelligence (SSCI), pages 01–07. IEEE
2. Karak ̈ose, M., Akın, E., and Yaman, O. (2016). Detection of rail switch passages through image processing on railway line and use of condition-monitoring approach
3. Zendel, O., Murschitz, M., Zeilinger, M., Steininger, D., Abbasi, S., and Beleznai, C. (2019). Railsem19: A dataset for semantic rail scene understanding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops.
4. Christian Growitsch and Heike Wetzel. “Testing for economies of scope in European railways: an efficiency analysis”. In: Journal of Transport Economics and Policy (JTEP) 43.1 (2009), pp. 1–24.
5. Kanwal Jahan, Jeethesh Pai Umesh, and Michael Roth. “Anomaly Detection on the Rail Lines Using Semantic Segmentation and Self-supervised Learning”. In: SSCI. IEEE. 2021, pp. 1–7
6. Haoran Li et al. “RailNet: An Information Aggregation Network for Rail Track Segmentation”. In: 2020 International Joint Conference on Neural Networks (IJCNN). IEEE. 2020, pp. 1–7
7. Zhen Tao et al. “Accurate and Lightweight RailNet for Real-Time Rail Line Detection”. In: Electronics 10.16 (2021), p. 2038


**Imagini si alte date**
1. INRIA http://pascal.inrialpes.fr/data/human/
2. Daimler http://www.lookingatpeople.com/download-daimler-stereo-ped-det-benchmark/index.html
3. Caltech http://vision.caltech.edu/Image_Datasets/CaltechPedestrians/index.html
4. JAAD http://data.nvision2.eecs.yorku.ca/JAAD_dataset/
5. RailSem https://wilddash.cc/railsem19



