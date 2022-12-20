create database email_sender;

\c email_sender

create TABLE emails (
 serial id not null,
 timestamp not null default CURRENT_TIMESTAMP,
 subject VARCHAR(100) NOT NULL,
 message VARCHAR(250) NOT NULL
);
