import tensorflow as tf
import os

class AnimalClassifier:
    def __init__(self, model_adi='benim_yapay_zekam.keras'):
        self.model_adi = model_adi
        self.model = None

    def sifirdan_egit_ve_kaydet(self, train_ds, val_ds):
        print("Model eğitiliyor...")
        pass

    def kayitli_modeli_yukle(self):
        if os.path.exists(self.model_adi):
            self.model = tf.keras.models.load_model(self.model_adi)
            print("Kayıtlı model başarıyla yüklendi!")
        else:
            print("Kayıtlı model bulunamadı, önce eğitim yapmalısınız.")

    def tahmin_et(self, resim_yolu):
        if not os.path.exists(resim_yolu):
            print("Fotoğraf bulunamadı!")
            return

        img = tf.keras.utils.load_img(resim_yolu, target_size=(160, 160))
        img_array = tf.expand_dims(tf.keras.utils.img_to_array(img), 0)
        tahmin = self.model.predict(img_array)

        if tahmin[0] < 0:
            print(f"🚨 KARAR: KEDİ 🐱 (Skor: {tahmin[0][0]:.2f})")
        else:
            print(f"🚨 KARAR: KÖPEK 🐶 (Skor: {tahmin[0][0]:.2f})")