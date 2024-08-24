from flask import Flask, request, Response
from googletrans import Translator
import json

app = Flask(__name__)
translator = Translator()

@app.route('/cevir', methods=['GET'])
def translate():
    # GET parametrelerini al
    cumle = request.args.get('cumle')
    src = request.args.get('src')
    dest = request.args.get('dest')
    
    # Parametrelerin doğruluğunu kontrol et
    if not cumle or not src or not dest:
        return Response(
            response=json.dumps({
                'success': False,
                'message': 'Lütfen geçerli bir cümle, kaynak dil ve hedef dil girin.'
            }, ensure_ascii=False),
            status=400,
            mimetype='application/json; charset=utf-8'
        )

    # Çeviriyi gerçekleştir
    cevap = translator.translate(cumle, src=src, dest=dest)

    # JSON çıktısını oluştur
    response = {
        'success': True,
        'developer': 'Atsız Yazılım',
        'original': cumle,
        'translation': cevap.text,
        'src': src,
        'dest': dest
    }
    
    return Response(
        response=json.dumps(response, ensure_ascii=False),
        status=200,
        mimetype='application/json; charset=utf-8'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3355)
