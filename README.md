# Türkçe - Çeviri API

Bu API, Google Translate Kütüphanesini kullanarak metinleri farklı dillere çevirmenizi sağlar.  

### Nasıl Kullanılır?

API'ye şu şekilde istek gönderebilirsiniz:

GET localhost:3355/cevir?cumle={ÇEVİRİLECEK_CÜMLE}&src={KAYNAK_DİL_KODU}&dest={HEDEDF_DİL_KODU}

**Parametreler:**

* **cumle:** Çevrilecek metin.
* **src:** Kaynak dilin iki harfli kodu (örneğin: tr, en, de, fr).
* **dest:** Hedef dilin iki harfli kodu.

**Örnek İstek:**

GET localhost:3355/cevir?cumle=Merhaba Dünya!&src=tr&dest=en

**Örnek Yanıt:**

```json
{
  "success": true,
  "developer": "Atsız Yazılım",
  "original": "Merhaba Dünya!",
  "translation": "Hello World!",
  "src": "tr",
  "dest": "en"
}
```

### Hata Durumları

Eksik veya hatalı parametreler girildiğinde şu şekilde bir hata yanıtı alınır:

```json
{
  "success": false,
  "message": "Lütfen geçerli bir cümle, kaynak dil ve hedef dil girin."
}
```

### Kurulum

1. Python ve Flask'ın yüklü olduğundan emin olun.
2. `pip install googletrans flask` komutuyla gerekli kütüphaneleri yükleyin.
3. Kodu kaydedin ve `python translate-api.py` komutuyla çalıştırın.

### Lisans

Bu proje [GNU Genel Kamu Lisansı v3.0](LICENSE) ile lisanslanmıştır.




# English - Translation API

This API uses the Google Translate Library to allow you to translate text into different languages.

### How to Use?

You can make requests to the API as follows:

GET localhost:3355/cevir?cumle={TEXT_TO_TRANSLATE}&src={SOURCE_LANGUAGE_CODE}&dest={TARGET_LANGUAGE_CODE}

**Parameters:**

* **cumle:** The text to be translated.
* **src:** The two-letter code of the source language (e.g., tr, en, de, fr).
* **dest:** The two-letter code of the target language.

**Example Request:**

GET localhost:3355/cevir?cumle=Hello World!&src=en&dest=tr

**Example Response:**

```json
{
  "success": true,
  "developer": "Atsız Yazılım",
  "original": "Hello World!",
  "translation": "Merhaba Dünya!",
  "src": "en",
  "dest": "tr"
}
```

### Error Handling

If incorrect or missing parameters are provided, an error response will be returned:

```json
{
  "success": false,
  "message": "Lütfen geçerli bir cümle, kaynak dil ve hedef dil girin."
}
```

### Installation

1. Make sure you have Python and Flask installed.
2. Install the required libraries with `pip install googletrans flask`.
3. Save the code and run it with `python translate-api.py`.

### License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Dil Kodları / Language Codes

| Dil Adı / Language         | Dil Kodu / Language Code |
|----------------------------|--------------------------|
| Türkçe / Turkish           | tr                       |
| Azerbaycan Türkçesi / Azerbaijani      | az                       |
| İngilizce / English        | en                       |
| Afrikaanca / Afrikaans     | af                       |
| Arapça / Arabic            | ar                       |
| Arnavutça / Albanian       | sq                       |
| Bengalce / Bengali         | bn                       |
| Boşnakça / Bosnian         | bs                       |
| Bulgarca / Bulgarian       | bg                       |
| Çekçe / Czech              | cs                       |
| Çince (Basitleştirilmiş) / Chinese (Simplified)   | zh-CN                    |
| Çince (Geleneksel) / Chinese (Traditional)       | zh-TW                    |
| Danca / Danish             | da                       |
| Endonezce / Indonesian     | id                       |
| Farsça / Persian           | fa                       |
| Fince / Finnish            | fi                       |
| Fransızca / French         | fr                       |
| Galce / Welsh              | cy                       |
| Gürcüce / Georgian         | ka                       |
| Hintçe / Hindi             | hi                       |
| Hırvatça / Croatian        | hr                       |
| Hollandaca / Dutch         | nl                       |
| İspanyolca / Spanish       | es                       |
| İsveççe / Swedish          | sv                       |
| İtalyanca / Italian        | it                       |
| Japonca / Japanese         | ja                       |
| Katalanca / Catalan        | ca                       |
| Korece / Korean            | ko                       |
| Lehçe / Polish             | pl                       |
| Macarca / Hungarian        | hu                       |
| Malayca / Malay            | ms                       |
| Norveççe / Norwegian       | no                       |
| Osmanlıca / Ottoman Turkish | tr-OT                   |
| Özbekçe / Uzbek            | uz                       |
| Portekizce / Portuguese    | pt                       |
| Rumence / Romanian         | ro                       |
| Rusça / Russian            | ru                       |
| Sırpça / Serbian           | sr                       |
| Slovakça / Slovak          | sk                       |
| Slovence / Slovenian       | sl                       |
| Tayca / Thai               | th                       |
| Ukraynaca / Ukrainian      | uk                       |
| Urduca / Urdu              | ur                       |
| Vietnamca / Vietnamese     | vi                       |
| Yunanca / Greek            | el                       |
