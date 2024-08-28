create table 
	nacionalidades(
		id serial primary KEY
		, descripcion varchar(60) UNIQUE
	);
	
	SELECT id, descripcion 
        FROM nacionalidades;