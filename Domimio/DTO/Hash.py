import bcrypt

class Hashpass:

    def hashTexto(self, texto):
        sal = bcrypt.gensalt()
        texto_hasheado = bcrypt.hashpw(texto.encode('utf-8'), sal)
        return texto_hasheado

    def verificarTexto(self, texto, texto_hasheado):
        # Verificamos si el texto coincide con el hash almacenado
        return bcrypt.checkpw(texto.encode('utf-8'),texto_hasheado.encode('utf-8'))