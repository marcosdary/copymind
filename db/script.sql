create table conversations ( 
	conversationId varchar(255) primary key,
	title varchar(255) not null,
	createdAt timestamp default current_timestamp(),
	updatedAt timestamp default current_timestamp()
);

create table messages(
	messageId varchar(255) primary key,
	conversationId varchar(255) not null,
	content text not null,
	role enum('system', 'user', 'assistant') not null default 'user',
	total_tokens bigint not null default 0,
	completion_time decimal(12, 3) default 0.0,
	createdAt timestamp default current_timestamp(),
	updatedAt timestamp default current_timestamp(),
	
	foreign key (conversationId) references conversations(conversationId) on delete cascade
);
