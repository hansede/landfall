create table rarities( 
  id int not null auto_increment, 
  name varchar(100) not null, 
  primary key (id),
  unique(name) 
);

create table colors( 
  id int not null auto_increment, 
  name varchar(100) not null, 
  primary key (id),
  unique(name)
);

create table types( 
  id int not null auto_increment, 
  name varchar(100) not null, 
  primary key (id),
  unique(name)
);

create table releases( 
  id int not null auto_increment, 
  name varchar(100) not null, 
  primary key (id),
  unique(name)
);

create table cards( 
  id int not null auto_increment, 
  name varchar(100) not null, 
  `release` int, 
  cmc varchar(100) not null, 
  type int, 
  color int, 
  rarity int, 
  primary key (id), 
  foreign key (`release`) references releases(id), 
  foreign key (type) references types(id), 
  foreign key (color) references colors(id), 
  foreign key (rarity) references rarities(id),
  unique(name, `release`)
);

create table `values`( 
  id int not null auto_increment, 
  high DECIMAL(6,2) unsigned not null, 
  medium DECIMAL(6,2) unsigned not null, 
  low DECIMAL(6,2) unsigned not null, 
  card int, 
  created TIMESTAMP DEFAULT NOW(), 
  primary key (id), 
  foreign key (card) references cards(id)
);

