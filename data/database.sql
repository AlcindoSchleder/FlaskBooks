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

CREATE TABLE public.users
(
    pk_users integer NOT NULL DEFAULT nextval('seq_users'::regclass),
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    username character varying(150) NOT NULL,
    email character varying(255) NOT NULL,
    login character varying(100) NOT NULL,
    passwd character varying(255) NOT NULL,
    insert_date timestamp without time zone,
    update_date timestamp without time zone,
    CONSTRAINT pk_users PRIMARY KEY (pk_users),
    CONSTRAINT users_id UNIQUE (id)
);


CREATE TABLE public.customers
(
    pk_customers integer NOT NULL DEFAULT nextval('seq_customers'::regclass),
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    name character varying(150) NOT NULL,
    address text COLLATE NOT NULL,
    city character varying(100) NOT NULL,
    state character(2) NOT NULL,
    phone character varying(25) NOT NULL,
    zip_code character varying(15) NOT NULL,
    insert_date timestamp without time zone NOT NULL,
    update_date timestamp without time zone,
    CONSTRAINT pk_customers PRIMARY KEY (pk_customers),
    CONSTRAINT customers_id UNIQUE (id)
);

CREATE TABLE public.books
(
    pk_books integer NOT NULL DEFAULT nextval('seq_books'::regclass),
    id uuid  NOT NULL DEFAULT uuid_generate_v4(),
    publisher_name character varying(150) NOT NULL,
    author_name character varying(150) NOT NULL,
    publisher character varying(150) NOT NULL,
    customer_review text,
    insert_date timestamp without time zone[],
    update_date timestamp without time zone NOT NULL,
    CONSTRAINT pk_books PRIMARY KEY (pk_books)
    CONSTRAINT books_id UNIQUE (id)
);

CREATE TABLE public.transactions
(
    fk_customers integer NOT NULL,
    fk_books integer NOT NULL,
    pk_transactions time without time zone NOT NULL,
    id uuid  NOT NULL DEFAULT uuid_generate_v4(),
    value double precision NOT NULL DEFAULT 0.00,
    status smallint NOT NULL,
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
        ON DELETE CASCADE,
    CONSTRAINT transactions_id UNIQUE (id)
);
