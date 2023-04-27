Proje Dökümantasyonu
Projenin Amacı:
	Proje’nin amacı Hava Araçları için basit düzeyde e-ticaret sitesi oluşturmaktır.
Projede Kullanılan Araçlar:
	Django, Jazzmin, Django Rest Framework
Projenin İndirilmesi ve Çalıştırılması:
	git clone https://github.com/yemredogru/iha_project.git komutu ile projemizi indiriyoruz.
	
	cd iha komutu ile iha klasörüne geçiş yapıyoruz
	pip install -r requirements.txt komutu ile paketlerimizi kuruyoruz.
	py manage.py runserver ile projemizi ayağa kaldırıyoruz.

 Projenin Tanıtımı:
  Bu bölümde, projede yer alan sayfalar ve bu sayfaların nasıl kullanılacağı anlatılmak istenmektedir.
Projede sepete ürün ekleme bulunmaktadır fakat, ürün adeti, sepetten silme gibi fonksiyonlar aktif edilmemiştir.
Projede Yer Alan Sayfalar
1-	Ana sayfa http://127.0.0.1:8000/
2-	Admin Ürün Listeleme ve Ürün Ekleme http://127.0.0.1:8000/list/
3-	Admin Marka, Model ve Kategori Ekleme http://127.0.0.1:8000/add/
4-	Alışveriş Sepeti http://127.0.0.1:8000/cart/
5-	Giriş Yap http://127.0.0.1:8000/login/
6-	Kayıt Ol http://127.0.0.1:8000/register/
7-	API arayüzü http://127.0.0.1:8000/api/


Admin Marka, Model ve Kategori Ekleme Sayfası’nın Kullanımı

Ekleme işlemlerinden sonra sayfa yenilenmelidir.
Select işlemlerinin front-end tarafında daha iyi yönetilebilmesi için birden fazla kategori, marka ve model eklenerek devam edilmelidir, bu gereksinimler sağlandıktan sonra Admin Ürün Ekleme sayfası kullanılmalıdır.



Admin Ürün Ekleme Sayfası’nın Kullanımı
	Tüm alanlar doldurulmalıdır.
	Fiyat ve ağırlık alanlarına sadece sayı girilmelidir.
	
Projenin İlerleme Aşaması ve Sonuçlar:
	Öncelikle projede hangi sayfaların yer alacağı, hangi fonksiyonelliklerin olacağı belirlendi.
	Gereksinimler belirlendikten sonra django rest framework kullanılarak API oluşturuldu. Bu api ile iha ekleme, model ekleme, kategori ekleme, marka ekleme gibi işlemler yapıldı.
	Admin Ürün Ekleme, Silme, Güncelleme gibi tüm CRUD işlemleri API üzerinden yapıldı.
	Sepete ürün ekleme işlemleri için session yapısı araştırıldı ve uygulandı.
	Sonuç olarak basit bir e-ticaret sitesi elde ettik.



