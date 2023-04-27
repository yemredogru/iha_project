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

<div class="nextPromise">
<p class="c2 c3"><span class="c16"></span></p>
<a id="id.44sinio"></a>
<h1 class="c190" id="href-description"><span class="c155">2 Overall Description</span></h1>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>&nbsp;</span><span class="c34">BASE_URL</span>=<span class="c16" data-sl-text="baseUrl">https://api.dpd.ro/v1</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="id.2jxsxqh"></a>
<h2 class="c74" id="href-shipment-service"><span class="c34 c35">2.1 Shipment Service</span></h2>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/shipment</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-create-shipment-req"><span>2</span><span class="c66 c34">.1.1 Create Shipment Request (CreateShipmentRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Input parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">CreateShipmentRequest</span></p>
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
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example Request:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"service":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "serviceId":2002,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "additionalServices":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"declaredValue":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":100.0</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"returns":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "rod":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"enabled":true</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; },</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "returnReceipt":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"enabled":true</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; },</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "swap":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"serviceId":2002,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"parcelsCount":1</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"content":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "parcelsCount":1,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "totalWeight":20.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "contents":"FURNITURE",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "package":"BOX"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"payment":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "courierServicePayer":"SENDER"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"recipient":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "phone1":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"number":"0999123321"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; },</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "privatePerson": true,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "clientName":"TEST",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "contactName":"TEST",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "email":"a@b.c",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "address":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"siteName":"Sibiu",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"streetType":"str.",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"streetName":"ACILIU",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"streetNo":"3"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"shipmentNote":"Test note",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"ref1":"R1",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"ref2":"R2"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-create-shipment-resp"><span>2</span><span>.1.2 Create Shipment Response (CreateShipmentResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Output parameters:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c171" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">CreateShipmentResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c138 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c63 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c138" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c63" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Generated shipment id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c138" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-created-shipment-parcel">CreatedShipmentParcel</a></span><span class="c24">[]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c63" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Generated parcels.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">price</span></p>
</td>
<td class="c138" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-price">ShipmentPrice</a></span></p>
</td>
<td class="c63" colspan="1" rowspan="1">
<p class="c2"><span class="c24">Returned, if customer has access to view the amounts of the shipment. </span></p>
</td>
</tr>
<tr class="c14">
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupDate</span></p>
</td>
<td class="c138" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (date)</span></p>
</td>
<td class="c63" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment pickup date.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">deliveryDeadline</span></p>
</td>
<td class="c138" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (datetime)</span></p>
</td>
<td class="c63" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Deadline for delivery. Returned, if available.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c138" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-errors">Error</a></span></p>
</td>
<td class="c63" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example response:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"id":"80002589418",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"pickupDate":"2018-01-22",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"price":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "amount":47.17,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "vat":8.96,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "total":56.13,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "details":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"netAmount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":46.5,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"fixedDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"dropOffDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"pickUpDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"additionalDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"fuelSurcharge":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.47,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":1.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"islandSurcharge":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"codPremium":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"insurancePremium":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; },</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "amountLocal":47.17,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "vatLocal":8.96,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "totalLocal":56.13,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "currencyLocal":"RON",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "detailsLocal":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"netAmount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":46.5,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"fixedDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"dropOffDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"pickUpDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"additionalDiscount":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"fuelSurcharge":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.47,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "percent":1.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"islandSurcharge":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"codPremium":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.0,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"insurancePremium":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "amount":0.2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "vatPercent":0.19</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; },</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "currencyExchangeRateUnit":1,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "currencyExchangeRate":1.0</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"deliveryDeadline":"2018-01-23T17:30:00+0200"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-create-shipment-url"><span>2</span><span class="c66 c34">.1.3 Create Shipment - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to create shipments, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span>&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: “application/x-www-form-urlencoded; </span><span class="c34">charset</span><span class="c16">=utf-8”</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">CreateShipmentRequest</span></p>
</td>
 </tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Sender details</span></p>
<p class="c2"><span class="c25 c24">If the logged user is the sender, you may skip providing sender details at all. </span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client’s id in sender_id parameter and other sender parameters may be skipped at all also. However, in these cases, if the user needs to change the defaults stored in the system, the following parameters could be provided in addition:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0 start">
<li class="c2 c36"><span class="c25 c24">sender phone(s)</span></li>
<li class="c2 c36"><span class="c25 c24">sender contact in case the referred customer is a company (not a private person), otherwise should be skipped</span></li>
<li class="c2 c36"><span class="c25 c24">sender email</span></li>
<li class="c2 c36"><span class="c25 c24">sender address note</span></li>
</ul>
<p class="c2"><span class="c25 c24">If you provide information in other sender parameters, you’ll receive an error that data is not expected in that field.</span></p>
<p class="c2 c3"><span class="c25 c24"></span></p>
<p class="c2"><span class="c25 c24">Otherwise, sender_id should stay empty and it is required to provide as a minimum:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c25 c24">sender phone</span></li>
<li class="c2 c36"><span class="c25 c24">sender name</span></li>
<li class="c2 c36"><span class="c162 c24">sender </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">sender contact in case privatePerson is false, otherwise should be skipped</span></li>
<li class="c2 c36"><span class="c25 c24">sender address or dropoffOfficeId</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderId | sender_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer а sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for existence.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPhone | sender_phone</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Mandatory in case sender_id is empty and sender_name is not. Otherwise, it is allowed but not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender phone number.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPhoneExt | sender_phone_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender phone number extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPhone2 | sender_phone2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender phone number 2.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPhone2Ext | sender_phone2_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender phone number 2 extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPhone3 | sender_phone3</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender phone number extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPhone3Ext | sender_phone3_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender phone number 3 extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderName | sender_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If sender_id is provided, it is forbidden. If the sender is the logged user, should be omitted too. Otherwise, it is mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender name.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Minimum 3 symbols, maximum 60</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderContact | sender_contact</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Required, if privatePerson flag is false.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender contact name.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum 60 symbols.</span></p>
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderEmail | sender_email</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender email.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum 255 symbols.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPrivatePerson | sender_private_person</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If sender_id is provided, it is forbidden. If the sender is the logged user, should be omitted too. Otherwise, it is mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender private person flag.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Sender Address</span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-address">ShipmentAddress </a></span><span class="c7">for more details.</span></p>
<p class="c2"><span class="c7">The sender address is expected when sender_id is empty and sender_name is not and sender_dropoff_office_id is empty and not required. In other words, the sender address is required when the sender is not a referred customer or logged user and pickup at sender’s address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressCountryId | sender_address_country_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country ISO code. If not provided, the local country is assumed.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStateId | sender_address_state_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country supports states.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 2 (foreign address).</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteId | sender_address_site_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id.</span></p>
<p class="c2"><span class="c7">Used for all address types. If not provided, but site type and name or post code is provided - the system will try to find unique match by them in country</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteType | sender_address_site_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteName | sender_address_site_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressPostcode | senderAddressPostCode | sender_address_postcode</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid postcode in site and country.</span></p>
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStreetId | sender_address_street_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street identifier. If not provided, but street type and street name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStreetType | sender_address_street_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStreetName | sender_address_street_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStreetNumber | sender_address_street_number</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street number.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressComplexId | sender_address_complex_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex identifier. If not provided, but complex type and complex name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressComplexType | sender_address_complex_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressComplexName | sender_address_complex_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressBlock | senderAddressBlockNo | sender_address_block</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Block No.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 32 </span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressEntrance | senderAddressEntranceNo | sender_address_entrance</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Entrance.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressFloor | senderAddressFloorNo | sender_address_floor</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Floor.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressApartment | senderAddressApartmentNo | sender_address_apartment</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Apartment.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressPoiId | sender_address_poi_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Point of interest identifier.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressNote | sender_address_note</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address note.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">200</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressLine1 | sender_address_line1</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required for address type 2.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 1. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressLine2 | sender_address_line2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 2. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressX | sender_address_x</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - X.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressY | sender_address_y</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - Y.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dropoffOfficeId | dropOffOfficeId | senderDropoffOfficeId | senderDropOffOfficeId | dropoff_office_id | sender_dropoff_office_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if the sender is an &nbsp;internal <span data-sl-text="company">DPD</span> customer. If sender address is provided, it is forbidden.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Drop off office id.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible office.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">sender_geo_pudo_id | senderGeoPUDOId | senderDropoffGeoPUDOId | senderDropOffGeoPUDOId | dropoff_geo_pudo_id | dropoff_geo_pudo_id | dropoffGeoPUDOId | dropOffGeoPUDOId</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No. Must be empty if dropoffOfficeId is provided</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DPD drop off office PUDO id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible DPD office.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Shipment Recipient</span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client’s id in recipient_id parameter and other recipient parameters may be skipped at all. However, if the user needs to change the defaults stored in the system, the following parameters could be provided in addition:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c25 c24">recipient phone(s)</span></li>
<li class="c2 c36"><span class="c25 c24">recipient contact in case the referred customer is a company (not a private person), otherwise should be skipped</span></li>
<li class="c2 c36"><span class="c25 c24">recipient email</span></li>
<li class="c2 c36"><span class="c25 c24">recipient address note</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
<p class="c2"><span class="c25 c24">If you provide information in other recipient parameters, you’ll receive error that data is not expected in that field.</span></p>
<p class="c2"><span class="c25 c24">Otherwise, recipient_id should stay empty and it is required to provide as a minimum:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c24 c25">recipient phone - could be omitted but is required for the same day delivery services, saturday delivery and delivery abroad</span></li>
<li class="c2 c36"><span class="c25 c24">recipient name</span></li>
<li class="c2 c36"><span class="c162 c24">recipient </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">recipient contact in case privatePerson is false otherwise should be skipped</span></li>
<li class="c2 c36"><span class="c24 c162">recipient address or pickupOfficeId</span></li>
</ul>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientId | recipient_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer a recipient.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for existence.</span></p>
</td>
</tr>
<tr class="c14">
 <td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPhone | recipient_phone</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Mandatory in case recipient_id is empty and recipient_name is not. Otherwise, it is allowed but not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient phone number.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPhoneExt | recipient_phone_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient phone number extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPhone2 | recipient_phone2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient phone number 2.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPhone2Ext | recipient_phone2_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient phone number 2 extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPhone3 | recipient_phone3</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient phone number extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPhone3Ext | recipient_phone3_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient phone number 3 extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientName | recipient_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If recipient_id is provided, it is forbidden. Otherwise, it is mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient name.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Minimum 3 symbols, maximum 60</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientContact | recipient_contact</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Required, if privatePerson flag is false.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient &nbsp;contact name.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum 60.</span></p>
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientEmail | recipient_email</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient email.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum &nbsp;255. Mandatory for international shipments</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPrivatePerson | recipient_private_person</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If recipient_id is provided, it is forbidden. Otherwise, it is mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient &nbsp;private person flag.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Recipient Address</span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-address">ShipmentAddress </a></span><span class="c7">for more details.</span></p>
<p class="c2"><span class="c7">The recipient address is expected when recipient_id is empty and recipient_name is not and recipient_pickup_office is empty and not required. In other words, the recipient address is required when the recipient is not a referred customer and delivery at recipient’s address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressCountryId | recipient_address_country_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country ISO code. If not provided, local country is assumed.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStateId | recipient_address_state_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country supports states.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 2 (foreign address).</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteId | recipient_address_site_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id.</span></p>
<p class="c2"><span class="c7">Used for all address types. If not provided, but site type and name or post code is provided - the system will try to find unique match by them in country</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteType | recipient_address_site_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteName | recipient_address_site_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressPostcode | recipientAddressPostCode | recipient_address_postcode</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid postcode in site and country.</span></p>
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStreetId | recipient_address_street_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street identifier. If not provided, but street type and street name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStreetType | recipient_address_street_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStreetName | recipient_address_street_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStreetNumber | recipient_address_street_number</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street number.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressComplexId | recipient_address_complex_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex identifier. If not provided, but complex type and complex name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressComplexType | recipient_address_complex_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressComplexName | recipient_address_complex_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressBlock | recipientAddressBlockNo | recipient_address_block</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Block No.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 32 </span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressEntrance | recipientAddressEntranceNo | recipient_address_entrance</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Entrance.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressFloor | recipientAddressFloorNo | recipient_address_floor</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Floor.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressApartment | recipientAddressApartmentNo | recipient_address_apartment</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Apartment.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressPoiId | recipient_address_poi_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Point of interest identifier.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressNote | recipient_address_note</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address note.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">200</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressLine1 | recipient_address_line1</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required for address type 2</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 1. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressLine2 | recipient_address_line2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 2. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressX | recipient_address_x</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - X.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressY | recipient_address_y</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - Y.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupOfficeId | pickUpOfficeId | recipientPickupOfficeId | recipientPickUpOfficeId | pickup_office_id | recipient_pickup_office_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if recipient is internal <span data-sl-text="company">DPD</span> client. If recipient address is provided, it is forbidden</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup office id.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to valid accessible office.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipient_geo_pudo_id | recipientGeoPUDOId | recipientPickupGeoPUDOId | recipientPickUpGeoPUDOId | pickup_geo_pudo_id | pickupGeoPUDOId | pickUpGeoPUDOId</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No. Must be empty if pickupOfficeId is provided</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DPD pickup office PUDO id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible DPD office.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Shipment Service</span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-service">ShipmentService </a></span><span class="c7">for more details.</span></p>
<p class="c2"><span class="c7">Shipment service defines agreement with customer for courier service. This includes:</span></p>
<ul class="c92 lst-kix_gi2k1nht73no-0 start">
<li class="c2 c36"><span class="c7">Pickup date</span></li>
<li class="c2 c36"><span class="c7">Service id (code)</span></li>
<li class="c2 c36"><span class="c7">Optional defer days or saturday delivery</span></li>
<li class="c2 c36"><span class="c7">Additional services (like COD, Declared value, SWAP, ROD and etc.)</span></li>
</ul>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupDate | pickup_date</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (date)</span></p>
<p class="c2"><span class="c24">Example: &nbsp;“</span><span class="c96 c24 c34">2017-12-11"</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
<p class="c2"><span class="c7">(default value is today)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">The date for shipment pick-up.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Could be today or a future date.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">autoAdjustPickupDate | auto_adjust_pickup_date | autoadjust_pickup_date</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default is false)</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">To find first available date for pickup starting from pickupDate according to pickup schedule for services</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">serviceId | service_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service to be used for shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service id (code) should be valid for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">deferredDays | deferred_days</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default value is 0)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This parameter allows &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users to specify by how many (business) days they would like to postpone the shipment delivery from the standard term.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Allowed values are 0, 1 and 2.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">saturdayDelivery | saturday_delivery</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This parameter may adjust the delivery date to the first business day, if the standard calculated delivery day is a half-working day. If not specified, system will determine this flag based on configured recipient working schedule.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">COD Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-cod">ShipmentCODAdditionalService</a></span><span class="c24">.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codAmount | cod_amount</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">double</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment COD base amount.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against maximum allowed amounts for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codCurrency | cod_currency</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is the currency code of the destination country)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment COD currency code.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against allowed currency code of destination country.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codProcessingType | cod_processing_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“CASH”, “POSTAL_MONEY_TRANSFER”]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is “CASH”)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines COD processing type.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Appropriate contract and annexes may be required.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codPayoutThirdParty | cod_payout_third_party</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If this flag is set, the COD is paid to a third party (not to the &nbsp;sender).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires the third party to be the payer of the courier service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codPayoutLoggedClient | cod_payout_logged_client</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If this flag is set, the COD is paid to a logged client.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codWithShippingPrice | cod_with_shipping_price</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag indicating whether the shipping price should be included in the COD.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codCardPaymentForbidden | cod_card_payment_forbidden</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag indicating that COD/PMT card payment is forbidden.</span>
</p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Options before payment details Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-obpd">ShipmentOBPD</a></span><span class="c7">.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">obpd_option</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“OPEN”, “TEST”]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(For certain destinations could be required.)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines option to be used.</span></p>
<p class="c2"><span class="c7">Open parcels before payment or open and test parcels before payment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment is validated for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">obpd_return_service_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(For certain destinations could be required.)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines service id to be used on return, if COD payment is refused.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment is validated for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">obpd_return_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“SENDER”, “RECIPIENT”, “THIRD_PARTY”]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(For certain destinations could be required.)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines who pays the return shipment, if COD payment is refused.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment is validated for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Declared Value (Extended Liability) Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-ins">ShipmentDeclaredVaueAdditionalService</a></span><span class="c7">.</span></p>
<p class="c2"><span class="c24">Declared value payer is required when declared value amount is provided and is set in payment section.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValueAmount | declared_value_amount</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">double</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment Declared Value (extended liability) base amount. Declared value amount is always in local system currency.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against maximum allowed amounts.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fragile | declaredValueFragile | declared_value_fragile</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines fragile flag for shipment content.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Fragile shipments requires declared value sub service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Fixed Time Delivery Additional Service</span></p>
<p class="c2"><span class="c7">Fixed time delivery is an additional service that provides instruction to deliver shipment at a certain time on the delivery date.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fixedTimeDelivery | fixed_time_delivery</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This option fixes the time of delivery on the delivery date. 1130 - means 11:30</span></p>
<p class="c2"><span class="c7">920 - means 09:20</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This option is checked against configured allowed time frame for the service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Return of Documents (ROD) Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-returns-rod">ShipmentRODAdditionalService</a></span><span class="c24">.</span></p>
<p class="c2"><span class="c7">Return documents is an additional service that provides instruction to collect documents on shipment delivery in return.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">rodEnabled | rod_enabled</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” &nbsp;- all case insensitive)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Enabled flag</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">rodComment | rod_comment</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return documents comment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max size 512</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">rodReturnToClientId | rod_return_to_client_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines customer - recipient for the ROD shipment. If not specified and rod_return_to_office_id is not specified also, the reverse shipment is returned to the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Cannot be specified together with rod_return_to_office_id. The same value should be set for ROD and Return Receipt, if the sub-service presents. Cannot be specified if SWAP presents</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">rodReturnToOfficeId | rod_return_to_office_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
 <td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines delivery pickup depot for ROD shipment. If not specified and rod_return_to_client_id is not specified also, the return shipment is returned to primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Cannot be specified together with rod_return_to_client_id. The same value should be set for ROD, Return Receipt and SWAP, if the sub-service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">rodThirdPartyPayer | rod_third_party_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines a third party payer for ROD shipment. Otherwise, payer is the &nbsp;primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires a third party payer of the primary shipment. The same value should be set for ROD, Return Receipt, ROP and SWAP, if the &nbsp;sub-service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Return Receipt Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-returns-receipt">ShipmentReturnReceiptAdditionalService</a></span><span class="c24">.</span></p>
<p class="c2"><span class="c7">Return receipt is an additional service that provides instruction to collect a receipt on shipment delivery in return.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">receiptEnabled | receipt_enabled</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Enabled flag</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">receiptReturnToClientId | receipt_return_to_client_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td> 
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines customer - recipient for the Return Receipt shipment. If not specified and receipt_return_to_office_id is not specified also, the return shipment is returned to the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Cannot be specified together with receipt_return_to_office_id. The same values should be set for ROD and Return Receipt, if the sub service presents. Cannot be specified if SWAP presents</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">receiptReturnToOfficeId | receipt_return_to_office_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines delivery pickup depot for the Return Receipt shipment. If not specified and receipt_return_to_client_id is not specified also, the return shipment is returned to the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Cannot be specified together with receipt_return_to_client_id. The same values should be set for ROD, Return Receipt and SWAP, if the sub service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">receiptThirdPartyPayer | receipt_third_party_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines a third party payer for the Return Receipt shipment. Otherwise, payer is the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires a third party payer of the primary shipment. The same values should be set for ROD, Return Receipt, ROP and SWAP, if the sub service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">SWAP Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-returns-swap">ShipmentSWAPAdditionalService</a></span><span class="c24">.</span></p>
<p class="c2"><span class="c7">SWAP is an additional service that provides instruction to collect a reverse shipment with predefined parameters on shipment delivery in return.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">swapServiceId | swap_service_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service to be used in return.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowance and destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">swapParcelsCount | swap_parcels_count</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Number of parcels to return.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against maximum allowed parcels.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">swapDeclaredValueAmount | swap_declared_value_amount</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Declared value for the reverse shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowance and maximum amount.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">swapDeclaredValueFragile | swap_declared_value_fragile</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Fragile content flag for the reverse shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Fragile shipments requires declared value.</span></p>
</td>
</tr>

<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">swapReturnToOfficeId | swap_return_to_office_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines delivery pickup depot for the SWAP &nbsp;shipment. If not specified, the return shipment is returned to the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The same value should be set for ROD, Return Receipt and SWAP, if sub-service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">swapThirdPartyPayer | swap_third_party_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines a third party payer for the SWAP shipment. Otherwise, payer is the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires a third party payer of the primary shipment. The same values should be set for ROD, Return Receipt, ROP and SWAP, if the sub service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Return of Pallets (ROP) Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-returns-rop">ShipmentROPAdditionalService</a></span><span class="c24">.</span></p>
<p class="c2"><span class="c7">Return of pallets is an additional service that provides instruction to collect pallets (used to wrap parcels for transport) in return. </span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ropPallets | rop_pallets</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format for single pair is:</span></p>
<p class="c2"><span class="c7">“&lt;serviceId&gt;,&lt;parcelsCount&gt;”</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple pairs are separated with %7C (‘|’) character.</span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-returns-rop-lines">ShipmentROPAdditionalServiceLine</a></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines pallets to return grouped by service id.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Total number of returned pallets should not exceed parcels count of the primary shipment.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ropThirdPartyPayer | rop_third_party_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines a third party payer for the returned pallets. Otherwise, payer is the primary shipment sender.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires a third party payer of the primary shipment. The same values should be set for ROD, Return Receipt, ROP and SWAP, if the sub service presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Return Voucher Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-returns-voucher">ShipmentReturnVoucherAdditionalService</a></span><span class="c24">.</span></p>
<p class="c2"><span class="c7">Return voucher provides an option for the recipient to initiate a return, based on the delivered shipment, within predefined voucher validity period.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">voucherServiceId | voucher_service_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service id of the return voucher shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">voucherPayer | voucher_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the return voucher payer.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Allowed payers are validated against service configuration and destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">voucherValidityPeriod | voucher_validy_period</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c42" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if caller client has no annex for return voucher.</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return voucher validity period in days. The annex return voucher period is used by default in case caller client has such in his contract and value is omitted</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Verified to not exceed the configured internal maximum in the system</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Special Delivery Additional Service</span></p>
<p class="c2"><span class="c7">Special delivery is an additional service that provides instruction to the courier to do additional (special) checks and actions on delivery. These checks and actions are negotiated and contracted in a special delivery annex. For example, the courier could be instructed to check IDs of recipient party at delivery.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">specialDeliveryId | special_delivery_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Specifies special delivery identifier for the shipments. Identifiers are determined in a special delivery annex.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires annex for special delivery.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Delivery to Floor Additional Service</span></p>
<p class="c2"><span class="c7">Delivery to floor is an additional service that provides instruction to the courier that the shipment should not be delivered to the entrance of a multi floor building, but should be moved to a certain floor before delivery.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">deliveryToFloor | delivery_to_floor</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Specifies the floor number in the building where to deliver shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This additional service requires annex.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Shipment Content</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-content">ShipmentContent</a></span><span class="c7">.</span></p>
<p class="c2"><span class="c24">Defines what is to be delivered with the shipment.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcelsCount | parcels_count</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required when parcels list is empty and pending_parcels is false.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Total shipment’s parcels count. Ignored, if parcels list is not empty. The parcels count is the number of parcels in the lits in that case.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against minimum and maximum allowed for the service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">totalWeight | total_weight</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required when parcels list is empty and pending_parcels is false.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Total weight declared for the shipment. Ignored, if parcels list is not empty. The total weight is the sum of all parcel’s weight in that case.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against minimum and maximum allowed for the service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">contents</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment’s contents description.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">100</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">package</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment’s package.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">documents</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Documents flag of the shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">palletized</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Palletized flag of the shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format for single parcel is:</span></p>
<p class="c2"><span class="c7">&lt;seqNo&gt;,&lt;weight&gt;,</span></p>
<p class="c2"><span class="c7">&lt;width&gt;x&lt;depth&gt;x&lt;height&gt;,</span></p>
<p class="c2"><span class="c7">&lt;packageUniqueNumber&gt;,</span></p>
<p class="c2"><span class="c7">&lt;id&gt;,</span></p>
<p class="c2"><span class="c7">&lt;externalCarrierParcelNumber&gt;</span></p>
<p class="c2"><span class="c7">&lt;ref1&gt;</span></p>
<p class="c2"><span class="c7">&lt;ref2&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels should be separated with %7C (‘|’) character.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-content-parcel">ShipmentParcel</a></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required for pallet and postal services. For multiple parcels add the same url parameter again. The parameters are parsed in the order of their occurrence. If the sequence is incomplete, the missing parameters are considered empty.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcels. If omitted, a single default (first) parcel will be created for non-pallet and non-postal services. </span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against service configuration and pickup and delivery capacity of the depots and the couriers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pendingParcels | pending_parcels</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Partial shipment flag indicating parcels are not complete and new parcels are expected.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">exciseGoods | excise_goods</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag shipment contains excise goods.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Shipment Payment</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-payment">ShipmentPayment</a></span><span class="c7">.</span></p>
<p class="c2"><span class="c24">Defines who-pays-what in shipment and other payment parameters.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">courierServicePayer | courier_service_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Courier service payer.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against the service, destination, contracts and annexes.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValuePayer | declared_value_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Declared value payer. If not provided, the courier service payer is assumed. Not expected, if the declared value amount is empty.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against the service, destination, contracts and annexes.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">packagePayer | package_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Package payer. If not provided, the courier service payer is assumed.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against the service, destination, contracts and annexes.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">thirdPartyClientId | third_party_client_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
 <td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment third party - used as a payer of any of shipment payable components.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Third party customer should be registered customer with valid contract and annex for delayed payment at pickup date. Third party customer should be customer(object) in the same contract as the logged user.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Discount card</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-payment-discount-card">ShipmentDiscountCardId</a></span><span class="c7">.</span></p>
<p class="c65"><span class="c24">Discount cards provide promotional discounts.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">discountCardContractId | discount_card_contract_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Discount card contract id.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against a referred contract.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">discountCardId | discount_card_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Discount card id for contract.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against a referred discount card.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Sender Bank account</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-bank-account">BankAccount</a></span><span class="c7">.</span></p>
<p class="c65"><span class="c24">Sender COD payout bank account.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderBankAccountIban | sender_bank_account_iban</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender bank account iban</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">IBAN format validation is applied</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderBankAccountHolder | sender_bank_account_holder</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender bank account holder</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 60 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">administrativeFee | administrative_fee</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to apply administrative fee on price calculations</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Usage of administrative fee is enabled and configured in client contract. Ignored if not applicable for user.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Common parameters</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentNote | shipment_note</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Customer note associated with the shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">200 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ref1</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Reference number or text.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">30</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ref2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Reference number or text.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">30</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">consolidation_ref | consolidationRef</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Consolidation reference number or text.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">30</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">require_unsuccessful_delivery_sticker_image | requireUnsuccessfulDeliveryStickerImage</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Require unsuccessful delivery sticker image flag.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c16">Examples:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">BASE_URL</span><span class="c23">/shipment?username=test&amp;password=test&amp;language=EN&amp;sender_id=34993782000&amp;recipient_id=34993782000&amp;service_id=2113&amp;parcels_count=1&amp;total_weight=3&amp;courier_service_payer=SENDER&amp;contents=FURNITURE&amp;package=BOX</span></p>
<p class="c2 c3"><span class="c96 c24 c179"></span></p>
<p class="c2"><span class="c16">or</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">BASE_URL</span><span class="c23">/shipment?username=test&amp;password=test&amp;language=EN&amp;sender_id=34993782000&amp;service_id=2002&amp;courier_service_payer=SENDER&amp;contents=FURNITURE&amp;package=BOX&amp;recipient_address_site_name=SIBISEL&amp;recipient_name=Mr.%20Name&amp;recipient_address_postcode=337083&amp;recipient_address_street_name=STREET%20NAME&amp;recipient_address_country_id=642&amp;recipient_private_person=y&amp;parcels=1,5,8x8x8%7C2,3,8x8x8&amp;recipient_phone=423234&amp;recipient_phone_ext=33&amp;pickup_date=2017-12-06&amp;cod_amount=33&amp;cod_currency=RON&amp;swap_service_id=2002&amp;swap_parcels_count=2&amp;swap_declared_value_amount=33</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-cancel-shipment-req"><span>2</span><a id="kix.ccfrqtlr3pl4"></a><span class="c66 c34">.1.4 Cancel Shipment Request (CancelShipmentRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/cancel</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Or</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: DELETE</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Cancel shipment. Shipment can be cancelled, it is not ordered yet.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.26654342380b57ccfa34e6485781404d398be747"></a><a id="t.3"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">CancelShipmentRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
 <td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentId</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should have access rights to cancel the shipment.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">comment</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Cancel comment</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 1024</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"shipmentId":"80002589418",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"comment":"Cancel comment"</span></p>
<p class="c2"><span class="c16">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-cancel-shipment-resp"><span>2</span><a id="kix.mk4cruskjrdf"></a><span class="c66 c34">.1.5 Cancel Shipment Response (CancelShipmentResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Cancel response is an empty JSON, if the shipment is successfully cancelled. Otherwise, an error is included.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.039b82d8f0e391165f6a93b89ba8fb1819973e5c"></a><a id="t.4"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">CancelShipmentResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example JSON:</span></p>
<p class="c2"><span class="c23">{}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-cancel-shipment-url"><span>2</span><span class="c66 c34">.1.6 Cancel Shipment - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to cancel shipments, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/cancel</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: “application/x-www-form-urlencoded; </span><span class="c34">charset</span><span class="c16">=utf-8”</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.0a96fc0329ceda5271d1450108e6cb6cad52b262"></a><a id="t.5"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">CancelShipmentRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
 <td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentId | shipment_id</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id </span></p>
</td>
 <td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should have access rights to cancel shipment.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">comment</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Cancel comment</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 1024</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-add-parcel-req"><span>2</span><a></a><span class="c66 c34">.1.7 Add parcel Request (AddParcelRequest)</span></h3>
<p class="c2 c3"><span class="c16">Parcels can be added to shipments in pending parcels state (shipments created with pendingParcels flag true)</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/add_parcel</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">AddParcelRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentId</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer shipment in pending parcels state (not finalized yet with finalizePendingShipment method).</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcel</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-content-parcel">ShipmentParcel</a></span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel to add. Parcel id and sequence number are auto-generated and therefore ignored if present in request</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
 <tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codAmount</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">COD amount to add with this parcel to increase total COD amount</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValueAmount</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Declared value (extended liability) amount to add with this parcel to increase total amount</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If this parcel increases the amount of declared value, the shipment should be opened with Declared value (extended liability) additional service</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"shipmentId":"80002589418",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"parcel":&nbsp;{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;"weight":3,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;"size":&nbsp;{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"width":5,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"height":5,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"depth":5</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"codAmount":5.0</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-add-parcel-resp"><span>2</span><a></a><span class="c66 c34">.1.8 Add Parcel Response (AddParcelResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Add parcel response returns generated parcel. Otherwise, an error is included.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">CancelShipmentResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
 <p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcel</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-created-shipment-parcel">CreatedShipmentParcel</a></span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Created shipment parcel (with generated id and sequence number)</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example JSON:</span></p>
<p class="c2"><span class="c23">{}</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-add-parcel-req-url"><span>2</span><span class="c66 c34">.1.9 Add parcel Request (AddParcelRequest) - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to add parcels, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/add_parcel</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">AddParcelRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
 </td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentId | shipment_id</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer shipment in pending parcels state (not finalized yet with finalizePendingShipment method).</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">weight</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel weight</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">size</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format is &lt;width&gt;x&lt;depth&gt;x&lt;height&gt;</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(Required for pallet and postal services)</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel size</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">packageUniqueNumber | package_unique_number</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel package unique number</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalCarrierParcelNumber | external_carrier_parcel_number</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External carrier parcel id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codAmount | cod_amount</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">COD amount to add with this parcel to increase total COD amount</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValueAmount | declared_value_amount</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Declared value (extended liability) amount to add with this parcel to increase total amount</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If this parcel increases the amount of declared value, the shipment should be opened with Declared value (extended liability) additional service</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example request:</span></p>
<p class="c2"><span class="c34">BASE_URL</span><span class="c23">/shipment/add_parcel?username=test&amp;password=test&amp;language=EN&amp;shipment_id=89981002110&amp;size=10x15x20&amp;weight=13.5&amp;cod_amount=5</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-finalize-req"><span>2</span><a></a><span class="c66 c34">.1.10 Finalize Pending Shipment Request (FinalizePendingShipmentRequest)</span></h3>
<p class="c2 c3"><span class="c16">Pending shipments (opended with pendingParcels flag equal to true) should be finalized with this method</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/finalize</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FinalizePendingShipmentRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentId</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer shipment in pending parcels state (not finalized yet with finalizePendingShipment method).</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"shipmentId":"80002589418"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-finalize-resp"><span>2</span><a></a><span class="c66 c34">.1.11 Finalize Pending Shipment Response (FinalizePendingShipmentResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as </span><span class="c79 c24"><a class="c40" href="#href-create-shipment-resp">CreateShipmentResponse.</a></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-finalize-req-url"><span>2</span><span class="c66 c34">.1.12 Finalize Pending Shipment Request (FinalizePendingShipmentRequest) - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to finalize pending shipments providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/finalize</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FinalizePendingShipmentRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
 </td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentId | shipment_id</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id </span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer shipment in pending parcels state (not finalized yet with finalizePendingShipment method).</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example request:</span></p>
<p class="c2"><span class="c34">BASE_URL</span><span class="c23">/shipment/finalize?username=test&amp;password=test&amp;shipment_id=89981002110</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-shipment-info-req"><span>2</span><a></a><span class="c66 c34">.1.13 Shipment Information Request (ShipmentInformationRequest)</span></h3>
<p class="c2 c3"><span class="c16">This method provides shipment information</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/info</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ShipmentInformationRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentIds</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String[]</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment ids</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-shipment-info-resp"><span>2</span><a></a><span class="c66 c34">.1.14 Shipment Information Response (ShipmentInformationResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">ShipmentInformationResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipments</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment">Shipment</a></span><span class="c7">[]</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment information</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-shipment-info-req-url"><span>2</span><a></a><span class="c66 c34">.1.15 Shipment Information Request (ShipmentInformationRequest) - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to get shipment information providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/info</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ShipmentInformationRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
 </td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentIds | shipment_ids</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String[]</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Comma separated list of shipment ids</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-secondary-shipments-req"><span>2</span><a></a><span class="c66 c34">.1.16 Secondary Shipments Request (SecondaryShipmentsRequest)</span></h3>
<p class="c2 c3"><span class="c16">This method provides secodary shipments information</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/<b>{shipmentId}</b>/secondary</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">SecondaryShipmentsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">types</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum[] (array with values from enum: </span></p>
<p class="c2"><span class="c7">[“RETURN_SHIPMENT”, “STORAGE_PAYMENT”, “REDIRECT”, “SEND_BACK”, “MONEY_TRANSFER”, “TRANSPORT_DAMAGED”, “RETURN_VOUCHER”])</span></p>
<p class="c2">(Same as enum in field type in <span class="c79 c24"><a class="c40" href="#href-ds-primary-shipment">PrimaryShipment</a></span>)</p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">
Filters the list for shipments of the specified type(s) only.
No filter is applied if not provided (all secondary shipments are returned).
</span></p><ul>
<li>RETURN_SHIPMENT - any of return of documents (rod) / returnReceipt / swap / return of pallets (rop)</li>
<li>STORAGE_PAYMENT - warehouse charges</li>
<li>REDIRECT - redirect shipment</li>
<li>SEND_BACK - return to sender</li>
<li>MONEY_TRANSFER - money transfer</li>
<li>TRANSPORT_DAMAGED - damaged shipment transport</li>
<li>VOUCHER_RETURN - return with voucher</li>
</ul>
<p></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-secondary-shipments-resp"><span>2</span><a></a><span class="c66 c34">.1.17 Secondary Shipments Response (SecondaryShipmentsResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">SecondaryShipmentsResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipments</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-secondary-shipment">SecondaryShipment</a></span><span class="c7">[]</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">List of secondary shipments</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-secondary-shipments-req-url"><span>2</span><a></a><span class="c66 c34">.1.18 Secondary Shipments Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to get secondary shipments providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/<b>{shipmentId}</b>/secondary</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">SecondaryShipmentsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">types</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum[] (array with values from enum: </span></p>
<p class="c2"><span class="c7">[“RETURN_SHIPMENT”, “STORAGE_PAYMENT”, “REDIRECT”, “SEND_BACK”, “MONEY_TRANSFER”, “TRANSPORT_DAMAGED”, “RETURN_VOUCHER”])</span></p>
<p class="c2">(Same as enum in field type in <span class="c79 c24"><a class="c40" href="#href-ds-primary-shipment">PrimaryShipment</a></span>)</p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">
Comma separated list of secondry shipment types.
Filters the list for shipments of the specified type(s) only.
No filter is applied if not provided (all secondary shipments are returned).
</span></p><ul>
<li>RETURN_SHIPMENT - any of return of documents (rod) / returnReceipt / swap / return of pallets (rop)</li>
<li>STORAGE_PAYMENT - warehouse charges</li>
<li>REDIRECT - redirect shipment</li>
<li>SEND_BACK - return to sender</li>
<li>MONEY_TRANSFER - money transfer</li>
<li>TRANSPORT_DAMAGED - damaged shipment transport</li>
<li>VOUCHER_RETURN - return with voucher</li>
</ul>
<p></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-update-shipment-req"><span>2</span><span class="c66 c34">.1.19 Update Shipment Request (UpdateShipmentRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/shipment/update</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Full update of already created shipment. Allowed only if shipment is not requested for pick up or is not picked up yet.</span></p>
<p class="c2"><span class="c16">Currently saved shipment data is cleared and replaced with new shipment data</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Input parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">UpdateShipmentRequest</span></p>
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
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-create-shipment-req">CreateShipmentRequest</a></span><span class="c1"><i> fields are here</i></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment with that id must exisists, should be accessible to method caller and shipment state must allow requested property update</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-update-shipment-resp"><span>2</span><span>.1.20 Update Shipment Response (UpdateShipmentResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Response is <span class="c79 c24"><a class="c40" href="#href-create-shipment-resp">CreateShipmentResponse</a></span> - same returned in createShipment method</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Output parameters:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c171" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">UpdateShipmentResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c138 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c63 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="3" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-create-shipment-resp">CreateShipmentResponse</a></span><span class="c1"><i> fields are here</i></span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-update-shipment-req-url"><span>2</span><span class="c66 c34">.1.21 Update Shipment - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to update shipments, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span>&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/update</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: “application/x-www-form-urlencoded; </span><span class="c34">charset</span><span class="c16">=utf-8”</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Full update of already created shipment. Allowed only if shipment is not requested for pick up or is not picked up yet.</span></p>
<p class="c2"><span class="c16">Currently saved shipment data is cleared and replaced with new shipment data</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">UpdateShipmentRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-create-shipment-url">CreateShipmentRequest</a></span><span class="c1"><i> params are here</i></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment with that id must exisists, should be accessible to method caller and shipment state must allow requested property update</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-update-shipment-properties-req"><span>2</span><span class="c66 c34">.1.22 Update Shipment Properties Request (UpdateShipmentPropertiesRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/shipment/update/properties</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Update shipment properties. All properties can be changed if shipment is not requested for pick up or is not picked up yet.</span></p>
<p class="c2"><span class="c16">Recipient phone and COD properties can be updated after pickup request if shipment is still not given to courier for delivery and is not cancelled or closed</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Input parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">UpdateShipmentPropertiesRequest</span></p>
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment with that id must exisists, should be accessible to method caller and shipment state must allow requested property update</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">properties</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Map&lt;String, String&gt;</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The map key is shipment property name and the map value is new propery value to be set in shipment.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The allowed key (property) names are the same as url parameter names (synonims) defined in <span class="c79 c24"><a class="c40" href="#href-create-shipment-url">CreateShipmentRequest</a></span><span class="c1"></span></span></p>
<p class="c2"><span class="c7">The values expected to be in the format defined for corresponding url parameter in that method sepcification.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example Request:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"id":"89988881389",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"properties":{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "total_weight":13,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; "pickup_date":"2020-04-15"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-update-shipment-properties-resp"><span>2</span><span>.1.23 Update Shipment Propeties Response (UpdateShipmentPropertiesResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Response is <span class="c79 c24"><a class="c40" href="#href-update-shipment-resp">UpdateShipmentResponse</a></span> - same returned in updateShipment method</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Output parameters:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c171" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">UpdateShipmentPropertiesResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c138 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c63 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="3" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-update-shipment-resp">UpdateShipmentResponse</a></span><span class="c1"><i> fields are here</i></span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-update-shipment-properties-req-url"><span>2</span><span class="c66 c34">.1.24 Update Shipment Properties - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to update shipment properties, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span>&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/update/properties</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: “application/x-www-form-urlencoded; </span><span class="c34">charset</span><span class="c16">=utf-8”</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Update shipment properties. All properties can be changed if shipment is not requested for pick up or is not picked up yet.</span></p>
<p class="c2"><span class="c16">Recipient phone and COD properties can be updated after pickup request if shipment is still not given to courier for delivery and is not cancelled or closed</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">UpdateShipmentPropertiesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-create-shipment-url">CreateShipmentRequest</a></span><span class="c1"><i> params are here</i></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c89" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c119" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c94" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment with that id must exisists, should be accessible to method caller and shipment state must allow requested property update</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-find-parcels-req"><span>2</span><a></a><span class="c66 c34">.1.25 Find Parcels By Reference Request (FindParcelsByRefRequest)</span></h3>
<p class="c2 c3"><span class="c16">This method returns parcels by reference number</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/search</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindParcelsByRefRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ref</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client reference</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">searchInRef</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Specifies where to search: 0 means [Ref1 or Ref2], 1 means [Ref1], 2 means [Ref2]</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentsOnly</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">boolean</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If true - search in shipments only, otherwise in shipment and parcels. Default is true</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">includeReturns</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">boolean</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If true - search in return shipments also. Default is false</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fromDateTime</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd'T'HH:mm:ssZ”)</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pick-up date - from. Up to 6 months before</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">toDateTime</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd'T'HH:mm:ssZ”)</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pick-up date - to</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c96 c24 c34">&nbsp; &nbsp; "userName":</span><span class="c96 c24 c34">"testUser</span><span class="c23">",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "ref":"634",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "fromDateTime":"2020-10-01T00:00:00+0300",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "toDateTime":"2020-10-15T00:00:00+0300",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-find-parcels-resp"><span>2</span><a></a><span class="c66 c34">.1.26 Find Parcels By Reference Response (FindParcelsByRefResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">FindParcelsByRefResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">barcodes</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span><span class="c7">[]</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">List of barcodes found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-find-parcels-req-url"><span>2</span><a></a><span class="c66 c34">.1.27 Find Parcels By Reference Request (FindParcelsByRefRequest) - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to find parcels by reference providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/search</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindParcelsByRefRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
 <p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ref</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client reference</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">searchInRef | search_in_ref</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Specifies where to search: 0 means [Ref1 or Ref2], 1 means [Ref1], 2 means [Ref2]</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentsOnly | shipments_only</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If true - search in shipments only, otherwise in shipment and parcels. Default is true</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">includeReturns | include_returns</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If true - search in return shipments also. Default is false</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fromDateTime | from_date_time</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd'T'HH:mm:ssZ”)</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pick-up date - from. Up to 6 months before</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">toDateTime | to_date_time</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd'T'HH:mm:ssZ”)</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pick-up date - to</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-handover-req"><span>2</span><a></a><span class="c66 c34">.1.28 Handover To Courier Request (HandoverToCourierRequest)</span></h3>
<p class="c2 c3"><span class="c16">Register handover to courier barcode operations</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/handover</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">HandoverToCourierRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-parcel-handover">ParcelHandover</a></span><span class="c24">[]</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel barcodes with datetime to register handover to courier operations</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer accessible shipment parcels</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-handover-resp"><span>2</span><a></a><span class="c66 c34">.1.29 Handover To Courier Response (HandoverToCourierResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Response is empty on success. Otherwise, an error is included.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">HandoverToCourierResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-handover-req-url"><span>2</span><span class="c66 c34">.1.30 Handover To Courier (HandoverToCourierRequest) - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to handover parcels to courier, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/handover</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
 <p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">HandoverToCourierRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;id&gt;,&lt;dateTime&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple items are separated with %7C (‘|’) character. Datetime is in format dd.MM.yyyy HH:mm:ss</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel ids</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Should refer accessible shipment parcels</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalCarrierParcels | external_carrier_parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;externalCarrierParcelId&gt;,&lt;dateTime&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple items are separated with %7C (‘|’) character. Datetime is in format dd.MM.yyyy HH:mm:ss</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External carrier parcel ids</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Should refer accessible shipment parcels</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-handover-to-midway-carrier-req"><span>2</span><a></a><span class="c66 c34">.1.31 Handover To Midway Carrier Request (HandoverToMidwayCarrierRequest)</span></h3>
<p class="c2 c3"><span class="c16">Register handover to midway carrier barcode operations</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/handover-to-midway-carrier</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">HandoverToMidwayCarrierRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-midway-carrier-parcel-handover">MidwayCarrierParcelHandover</a></span><span class="c24">[]</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel barcodes with datetime, country and site name to register handover to midway carrier operations</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer accessible shipment parcels</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-handover-to-midway-carrier-resp"><span>2</span><a></a><span class="c66 c34">.1.32 Handover To Midway Carrier Response (HandoverToMidwayCarrierResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Response is empty on success. Otherwise, an error is included.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">HandoverToMidwayCarrierResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-handover-to-midway-carrier-req-url"><span>2</span><span class="c66 c34">.1.33 Handover To Midway Carrier Request (HandoverToCourierRequest) - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to handover parcels to midway carrier, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/handover-to-midway-carrier</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">HandoverToMidwayCarrierRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;id&gt;,&lt;countryId&gt;,&lt;dateTime&gt;,&lt;siteName&gt;</span></p>
<p class="c2 c3"><span class="c7">or</span></p>
<p class="c2"><span class="c7">&lt;id&gt;,&lt;countryId&gt;,&lt;dateTime&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple items are separated with %7C (‘|’) character. Datetime is in format dd.MM.yyyy HH:mm:ss</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel ids</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Should refer accessible shipment parcels</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-barcode-information-req"><span>2</span><a></a><span class="c66 c34">.1.34 Barcode Information Request (BarcodeInformationRequest)</span></h3>
<p class="c2 c3"><span class="c16">Get parcel information by parcel barcode</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/barcode-information</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">BarcodeInformationRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c90 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c43 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c55 c45" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
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
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcel</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-parcel-ref">ShipmentParcelRef</a></span><span class="c24"></span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel to get info for</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c96 c24 c34">&nbsp; &nbsp; "userName":</span><span class="c96 c24 c34">"testUser</span><span class="c23">",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "parcel": {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp;&nbsp;"fullBarcode":"1000509431237540020002030017" &nbsp; &nbsp;</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-barcode-information-resp"><span>2</span><a></a><span class="c66 c34">.1.35 Barcode Information Response (BarcodeInformationResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Barcode information response</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c205" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">BarcodeInformationResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c167" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">labelInfo</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-label-info">LabelInfo</a></span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Label info</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">primaryShipment</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-primary-shipment">PrimaryShipment</a></span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Primary shipment.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">primaryParcelId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Primary parcel id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">returnShipmentId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">returnParcelId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return parcel id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">redirectShipmentId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Redirect shipment id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">redirectParcelId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Redirect parcel id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">initialShipmentId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Initial shipment id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">initialParcelId</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Initial parcel id.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c167" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "labelsInfo”: {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; "hubId": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; "officeId": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; "deadlineDay": 18,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; "deadlineMonth": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; "tourId": 2203,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; "fullBarcode": "1000509431237540020002030017"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp;"initialShipmentId": "50943123000"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-barcode-information-req-url"><span>2</span><span class="c66 c34">.1.36 Barcode Information Request (BarcodeInfomationRequest) - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16">This approach is used to get barcode information providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/shipment/barcode-information</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c41" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">BarcodeInformationRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fullBarcode | full_barcode</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes if no id or externalCarrierParcelNumber is provided</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Full barcode</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes if no fullBarcode or externalCarrierParcelNumber is provided</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c18" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalCarrierParcelNumber | external_carrier_parcel_number</span></p>
</td>
<td class="c90" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c43" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes if no id or fullBarcode is provided</span></p>
</td>
<td class="c55" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External carrier parcel number</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Example request:</span></p>
<p class="c2"><span class="c34">BASE_URL</span><span class="c23">/shipment/barcode-information?username=test&amp;password=test&amp;fullBarocde=1000899999993951420001320013</span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h2 class="c74" id="href-print-service"><span class="c35 c34">2.2 Print Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/print</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2">
Used to create labels (waybills, stickers and etc.)
<br><br>
<strong>PDF Examples:</strong>
</p>
<ul style="text-align: left">
<li><a href="examples/A4WithoutCOD_RO.pdf" target="_blank" data-sl-link="pdfA4WithoutCODExample">Waybill (A4)</a></li>
<li><a href="examples/A4_RO.pdf" target="_blank" data-sl-link="pdfA4Example">Waybill (A4) with "cash on delivery"</a></li>
<li><a href="examples/LabelWithoutCOD_RO.pdf" target="_blank" data-sl-link="pdfLabelWithoutCODExample">Parcel sticker (A6)</a></li>
<li><a href="examples/LabelWithCOD_RO.pdf" target="_blank" data-sl-link="pdfLabelWithCODExample">Parcel sticker (A6) with "cash on delivery"</a></li>
<li><a href="examples/ReturnVoucher_RO.pdf" target="_blank" data-sl-link="pdfReturnVoucherExample">Return voucher</a></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-print-req"><span>2</span><span class="c66 c34">.2.1 Print Request (PrintRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c34 c178">PrintRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c24 c140 c34">Name </span></p>
</td>
<td class="c109 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c24 c34 c140">Type</span></p>
</td>
<td class="c68 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c24 c140 c34">Required</span></p>
</td>
<td class="c67 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c24 c140 c34">Data</span></p>
</td>
<td class="c30 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c24 c140 c34">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">format</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“pdf”, “zpl”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is pdf)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Output format</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
 </tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">paperSize</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“A4”, “A6”, “A4_4xA6”]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Print paper size</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed format. For example zpl is allowed with A6 only.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-parcel-to-print">ParcelToPrint</a></span><span class="c7">[]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcels to print</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">printerName</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Printer name to be used for direct printing.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dpi</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“dpi203”, “dpi300”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is dpi203)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Dpi used for rendering. Makes sense for zpl format, otherwise ignored</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">additionalWaybillSenderCopy</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“NONE”, “ON_SAME_PAGE”, “ON_SINGLE_PAGE”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is NONE)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines whether and how to print additional waybill copy for sender.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">A4 pdf printing is required if print mode is different than NONE.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c96 c24 c34">&nbsp; &nbsp; "userName":</span><span class="c96 c24 c34">"testUser</span><span class="c23">",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "paperSize":"A4_4xA6",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "parcels": [</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "parcel": {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"id":"80002338331" &nbsp; &nbsp;</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "parcel": {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"id":"80002338159" &nbsp; &nbsp;</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp;]</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-print-resp"><span>2</span><span class="c66 c34">.2.2 Print Response (PrintResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">In case the response is a PDF document, the result content type is application/pdf.</span></p>
<p class="c2"><span class="c34">Content-type</span><span class="c16">: application/pdf</span></p>
<p class="c2"><span class="c16">And content contains pdf bytes.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">In case it is a zpl, the content type is text/plain.</span></p>
<p class="c2"><span class="c34">Content-type</span><span class="c16">:text/plain</span></p>
<p class="c2"><span class="c16">And content contains zpl text string.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">In case of an error, the content type is application/json.</span></p>
<p class="c2"><span class="c34">Content-type</span><span class="c16">:application/json</span></p>
<p class="c2"><span>And content is a JSON with </span><span class="c79"><a class="c40" href="#href-ds-errors">Error </a></span><span class="c16">structure.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-print-req-url"><span>2</span><span class="c66 c34">.2.3 Print Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to print parcels, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">PrintRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c121" colspan="1" rowspan="1">
<p class="c2"><span class="c7">format</span></p>
</td>
<td class="c28" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“pdf”, “zpl”]</span></p>
</td>
<td class="c77" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is pdf)</span></p>
</td>
<td class="c102" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Output format</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c121" colspan="1" rowspan="1">
<p class="c2"><span class="c7">paperSize | paper_size</span></p>
</td>
<td class="c28" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“A4”, “A6”, “A4_4xA6”]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c77" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c102" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Print paper size</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed format. For example zpl is allowed with A6 only.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c121" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c28" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;id&gt;,</span></p>
<p class="c2"><span class="c7">&lt;additionalBarcodeValue&gt;, &lt;additionalBarcodeLabel&gt;, &lt;additionalBarcodeFormat&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character</span></p>
</td>
<td class="c77" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c102" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcels to print.</span></p>
<p class="c2"><span class="c7">Parcel parameters are parsed in the order of their occurrence and missing parameters are considered empty.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c121" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalCarrierParcels | external_carrier_parcels</span></p>
</td>
<td class="c28" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;externalCarrierParcelId&gt;, &lt;additionalBarcodeValue&gt;, &lt;additionalBarcodeLabel&gt;, &lt;additionalBarcodeFormat&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character</span></p>
</td>
<td class="c77" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c102" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External carrier parcels to print.</span></p>
<p class="c2"><span class="c7">Parcel parameters are parsed in the order of their occurrence and missing parameters are considered empty.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c121" colspan="1" rowspan="1">
<p class="c2"><span class="c7">printerName | printer_name</span></p>
</td>
<td class="c28" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c77" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c102" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Printer name to be used for direct printing. Includes javascript in pdf to print document directly to the provided printer on document opening. Make sense for pdf printing.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dpi</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“dpi203”, “dpi300”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is dpi203)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Dpi used for rendering. Makes sense for zpl format, otherwise ignored</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">additionalWaybillSenderCopy | additional_waybill_wender_copy</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“NONE”, “ON_SAME_PAGE”, “ON_SINGLE_PAGE”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is NONE)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines whether and how to print additional waybill copy for sender.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">A4 pdf printing is required if print mode is different than NONE.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-extended-print-req"><span>2</span><span class="c66 c34">.2.4 Extended Print Request</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print/extended</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>The same </span><span class="c79"><a class="c40" href="#href-print-req">PrintRequest </a></span><span class="c16">structure is send to /extended path to get JSON response with an extended routing information described in next section.</span></p>
<p class="c2 c3"><span class="c96 c34 c177"></span></p>
<h3 class="c12" id="href-extended-print-resp"><span>2</span><a id="kix.vc3wfppk5f0o"></a><span class="c66 c34">.2.5 Extended Print Response (ExtendedPrintResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.c774d7fa31efa6a5b6d02802212bbba04e611672"></a><a id="t.8"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c156 c20" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">ExtendedPrintResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c129 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c45 c148" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">data</span></p>
</td>
<td class="c129" colspan="1" rowspan="1">
<p class="c2"><span class="c7">byte[] </span></p>
<p class="c2"><span class="c7">(BASE64 encoded string)</span></p>
</td>
<td class="c148" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Response data - base64 encoded binary data (pdf)</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">printLabelsInfo</span></p>
</td>
<td class="c129" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-label-info">LabelInfo</a></span><span class="c24">[]</span></p>
</td>
<td class="c148" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Print labels info</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c129" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c148" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "data": "ADABDAS..."</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "labelsInfo”: [</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "parcelId": "50943123754",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "hubId": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "officeId": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "deadlineDay": 18,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "deadlineMonth": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "tourId": 2203,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "fullBarcode": "1000509431237540020002030017"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; ]</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-extended-print-req-url"><span>2</span><a id="kix.ltxg62lfvqwj"></a><span class="c66 c34">.2.6 Extended Print Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to print parcels, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print/extended</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>The same </span><span class="c79"><a class="c40" href="#href-print-req">PrintRequest </a></span><span class="c16">&nbsp;parameters are sent to /extended path to get JSON response with an extended routing information.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using in JSON POST schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-label-inf-req"><span>2</span><span class="c34 c66">.2.7 Label Info Request (LabelInfoRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print/labelInfo</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">LabelInfoRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c109 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c68 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c67 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c30 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-parcel-ref">ShipmentParcelRef</a></span><span class="c24">[]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcels to get label info for</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "parcels": [</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"id":"80002338331" &nbsp; &nbsp;</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;},</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"id":"80002338159" &nbsp; &nbsp;</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp;}</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp;]</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-label-inf-resp"><span>2</span><span class="c66 c34">.2.8 Label Info Response (LabelInfoResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.4bb61188f78417a1dceddb1a22f53fb9a433d719"></a><a id="t.10"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c20 c156" colspan="3" rowspan="1">
<p class="c17"><span class="c33 c24">LabelInfoResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c129 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c148 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">printLabelsInfo</span></p>
</td>
<td class="c129" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-label-info">LabelInfo</a></span><span class="c24">[]</span></p>
</td>
<td class="c148" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Print labels info</span></p>
</td>
</tr>
<tr class="c14">
<td class="c56" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c129" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c148" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "labelsInfo”: [</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; {</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "parcelId": "50943123754",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "hubId": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "officeId": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "deadlineDay": 18,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "deadlineMonth": 2,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "tourId": 2203,</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "fullBarcode": "1000509431237540020002030017"</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; &nbsp; &nbsp; }</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; ]</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-label-inf-req-url"><span>2</span><span class="c66 c34">.2.9 Label Info Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get print label info, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print/labelInfo</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
 <p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.8880848b66bb90b015865e0ff34234757303d1e6"></a><a id="t.11"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">LabelInfoRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;id&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character.</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcels to get print label info for.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalCarrierParcels | external_carrier_parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;externalCarrierParcelId&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character.</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External carrier parcels to get print label info for.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-print-voucher-req"><span>2</span><span class="c34 c66">.2.10 Print Voucher Request (PrintVoucherRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print/voucher</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">PrintVoucherRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c109 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c68 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c67 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c30 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentIds</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String[]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment ids</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access. All shipments must have voucher request</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">printerName</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Printer name to be used for direct printing. Includes javascript in pdf to print document directly to the provided printer on document opening.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">format</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“pdf”, “zpl”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is pdf)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Output format</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dpi</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“dpi203”, “dpi300”]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is dpi203)</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Dpi used for rendering. Makes sense for zpl format, otherwise ignored</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; &nbsp; "shipmentIds": ["80002338331"]</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-print-voucher-resp"><span>2</span><span class="c66 c34">.2.11 Print Voucher Response (PrintVoucherResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The result content type is application/pdf.</span></p>
<p class="c2"><span class="c34">Content-type</span><span class="c16">: application/pdf</span></p>
<p class="c2"><span class="c16">And content contains pdf bytes.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">In case of an error, the content type is application/json.</span></p>
<p class="c2"><span class="c34">Content-type</span><span class="c16">:application/json</span></p>
<p class="c2"><span>And content is a JSON with </span><span class="c79"><a class="c40" href="#href-ds-errors">Error </a></span><span class="c16">structure.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-print-voucher-req-url"><span>2</span><span class="c66 c34">.2.12 Print Voucher Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to print vouchers, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/print/voucher</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">PrintVoucherRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">shipmentIds | shipment_ids</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String (comma separated shipment ids)</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment ids.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for allowed access. All shipments must have voucher request</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">printerName | printer_name</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Printer name to be used for direct printing. Includes javascript in pdf to print document directly to the provided printer on document opening.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h2 class="c74" id="href-track-and-trace-service"><span class="c35 c34">2.3 Track And Trace Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/track</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-track-req"><span>2</span><a id="kix.6spjytuaujdb"></a><span class="c66 c34">.3.1 Track Request (TrackRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/track</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.d4469386e653f7067f64e43d0c571c9dc9e6d256"></a><a id="t.12"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">TrackRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c109 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c68 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c67 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c30 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-track-shipment-parcel-ref">TrackShipmentParcelRef</a></span><span class="c7">[]</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcels to track</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">lastOperationOnly</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to return last operation only’</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-track-resp"><span>2</span><span class="c66 c34">.3.2 Track Response (TrackResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.544b9b13bd2b19edf6fe541633a70b57e461feb2"></a><a id="t.13"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">TrackResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c97 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c130 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c182 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c192 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c97" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c130" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-tracked-parcel">TrackedParcel</a></span><span class="c24">[]</span></p>
</td>
<td class="c182" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c192" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel track information</span></p>
</td>
</tr>
<tr class="c14">
<td class="c97" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c130" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c182" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c192" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-track-req-url"><span>2</span><span class="c66 c34">.3.3 Track Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to track parcels, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: </span><span class="c34">BASE_URL</span><span class="c16">/track</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<a id="t.4070f903070023986c3cef445774ea96867365df"></a><a id="t.14"></a>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">TrackRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;id&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character.</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel ids to track</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalCarrierParcels | external_carrier_parcels</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;externalCarrierParcelId&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character.</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External carrier parcel ids to track</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">refs</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format:</span></p>
<p class="c2"><span class="c7">&lt;ref&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels are separated with %7C (‘|’) character.</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Parcel references to search and track referred parcels</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">lastOperationOnly | last_opeartion_only</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
 </td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c113" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to return last operation only.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2"><span class="c34">BASE_URL</span><span class="c23">/track?username=test&amp;password=test&amp;language=EN&amp;client_system_id=9&amp;parcels=89981001249%7C89981001254&amp;last_opeartion_only=n</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-bulk-tracking-data-files-req"><span>2</span><span class="c66 c34">.3.4 Bulk Tracking Data Files Request (BulkTrackingDataFilesRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Bulk tracking data files are json files with file id assigned and contain data in format: </span><span class="c79 c24"><a class="c40" href="#href-ds-tracked-parcel">TrackedParcel</a></span><span class="c24">[]</span></p>
<p class="c2"><span class="c16">A greater file id corresponds to a later file publishing.</span></p>
<p class="c2"><span class="c16">This method is used to provide links for downloading published data files with tracking information.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c16">This method requires bulk tracking service enrolment, for which you may contact your key account manager.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/track/bulk</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">BulkTrackingDataFilesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c109 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c68 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c67 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c30 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c21" colspan="1" rowspan="1">
<p class="c2"><span class="c7">lastProcessedFileId</span></p>
</td>
<td class="c109" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c68" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The greatest data file id processed in client system. To get all published data files during last 10 days use 0 as lastProcessedFileId</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">The last processed file id must refer to a file published during last 10 days. Otherwise, error is returned.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-bulk-tracking-data-files-resp"><span>2</span><span class="c66 c34">.3.5 Bulk Tracking Data Files Response (BulkTrackingDataFilesResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">BulkTrackingDataFilesResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c97 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c130 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c182 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c192 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c97" colspan="1" rowspan="1">
<p class="c2"><span class="c7">files</span></p>
</td>
<td class="c130" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-bulk-traking-data-file">BulkTrackingDataFile</a></span><span class="c24">[]</span></p>
</td>
<td class="c182" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c192" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Bulk traking data files ordered by file id in ascending order. The geratest file id returned in this response is expected to be passed in next request for incremental processing</span></p>
</td>
</tr>
<tr class="c14">
<td class="c97" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c130" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c182" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c192" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-bulk-tracking-data-files-req-url"><span>2</span><span class="c66 c34">.3.6 Bulk Tracking Data Files Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get published bulk tracking file links, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">Bulk tracking data files are json files with file id assigned and contain data in format: </span><span class="c79 c24"><a class="c40" href="#href-ds-tracked-parcel">TrackedParcel</a></span><span class="c24">[]</span></p>
<p class="c2"><span class="c16">A greater file id corresponds to a later file publishing.</span></p>
<p class="c2"><span class="c16">This method is used to provide links for downloading published data files with tracking information.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c16">This method requires bulk tracking service enrolment, for which you may contact your key account manager.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: </span><span class="c34">BASE_URL</span><span class="c16">/track/bulk</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">BulkTrackingDataFilesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">last_processed_file_id</span></p>
</td>
<td class="c120" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c50" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c67" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The greatest data file id processed in client system. To get all published data files during last 10 days use 0 as lastProcessedFileId</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">The last processed file id must refer to a file published during last 10 days. Otherwise, error is returned.</span></p>
</td>
</tr>
</tbody>
</table>
<h2 class="c74" id="href-pickup-service"><span class="c35 c34">2.4 Pickup</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/pickup</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-pickup-req"><span>2</span><span class="c66 c34">.4.1 Pickup Request (PickupRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/pickup</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">PickupRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
 <td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupDateTime</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd'T'HH:mm:ssZ”)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup datetime. If not provided, it is assumed now. Seconds and milliseconds are ignored.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
 <tr class="c107">
<td class="c52" colspan="1" rowspan="1">
<p class="c2"><span class="c7">autoAdjustPickupDate</span></p>
</td>
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c24">Boolean</span></p>
</td>
<td class="c60" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default value is false)</span></p>
</td>
<td class="c60" colspan="1" rowspan="1">
<p class="c2"><span class="c7">To find first available date for pickup starting from pickupDate according to pickup schedule for services</span></p>
</td>
<td class="c60" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupScope</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“EXPLICIT_SHIPMENT_ID_LIST”,</span></p>
<p class="c2"><span class="c7">“ALL_CREATED_BY_LOGGED_USER”,</span></p>
<p class="c2"><span class="c7">“ALL_CREATED_BY_SAME_CLIENT”]</span></p>
<p class="c2"><span class="c7">“ALL_CREATED_BY_SAME_CONTRACT_USERS”]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Default is EXPLICIT_SHIPMENT_ID_LIST</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Scope of shipments to order.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ALL_CREATED_BY_SAME_CONTRACT_USERS can be used in case a logged user have the access rights to access shipments created by other users in the same contract.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">explicitShipmentIdList</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String[]</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Required when pickup scope is EXPLICIT_SHIPMENT_ID_LIST</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">visitEndTime</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String (format HH:ss)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
<p class="c2"><span class="c7">Example 9:30, or 11:35</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The last possible time when the address could be visited on the pickup date.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">contactName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phoneNumber</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ShipmentPhoneNumber</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Customer’s phone number.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "pickupDateTime":"2017-12-05T14:30:00+0200",</span></p>
<p class="c2"><span class="c96 c24 c34">&nbsp; "explicitShipmentIdList":[</span><span class="c24 c34 c96">"</span><span class="c96 c24 c34">80002338331</span><span class="c96 c24 c34">"</span><span class="c23">, "80002338159"],</span></p>
<p class="c2"><span class="c23">&nbsp; "visitEndTime": 18:20</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-pickup-resp"><span>2</span><span class="c66 c34">.4.2 Pickup Response (PickupResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">PickupResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">orders</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-pickup-order">PickupOrder</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup orders created</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-pickup-req-url"><span>2</span><span class="c66 c34">.4.3 Pickup Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to request a pickup, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/pickup</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">PickupRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupDateTime | pickup_date_time</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “dd.MM.yyyy HH:mm”)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup date time. If not provided it is assumed the current datetime.Seconds and milliseconds are ignored.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">autoAdjustPickupDate | auto_adjust_pickup_date | autoadjust_pickup_date</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default is false)</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">To find first available date for pickup starting from pickupDate according to pickup schedule for services</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupScope | pickup_scope</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“EXPLICIT_SHIPMENT_ID_LIST”,</span></p>
<p class="c2"><span class="c7">“ALL_CREATED_BY_LOGGED_USER”,</span></p>
<p class="c2"><span class="c7">“ALL_CREATED_BY_SAME_CLIENT”,</span></p>
<p class="c2"><span class="c7">“ALL_CREATED_BY_SAME_CONTRACT_USERS”]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Default is EXPLICIT_SHIPMENT_ID_LIST</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Scope of shipments to order.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ALL_CREATED_BY_SAME_CONTRACT_USERS can be used in case a logged user have the access rights to access shipments created by other users in the same contract.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">explicitShipmentIdList | explicit_shipment_id_list</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">(comma separated list of ids)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Required when pickup scope is EXPLICIT_SHIPMENT_ID_LIST</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">visitEndTime | visit_end_time</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String (format HH:ss)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The last possible time when the address could be visited on the pickup date.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">contactName | contact_name</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact name.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phoneNumber | phone_number</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Customer’s phone number.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid phone number.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phoneNumberExt | phone_number_ext</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Customer’s phone number extension.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid phone number extension.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/pickup?username=test&amp;password=test&amp;language=EN&amp;client_system_id=9&amp;pickup_date_time=2017-12-07T16%3A00%3A00%2B0200&amp;explicit_shipment_id_list=89981001489&amp;visit_end_time=19%3A00&amp;phone_number=123123&amp;pickup_scope=EXPLICIT_SHIPMENT_ID_LIST</span></p>
<h3 class="c12" id="href-pickup-terms-req"><span>2</span><a></a><span class="c66 c34">.4.4 Pickup Terms Request (PickupTermsRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/pickup/terms</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">PickupTermsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">serviceId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service Id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">startingDate</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd”)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The first date when the shipment will be ready for pickup. If not provided, it is assumed today.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Should not be a date before today</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">sender</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-sender">CalculationSender</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (If not specifed, logged user is used)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client and location for pickup.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderHasPayment</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to indicate, whether sender should pay at least one of courier service, declared value or packings.If this parameter is missing assumed value is - false.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-pickup-terms-resp"><span>2</span><a></a><span class="c66 c34">.4.5 Pickup Terms Response (PickupTermsResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p> 
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">PickupTermsResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">cutoffs</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DateTime<span class="c24">[]</span></span></p>
<p class="c2"><span class="c7">(format yyyy-MM-dd'T'HH:mm:ssZ)</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup cutoffs for next days. Pickup is not allowed for missing days in the result list</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-pickup-terms-req-url"><span>2</span><a></a><span class="c66 c34">.4.6 Pickup Terms Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to request pickup terms, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/pickup/terms</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">PickupTermsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">serviceId | service_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">int</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">startingDate | starting_date</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date</span></p>
<p class="c2"><span class="c7">(String in format “yyyy-MM-dd”)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The first date when the shipment will be ready for pickup. If not provided, it is assumed today.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Should not be a date before today</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation sender details</span></p>
<p class="c2"><span class="c25 c24">If logged user is the sender, you may skip providing sender details at all. </span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client’s id in sender_id parameter and other sender parameters may be skipped at all also.</span></p>
<p class="c2"><span class="c25 c24">Otherwise, sender_id should stay empty and it is required to provide as a minimum:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c162 c24">sender </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">sender address location or dropoffOfficeId</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderId | sender_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer Ð° sender</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for existence.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPrivatePerson | sender_private_person</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If sender_id is provided, it is forbidden. If the sender is the logged user, should be omitted too. Otherwise, it is mandatory</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender private person flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Sender Address Location Details</span></p>
<p class="c2"><span class="c25 c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-address-location">AddressLocation</a></span><span class="c25 c24"> for more details.</span></p>
<p class="c2"><span class="c25 c24">The sender address location is expected when sender_id is empty and sender_dropoff_office_id is empty and not required. In other words, the sender address location is required when the sender is not a referred customer or logged user and pickup at senderâs address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressCountryId | sender_address_country_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country ISO code. If not provided, the local country is assumed. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country code</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStateId | sender_address_state_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires state</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country state.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteId | sender_address_site_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Site id. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid site and value is required</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteType | sender_address_site_type</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for addresses of type 1 (local address)</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteName | sender_address_site_name</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressPostcode | senderAddressPostCode | sender_address_postcode</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dropoffOfficeId | dropOffOfficeId | senderDropoffOfficeId | senderDropOffOfficeId | dropoff_office_id | sender_dropoff_office_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if the sender is an internal customer. If sender address is provided, it is forbidden.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Drop off office id.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible office</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderHasPayment | sender_has_payment</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to indicate, whether sender should pay at least one of </span></p>
<p class="c2"><span class="c25 c24">courier service</span></p>
<p class="c2"><span class="c25 c24">declared value</span></p>
<p class="c2"><span class="c25 c24">or packings.</span></p>
<p class="c2"><span class="c7">If this parameter is missing assumed value is - false.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/pickup/terms?username=test&amp;password=test&amp;language=EN&amp;client_system_id=9&amp;starting_date=2017-12-07&amp;service_id=2002</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h2 class="c74" id="href-location-service"><span class="c35 c34">2.5 Location Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location</span></p>
<h3 class="c12" id="href-location-service-country"><span>2</span><span class="c66 c34">.5.1 Country</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed countries</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/country</span></p>
<h4 class="c12" id="href-get-country-req"><span>2</span><span class="c147 c34">.5.1.1 Get Country Request (GetCountryRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/country/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get country by id. Country id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetCountryRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
 <td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-country-resp"><span>2</span><span class="c147 c34">.5.1.2 Get Country Response (GetCountryResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetCountryResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">country</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-country">Country</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Found country or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-country-req-url"><span>2</span><span class="c147 c34">.5.1.3 Get Country Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get country by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/country/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetCountryRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/country/642?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-country-req"><span>2</span><span class="c147 c34">.5.1.4 Find Country Request (FindCountryRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/country</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find country using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindCountryRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country search term. Filters the results by country name prefix or part of country name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">isoAlpha2</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country iso alpha 2. Filters result by exact match if presents. ISO alpha 2 value uniquely identifies country and other criterias are not needed if this one presents</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">isoAlpha3</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country iso alpha 3. Filters result by exact match if presents. ISO alpha 3 value uniquely identifies country and other criterias are not needed if this one presents</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"ROMA"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-country-resp"><span>2</span><span class="c147 c34">.5.1.5 Find Country Response (FindCountryResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The countries in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">Country name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">Country name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindCountryResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countries</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-country">Country</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of countries</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-country-req-url"><span>2</span><span class="c147 c34">.5.1.6 Find Country Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find country, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/country</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindCountryRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country search term. Filters the results by country name prefix or part of country name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">isoAlpha2 | iso_alpha2</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country iso alpha 2. Filters result by exact match if presents. ISO alpha 2 value uniquely identifies country and other criterias are not needed if this one presents</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">isoAlpha3 | iso_alpha3</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Country iso alpha 3. Filters result by exact match if presents. ISO alpha 3 value uniquely identifies country and other criterias are not needed if this one presents</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/country/?username=test&amp;password=test&amp;name=ro</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-countries-req"><span>2</span><span class="c147 c34">.5.1.7 Get All Countries Request (GetAllCountriesRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/country/csv</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all countries as csv file</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllCountriesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
 </td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-countries-resp"><span>2</span><span class="c147 c34">.5.1.8 Get All Countries Response (GetAllCountriesResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-country">Country</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>id</b> - ISO country id</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - Country name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - Country name in English</span></li>
<li class="c2 c36"><span class="c16"><b>isoAlpha2</b> - ISO alpha 2 code</span></li>
<li class="c2 c36"><span class="c16"><b>isoAlpha3</b> - ISO alpha 3 code</span></li>
<li class="c2 c36"><span class="c16"><b>postCodeFormats</b> - all allowed postcode patterns are separated with comma and the whole value is escaped with quotation marks</span></li>
<li class="c2 c36"><span class="c16"><b>requireState</b> - flag whether country requires state</span></li>
<li class="c2 c36"><span class="c16"><b>addressType</b> - address type (1 or 2) for this country (see ShipmentAddress)</span></li>
<li class="c2 c36"><span class="c16"><b>currencyCode</b> - current active currency code used for COD</span></li>
<li class="c2 c36"><span class="c16"><b>defaultOfficeId</b> - default office id</span></li>
<li class="c2 c36"><span class="c16"><b>streetTypes</b> - comma separated list of all street types escaped with quotation marks in local language. This value is applicable for addressType 1 only</span></li>
<li class="c2 c36"><span class="c16"><b>streetTypesEn</b> - comma separated list of all street types escaped with quotation marks in English. This value is applicable for addressType 1 only</span></li>
<li class="c2 c36"><span class="c16"><b>complexTypes</b> - comma separated list of all complex types escaped with quotation marks in local language. This value is applicable for addressType 1 only</span></li>
<li class="c2 c36"><span class="c16"><b>complexTypesEn</b> - comma separated list of all complex types escaped with quotation marks in English. This value is applicable for addressType 1 only</span></li>
<li class="c2 c36"><span class="c16"><b>siteNomen</b> - site nomenclature (0, 1 ,2)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-countries-req-url"><span>2</span><span class="c147 c34">.5.1.9 Get All Countries Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all countries as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/country</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllCountriesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/country/csv?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-state"><span>2</span><span class="c66 c34">.5.2 State</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed states</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/state</span></p>
<h4 class="c12" id="href-get-state-req"><span>2</span><span class="c147 c34">.5.2.1 Get State Request (GetStateRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/state/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get state by id. State id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetStateRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p> 
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-state-resp"><span>2</span><span class="c147 c34">.5.2.2 Get State Response (GetStateResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetStateResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">site</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-state">State</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">State found or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-state-req-url"><span>2</span><span class="c147 c34">.5.2.3 Get State Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get state by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/state/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Site id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetStateRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td> 
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/state/CA-AB?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-state-req"><span>2</span><span class="c147 c34">.5.2.4 Find State Request (FindStateRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/state</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find state using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindStateRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for state name. Filters the results by state name prefix or part of state name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "countryId":840,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-state-resp"><span>2</span><span class="c147 c34">.5.2.5 Find State Response (FindStateResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The states in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">State name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">State name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindStateResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">states</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-state">State</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of sites</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-state-req-url"><span>2</span><span class="c147 c34">.5.2.6 Find State Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find site, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/state</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindStateRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId | country_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for state name. Filters the results by state name prefix or part of state name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/state/?username=test&amp;password=test&amp;country_id=840&amp;name=a</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-states-req"><span>2</span><span class="c147 c34">.5.2.7 Get All States Request (GetAllStatesRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/state/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all states for a country in csv file. Country id is specified as path parameter</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllStatesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-states-resp"><span>2</span><span class="c147 c34">.5.2.8 Get All States Response (GetAllStatesResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-state">State</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>id</b> - state id</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - state name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - state name in English</span></li>
<li class="c2 c36"><span class="c16"><b>isoAlpha</b> - ISO alpha code</span></li>
<li class="c2 c36"><span class="c16"><b>countryId</b> - country id (ISO code)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-states-req-url"><span>2</span><span class="c147 c34">.5.2.9 Get All States Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all states as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/state/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllStatesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
 <td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/state/csv/840?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-site"><span>2</span><span class="c66 c34">.5.3 Site</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed sites</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/site</span></p>
<h4 class="c12" id="href-get-site-req"><span>2</span><span class="c147 c34">.5.3.1 Get Site Request (GetSiteRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/site/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get site by id. Site id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetSiteRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-site-resp"><span>2</span><span class="c147 c34">.5.3.2 Get Site Response (GetSiteResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetSiteResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">site</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-site">Site</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Found site or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-site-req-url"><span>2</span><span class="c147 c34">.5.3.3 Get Site Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get site by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/site/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Site id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetSiteRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/site/642279132?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-site-req"><span>2</span><span class="c147 c34">.5.3.4 Find Site Request (FindSiteRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/site</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find site using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindSiteRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for site name. Filters the results by site name prefix or part of site name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">postCode</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by postcode - valid postcode for site</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">type</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by site type (exact match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">municipality</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter by municipality (prefix match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">region</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Filter by region (prefix match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "countryId":642,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-site-resp"><span>2</span><span class="c147 c34">.5.3.5 Find Site Response (FindSiteResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The sites in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">Site name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">Site name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindSiteResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">sites</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-site">Site</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of sites</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-site-req-url"><span>2</span><span class="c147 c34">.5.3.6 Find Site Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find site, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/site</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindSiteRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId | country_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for site name. Filters the results by site name prefix or part of site name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">postcode | postCode | post_code</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by postcode - valid postcode for site</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">type</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by site type (exact match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">municipality</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter by municipality (prefix match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">region</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter by region (prefix match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/site/?username=test&amp;password=test&amp;country_id=642&amp;name=a</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-sites-req"><span>2</span><span class="c147 c34">.5.3.7 Get All Sites Request (GetAllSitesRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/site/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all sites for a country in csv file. Country id is specified as path parameter</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllSitesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-sites-resp"><span>2</span><span class="c147 c34">.5.3.8 Get All Sites Response (GetAllSitesResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-site">Site</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>id</b> - site id</span></li>
<li class="c2 c36"><span class="c16"><b>countryId</b> - country id (ISO code)</span></li>
<li class="c2 c36"><span class="c16"><b>mainSiteId</b> - reference to main site if this site is a "satellite" one</span></li>
<li class="c2 c36"><span class="c16"><b>type</b> - site type in local language</span></li>
<li class="c2 c36"><span class="c16"><b>typeEn</b> - site type in English</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - site name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - site name in English</span></li>
<li class="c2 c36"><span class="c16"><b>municipality</b> - municipality in local language</span></li>
<li class="c2 c36"><span class="c16"><b>municipalityEn</b> - municipality in English</span></li>
<li class="c2 c36"><span class="c16"><b>region</b> - region in local language</span></li>
<li class="c2 c36"><span class="c16"><b>regionEn</b> - region in English</span></li>
<li class="c2 c36"><span class="c16"><b>postCode</b> - default post code for this site (if any)</span></li>
<li class="c2 c36"><span class="c16"><b>addressNomenclature</b> - code for address nomenclature (streets, complexes, blocks, poi) support. Values are: 0 - no address nomenclature, 1 - partial address nomenclature, 2 - full address nomenclature</span></li>
<li class="c2 c36"><span class="c16"><b>x</b> - X (longitude) coordinate of site center</span></li>
<li class="c2 c36"><span class="c16"><b>y</b> - Y (latitude) coordinate of site center</span></li>
<li class="c2 c36"><span class="c16"><b>servingDays</b> - serving days for this site. Format: 7 serial digits (0 or 1) where each digit corresponds to a day in week (the first digit corresponds to Monday, the second to Tuesday and so on). Value of '0' (zero) means that the site is not served by Speedy on this day while '1' (one) means that it is served. (Example: the text "0100100" means that the site is served on Tuesday and Friday only.)</span></li>
<li class="c2 c36"><span class="c16"><b>servingOfficeId</b> - Site's serving office</span></li>
<li class="c2 c36"><span class="c16"><b>servingHubOfficeId</b> - The hub office ID to which serving office is connected</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-sites-req-url"><span>2</span><span class="c147 c34">.5.3.9 Get All Sites Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all sites as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/site/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllSitesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/site/csv/642?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-street"><span>2</span><span class="c66 c34">.5.4 Street</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed streets</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/street</span></p>
<h4 class="c12" id="href-get-street-req"><span>2</span><span class="c147 c34">.5.4.1 Get Street Request (GetStreetRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/street/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get street by id. Street id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetStreetRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-street-resp"><span>2</span><span class="c147 c34">.5.4.2 Get Street Response (GetStreetResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetStreetResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">street</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-street">Street</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Found street or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-street-req-url"><span>2</span><span class="c147 c34">.5.4.3 Get Street Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get street by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/street/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Street id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetStreetRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/street/642075720?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-street-req"><span>2</span><span class="c147 c34">.5.4.4 Find Street Request (FindStreetRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/street</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find street using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindStreetRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for street name. Filters the results by street name prefix or part of street name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">type</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by street type (exact match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "siteId":642279132,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>

<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-street-resp"><span>2</span><span class="c147 c34">.5.4.5 Find Street Response (FindStreetResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The streets in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">Street name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">Street name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindStreetResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">streets</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-street">Street</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of streets</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-street-req-url"><span>2</span><span class="c147 c34">.5.4.6 Find Street Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find street, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/street</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindStreetRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for street name. Filters the results by street name prefix or part of street name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">type</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by street type (exact match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/street/?username=test&amp;password=test&amp;site_id=642279132&amp;name=a</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-streets-req"><span>2</span><span class="c147 c34">.5.4.7 Get All Streets Request (GetAllStreetsRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/street/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all streets for a country in csv file. Country id is specified as path parameter.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllStreetsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-streets-resp"><span>2</span><span class="c147 c34">.5.4.8 Get All Streets Response (GetAllStreetsResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-street">Street</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>id</b> - street id</span></li>
<li class="c2 c36"><span class="c16"><b>siteId</b> - site id</span></li>
<li class="c2 c36"><span class="c16"><b>type</b> - street type in local language</span></li>
<li class="c2 c36"><span class="c16"><b>typeEn</b> - street type in English</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - street name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - street name in English</span></li>
<li class="c2 c36"><span class="c16"><b>actualId</b> - actual street id (in case this street is renamed)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-streets-req-url"><span>2</span><span class="c147 c34">.5.4.9 Get All Streets Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all streets as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/street/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllStreetsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/street/csv/642?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-complex"><span>2</span><span class="c66 c34">.5.5 Complex</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed complexes</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/complex</span></p>
<h4 class="c12" id="href-get-complex-req"><span>2</span><span class="c147 c34">.5.5.1 Get Complex Request (GetComplexRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/complex/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get complex by id. Complex id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetComplexRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-complex-resp"><span>2</span><span class="c147 c34">.5.5.2 Get Complex Response (GetComplexResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetComplexResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">complex</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-complex">Complex</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex found or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-complex-req-url"><span>2</span><span class="c147 c34">.5.5.3 Get Complex Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get complex by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/complex/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Complex id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetComplexRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/complex/1?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-complex-req"><span>2</span><span class="c147 c34">.5.5.4 Find Complex Request (FindComplexRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/complex</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find complex using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindComplexRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for complex name. Filters the results by complex name prefix or part of complex name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">type</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by complex type (exact match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "siteId":100,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-complex-resp"><span>2</span><span class="c147 c34">.5.5.5 Find Complex Response (FindComplexResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The complexes in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">Complex name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">Complex name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindComplexResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">complexes</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-complex">Complex</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of complexes</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-complex-req-url"><span>2</span><span class="c147 c34">.5.5.6 Find Complex Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find complex, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/complex</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindComplexRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for complex name. Filters the results by xomplex name prefix or part of xomplex name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">type</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filter results by complex type (exact match)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/complex/?username=test&amp;password=test&amp;site_id=100&amp;name=a</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-complexes-req"><span>2</span><span class="c147 c34">.5.5.7 Get All Complexes Request (GetAllComplexesRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/complex/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all complexes for a country in csv file. Country id is specified as path parameter.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllComplexesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-complexes-resp"><span>2</span><span class="c147 c34">.5.5.8 Get All Complexes Response (GetAllComplexesResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-complex">Complex</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>id</b> - street id</span></li>
<li class="c2 c36"><span class="c16"><b>siteId</b> - site id</span></li>
<li class="c2 c36"><span class="c16"><b>type</b> - street type in local language</span></li>
<li class="c2 c36"><span class="c16"><b>typeEn</b> - street type in English</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - street name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - street name in English</span></li>
<li class="c2 c36"><span class="c16"><b>actualId</b> - actual street id (in case this street is renamed)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-complexes-req-url"><span>2</span><span class="c147 c34">.5.5.9 Get All Complexes Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all complexes as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/complex/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllComplexesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1"> 
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/complex/csv/642?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-block"><span>2</span><span class="c66 c34">.5.6 Block</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed blocks</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/block</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-block-req"><span>2</span><span class="c147 c34">.5.6.1 Find Block Request (FindBlockRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/block</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find block using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindBlockRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for block name. Filters the results by block name prefix or part of block name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "siteId":10135,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-block-resp"><span>2</span><span class="c147 c34">.5.6.2 Find Block Response (FindBlockResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The blocks in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">Block name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">Block name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindBlockResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">blocks</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-block">Block</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of blocks</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
 <p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-block-req-url"><span>2</span><span class="c147 c34">.5.6.3 Find Block Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find block, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/block</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindBlockRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for block name. Filters the results by block name prefix or part of block name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/block/?username=test&amp;password=test&amp;site_id=10135&amp;name=a</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-blocks-req"><span>2</span><span class="c147 c34">.5.6.4 Get All Blocks Request (GetAllBlocksRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/block/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all blocks for a country in csv file. Country id is specified as path parameter.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllBlockRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-blocks-resp"><span>2</span><span class="c147 c34">.5.6.5 Get All Blocks Response (GetAllBlocksResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-block">Block</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>siteId</b> - site id</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - block name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - block name in English</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-blocks-req-url"><span>2</span><span class="c147 c34">.5.6.6 Get All Blocks Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all blocks as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/block/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllBlocksRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/block/csv/100?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-poi"><span>2</span><span class="c66 c34">.5.7 POI (Point of Interest)</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed points of interest</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/poi</span></p>
<h4 class="c12" id="href-get-poi-req"><span>2</span><span class="c147 c34">.5.7.1 Get POI Request (GetPOIRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/poi/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get POI by id. POI id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetPOIRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-poi-resp"><span>2</span><span class="c147 c34">.5.7.2 Get POI Response (GetPOIResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetPOIResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">poi</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-poi">PointOfInterest</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">POI found or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-poi-req-url"><span>2</span><span class="c147 c34">.5.7.3 Get POI Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get POI by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/poi/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">POI id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetPOIRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/poi/1?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-poi-req"><span>2</span><span class="c147 c34">.5.7.4 Find POI Request (FindPOIRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/poi</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find POI using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindPOIRequest</span></p>
</td>
 </tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for POI name. Filters the results by POI name prefix or part of POI name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "siteId":100,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-poi-resp"><span>2</span><span class="c147 c34">.5.7.5 Find POI Response (FindPOIResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The points of interest in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">POI name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">POI name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The result is limited to 10 records.</p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindPOIResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pois</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-poi">PointOfInterest</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of points of interest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-poi-req-url"><span>2</span><span class="c147 c34">.5.7.6 Find POI Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find POI, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/poi</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindPOIRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for POI name. Filters the results by POI name prefix or part of POI name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/poi/?username=test&amp;password=test&amp;site_id=100&amp;name=a</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-poi-req"><span>2</span><span class="c147 c34">.5.7.7 Get All Points of Interest Request (GetAllPOIRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/poi/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all Points of Interest for a country in csv file. Country id is specified as path parameter.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllPOIRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-poi-resp"><span>2</span><span class="c147 c34">.5.7.8 Get All Points of Interest Response (GetAllPOIResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">See </span><span class="c79 c24"><a class="c40" href="#href-ds-poi">PointOfInterest</a></span> data structure for additional information.</p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>id</b> - POI id</span></li>
<li class="c2 c36"><span class="c16"><b>siteId</b> - site id</span></li>
<li class="c2 c36"><span class="c16"><b>name</b> - POI name in local language</span></li>
<li class="c2 c36"><span class="c16"><b>nameEn</b> - POI name in English</span></li>
<li class="c2 c36"><span class="c16"><b>address</b> - POI address in local language</span></li>
<li class="c2 c36"><span class="c16"><b>addressEn</b> - POI address in English</span></li>
<li class="c2 c36"><span class="c16"><b>x</b> - X coordinate</span></li>
<li class="c2 c36"><span class="c16"><b>y</b> - Y coordinate</span></li>
<li class="c2 c36"><span class="c16"><b>type</b> - POI type in local language</span></li>
<li class="c2 c36"><span class="c16"><b>typeEn</b> - POI type in English</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-poi-req-url"><span>2</span><span class="c147 c34">.5.7.9 Get All Points of Interest Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all Points of Interest as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/poi/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2"><span class="c16">This method requires a license (additional licensing contract) and permissions (access rights).</span></p>
<p class="c2"><span class="c16">To obtain such license please contact your key account manager.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllPOIRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/poi/csv/100?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-postcodes"><span>2</span><span class="c66 c34">.5.8 Postcodes</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for allowed country postcodes</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/postcode</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-postcodes-req"><span>2</span><span class="c147 c34">.5.8.1 Get All Postcodes Request (GetAllPostcodesRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/postcode/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get all postcodes for a country in csv file. Country id is specified as path parameter.</span></p>

<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetAllPostcodesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-postcodes-resp"><span>2</span><span class="c147 c34">.5.8.2 Get All Postcodes Response (GetAllPostcodesResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Response is CSV (comma separated) file int UTF8 encoding. The format is:</span></p>
<ul class="c92 lst-kix_h7igyyxripfi-0 start">
<li class="c2 c36"><span class="c16"><b>postcode</b> - Postcode</span></li>
<li class="c2 c36"><span class="c16"><b>siteId</b> - site id</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-all-postcodes-req-url"><span>2</span><span class="c147 c34">.5.8.3 Get All Postcodes Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get all postcodes as CSV file (UTF8 encoded), providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/postcode/csv/<b>{countryId}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Country id is is specified as a path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetAllPostcodesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/postcodes/csv/642?username=test&amp;password=test</span></p>
<h3 class="c12" id="href-location-service-office"><span>2</span><span class="c66 c34">.5.9 Office</span></h3>
<p class="c2 c3"><span class="c16">This section specifies methods to query system for available offices</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/location/office</span></p>
<h4 class="c12" id="href-get-office-req"><span>2</span><span class="c147 c34">.5.9.1 Get Office Request (GetOfficeRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/office/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get office by id. Office id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetOfficeRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
 </td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-office-resp"><span>2</span><span class="c147 c34">.5.9.2 Get Office Response (GetOfficeResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetOfficeResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">office</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-office">Office</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Office found or null if not found</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-get-office-req-url"><span>2</span><span class="c147 c34">.5.9.3 Get Office Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get office by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/office/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Office id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetOfficeRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/office/2?username=test&amp;password=test</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-office-req"><span>2</span><span class="c147 c34">.5.9.4 Find Office Request (FindOfficeRequest)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/office</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Find office using search criteria</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">FindOfficeRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id ISO. Limits the search scope in the set of offices for specified country. System default country is used if country id is omitted. If -1 is specified - offices in all countires are searched</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id. Limits the search scope in the set of offices for specified site. If omitted - all country offices are searched</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filters the results by office site name prefix or part of it.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for office name. Filters the results by office name prefix or part of site name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">limit</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The number of records to return in response. All records are returned if this parameter is ommited</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example JSON:</span></p>
<p class="c2"><span class="c23">{</span></p>
<p class="c2"><span class="c23">&nbsp; "userName":"testUser",</span></p>
<p class="c2"><span class="c23">&nbsp; "password":"password",</span></p>
<p class="c2"><span class="c23">&nbsp; "countryId":642,</span></p>
<p class="c2"><span class="c23">&nbsp; "name":"A"</span></p>
<p class="c2"><span class="c23">}</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-office-resp"><span>2</span><span class="c147 c34">.5.9.5 Find Office Response (FindOfficeResponse)</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span>The offices in return are these that match search criteria in request and ordered by:</p>
<ul class="c92 start">
<li class="c2 c36"><span class="c16">Exact match is on top, followed by</span></li>
<li class="c2 c36"><span class="c16">Office name prefix matches, followed by</span></li>
<li class="c2 c36"><span class="c16">Office name contains matches (search term is in the name but not a prefix)</span></li>
</ul>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">FindOfficeResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">offices</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-office">Office</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Array of offices</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h4 class="c12" id="href-find-office-req-url"><span>2</span><span class="c147 c34">.5.9.6 Find Office Request - URL (GET) schema</span></h4>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to find office, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/location/office</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">FindOfficeRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId | country_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id ISO. Limits the search scope in the set of offices for specified country. System default country is used if country id is omitted. If -1 is specified - offices in all countires are searched.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id.Limits the search scope in the set of offices for specified site. If omitted - all country offices are searched</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteName | site_name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Filters the results by office site name prefix or part of it</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">name</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Search term for office name. Filters the results by office name prefix or part of office name.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
 <tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">limit</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The number of records to return in response. All records are returned if this parameter is ommited</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Example:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c23">BASE_URL/location/office/?username=test&amp;password=test&amp;country_id=642&amp;name=a</span></p>
<h2 class="c74" id="href-calculation-service"><span class="c35 c34">2.6 Calculation Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/calculate</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-calculation-req"><span>2</span><span class="c66 c34">.6.1 Calculation Request (CalculationRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/calculate</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">CalculationRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
 </tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">sender</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-sender">CalculationSender</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the pickup place. If not specified, the logged user location is considered as a sender location.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipient</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-recipient">CalculationRecipient</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the recipient delivery place.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">service</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-service">CalculationService</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Defines service agreemen</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">content</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-content">CalculationContent</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines content - parcels, weight and etc</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">payment</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-payment">ShipmentPayment</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines who-pays-what in shipment</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-calculation-resp"><span>2</span><span class="c66 c34">.6.2 Calculation Response (CalculationResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">CalculationResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr> 
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">calculations</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-result">CalculationResult[]</a></span><span class="c24">[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Calculations for all service ids in request</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-calculation-req-url"><span>2</span><span class="c66 c34">.6.3 Calculation Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to calculate, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/calculate</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">CalculationRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation sender details</span></p>
<p class="c2"><span class="c25 c24">If logged user is the sender, you may skip providing sender details at all. </span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client’s id in sender_id parameter and other sender parameters may be skipped at all also.</span></p>
<p class="c2"><span class="c25 c24">Otherwise, sender_id should stay empty and it is required to provide as a minimum:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c162 c24">sender </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">sender address location or dropoffOfficeId</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderId | sender_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer Ð° sender</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for existence.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPrivatePerson | sender_private_person</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If sender_id is provided, it is forbidden. If the sender is the logged user, should be omitted too. Otherwise, it is mandatory</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender private person flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Sender Address Location Details</span></p>
<p class="c2"><span class="c25 c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-address-location">AddressLocation</a></span><span class="c25 c24"> for more details.</span></p>
<p class="c2"><span class="c25 c24">The sender address location is expected when sender_id is empty and sender_dropoff_office_id is empty and not required. In other words, the sender address location is required when the sender is not a referred customer or logged user and pickup at senderâs address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressCountryId | sender_address_country_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Country ISO code. If not provided, the local country is assumed. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country code</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStateId | sender_address_state_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires state</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country state.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteId | sender_address_site_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid site and value is required</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteType | sender_address_site_type</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for addresses of type 1 (local address)</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteName | sender_address_site_name</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressPostcode | senderAddressPostCode | sender_address_postcode</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires post code</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dropoffOfficeId | dropOffOfficeId | senderDropoffOfficeId | senderDropOffOfficeId | dropoff_office_id | sender_dropoff_office_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if the sender is an internal customer. If sender address is provided, it is forbidden.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Drop off office id.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible office</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">sender_geo_pudo_id | senderGeoPUDOId | dropoff_geo_pudo_id | dropoffGeoPUDOId</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No. Must be empty if dropoffOfficeId is provided</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DPD drop off office PUDO id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible DPD office.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation recipient details</span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client's id in recipient_id parameter and other recipient parameters may be skipped at all </span></p>
<p class="c2"><span class="c25 c24">Otherwise, recipient_id should stay empty and it is required to provide as a minimum:.</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c162 c24">recipient </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">recipient address location or pickupOfficeId</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientId | recipient_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer Ð° recipient</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for existence.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPrivatePerson | recipient_private_person</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If recipient_id is provided, it is forbidden. Otherwise, it is mandatory</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient private person flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Recipient Address Location Details</span></p>
<p class="c2"><span class="c25 c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-address-location">AddressLocation</a></span><span class="c25 c24"> for more details.</span></p>
<p class="c2"><span class="c25 c24">The recipient address location is expected when recipient_id is empty and recipient_pickup_office_id is empty and not required. In other words, the recipient address location is required when the recipient is not a referred customer and delivery at recipientâs address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressCountryId | recipient_address_country_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Country ISO code. If not provided, the local country is assumed. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country code</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStateId | recipient_address_state_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires state</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country state.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteId | recipient_address_site_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid site and value is required</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteType | recipient_address_site_type</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for addresses of type 1 (local address)</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteName | recipient_address_site_name</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressPostcode | recipientAddressPostCode | recipient_address_postcode</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires post code</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupOfficeId | pickUpOfficeId | recipientPickupOfficeId | recipientPickUpOfficeId | pickup_office_id | recipient_pickup_office_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if the recipient is an internal customer. If recipient address is provided, it is forbidden.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup office id.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible office</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipient_geo_pudo_id | recipientGeoPUDOId | pickup_geo_pudo_id | pickupGeoPUDOId</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No. Must be empty if pickupOfficeId is provided</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DPD pickup office PUDO id</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible DPD office.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation Service Details</span></p>
<p class="c2"><span class="c25 c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-service">CalculationService</a></span><span class="c25 c24"> for more details.</span></p>
<p class="c2"><span class="c25 c24">Shipment service defines agreement with customer for courier service. This includes:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c162 c24">Pickup date </span></li>
<li class="c2 c36"><span class="c25 c24">Service ids (codes)</span></li>
<li class="c2 c36"><span class="c25 c24">Optional defer days or saturday delivery</span></li>
<li class="c2 c36"><span class="c25 c24">Additional services (like COD, Declared value,and etc.)</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupDate | pickup_date</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (date) Example: â2018-01-22"</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default value is today)</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">The date for shipment pick-up</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Could be today or a future date.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">autoAdjustPickupDate | auto_adjust_pickup_date | autoadjust_pickup_date</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default is false)</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">To find first available date for pickup starting from pickupDate according to pickup schedule for services</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">serviceIds | service_ids</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String (comma separated service ids)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Service ids to get calculation for.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Each service id (code) should be valid for destination</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">deferredDays | deferred_days</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default value is 0)</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This parameter allowscusers to specify by how many (business) days they would like to postpone the shipment delivery from the standard term..</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Allowed values are 0, 1 and 2</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">saturdayDelivery | saturday_delivery</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No)</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This parameter may adjust the delivery date to the first business day, if the standard calculated delivery day is a half-working day. If not specified, system will determine this flag based on configured recipient working schedule.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">COD Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-cod">ShipmentCODAdditionalService</a></span><span class="c24">.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codAmount | cod_amount</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">double</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment COD base amount.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against maximum allowed amounts for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codCurrency | cod_currency</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is the currency code of the destination country)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment COD currency code.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against allowed currency code of destination country.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codProcessingType | cod_processing_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“CASH”, “POSTAL_MONEY_TRANSFER”]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(default is “CASH”)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines COD processing type.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Appropriate contract and annexes may be required.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codPayoutThirdParty | cod_payout_third_party</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If this flag is set, the COD is paid to a third party (not to the &nbsp;sender).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires the third party to be the payer of the courier service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">codWithShippingPrice | cod_with_shipping_price</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag indicating whether the shipping price should be included in the COD.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Options before payment details Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-obpd">ShipmentOBPD</a></span><span class="c7">.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">obpd_option</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“OPEN”, “TEST”]</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(For certain destinations could be required.)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines option to be used.</span></p>
<p class="c2"><span class="c7">Open parcels before payment or open and test parcels before payment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment is validated for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">obpd_return_service_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(For certain destinations could be required.)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines service id to be used on return, if COD payment is refused.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment is validated for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">obpd_return_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[“SENDER”, “RECIPIENT”, “THIRD_PARTY”]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">(For certain destinations could be required.)</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines who pays the return shipment, if COD payment is refused.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Return shipment is validated for destination.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Declared Value (Extended Liability) Additional Service</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-add-services-ins">ShipmentDeclaredVaueAdditionalService</a></span><span class="c7">.</span></p>
<p class="c2"><span class="c24">Declared value payer is required when declared value amount is provided and is set in payment section.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValueAmount | declared_value_amount</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">double</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment Declared Value (extended liability) base amount. Declared value amount is always in local system currency.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against maximum allowed amounts.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fragile | declaredValueFragile | declared_value_fragile</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines fragile flag for shipment content.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Fragile shipments requires declared value sub service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValueIgnoreIfNotApplicable | declared_value_ignore_if_not_applicable</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to ignore declared value additional service in case it is not applicable for shipment on calculation</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">E-shops usually configure declared value (extended liability) by default for their shipments, However there are some certain internal rules when this option is not available. The flag is used in calculation service to provide price to end clients without repeating the calculation request with removed additional service</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Fixed Time Delivery Additional Service</span></p>
<p class="c2"><span class="c7">Fixed time delivery is an additional service that provides instruction to deliver shipment at a certain time on the delivery date.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fixedTimeDelivery | fixed_time_delivery</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This option fixes the time of delivery on the delivery date. 1130 - means 11:30</span></p>
<p class="c2"><span class="c7">920 - means 09:20</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This option is checked against configured allowed time frame for the service.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Special Delivery Additional Service</span></p>
<p class="c2"><span class="c7">Special delivery is an additional service that provides instruction to the courier to do additional (special) checks and actions on delivery. These checks and actions are negotiated and contracted in a special delivery annex. For example, the courier could be instructed to check IDs of recipient party at delivery.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">specialDeliveryId | special_delivery_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Specifies special delivery identifier for the shipments. Identifiers are determined in a special delivery annex.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Requires annex for special delivery.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Delivery to Floor Additional Service</span></p>
<p class="c2"><span class="c7">Delivery to floor is an additional service that provides instruction to the courier that the shipment should not be delivered to the entrance of a multi floor building, but should be moved to a certain floor before delivery.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">deliveryToFloor | delivery_to_floor</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Specifies the floor number in the building where to deliver shipment.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">This additional service requires annex.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation Content</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-content">CalculationContent</a></span><span class="c7">.</span></p>
<p class="c2"><span class="c24">Defines what is to be delivered with the shipment.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcelsCount | parcels_count</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required when parcels list is empty</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Total shipmentâs parcels count. Ignored, if parcels list is not empty. The parcels count is the number of parcels in the lits in that case</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against minimum and maximum allowed for the service</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">totalWeight | total_weight</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required when parcels list is empty</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Total weight declared for the shipment. Ignored, if parcels list is not empty. The total weight is the sum of all parcelâs weight in that case.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against minimum and maximum allowed for the service</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">documents</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean (true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Documents flag of the shipment</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">palletized</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean (true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Palletized flag of the shipment</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">parcels</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
<p class="c2"><span class="c7">Format for single parcel is:</span></p>
<p class="c2"><span class="c7">&lt;seqNo&gt;,&lt;weight&gt;,</span></p>
<p class="c2"><span class="c7">&lt;width&gt;x&lt;depth&gt;x&lt;height&gt;,</span></p>
<p class="c2"><span class="c7">&lt;packageUniqueNumber&gt;,</span></p>
<p class="c2"><span class="c7">&lt;id&gt;,</span></p>
<p class="c2"><span class="c7">&lt;externalCarrierParcelNumber&gt;</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c7">Multiple parcels should be separated with %7C (‘|’) character.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-content-parcel">ShipmentParcel</a></span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required for pallet and postal services. For multiple parcels add the same url parameter again. The parameters are parsed in the order of their occurrence. If the sequence is incomplete, the missing parameters are considered empty.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">List of parcels. If provided, parcel_count and total_weight are ignored</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against service configuration and pickup and delivery capacity of the depots and the couriers.</span></p>
</td>
</tr>
 <tr class="c14">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Shipment Payment</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-payment">ShipmentPayment</a></span><span class="c7">.</span></p>
<p class="c2"><span class="c24">Defines who-pays-what in shipment and other payment parameters.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">courierServicePayer | courier_service_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Courier service payer.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against the service, destination, contracts and annexes.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">declaredValuePayer | declared_value_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Declared value payer. If not provided, the courier service payer is assumed. Not expected, if the declared value amount is empty.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against the service, destination, contracts and annexes.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">packagePayer | package_payer</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">enum</span></p>
<p class="c2"><span class="c7">[ "SENDER", "RECIPIENT", "THIRD_PARTY" ]</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Package payer. If not provided, the courier service payer is assumed.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against the service, destination, contracts and annexes.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">thirdPartyClientId | third_party_client_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines shipment third party - used as a payer of any of shipment payable components.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Third party customer should be registered customer with valid contract and annex for delayed payment at pickup date. Third party customer should be customer(object) in the same contract as the logged user.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Discount card</span></p>
<p class="c2"><span class="c24">For more information see </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-payment-discount-card">ShipmentDiscountCardId</a></span><span class="c7">.</span></p>
<p class="c65"><span class="c24">Discount cards provide promotional discounts.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">discountCardContractId | discount_card_contract_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Discount card contract id.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against a referred contract.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">discountCardId | discount_card_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Discount card id for contract.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against a referred discount card.</span></p>
</td>
</tr>
</tbody>
</table>
<h2 class="c74" id="href-client-service"><span class="c35 c34">2.7 Client Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/client</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-client-req"><span>2</span><span class="c66 c34">.7.1 Get Client Request (GetClientRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
 <p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get client by id. Client id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetClientRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-client-resp"><span>2</span><span class="c66 c34">.7.2 Get Client Response (GetClientResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetClientResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">client</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-client">Client</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-client-req-url"><span>2</span><span class="c66 c34">.7.3 Get Client Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get client by id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">Client id is provided as URL path paramter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetClientRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-contract-clients-req"><span>2</span><span class="c66 c34">.7.4 Get Contract Clients Request (GetContractClientsRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contract</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get clients with same contract as logged user's one, if any</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetContractClientsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-contract-clients-resp"><span>2</span><span class="c66 c34">.7.5 Get Contract Clients Response (GetContractClientsResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetContractClientsResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clients</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-client">Client</a></span><span>[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Clients with same contract as logged users's one, if any</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-contract-clients-req-url"><span>2</span><span class="c66 c34">.7.6 Get Contract Clients Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get clients with the same contract as logged user's one, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contract</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetContractClientsRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-contact-req"><span>2</span><span class="c66 c34">.7.7 Create Contact Request (CreateContactRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contact</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Create contact associating externalId as unique reference</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">CreateContactRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalContactId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External contact id (caller client Id unique reference)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 36 characters. Unique for caller</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">secretKey</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External contact secret key</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 36 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phone1</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c24 c79"><a class="c40" href="#href-ds-shipment-phone-number">ShipmentPhoneNumber</a></span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact phone number (for example: +40799123456, 0040799123456, +359999123456 - international format numbers or 0799123456, 0999123456 - local numers).</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max size is 20 chars.
Phone numbers must contain digits only. The "+" sign is also permitted as a leading symbol. Only spaces are allowed as separators. Only phone numbers starting with "0" (zero) or "+" sign are allowed. </span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phone2</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-phone-number">ShipmentPhoneNumber</a></span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact phone number 2.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validate for valid phone number, if presents.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientName</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact customer name.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validate for valid name (minimum 3 symbols, maximum 60).</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">objectName</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Forbidden for private persons. Not mandatory for companies</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact customer object name.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validate for valid name (maximum 60 symbols).</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">contactName</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden for private persons. Required for companies</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact name of contact</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum 60</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">email</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact email.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum &nbsp;255</span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">privatePerson</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Private person flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c22" colspan="1" rowspan="1">
<p class="c2"><span class="c7">address</span></p>
</td>
<td class="c46" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-address">ShipmentAddress</a></span></p>
</td>
<td class="c26" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c8" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact address.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid values.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-contact-resp"><span>2</span><span class="c66 c34">.7.8 Create Contact Response (CreateContactResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">CreateContactResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientId</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client Id associated for created contact in the system</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-contact-req-url"><span>2</span><span class="c66 c34">.7.9 Create Contact Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to create contact, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contact</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">CreateContactRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">externalContactId | external_contact_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External contact id (caller client Id unique reference)</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 30 characters. Unique for caller</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">secretKey | secret_key</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">External contact secret key</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 36 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phone1</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">First phone number.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phone1Ext | phone1_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">First phone number extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phone2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Second phone number.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">phone2Ext | phone2_ext</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Second phone number extension.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientName | client_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Conact customer name.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Minimum 3 symbols, maximum 60</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">objectName | object_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden for private persons. Not mandatory for companies</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Conact customer object name.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Minimum 3 symbols, maximum 60</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">contactName | contact_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden for private persons. Required for companies.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact name of contact.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum 60.</span></p>
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">email</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact email.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Maximum &nbsp;255</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">privatePerson | private_person</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contact private person flag.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Contact Address</span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-address">ShipmentAddress </a></span><span class="c7">for more details.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressCountryId | address_country_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country ISO code. If not provided, local country is assumed.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressStateId | address_state_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country supports states.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 2 (foreign address).</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressSiteId | address_site_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id.</span></p>
<p class="c2"><span class="c7">Used for all address types. If not provided, but site type and name or post code is provided - the system will try to find unique match by them in country</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressSiteType | address_site_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressSiteName | address_site_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressPostcode | addressPostCode | address_postcode</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid postcode in site and country.</span></p>
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressStreetId | address_street_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street identifier. If not provided, but street type and street name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressStreetType | address_street_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressStreetName | address_street_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressStreetNumber | address_street_number</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street number.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressComplexId | address_complex_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex identifier. If not provided, but complex type and complex name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressComplexType | address_complex_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressComplexName | address_complex_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressBlock | addressBlockNo | address_block</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Block No.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 32 </span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressEntrance | addressEntranceNo | address_entrance</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
 <td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Entrance.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressFloor | addressFloorNo | address_floor</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Floor.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressApartment | addressApartmentNo | address_apartment</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Apartment.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressPoiId | address_poi_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Point of interest identifier.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressNote | address_note</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address note.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">200</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressLine1 | address_line1</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required for address type 2</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 1. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressLine2 | address_line2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 2. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressX | address_x</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - X.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressY | address_y</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - Y.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
 <p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-get-external-contact-req"><span>2</span><span class="c66 c34">.7.10 Get Contact By External Id Request (GetContactByExternalIdRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contact/external/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get contact by external id. External client id is provided as parameter in URL path</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetContactByExternalIdRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">secretKey</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Secret key</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 36 characters</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-get-external-contact-resp"><span>2</span><span class="c66 c34">.7.11 Get Contact By External Id Response (GetContactByExternalIdResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetContactByExternalIdResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">client</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-client">Client</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-get-external-contact-req-url"><span>2</span><span class="c66 c34">.7.12 Get Contact By External Id Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get contact by external id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contact/external/<b>{id}</b></span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">External contact id is provided as URL path parameter. The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetContactByExternalIdRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
  <tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">secretKey | secret_key</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Secret key</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 36 characters</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-own-client-id-req"><span>2</span><span class="c66 c34">.7.13 Get Own Client Id Request (GetOwnClientIdRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get own client id</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">GetOwnClientIdRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-own-client-id-resp"><span>2</span><span class="c66 c34">.7.14 Get Own Client Id Response (GetOwnClientIdResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">GetOwnClientIdResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientId</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Own client id</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-own-client-id-req-url"><span>2</span><span class="c66 c34">.7.15 Get Own Client Id Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get own client id, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">GetOwnClientIdRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
 </td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-contract-info-req"><span>2</span><span class="c66 c34">.7.16 Contract Info Request (ContractInfoRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contract/info</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get information about logged user contract</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ContractInfoRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
 <td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-contract-info-resp"><span>2</span><span class="c66 c34">.7.17 Contract Info Response (ContractInfoResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">ContractInfoResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">id</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Contract id</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">specialDeliveryRequirements</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-special-delivery-requirements">SpecialDeliveryRequirements</a></span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Special delivery requirements</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-payout-req-url"><span>2</span><span class="c66 c34">.7.18 Contract Info Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get contract information, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/client/contract/info</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">ContractInfoRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
 </td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
</tbody>
</table>
<h2 class="c74" id="href-validation-service"><span class="c35 c34">2.8 Validation Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/validation</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-address-req"><span>2</span><span class="c66 c34">.8.1 Validate Address Request (ValidateAddressRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/address</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">This method validates shipment address</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ValidateAddressRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">address</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span class="c79 c24"><a class="c40" href="#href-ds-shipment-address">ShipmentAddress</a></span></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment address to validate</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validation-resp"><span>2</span><span class="c66 c34">.8.2 Validate Address Response (ValidationResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">ValidationResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">valid</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2">Boolean</p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validation result flag</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-address-req-url"><span>2</span><span class="c66 c34">.8.3 Validate Address Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to validate address, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/address</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">ValidateAddressRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c71" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Shipment Address</span></p>
<p class="c2"><span class="c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-shipment-address">ShipmentAddress </a></span><span class="c7">for more details.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId | country_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country ISO code. If not provided, the local country is assumed.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">stateId | state_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country supports states.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 2 (foreign address).</span></p>
<p class="c2 c3"><span class="c7"></span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id.</span></p>
<p class="c2"><span class="c7">Used for all address types. If not provided, but site type and name or post code is provided - the system will try to find unique match by them in country</span></p>
<p class="c2 c3"><span class="c7"></span></p>
  </td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteType | site_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteName | site_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">postcode | postCode | post_code</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated for valid postcode in site and country.</span></p>
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">streetId | street_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street identifier. If not provided, but street type and street name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">streetType | street_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">streetName | street_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if street_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">streetNumber | street_number</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Street number.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">complexId | complex_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex identifier. If not provided, but complex type and complex name are provided - the system will try to find unique match by them in site.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
 <p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">complexType | complex_type</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex type.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 15</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">complexName | complex_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
<p class="c2"><span class="c7">Forbidden, if complex_id is provided.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Complex name.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">block | blockNo | block_no</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Block No.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 32 </span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">entrance | entranceNo | entrance_no</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Entrance.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">floor | floorNo | floor_no</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Floor.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">apartment | apartmentNo | apartment_no</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No </span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Apartment.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">poiId | poi_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Point of interest identifier.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressNote | address_note | note</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address note.</span></p>
<p class="c2"><span class="c7">Used for addresses of type 1 (local address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">200</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressLine1 | address_line1 | line1</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required for address type 2.</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 1. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">addressLine2 | address_line2 | line2</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Address line 2. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 35</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">X | x</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - X.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
<p class="c2 c3"><span class="c7"></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Y | y</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Double</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">GIS coordinates - Y.</span></p>
<p class="c2"><span class="c7">Used for all address types.</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-validate-postcode-req"><span>2</span><span class="c66 c34">.8.4 Validate Postcode Request (ValidatePostCodeRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/postcode</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">This method validates post code</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ValidatePostCodeRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes - if siteId is not specified</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes - if countryId is not specified</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">postCode</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Postcode to validate</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-postcode-resp"><span>2</span><span class="c66 c34">.8.5 Validate Postcode Response (ValidationResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Same as <span class="c79 c24"><a class="c40" href="#href-validation-resp">2.8.2 ValidationResponse</a></span></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-postcode-req-url"><span>2</span><span class="c66 c34">.8.6 Validate Postcode Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to validate post code, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/postcode</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">ValidatePostCodeRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
 <td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">countryId | country_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes - if siteId is not specified</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">siteId | site_id</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes - if countryId is not specified</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">postcode | postCode | post_code</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Postcode to validate</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-validate-phone-req"><span>2</span><span class="c66 c34">.8.7 Validate Phone Request (ValidatePhoneRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/phone</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">This method validates phone number</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ValidatePhoneRequest</span></p>
</td>
 </tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
 <td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">number</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Phone number</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ext</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Phone number extension</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-phone-resp"><span>2</span><span class="c66 c34">.8.8 Validate Phone Response (ValidationResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Same as <span class="c79 c24"><a class="c40" href="#href-validation-resp">2.8.2 ValidationResponse</a></span></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-phone-req-url"><span>2</span><span class="c66 c34">.8.9 Validate Phone Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to validate phone, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/phone</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">ValidatePhoneRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">number</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Phone number</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">ext</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Phone number extension</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-validate-shipment-req"><span>2</span><span class="c66 c34">.8.10 Validate Shipment Request (ValidateShipmentRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/validation/shipment</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This method applies validation on shipment request</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Input parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ValidateShipmentRequest</span></p>
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
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-create-shipment-req">CreateShipmentRequest</a></span><span class="c1"><i> fields are here</i></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c23"></span></p>
<h3 class="c12" id="href-validate-shipment-resp"><span>2</span><span>.8.11 Validate Shipment Response (ValidateShipmentResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Same as <span class="c79 c24"><a class="c40" href="#href-validation-resp">2.8.2 ValidationResponse</a></span></span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-validate-shipment-req-url"><span>2</span><span class="c66 c34">.8.12 Validate Shipment - URL (GET) Schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to validate shipments, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span>&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/validation/shipment</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: “application/x-www-form-urlencoded; </span><span class="c34">charset</span><span class="c16">=utf-8”</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ValidateShipmentRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c17"><span class="c79 c24"><a class="c40" href="#href-create-shipment-url">CreateShipmentRequest</a></span><span class="c1"><i> params are here</i></span></p>
</td>
</tr>
</tbody>
</table>
<h2 class="c74" id="href-services-service"><span class="c35 c34">2.9 Services Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/services</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-services-req"><span>2</span><span class="c66 c34">.9.1 Services Request (ServicesRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/services</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get available services for date</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
 <td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">ServicesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">date</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (yyyy-MM-dd)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date. Current date is assumed if not provided</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-services-resp"><span>2</span><span class="c66 c34">.9.2 Services Response (ServicesResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">ServicesResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">services</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-courier-service">CourierService</a></span>[]</p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Available courier services</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-services-req-url"><span>2</span><span class="c66 c34">.9.3 Services Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get services, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/services</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">ServicesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">date</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (yyyy-MM-dd)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date. Current date is assumed if not provided</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<h3 class="c12" id="href-destination-services-req"><span>2</span><span class="c66 c34">.9.4 Destination Services Request (DestinationServicesRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/services/destination</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get available services for date and destination</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">DestinationServicesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">date</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (yyyy-MM-dd)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date. Current date is assumed if not provided</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">sender</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-sender">CalculationSender</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the pickup place. If not specified, the logged user client location is considered as a sender location.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipient</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-calculation-recipient">CalculationRecipient</a></span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Defines the recipient delivery place.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-destination-services-resp"><span>2</span><span class="c66 c34">.9.5 Destination Services Response (DestinationServicesResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">DestinationServicesResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">services</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-extended-courier-service">ExtendedCourierService</a></span><span>[]</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Available courier services for destination</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-destination-services-req-url"><span>2</span><span class="c66 c34">.9.6 Destination Services Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get services for date and destination, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/services/destination</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">DestinationServicesRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
 </td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">date</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (yyyy-MM-dd)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date. Current date is assumed if not provided</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation sender details</span></p>
<p class="c2"><span class="c25 c24">If logged user is the sender, you may skip providing sender details at all. </span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client’s id in sender_id parameter and other sender parameters may be skipped at all also.</span></p>
<p class="c2"><span class="c25 c24">Otherwise, sender_id should stay empty and it is required to provide as a minimum:</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c162 c24">sender </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">sender address location or dropoffOfficeId</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderId | sender_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
 <p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer Ð° sender</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for existence.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderPrivatePerson | sender_private_person</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If sender_id is provided, it is forbidden. If the sender is the logged user, should be omitted too. Otherwise, it is mandatory</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Sender private person flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Sender Address Location Details</span></p>
<p class="c2"><span class="c25 c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-address-location">AddressLocation</a></span><span class="c25 c24"> for more details.</span></p>
<p class="c2"><span class="c25 c24">The sender address location is expected when sender_id is empty and sender_dropoff_office_id is empty and not required. In other words, the sender address location is required when the sender is not a referred customer or logged user and pickup at senderâs address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressCountryId | sender_address_country_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Country ISO code. If not provided, the local country is assumed. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country code</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressStateId | sender_address_state_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires state</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country state.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteId | sender_address_site_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid site and value is required</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteType | sender_address_site_type</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for addresses of type 1 (local address)</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressSiteName | sender_address_site_name</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">senderAddressPostcode | senderAddressPostCode | sender_address_postcode</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires post code</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">dropoffOfficeId | dropOffOfficeId | senderDropoffOfficeId | senderDropOffOfficeId | dropoff_office_id | sender_dropoff_office_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if the sender is an internal customer. If sender address is provided, it is forbidden.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Drop off office id.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible office</span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Calculation recipient details</span></p>
<p class="c2"><span class="c25 c24">If you refer an existing customer, provide client's id in recipient_id parameter and other recipient parameters may be skipped at all </span></p>
<p class="c2"><span class="c25 c24">Otherwise, recipient_id should stay empty and it is required to provide as a minimum:.</span></p>
<ul class="c92 lst-kix_4vl8kb4v7x25-0">
<li class="c2 c36"><span class="c162 c24">recipient </span><span class="c7">privatePerson flag</span></li>
<li class="c2 c36"><span class="c25 c24">recipient address location or pickupOfficeId</span></li>
</ul>
<p class="c2 c3"><span class="c25 c24"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientId | recipient_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client id to refer Ð° recipient</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for existence.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientPrivatePerson | recipient_private_person</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, âyes/noâ - all case insensitive)</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">If recipient_id is provided, it is forbidden. Otherwise, it is mandatory</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Recipient private person flag.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c146">
<td class="c54 c157" colspan="5" rowspan="1">
<p class="c87"><span class="c0">Recipient Address Location Details</span></p>
<p class="c2"><span class="c25 c24">See </span><span class="c79 c24"><a class="c40" href="#href-ds-calculation-address-location">AddressLocation</a></span><span class="c25 c24"> for more details.</span></p>
<p class="c2"><span class="c25 c24">The recipient address location is expected when recipient_id is empty and recipient_pickup_office_id is empty and not required. In other words, the recipient address location is required when the recipient is not a referred customer and delivery at recipientâs address is expected.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressCountryId | recipient_address_country_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Country ISO code. If not provided, the local country is assumed. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country code</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressStateId | recipient_address_state_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires state</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Country state. Used for addresses of type 2 (foreign address).</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid country state.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteId | recipient_address_site_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if country has full site nomenclature and pair (site_type, site_name) not provided</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site id. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7">Validate for valid site and value is required</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteType | recipient_address_site_type</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for addresses of type 1 (local address)</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 20 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressSiteName | recipient_address_site_name</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Forbidden, if site id is provided. Otherwise, is not mandatory.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Site type can be used in conjunction with country_id and site_name to find unique site. Used for all address types.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 50 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">recipientAddressPostcode | recipientAddressPostCode | recipient_address_postcode</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required if country requires post code</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Can be used in conjunction with countryId to find unique site. Used for all address types</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Max 10 characters</span></p>
</td>
</tr>
<tr class="c14">
<td class="c112" colspan="1" rowspan="1">
<p class="c2"><span class="c7">pickupOfficeId | pickUpOfficeId | recipientPickupOfficeId | recipientPickUpOfficeId | pickup_office_id | recipient_pickup_office_id</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Integer</span></p>
</td>
<td class="c51" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Required, if the recipient is an internal customer. If recipient address is provided, it is forbidden.</span></p>
</td>
<td class="c37" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Pickup office id.</span></p>
</td>
<td class="c30" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Should refer to a valid accessible office</span></p>
</td>
</tr>
</tbody>
</table>
<h2 class="c74" id="href-payments-service"><span class="c35 c34">2.10 Payments Service</span></h2>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span>Web service URL: </span><span class="c34">BASE_URL</span><span class="c16">/payments</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-payout-req"><span>2</span><span class="c66 c34">.10.1 Payout Request (PayoutRequest)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/payments</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: POST</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/json; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2 c3"><span class="c16">Get shipment payout details for a period</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c33 c24">PayoutRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
<td class="c57 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c39 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
<td class="c9 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">fromDate</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DateTime (yyyy-MM-dd'T'HH:mm:ssZ)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Start of period date time.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">toDate</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">DateTime (yyyy-MM-dd'T'HH:mm:ssZ)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">End of period date time.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">includeDetails</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">boolean</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (default value is false)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Include payout details flag</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-payout-resp"><span>2</span><span class="c66 c34">.10.2 Payout Response (PayoutResponse)</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c54 c20" colspan="4" rowspan="1">
<p class="c17"><span class="c33 c24">PayoutResponse</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Name </span></p>
</td>
 <td class="c62 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c133 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Mandatory</span></p>
</td>
<td class="c75 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">payouts</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c79 c24"><a class="c40" href="#href-ds-payout">Payout</a></span>[]</p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Shipment payouts for a period</span></p>
</td>
</tr>
<tr class="c14">
<td class="c82" colspan="1" rowspan="1">
<p class="c2"><span class="c7">error</span></p>
</td>
<td class="c62" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Error</span></p>
</td>
<td class="c133" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c75" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Response error</span></p>
</td>
</tr>
</tbody>
</table>
<p class="c2 c3"><span class="c16"></span></p>
<h3 class="c12" id="href-payout-req-url"><span>2</span><span class="c66 c34">.10.3 Payout Request - URL (GET) schema</span></h3>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">This approach is used to get shipment payouts, providing data in an URL instead of JSON data in the content.</span></p>
<p class="c2"><span class="c16">&nbsp;</span></p>
<p class="c2"><span class="c34">Web service URL</span><span>: &nbsp;</span><span class="c34">BASE_URL</span><span class="c16">/payments</span></p>
<p class="c2"><span class="c34">Method</span><span class="c16">: GET</span></p>
<p class="c2"><span class="c34">Content-type</span><span>: application/x-www-form-urlencoded; &nbsp;</span><span class="c34">charset</span><span class="c16">=utf-8</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c16">The response is the same as method using JSON schema.</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<p class="c2"><span class="c34">URL parameters</span><span class="c16">:</span></p>
<p class="c2 c3"><span class="c16"></span></p>
<table class="c32">
<tbody>
<tr class="c84">
<td class="c41 c20" colspan="5" rowspan="1">
<p class="c17"><span class="c24 c33">PayoutRequest</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">URL Parameter Name</span></p>
<p class="c17"><span class="c1">(synonyms are separated with |)</span></p>
</td>
<td class="c13 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Type</span></p>
</td>
<td class="c15 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Required</span></p>
</td>
<td class="c11" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Data</span></p>
 </td>
<td class="c49 c45" colspan="1" rowspan="1">
<p class="c17"><span class="c1">Constraints</span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">userName | username | user_name</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">User name</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">password</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Password</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">language | lang</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">String</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7"><span data-sl-text="defaultLanguage"></span></span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2 c3"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c47" colspan="1" rowspan="1">
<p class="c2"><span class="c7">clientSystemId | client_system_id</span></p>
</td>
<td class="c13" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Long</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No</span></p>
</td>
<td class="c19" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Client system id</span></p>
</td>
<td class="c49" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Validated against system register for external customers.</span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">date_from</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (yyyy-MM-dd'T'HH:mm:ssZ)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Start of period date time.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">date_to</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Date (yyyy-MM-dd'T'HH:mm:ssZ)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Yes</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">End of period date time.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
<tr class="c14">
<td class="c124" colspan="1" rowspan="1">
<p class="c2"><span class="c7">include_details</span></p>
</td>
<td class="c57" colspan="1" rowspan="1">
<p class="c2"><span class="c7">boolean</span></p>
<p class="c2"><span class="c7">(true/false, y/n, “yes/no” - all case insensitive)</span></p>
</td>
<td class="c39" colspan="1" rowspan="1">
<p class="c2"><span class="c7">No (Default value is false)</span></p>
</td>
<td class="c15" colspan="1" rowspan="1">
<p class="c2"><span class="c7">Flag to include payout details.</span></p>
</td>
<td class="c9" colspan="1" rowspan="1">
<p class="c2"><span class="c7"></span></p>
</td>
</tr>
</tbody>
</table>
</div>



