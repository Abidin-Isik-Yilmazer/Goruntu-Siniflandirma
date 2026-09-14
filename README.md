# 🐾 Görüntü Sınıflandırma (Kedi ve Köpek Tespiti)

Bu proje, **TensorFlow**, **Keras** ve **MobileNetV2** mimarisi kullanılarak geliştirilmiş derin öğrenme tabanlı bir görüntü sınıflandırma (Image Classification) uygulamasıdır.
Sıfırdan model eğitmek yerine **Transfer Learning (Transfer Öğrenme)** yöntemi kullanılarak yüksek doğruluk oranına hızlı bir şekilde ulaşılmıştır.

## 🚀 Kullanılan Teknolojiler ve Kütüphaneler
* **Python**
* **TensorFlow / Keras**
* **MobileNetV2** (Önceden eğitilmiş ana model)

## 📂 Proje Yapısı (Modüler Mimari)
Projeyi sürdürülebilir ve temiz tutmak adına OOP prensiplerine uygun olarak modüllere ayırdık:
* `data_manager.py`: Veri setinin indirilmesi ve ön işleme adımlarını yönetir.
* `model_manager.py`: MobileNetV2 tabanlı yapay zeka modelinin kurulması, yüklenmesi ve tahmin yapılması işlemlerini barındırır.
* `main.py`: Projenin kontrol merkezidir; kayıtlı modeli diskten yükler ve test fotoğraflarını analiz eder.
* `benim_yapay_zekam.keras`: Eğitilmiş yapay zeka modelinin kalıcı olarak saklandığı ağırlık dosyasıdır.

##⚙️ Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/Abidin-Isik-Yilmazer/Goruntu-Siniflandirma.git](https://github.com/Abidin-Isik-Yilmazer/Goruntu-Siniflandirma.git)
   ```

2. Proje dizinine gidin:
   ```bash
   cd Goruntu-Siniflandirma
   ```

3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install tensorflow
   ```
   *(Not: Eğer requirements.txt dosyası eklerseniz `pip install -r requirements.txt` komutunu yazabilirsiniz)*

4. Projeyi çalıştırın:
   ```bash
   python main.py
   ```
