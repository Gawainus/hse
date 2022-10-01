--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: building; Type: TABLE; Schema: public; Owner: yumentsao
--

CREATE TABLE public.building (
    building_id integer NOT NULL,
    building_name character varying(32) NOT NULL,
    latitude integer NOT NULL,
    longitude integer NOT NULL,
    num_rooms integer NOT NULL,
    num_floors integer NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.building OWNER TO yumentsao;

--
-- Name: building_building_id_seq; Type: SEQUENCE; Schema: public; Owner: yumentsao
--

ALTER TABLE public.building ALTER COLUMN building_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.building_building_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: guest; Type: TABLE; Schema: public; Owner: yumentsao
--

CREATE TABLE public.guest (
    guest_id integer NOT NULL,
    last_name character varying(32) NOT NULL,
    first_name character varying(32) NOT NULL,
    dob date NOT NULL,
    passport_num character varying(32) NOT NULL,
    nationality character varying(32) NOT NULL
);


ALTER TABLE public.guest OWNER TO yumentsao;

--
-- Name: guest_guest_id_seq; Type: SEQUENCE; Schema: public; Owner: yumentsao
--

ALTER TABLE public.guest ALTER COLUMN guest_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.guest_guest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: reservation; Type: TABLE; Schema: public; Owner: yumentsao
--

CREATE TABLE public.reservation (
    reservation_id integer NOT NULL,
    guest_id integer,
    room_id integer,
    check_in_date date,
    duration_stay integer,
    check_in_ts timestamp without time zone,
    check_out_ts timestamp without time zone,
    board_type character varying(32)
);


ALTER TABLE public.reservation OWNER TO yumentsao;

--
-- Name: reservation_reservation_id_seq; Type: SEQUENCE; Schema: public; Owner: yumentsao
--

ALTER TABLE public.reservation ALTER COLUMN reservation_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.reservation_reservation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: room; Type: TABLE; Schema: public; Owner: yumentsao
--

CREATE TABLE public.room (
    room_id integer NOT NULL,
    size integer NOT NULL,
    num_beds integer NOT NULL,
    num_bath integer NOT NULL,
    capacity integer NOT NULL,
    floor integer NOT NULL,
    building_id integer NOT NULL
);


ALTER TABLE public.room OWNER TO yumentsao;

--
-- Name: room_room_id_seq; Type: SEQUENCE; Schema: public; Owner: yumentsao
--

ALTER TABLE public.room ALTER COLUMN room_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.room_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: building; Type: TABLE DATA; Schema: public; Owner: yumentsao
--

COPY public.building (building_id, building_name, latitude, longitude, num_rooms, num_floors, description) FROM stdin;
1	Main Hall	123	189	6	2	Hall used for administration and small amount of guests
2	Building 797	124	179	137	7	Main residental building to host most guests
\.


--
-- Data for Name: guest; Type: TABLE DATA; Schema: public; Owner: yumentsao
--

COPY public.guest (guest_id, last_name, first_name, dob, passport_num, nationality) FROM stdin;
1	Marshev	Mikhail	2001-04-01	MR78316204	Martian
2	Saturnov	Sergey	1969-03-05	SA12957811	Saturnian
3	Jupiterov	Julian	1958-06-19	JU50134833	Jupiterian
4	Venusov	Veronica	1987-08-23	VE88713449	Venusian
\.


--
-- Data for Name: reservation; Type: TABLE DATA; Schema: public; Owner: yumentsao
--

COPY public.reservation (reservation_id, guest_id, room_id, check_in_date, duration_stay, check_in_ts, check_out_ts, board_type) FROM stdin;
1	1	2	2022-02-22	3	2022-02-22 17:25:00	2022-02-25 11:27:00	FB
2	2	2	2022-03-13	7	2022-03-13 16:45:00	2022-03-20 06:13:00	BB
3	3	1	2022-02-22	3	2022-02-22 17:25:00	2022-02-25 11:27:00	HB
4	3	1	2022-03-13	7	2022-03-13 16:45:00	2022-03-20 06:13:00	HB
5	4	3	2022-02-22	3	2022-02-22 17:25:00	2022-02-25 11:27:00	BB
6	4	3	2022-03-13	7	2022-03-13 16:45:00	2022-03-20 06:13:00	FB
\.


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: yumentsao
--

COPY public.room (room_id, size, num_beds, num_bath, capacity, floor, building_id) FROM stdin;
1	77	1	1	2	2	1
2	113	2	1	4	3	2
3	135	1	2	2	7	2
\.


--
-- Name: building_building_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yumentsao
--

SELECT pg_catalog.setval('public.building_building_id_seq', 2, true);


--
-- Name: guest_guest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yumentsao
--

SELECT pg_catalog.setval('public.guest_guest_id_seq', 4, true);


--
-- Name: reservation_reservation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yumentsao
--

SELECT pg_catalog.setval('public.reservation_reservation_id_seq', 6, true);


--
-- Name: room_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yumentsao
--

SELECT pg_catalog.setval('public.room_room_id_seq', 3, true);


--
-- Name: building building_pkey; Type: CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.building
    ADD CONSTRAINT building_pkey PRIMARY KEY (building_id);


--
-- Name: guest guest_pkey; Type: CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.guest
    ADD CONSTRAINT guest_pkey PRIMARY KEY (guest_id);


--
-- Name: reservation reservation_pkey; Type: CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (reservation_id);


--
-- Name: room room_pkey; Type: CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (room_id);


--
-- Name: room fk_building_id; Type: FK CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT fk_building_id FOREIGN KEY (building_id) REFERENCES public.building(building_id) ON DELETE CASCADE;


--
-- Name: reservation fk_guest_id; Type: FK CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT fk_guest_id FOREIGN KEY (guest_id) REFERENCES public.guest(guest_id) ON DELETE CASCADE;


--
-- Name: reservation fk_room_id; Type: FK CONSTRAINT; Schema: public; Owner: yumentsao
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT fk_room_id FOREIGN KEY (room_id) REFERENCES public.room(room_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

