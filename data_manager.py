import tensorflow as tf
import os
import zipfile

class DataManager:
    def __init__(self):
        self.batch_size = 32
        self.img_size = (160, 160)
        self.url = 'https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip'
        self.path = None

    def indir_ve_temizle(self):
        path_to_zip = tf.keras.utils.get_file('kagglecatsanddogs.zip', origin=self.url)
        self.path = os.path.join(os.path.dirname(path_to_zip), 'PetImages')

        if not os.path.exists(self.path):
            with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(path_to_zip))

        print("Veri hazırlığı ve temizlik tamamlandı.")


    def veri_setlerini_al(self):
        train_ds = tf.keras.utils.image_dataset_from_directory(self.path, validation_split=0.2, subset="training",
                                                               seed=1337, image_size=self.img_size,
                                                               batch_size=self.batch_size)
        val_ds = tf.keras.utils.image_dataset_from_directory(self.path, validation_split=0.2, subset="validation",
                                                             seed=1337, image_size=self.img_size,
                                                             batch_size=self.batch_size)
        return train_ds, val_ds