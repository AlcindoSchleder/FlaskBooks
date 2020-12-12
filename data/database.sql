CREATE DATABASE pgeldorado
    WITH
    OWNER = sysdba
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    CONNECTION LIMIT = -1;

-- DROP TABLE public.transactions;
-- DROP TABLE public.customers;
-- DROP TABLE public.books;


CREATE TABLE public.customers
(
    pk_customers integer NOT NULL DEFAULT nextval('seq_customers'::regclass),
    id uuid DEFAULT uuid_generate_v4(),
    name character varying(150) COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    city character varying(100)[] COLLATE pg_catalog."default",
    state character(2)[] COLLATE pg_catalog."default",
    phone character varying(25)[] COLLATE pg_catalog."default",
    zip_code character varying(15)[] COLLATE pg_catalog."default",
    insert_date timestamp without time zone,
    update_date timestamp without time zone,
    CONSTRAINT pk_customers PRIMARY KEY (pk_customers),
    CONSTRAINT customers_id UNIQUE (id)
);

CREATE TABLE public.books
(
    pk_books integer NOT NULL DEFAULT nextval('seq_books'::regclass),
    id uuid DEFAULT uuid_generate_v4(),
    publisher_name character varying(150) COLLATE pg_catalog."default",
    author_name character varying(150)[] COLLATE pg_catalog."default",
    publisher character varying(150)[] COLLATE pg_catalog."default",
    customer_review text COLLATE pg_catalog."default",
    insert_date timestamp without time zone[],
    update_date timestamp without time zone NOT NULL,
    CONSTRAINT pk_books PRIMARY KEY (pk_books)
);

CREATE TABLE public.transactions
(
    fk_customers integer NOT NULL,
    fk_books integer NOT NULL,
    pk_transactions time without time zone NOT NULL,
    value double precision,
    status smallint,
    update_date timestamp without time zone NOT NULL,
    insert_date timestamp without time zone,
    CONSTRAINT pk_transactions PRIMARY KEY (fk_customers, fk_books, pk_transactions),
    CONSTRAINT fk_customers_transactions FOREIGN KEY (fk_customers)
        REFERENCES public.customers (pk_customers)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_books_transactions FOREIGN KEY (fk_books)
        REFERENCES public.books (pk_books)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
