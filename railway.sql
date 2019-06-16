drop table train_vagons;
drop table shedule_days;
drop table station_type;
drop table vagons;
drop table train_shedules;
drop table shedule_stations;
drop table stations;
drop table trains;






CREATE TABLE trains ( 
	train_id 	smallint auto_increment, 
	name 		varchar(20) not null,
	origin_station_id 	   smallint unsigned not null,
	destination_station_id smallint unsigned not null,
	PRIMARY KEY(train_id)
	#FOREIGN KEY(origin_station_id) REFERENCES stations(station_id)
	#FOREIGN KEY(destination_station_id) REFERENCES binzari.stations(station_id)
	);
INSERT INTO trains ( train_id, name, origin_station_id,destination_station_id ) VALUES ( null, 'D001',1,3 );
INSERT INTO trains ( train_id, name, origin_station_id,destination_station_id ) VALUES ( null, 'D002',2,3 );
INSERT INTO trains ( train_id, name, origin_station_id,destination_station_id ) VALUES ( null, 'D003',3,2 );
INSERT INTO trains ( train_id, name, origin_station_id,destination_station_id ) VALUES ( null, 'D004',4,1 );


CREATE TABLE vagons (
	vagon_id smallint unsigned auto_increment,
	first_class int(3) not null,
	second_class int(3) not null,
	PRIMARY KEY(vagon_id)
	);
INSERT INTO vagons ( first_class, second_class) VALUES ( 12 ,36);
INSERT INTO vagons ( first_class, second_class) VALUES ( 8 ,42);
INSERT INTO vagons ( first_class, second_class) VALUES ( 22 ,60);
INSERT INTO vagons ( first_class, second_class) VALUES ( 16 ,64);

CREATE TABLE stations (
	station_id smallint unsigned auto_increment, 
	station_name varchar(80) not null,
	station_city varchar(80) not null,
	station_country varchar(80) not null,
	PRIMARY KEY(station_id)
	);
INSERT INTO stations (station_id, station_name, station_city, station_country) VALUES ( null, 'Varsawa_station','Warsawa','Poland');
INSERT INTO stations (station_id, station_name, station_city, station_country) VALUES ( null, 'Bucharest_station','Bucharest','Romania');
INSERT INTO stations (station_id, station_name, station_city, station_country) VALUES ( null, 'Lodz_station','Lodz','Poland');
INSERT INTO stations (station_id, station_name, station_city, station_country) VALUES ( null, 'Krakow_station','Krakow','Poland');

CREATE TABLE station_type(
	station_id smallint unsigned not null,
	station_type varchar(80) not null,
	station_type_description varchar(280),
	FOREIGN KEY(station_id) REFERENCES stations(station_id)
);
INSERT INTO station_type ( station_id, station_type, station_type_description) VALUES( 1,'smth','smth more');
INSERT INTO station_type ( station_id, station_type, station_type_description) VALUES( 2,'smth','smth more');

CREATE TABLE shedule_stations(
	shedule_stations_id smallint unsigned auto_increment,
	station_id smallint unsigned not null,
	arrival_time TIME not null,
	departure_time TIME not null,
	FOREIGN KEY(station_id) REFERENCES stations(station_id),
	PRIMARY KEY(shedule_stations_id) 
);
INSERT INTO shedule_stations (shedule_stations_id, station_id, arrival_time, departure_time) VALUES( null, 1, '01:00:00', '01:05:00');

CREATE TABLE train_shedules(
	shedule_train_id smallint unsigned auto_increment,
	train_id smallint not null,
	operating_day varchar(15) not null,
	shedule_stations_id smallint unsigned,
	PRIMARY KEY(shedule_train_id),
	FOREIGN KEY(train_id) REFERENCES trains(train_id),
	FOREIGN KEY(shedule_stations_id) REFERENCES shedule_stations(shedule_stations_id)
);
CREATE TABLE shedule_days(
	shedule_stations_id smallint unsigned,
	data DATE,
	FOREIGN KEY(shedule_stations_id) REFERENCES shedule_stations(shedule_stations_id)
);
INSERT INTO shedule_days (shedule_stations_id, data) VALUES( 1, '2019-06-14');

CREATE TABLE train_vagons(
	train_id smallint not null,
	vagon_id smallint unsigned not null,
	FOREIGN KEY(vagon_id) REFERENCES vagons(vagon_id),
	FOREIGN KEY(train_id) REFERENCES trains(train_id)
	);

INSERT INTO train_vagons (train_id,vagon_id) VALUES (1,1)