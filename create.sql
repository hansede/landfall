create table cards( 
  id int not null auto_increment, 
  name varchar(100) not null, 
  rel varchar(100) not null,
  cmc varchar(100) not null, 
  type varchar(100) not null,
  color varchar(20) not null,
  rarity varchar(2) not null,
  primary key (id), 
  unique(name, rel)
);

create table prices( 
  id int not null auto_increment, 
  high DECIMAL(6,2) unsigned not null, 
  medium DECIMAL(6,2) unsigned not null, 
  low DECIMAL(6,2) unsigned not null, 
  card_id int, 
  created TIMESTAMP DEFAULT NOW(), 
  primary key (id), 
  foreign key (card_id) references cards(id)
);

