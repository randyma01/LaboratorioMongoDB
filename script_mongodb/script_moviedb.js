/*
----------------------------------------------------------------------

Área Académica de Administración de Tecnología de Información

Curso:
    Bases de Datos Avanzados - TI4601

Tarea:
    Laboratorio MongoDB

Fecha:
    7 de octubre, 2018
    Semestre II

Estudiante:
	Randy Martínez Sandí

Carnet: 2014047395

Índice:
    1. Creación de la base y colecciones.
    2. Llenado de las colecciones.
    3. Consultas hacia la base.

Nota:
    El siguiente código corresponde al script de la creación
		de la base de datos.

----------------------------------------------------------------------
*/

//--------------------------------------------------------//
//--------------Creación de la base de datos--------------//
//--------------------------------------------------------//

// Usar esta Base (si no existe se crea) //
use movieDB


// Crear una Colección //
db.createCollection('peliculas')
db.createCollection('productoras')

// Mostrar las Colecciones //
show collections

//--------------------------------------------------------//
//---------------Llenado de las Colecciones---------------//
//--------------------------------------------------------//

// Insertando Películas //
db.peliculas.insert(
 [
    {
        "nombrePelicula": "Quiero Matar a Mi Jefe",
        "nombreDirector": "Seth Gordon",
        "genero": "Comedia",
        "pais": "Estados Unidos",
        "estreno": 2011,
        "duracion": 106,
				"productora": "New Line Cinema",
				"actores": ["Jason Bateman", "Charlie Day", "Jason Sudeikis"]
    },

		{
        "nombrePelicula": "Rogue One: A Star Wars Story",
        "nombreDirector": "Gareth Edwards",
        "genero": "Ciencia-Ficcion",
        "franquicia": "Star Wars",
        "pais": "Inglaterra",
        "estreno": 2016,
        "duracion": 133,
				"productora": "Lucasfilm",
				"actores": ["Felicity Jones", "Diego Luna", "Alan Tudyk"]
    },

		{
        "nombrePelicula": "Pulp Fiction",
        "nombreDirector": "Quentin Tarantino",
        "genero": "Crimen",
        "pais": "Estados Unidos",
        "estreno": 1994,
        "duracion": 154,
				"productora": "Miramax",
				"actores": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]
    },

		{
        "nombrePelicula": "X-Men: First Class",
        "nombreDirector": "Matthew Vaughn",
        "genero": "Superheroes",
				"franquicia": "X-Men",
        "pais": "Estados Unidos",
        "estreno": 2011,
        "duracion": 131,
				"productora": "Twentieth Century Fox",
				"actores": ["James McAvoy", "Michael Fassbender", "Jennifer Lawrence"]
    },

		{
        "nombrePelicula": "La Era de Hielo",
        "nombreDirector": "Chris Wedge",
        "genero": "Animada",
				"franquicia": "Ice-Age",
        "pais": "Estados Unidos",
        "estreno": 2002,
        "duracion": 81,
				"productora": "Twentieth Century Fox",
				"actores": ["Denis Leary", "John Leguizamo", "Ray Romano"]
    },

		{
        "nombrePelicula": "Rapidos y Furioso: Reto Tokyo",
        "nombreDirector": "Justin Lin",
        "genero": "Accion",
				"franquicia": "Rapidos y Furiosos",
        "pais": "Japon",
        "estreno": 2006,
        "duracion": 104,
				"productora": "Universal Pictures",
				"actores": ["Lucas Black", "Zachery Ty Bryan", "Shad Moss"]
    },

		{
        "nombrePelicula": "Kung Pow: El maestro de la kung fusión",
        "nombreDirector": "Steve Oedekerk",
        "genero": "Parodia",
        "pais": "Estados Unidos",
        "estreno": 2002,
        "duracion": 81,
				"productora": "Twentieth Century Fox",
				"actores": ["Steve Oedekerk", "Fei Lung", "Leo Lee"]
    },

		{
        "nombrePelicula": "Pollitos en fuga",
        "nombreDirector": "Peter Lord Nick Park",
        "genero": "Animada",
        "pais": "Estados Unidos",
        "estreno": 2000,
        "duracion": 84,
				"productora": "DreamWorks",
				"actores": ["Mel Gibson", "Julia Sawalha", "Phil Daniels"]
    },

		{
        "nombrePelicula": "Shrek",
        "nombreDirector": "Andrew Adamson Vicky Jenson",
        "genero": "Animada",
        "pais": "Estados Unidos",
        "estreno": 2001,
        "duracion": 90,
				"productora": "DreamWorks",
				"actores": ["Mike Myers", "Eddie Murphy", "Cameron Diaz"]
    },
	]
)

// Insertando Productoras //
db.productoras.insert(
 [
    {
      "nombreProductora": "New Line Cinema",
      "fundacion": 1967,
      "paginaWeb": "//www.newline.com",
    },

		{
			"nombreProductora": "Lucasfilm",
			"fundacion": 1971,
			"paginaWeb": "www.lucasfilm.com",
    },

		{
			"nombreProductora": "Miramax",
			"fundacion": 1979,
			"paginaWeb": "www.miramax.com/",
    },

		{
			"nombreProductora": "Twentieth Century Fox",
			"fundacion": 1935,
			"paginaWeb": "www.foxmovies.com"
    },

		{
			"nombreProductora": "Universal Pictures",
			"fundacion": 1912,
			"paginaWeb": "www.universalpictures.com"
    },

		{
			"nombreProductora": "DreamWorks",
			"fundacion": 1994,
			"paginaWeb": "www.dreamworksanimation.com/"
    },
	]
)


//--------------------------------------------------------//
//--------------------------CRUD--------------------------//
//--------------------------------------------------------//

//---Busquedas---//

// Consultar todos los resultados //
db.peliculas.find().pretty()
db.productoras.find().pretty()

// Consultar toda la información de una película por su nombre //
db.peliculas.find(
  {
    "nombrePelicula": "Shrek"
  }
).pretty()

// Consultar toda la información de todas las pelícuals de una franquicia //
db.peliculas.find(
  {
    "franquicia": "Star Wars"
  }
).pretty()

// Consultar la información de una película estrenada en un rango de años //
db.peliculas.find(
  {
    "estreno" : {$gt: "2005", $lt: "2010"}
  }
).pretty()

// Consultar nombre, género, estreno de las peliculas producidas por una //
// por una productar en particular //
db.peliculas.find(
	{"productora": "Twentieth Century Fox"},
	{"nombrePelicula": 1, "genero": 1, "estreno":1, "_id": 0}
).pretty()

// Consultar la cantidad de peliculas //
db.peliculas.count()

// Consultar la película con menor duración //
db.peliculas.find(
	{},
	{"nombrePelicula": 1, "duracion": 1, "_id": 0}
).sort({"duracion":-1}).limit(1).pretty()

// Consultar la película con mayor duración //
db.peliculas.find(
	{},
	{"nombrePelicula": 1, "duracion": 1, "_id": 0}
).sort({"duracion":1}).limit(1).pretty()

// Consultar la duración promedio de las peliculas //
