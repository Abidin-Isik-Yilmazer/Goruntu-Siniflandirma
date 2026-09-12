from model_manager import AnimalClassifier

yapay_zeka = AnimalClassifier()
yapay_zeka.kayitli_modeli_yukle()

yapay_zeka.tahmin_et('test3.jpg')
