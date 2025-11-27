class Usuario:
    def __init__(self, id, nombre, run, password_hash, tipo="User") -> None:
        self.id = id
        self.nombre = nombre
        self.run = run
        self.password_hash = password_hash
        self.tipo = tipo
