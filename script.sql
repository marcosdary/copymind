create type roles as enum ('system', 'user', 'assistant');

create table conversations (
	"conversationId" varchar(255) primary key,
    "title" varchar(255) not null,
    "createdAt" timestamp not null,
    "updatedAt" timestamp default current_timestamp
);

create table messages (
	"messageId" varchar(255) primary key,
    "conversationId" varchar(255) not null,
    "content" text not null,
    "totalTokens" bigint not null,
    "role" roles default 'user',
    "totalResponseTime" decimal(10, 2) not null,
    "createdAt" timestamp not null,
    "updatedAt" timestamp default current_timestamp,
    
    foreign key ("conversationId") references conversations("conversationId")
);


select * from conversations;