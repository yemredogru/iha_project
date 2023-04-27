Proje Dökümantasyonu
Projenin Amacı:
	Proje’nin amacı Hava Araçları için basit düzeyde e-ticaret sitesi oluşturmaktır.
Projede Kullanılan Araçlar:
	Django, Jazzmin, Django Rest Framework
 Projenin Tanıtımı:
  Bu bölümde, projede yer alan sayfalar ve bu sayfaların nasıl kullanılacağı anlatılmak istenmektedir.
Projede Yer Alan Sayfalar
1-	Ana sayfa http://127.0.0.1:8000/
2-	Admin Ürün Listeleme ve Ürün Ekleme http://127.0.0.1:8000/list/
3-	Admin Marka, Model ve Kategori Ekleme http://127.0.0.1:8000/add/
4-	Alışveriş Sepeti http://127.0.0.1:8000/cart/
5-	Giriş Yap http://127.0.0.1:8000/login/
6-	Kayıt Ol http://127.0.0.1:8000/register/
7-	API arayüzü http://127.0.0.1:8000/api/


API Kullanım Klavuzu
2.1 Shipment Service
Web service URL: BASE_URL/shipment


2.1.1 Create Shipment Request (CreateShipmentRequest)

Method: POST

Content-type: application/json;  charset=utf-8


Input parameters:
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">Tüm Ihaları listeleme</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Parametre </span></p>
</td>
<td class="c89 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Tür</span></p>
</td>
 <td class="c119 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Gerekli</span></p>
</td>


</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
	<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
		<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
		<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>

</tr>
</tbody>
</table>
