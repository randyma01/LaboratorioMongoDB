/*
----------------------------------------------------------------------

Área Académica de Administración de Tecnología de Información

Curso:
    Bases de Datos Avanzados

Tarea:
    Laboratorio MongoDB

Fecha:
    7 de octubre, 2018
    Semestre II

Estudiante:
	Randy Martínez Sandí

Carnet: 2014047395

Índice:
    1. Creación de la base, colección y documentos.
    2. Llenado de documento y colecciones.
    3. Consultas hacia la base.

Nota:
    El siguiente código corresponde al script de la creación
		de la base de datos.

----------------------------------------------------------------------
*/

//--------------------------------------------------------//
//--------------Creación de la base de datos--------------//
//--------------------------------------------------------//

// 1. Buscar y usar esta base, si no existe se y se pasa a usarse.
use escuelaMusica

// 2. 'db' muestra cuál base de datos estoy usando.
db

// 3. 'show dbs' muestra todas las bases de datos que existen y que tengan datos guardados.
show dbs

// 4. Borrar la base datos con todos los datos.
db.dropDatabase()

// 5. Crear una colección.
db.createCollection('estudiantes')
db.profesores.insert({"nombre": "Max"})

// 6. Para ver las colecciones que tengo dentro de la db en la que estoy.
show collections

// 7. Eliminar una colección.
db.profesores.drop()

// 8. Insertando un nuevo documento.
db.estudiantes.insert(
	{
        "numeroEstudiante": "1",
        "nombre": "Sofía",
        "apellido": "Cortés",
        "edad": "21",
        "instrumento": "Piano",
        "gustoMusical": "Indie-Pop"
    }
)

// 9. Insertando varios documento al mismo tiempo
db.estudiantes.insert(
 [
    {
        "numeroEstudiante": "2",
        "nombre": "Sebastián",
        "apellido": "Valerio",
        "edad": "19",
        "instrumento": "Guitarra",
        "gustoMusical": "Rock"
    },

    {
        "numeroEstudiante": "3",
        "nombre": "Carolina",
        "apellido": "Villegas",
        "edad": "20",
        "instrumento": "Vocales",
        "gustoMusical": "Alternativo"
    },

    {
        "numeroEstudiante": "4",
        "nombre": "Giovanni",
        "apellido": "Rodríguez",
        "edad": "22",
        "instrumento": "Batería",
        "gustoMusical": "Jazz"
    },

    {
        "numeroEstudiante": "5",
        "nombre": "Cristhian",
        "apellido": "Martínez",
        "edad": "21",
        "gustoMusical": "Hip-Hop/Rap"

    },

    {
        "numeroEstudiante": "6",
        "nombre": "Bruno",
        "apellido": "Milano",
        "edad": "20"
    },

    {
        "numeroEstudiante": "7",
        "nombre": "Felipe",
        "apellido": "Moya",
        "edad": "19",
        "instrumento": "EquipoDJ",
        "gustoMusical": "House",
        "artistaFavorito": "The Chainsmokers"
    },

    {
        "numeroEstudiante": "8",
        "nombre": "Jorge",
        "apellido": "Vargas",
        "edad": "21",
        "instrumento": ["Guitarra","Batería","Bajo"],
        "gustoMusical": "Progresivo",
        "nombreBanda": "Cuerda Floja"
    },

    {
        "_id": "fR4Nc14",
        "numeroEstudiante": "10",
        "nombre": "Beatrice",
        "apellido": "Dugast",
        "edad": "22",
        "instrumento": "Vocales",
        "gustoMusical": "Pop"
    },

    {
        "numeroEstudiante": "9",
        "nombre": "Nicolle",
        "apellido": "Cordón",
        "edad": "20",
        "instrumento": "Piano",
        "gustoMusical": "Clásica",
        "hijo": {
                "nombre": "Diego",
                "apellido": "Villalobos",
                "instrumento": "Piano"
                }
    }
 ]
)

// 10. Obtener todos los documentos de la colección estudiantes.
db.estudiantes.find()

// 11. Obtener el primer elemento de la colección.
db.estudiantes.findOne()

// 12. Obtener documentos usando condiciones/restricciones.
db.estudiantes.find(
	{
	  "numeroEstudiante": "6"
	}
)

// 13. Obtener los documentos usando comparaciones.
db.estudiantes.find(
	{
	  "edad" : {$ne : "22"} //$gt, $lt, %gte, $lte, $ne
	}
)

// 14. Obteniendo documentos usando AND.
db.estudiantes.find(
	{
	  "instrumento": "Piano", "edad": "21"
	}
)

// 15. Obteniendo documentos usando OR.
db.estudiantes.find(
	{
	  $or : [{"instrumento": "Piano"}, {"edad": "21"}] //or es '$or'
	}
)

// 16. Obteniendo documentos usando AND y OR.
db.estudiantes.find(
	{
	  "nombre": "Giovanni", $or : [{"edad": "20"}, {"edad": "21"}]
	}
)

// 17. Actualizando documentos de la colección estudiantes: añadiendo un instrumento.
db.estudiantes.findOne({"nombre": "Cristhian"})

db.estudiantes.update(
	{ "nombre" : "Cristhian"},
	{$set : {"instrumento": "Beatbox"}}
)


// 18. Actualizando varios documentos que tenga una misma condición: cambiando apellido.

db.estudiantes.find()

db.estudiantes.update(
	{"edad" : "21"},
	{$set : {"apellido": "Musi"}}
)

db.estudiantes.update(
	{"edad" : "21"},
	{$set : {"apellido": "Musi"}},
	{multi: true}
)

// 19. Actualizar todo los datos de un documento de una vez.
db.estudiante.save(
	{
	    "_id" : ObjectId("59f0a95cf0c4baed276acffe"), //si el _id no existe, se crea el nuevo documento
    	"numeroEstudiante" : "1",
    	"nombre" : "Sofía",
    	"apellido" : "Cortés",
    	"edad" : "21",
    	"instrumento" : "Piano",
    	"gustoMusical" : "Indie-Pop"
	}
)


// 14. Borrando todos los  documentos de la colección
db.estudiantes.remove()

// 15. Borrando todos los documentos que cumplan una condición dada.
db.estudiantes.remove(
	{
	  "_id" : ObjectId("59f0a978f0c4baed276ad003")
	}
)
db.estudiantes.find()


// 16. Limitar el número de documentos a borrar que cumplan una condición dada.
db.estudiantes.remove(
	{
	   "edad": "21"
	}, 1
)

db.estudiantes.find()


// 17. Obtener todos los documentos de la colección.
db.estudiantes.find()

// 18. "Projection": Obtener datos específicos de uno o varios documentos: nombre e instrumento.
db.estudiantes.find(
	{},
	{"nombre" : 1, "instrumento" : 1}
)

// 19. Otener datos específicos: nombre e instrumento, sin el _id de cada documento.
db.estudiantes.find(
	{},
	{"nombre": 1, "instrumento":1, "_id": 0}
)

// 20. Obtener datos específicos con condiciones dadas.
db.estudiantes.find(
	{"numeroEstudiante": "8"},
	{"nombre": 1, "instrumento":1, "_id": 0}
)

// 21. Limitar la cantidad de resultados que se obtiene.
db.estudiantes.find(
	{},
	{"nombre": 1, "numeroEstudiante": 1, "_id": 0}
).limit(2)


// 22. Saltar los de resultados que se obtienen apartir de uno o unos cuantos.
db.estudiantes.find(
	{},
	{"nombre": 1, "numeroEstudiante": 1, "_id": 0}
).skip(2)

//s 23. Saltar y limitar los de resultados que se obtienen.
db.estudiantes.find(
	{},
	{"nombre": 1, "numeroEstudiante": 1, "_id": 0}
).skip(2).limit(3)

// 24. Ordenar los datos de manera ascendente.
db.estudiantes.find(
	{},
	{"nombre": 1, "edad": 1, "_id": 0}
).sort({"edad":1})

// 25. Ordenando los datos de manera descendente.
db.estudiantes.find(
	{},
	{"nombre": 1, "edad": 1, "_id": 0}
).sort({"edad":-1})

/*
26. "Indexes and Indexing"

for(i=0; i<1000000; i++){
  db.estudiante.insert({"numeroEstudiante":i});
}

db.estudiantes.find({"numeroEstudiante: 1346"})
*/


// 27. De una busqueda, sumar la cantidad de edadaes que hay.
db.estudiantes.aggregate(
	[
	{$group: {_id : "$edad", Cantidad: {$sum: 1}}}
	]
)

//-------------------------------------------------------------------//
