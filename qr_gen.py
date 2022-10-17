import qrcode

# Instalar librerias necesarias (qrcode)
# Desde una cadena de texto, convierte a QR
# Guarda el QR como .png


def generador_qr(texto):
    codigo = qrcode.QRCode(version=1, box_size=10, border=4)
    codigo.add_data(texto)
    codigo.make(fit=True)
    imagen = codigo.make_image(fill='black', back_color='white')
    imagen.save('qrimg.png')


def main():
    texto_a_generar = input("Texto a generar: ")
    generador_qr(texto_a_generar)
    print("Codigo QR creado con exito")


if __name__ == '__main__':
    main()