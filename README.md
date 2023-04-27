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
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c89 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
 <td class="c119 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c94 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c30 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
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
<p class="c2"><span class="c7">sender</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-sender">ShipmentSender</a></span></p>
</td>
 <td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the sender of the shipment and shipment's pickup place. If not specified, the logged user is considered as a sender.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipient</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-recipient">ShipmentRecipient</a></span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the recipient of the shipment and shipment’s delivery place.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">service</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-service">ShipmentService</a></span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment service level agreement. </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">content</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-content">ShipmentContent</a></span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment’s content - number of parcels, weight, size, etc.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">payment</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-payment">ShipmentPayment</a></span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines who-pays-what in shipment and other payment parameters. </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
 <p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentNote</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Customer’s note associated with the shipment.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">200 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ref1</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Reference number or text.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">30</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ref2</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Reference number or text.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">30</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">consolidationRef</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Consolidation reference number or text.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">30</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">requireUnsuccessfulDeliveryStickerImage</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Require unsuccessful delivery sticker image flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
