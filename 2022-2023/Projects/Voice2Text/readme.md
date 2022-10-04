
# Speech to text <img src="speech2text.png" alt="Voice to text"/>

## Obiective
Transformarea vocii in text si a textului in voce pentru limba romana


## Ideea de baza
Transformarea unor inregistrari vocale in text si invers poate fi utila persoanelor cu dizabilitati, reporterilor, medicilor (care analizeaza situatia pacientilor sau doresc sa realizeze fisa pacientului in timp ce mainile lor sunt ocupate cu salvarea pacientului), scriitorilor, cadrelor didactice (care doresc sa ofere notite aferente lectiilor explicate).


## TODOlist
1. Iteratia1 - e posibil sa fie efectuata deja la curusl de AI :)
- analiza seturi de date (voce, transcriere) pentru limba engleza si pentru limba romana
- parsarea vocii in text prin folosirea de modele inteligente (pre-trained) (de ex [link0](https://deepspeech.readthedocs.io/en/v0.8.2/?badge=latest), [link1](https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview), [link2](https://pypi.org/project/SpeechRecognition/))
- evaluarea performantei transformarii


2. Iteratia2
- dezvoltarea de modele inteligente pt SpeechToText (si antrenarea lor)  [link0](https://deepspeech.readthedocs.io/en/v0.7.4/TRAINING.html)
- evaluarea a performantei transformarii
- compararea modelelor pre-trained (iteratia 1) cu cele trained (iteratia 2)


## Date si referinte
**Date si biblioteci**
- [LibriSpeech](http://www.openslr.org/12)
- [TIMIT](https://catalog.ldc.upenn.edu/LDC93S1)


**Metode de lucru**
- Hannun, A., Case, C., Casper, J., Catanzaro, B., Diamos, G., Elsen, E., ... & Ng, A. Y. (2014). Deep speech: Scaling up end-to-end speech recognition. arXiv preprint arXiv:1412.5567
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30.
- https://github.com/flashlight/flashlight/tree/main/flashlight/app/asr 

