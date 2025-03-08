# Network Traffic Analyzer

Bu proje, ağ trafiğini analiz etmek için basit bir Python aracı sunmaktadır. Bu araç, ağ trafiğini gerçek zamanlı olarak yakalayarak, paketleri analiz eder ve potansiyel güvenlik tehditlerini (örneğin, DDoS saldırıları) tespit eder. Ayrıca, TCP trafiğini sayarak görselleştirir.

## Özellikler

- **Ağ Trafiği Analizi**: Gerçek zamanlı olarak ağ trafiğini yakalar ve analiz eder.
- **DDoS Saldırısı Tespiti**: Aynı IP adresinden gelen aşırı paketlerle DDoS saldırılarını tespit eder.
- **TCP Trafiği Sayma**: TCP paketlerini sayar ve sayıları görselleştirir.
- **Görselleştirme**: TCP trafiği bar grafiği ile görselleştirilir.

## Gereksinimler

Projenin çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

- **scapy**: Ağ paketlerini yakalamak ve analiz etmek için kullanılır.
- **matplotlib**: Trafik verisini görselleştirmek için kullanılır.

### Kurulum

1. Python'un yüklü olduğundan emin olun. Python 3.6+ önerilmektedir.
   
2. **Gerekli Python Kütüphanelerini Yükleyin**: Projeyi çalıştırmadan önce, gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

   ```bash
   pip install -r requirements.txt
Ana Python Dosyasını Çalıştırın: main.py dosyasını çalıştırmak için şu komutu kullanın:
python main.py

Bu komut ağ trafiğini yakalamaya başlayacak ve TCP trafiği ile ilgili analizleri yapacaktır. Ayrıca, DDoS saldırıları tespit edildiğinde size uyarı verecektir.

.......................


Kullanım
Ağ Trafiği Dinleme: Program, ağ trafiğini dinler ve TCP paketlerini sayar.
Görselleştirme: Program çalıştırıldıktan sonra, TCP trafiği hakkında bir bar grafiği oluşturulur.
DDoS Saldırısı Tespiti: Eğer aynı IP adresinden 100'den fazla paket gelirse, program bir DDoS saldırısı tespit ettiğine dair uyarı verir.
Teknolojiler
Python: Proje Python ile yazılmıştır. Python 3.6+ sürümünü kullanmak önerilir.
Scapy: Ağ trafiğini yakalamak ve analiz etmek için kullanılır. Bu araç, ağ paketlerini kontrol etmeye ve güvenlik tehditlerini tespit etmeye olanak tanır.
Matplotlib: Trafik verisini görselleştirmek için kullanılır. Bu araç, verileri görsel grafiklere dönüştürmek için mükemmeldir.
Katkıda Bulunma
Eğer projeye katkıda bulunmak isterseniz, aşağıdaki adımları izleyebilirsiniz:

1. Bu repository'yi fork edin.
2. Yeni bir branch oluşturun:
git checkout -b yeni-ozellik
3. Değişikliklerinizi yapın ve commit edin:
git commit -am "Yeni özellik eklendi"
4. Pull Request gönderin.
Katkılarınızı bekliyoruz!



