import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import re

# E-posta formatını doğrulama fonksiyonu
def validate_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(pattern, email)

# E-posta ayarlarınızı buraya girin
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'mail hesabını buraya yaz lütfen'
password = 'Şifreni buraya yaz lütfen'

# E-posta listesi ve PNG dosyalarını buraya girin
email_list = [ '2@gmail.com', '2@gmail.com', ... , 'n@gmail.com']
 # 183 e-posta adresi
png_files = [ '1.png', '2.png', ..., 'n.png']
 # 183 PNG dosyası

# Hatalı e-posta adreslerini saklamak için bir liste
failed_emails = []

# SMTP sunucusuna bağlan
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# Her bir e-posta ve PNG dosyası için döngü
for email, png_file in zip(email_list, png_files):
    if validate_email(email):
        try:
            # E-posta mesajını oluştur
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = email
            msg['Subject'] = 'Katılım Sertifikası'

            # PNG dosyasını e-postaya ekle
            with open(png_file, 'rb') as file:
                img = MIMEImage(file.read())
                img.add_header('Content-Disposition', 'attachment', filename=png_file)
                msg.attach(img)

            # E-postayı gönder
            server.send_message(msg)
            print(f"{email} adresine {png_file} gönderildi.")

            # Sunucunun gönderim sınırlarını aşmamak için bekleme süresi
            time.sleep(1)

        except Exception as e:
            print(f"{email} adresine {png_file} gönderilirken hata oluştu: {e}")
            failed_emails.append(email)
    else:
        print(f"Geçersiz e-posta adresi: {email}")
        failed_emails.append(email)

# Sunucuyu kapat
server.quit()

# Hatalı e-posta adreslerini yazdır
if failed_emails:
    print("Hatalı e-posta adresleri:")
    for failed_email in failed_emails:
        print(failed_email)