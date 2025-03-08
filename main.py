import matplotlib.pyplot as plt
from scapy.all import sniff
from collections import defaultdict

# TCP trafiğini saymak için bir değişken
tcp_count = 0
ip_count = defaultdict(int)

# DDoS saldırısını tespit etmek için bir eşik
DDoS_THRESHOLD = 100

# Paket analizi callback fonksiyonu
def packet_callback(packet):
    global tcp_count
    
    # IP paketlerini analiz et
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        ip_count[ip_src] += 1
        
        # DDoS tespiti
        if ip_count[ip_src] > DDoS_THRESHOLD:
            print(f"** DDoS saldırısı tespit edildi! IP: {ip_src} **")
        
        # TCP paketlerini sayma
        if packet.haslayer('TCP'):
            tcp_count += 1

# Paketleri yakalamak için Scapy'yi kullanarak trafik dinleyin
def start_sniffing():
    print("Ağ trafiği yakalanıyor...")
    sniff(prn=packet_callback, count=100)  # 100 paket yakala

# Trafik verisini görselleştir
def visualize_traffic():
    plt.bar(['TCP Paketleri'], [tcp_count])
    plt.title('TCP Trafiği Analizi')
    plt.xlabel('Paket Türü')
    plt.ylabel('Paket Sayısı')
    plt.show()

# Ana fonksiyon
if __name__ == '__main__':
    start_sniffing()
    visualize_traffic()