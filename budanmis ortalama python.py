#Gireceğimiz veri değerlerini eklemek için boş bir veriler listesi oluşturuyoruz.
veriler = []
#Sürekli girdi sağlamak için bir döngü oluşturuyoruz.
while True:
  veri = input("Veri giriniz 'x' veya 'X' ile veri girişini durdurun: ")
#Kullanıcı "x" veya "X" girerse veri girişini sonlandırıyoruz.
  if veri == "x" or veri == "X":
    break
#Girdiğimiz verileri "veriler" listesine eklemek için .append fonksiyonunu kullanıyoruz.
  veriler.append(float(veri))

#Bubble Sort algoritmasını iç içe bir döngü kurup "veriler" listesindeki değerleri karşılaştırarak küçükten büyüğe verileri sıralıyoruz.
for i in range(len(veriler) - 1):
  for j in range(len(veriler) - i - 1):
    if veriler[j] > veriler[j + 1]:
      veriler[j], veriler[j + 1] = veriler[j + 1], veriler[j]
#Daha budanmamış verileri göstermek için bu satırı yazıyorum.
print("girdiğiniz veriler:", veriler)
#Girilen veri sayısının %5'ini buluyoruz.
x=(int(len(veriler))*0.05)
#Eğer girilen veri sayısının %5'inin tam sayı kısmı 1'den küçük ise budanmış ortalama uygulanmamış şekilde girdiğimiz verileri yazdırıyoruz
if x<1:
  print("Lütfen verilerin %5'inin budanması için en az 20 adet değer giriniz")
  print("budanmış ortalama uygulanmamış",veriler)
#Eğer değilse kaç adet veri girdiğimizi yazdırıp veri listesinin başından ve sonundan bulduğumuz veri sayısının %5 kadar veriyi çıkartıp onu yazdırıyoruz.
else:
  print(len(veriler),"adet veri girdiniz")
  budanmis_ortalama=veriler[(int(x)):-(int(x))]
  print(budanmis_ortalama)
  total=0
  for sayi in budanmis_ortalama:
      total += sayi
  print("budanmış ortalama:\n",total/(len(budanmis_ortalama)))
