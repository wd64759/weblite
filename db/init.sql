drop table if exists entries;
CREATE TABLE entries (
id integer primary key autoincrement,
title text not null,
'text' text not null
);