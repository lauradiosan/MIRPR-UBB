
# Automatizarea planificarii vacantelor <img src="hollydaySmall.png" alt="On y va?"/>

##	Obiective
Dezvoltarea unui sistem automat de asistenta in planificarea vacantelor

##	Ideea de baza
Unora dintre oameni le-ar fi foarte utila o aplicatie care sa ii ajute in planificarea vacantelor. Pe langa alegerea locatiei, exista multe „probleme care trebuie rezolvate”: Unde ma voi caza? Ce voi manca? Ce voi vizita? Cum ajung si cum ma intorc de acolo? Pot prietenii mei sa vina si ei? Le va placea? Dezvoltarea unui chat-bot capabil sa raspunda unor astfel de intrebari ar inlesni mult procesul de planificare a vacantelor. 

## TO DO list
1.	Alegerea unei locatii
2.	Sugerarea unor posibilitati de cazare tinand cont de diferite criterii oferite de utilizator
3.	Sugerarea unor posibile locatii pentru servirea mesei tinand cont de diferite criterii oferite de utilizator
4.	Sugerarea unei liste de obiective de vizitat tinand cont de diferite criterii oferite de utilizator
5.	Sugerarea posibilitatilor de transport 

Fiecare sugestie oferita de catre asistentul automat trebuie sa ia in calcul informatii variate, multi-modale precum:
-	Informatii audio (criteriile solicitate de client, sugestiile oferite de sistem)
-	Informatii textuale (atat criteriile solicitate de client, cat si si descrierile elementelor printre care se face cautarea)
-	Informatii vizuale (atat criteriile solicitate de client, cat si si descrierile elementelor printre care se face cautarea)
-	Informatii dintr-o retea sociala (o retea de prieteni sau o retea de impresii/reviews despre anumite elemente turistice)
, https://www.microsoft.com/en-us/download/confirmation.aspx?id=52419, https://webscope.sandbox.yahoo.com/catalog.php?datatype=l, https://www.microsoft.com/en-us/download/58389, http://convai.io/data/
De exemplu, un client vrea sa mearga impreuna cu familia lui la mare in Creta, vrea sa fie cazat intr-un camping (pt ca merge cu rulota) a carui plaja sa fie cam asa <img src="whiteBeach.png" alt="white beach"/>  (plaja cu nisip alb), pe drum sa se opreasca in 2 locatii cu obiective istorice si vrea sa calatoreasca intr-o caravana cu alte 2 familii (una dintre familii doreste ca locatia de cazare sa aiba atat acces direct la mare, cat si acess la un aqua-parc).

## Date si referinte
**Voice and text processing**
1. Mikolov, T., Corrado, G., Chen, K., & Dean, J. (2013). Efficient Estimation of Word Representations in Vector Space. Proceedings of the International Conference on Learning Representations (ICLR 2013), 1–12.
2. Collobert, R., Weston, J., Bottou, L., Karlen, M., Kavukcuoglu, K., & Kuksa, P. (2011). Natural Language Processing (almost) from Scratch. Journal of Machine Learning Research, 12 (Aug), 2493–2537
3. Biadsy, Fadi, et al. "Parrotron: An End-to-End Speech-to-Speech Conversion Model and its Applications to Hearing-Impaired Speech and Speech Separation." arXiv preprint arXiv:1904.04169 (2019).
4. AYLIEN https://aylien.com/text-api/?redirect=portal
5. Google Duplex https://ai.googleblog.com/2018/05/duplex-ai-system-for-natural-conversation.html
6. Parrotron https://ai.googleblog.com/2019/07/parrotron-new-research-into-improving.html
7. Google chatbot corpus https://ai.googleblog.com/2019/01/natural-questions-new-corpus-and.html
8. Other corpus http://www.cs.cmu.edu/~ark/QA-data/, https://www.microsoft.com/en-us/download/confirmation.aspx?id=52419, https://webscope.sandbox.yahoo.com/catalog.php?datatype=l, https://www.microsoft.com/en-us/download/58389, http://convai.io/data/

**Community detection**
1. Fast Greedy:  Clauset et al., Finding com. struct. in very large networks. Phys. Rev. E, 70:1–6, 2004
2. Lovain: Blondel et al., Fast unfolding of communities in large networks, J. of statistical mechanics: theory and experiment, 10, 2008
3. Newman-Fast algorithm: Newmann, M. E. J., Fast algorithm for detecting com. struct. in networks. Phys. Rev. E, 69:1–12. 
4. Label Propagation: Raghavan et al., Near linear time algorithm to detect com. struct. in large-scale networks. Phys. Rev. E, 76:036106 
5. Infomap: Rosvall, M. and Bergstrom, C. T., An information-theoretic framework for resolving com. struct. in CNs. Proc. of the Nat. Acad. of Sciences, 104(18):7327–7331. 






