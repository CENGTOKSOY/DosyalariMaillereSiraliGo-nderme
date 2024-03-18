Proje Adı
===========

Bu proje, belirli e-posta adreslerine katılım sertifikalarını otomatik olarak göndermek için tasarlanmış bir Python betiği içerir.

Kullanım
--------

1. `main.py` dosyasını açın ve SMTP sunucu ayarlarınızı, kullanıcı adınızı ve parolanızı güncelleyin.

smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'kullanici_adi@gmail.com'
password = 'parola'

2. E-posta listesi ve PNG dosyalarını `email_list` ve `png_files` listelerine ekleyin.

email_list = ['a@gmail.com', 'b@gmail.com', 'c@gmail.com']
png_files = ['sertifika1.png', 'sertifika2.png', 'sertifika3.png']

3. Projeyi çalıştırın:

python main.py

Notlar
------

- `validate_email()` fonksiyonu, e-posta adreslerinin doğruluğunu kontrol eder. Eğer geçerli değilse, e-posta gönderimi yapılmaz ve hatalı e-posta listesine eklenir.
- Gönderim sırasında hatalar oluşursa, bu hatalar `failed_emails` listesine eklenir ve sonunda yazdırılır.



İletişim
---------

Herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen bana toksoyaligaffar@gmail.com adresinden ulaşın veya GitHub üzerinden bir konu açın.
