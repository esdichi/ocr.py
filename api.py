import requests

api_key = 'TU API KEY' 
ruta_imagen = 'imagen.jpg'      
idioma = 'eng'                # 'spa' para español, 'eng' para inglés

opciones = {
    'apikey': api_key,
    'language': idioma,
    'OCREngine': 2,   
    'isTable': True,  
}

with open(ruta_imagen, 'rb') as f:
    respuesta = requests.post(
        'https://api.ocr.space/parse/image',
        files={ruta_imagen: f},
        data=opciones
    )

datos = respuesta.json()

if datos.get('OCRExitCode') == 1:
    texto_final = datos['ParsedResults'][0]['ParsedText']
    print("--- TEXTO EXTRAÍDO ---")
    print(texto_final)
else:
    print("Error al procesar la imagen:")
    print(datos.get('ErrorMessage'))
