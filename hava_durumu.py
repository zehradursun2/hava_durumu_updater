
import requests

with open("version.txt", "r") as f:
    yerel_surum = f.read().strip()

url = "https://raw.githubusercontent.com/zehradursun2/hava_durumu_updater/refs/heads/main/latest_version.txt"
cevap = requests.get(url)

if cevap.status_code == 200:
    guncel_surum = cevap.text.strip()
    print(f" Şu anki sürüm: {yerel_surum} | En güncel sürüm: {guncel_surum}")

    if yerel_surum< guncel_surum:
        print("Yeni bir sürüm mevcut! güncellemeyi düüşünün.")
    else:
        print("Uygulama zaten en güncel sürümde.")

else:
    print("Güncel sürüm bilgisi alınamadı.")

print("Hello, Welcome Wheather APP!!!")

sehir = input("Lütfen bir şehir ismi girin: ")
print("Girdiğiniz şehir:", sehir)

api_key = "b354463c89dd8a09724c01ac930c82db" # openweather sitesinde aldığımız api key
url = f'https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=tr'
# Bu url ile apimizin şehirlerin hava durummu verilerini çekmesi gerektiğini beilirttik

# Apiden veri çekmek için:
response = requests.get(url)

# Apiden aldığımız cevabı json formtında çözmek için. json yani sözlük formatında veri.
veri = response.json()

#Çıktıyı göstermek için:
print(veri)

if response.status_code== 200:
    sicaklik = veri["main"]["temp"]
    aciklama = veri["weather"][0]["description"]

    print(f"\n {sehir.capitalize()} için hava durumu:")
    print(f"\n Sıcaklık: {sicaklik}°C")
    print(f" Durum: {aciklama}")
else:
    print("Şehir bulunamadı veya Api hatası oluştu.")