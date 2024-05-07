from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Plants(db.Model):

    rowid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(5000), unique=True, nullable=False)
    descriptionEnvironment = db.Column(db.String(5000), unique=True, nullable=False)
    image = db.Column(db.String(200), unique=True, nullable=False)
    invasive = db.Column(db.Boolean, unique=False, nullable=False)
    native = db.Column(db.Boolean, unique=False, nullable=False)
    exotic = db.Column(db.Boolean, unique=False, nullable=False)
    caracteristic = db.Column(db.String(500), unique=False, nullable=False)
    soil = db.Column(db.String(200), unique=False, nullable=False)
    prados = db.Column(db.Boolean, unique=False, nullable=False)
    campos = db.Column(db.Boolean, unique=False, nullable=False)
    jardines = db.Column(db.Boolean, unique=False, nullable=False)
    costa = db.Column(db.Boolean, unique=False, nullable=False)
    interior = db.Column(db.Boolean, unique=False, nullable=False)
    montaña = db.Column(db.Boolean, unique=False, nullable=False)
    otros = db.Column(db.Boolean, unique=False, nullable=False)

    def __str__(self):
        return "\Id: {}. Nombre: {}. Descripción: {}. Entorno: {}. Imagen: {}. Invasora: {}. Nativa: {}. Exótica: {}. Característica: {}. Suelo: {}. Prados: {}. Campos: {}. Jardines: {}. Costa: {}. Interior: {}. Montaña: {}. Otros: {}.\n".format(
            self.id,
            self.title,
            self.description,
            self.descriptionEnvironment,
            self.image,
            self.invasive,
            self.native,
            self.exotic,
            self.caracteristic,
            self.soil,
            self.prados,
            self.campos,
            self.jardines,
            self.costa,
            self.interior,
            self.montaña,
            self.otros,

        )

    def serialize(self):
        return{
            "rowid": self.rowid,
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "descriptionEnvironment": self.descriptionEnvironment,
            "image": self.image,
            "invasive" : self.invasive,
            "native": self.native,
            "exotic": self.exotic,
            "caracteristic": self.caracteristic,
            "soil": self.soil,
            "prados": self.prados,
            "campos": self.campos,
            "jardines": self.jardines,
            "costa": self.costa,
            "interior": self.interior,
            "montaña": self.montaña,
            "otros": self.otros,
        }