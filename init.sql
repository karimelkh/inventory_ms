insert into categories_category (id, clr, desc, name)
values
('c001', 'red', 'none', 'solid'),
('c002', 'green', 'none', 'food');


insert into products_product (ttl, desc, img, id, cat_id)
values
('chair', 'used to seat', 'imgs/chair_h6pQLPi.jpeg', 'p001', 'c001'),
('table', 'used to eat on it', '', 'p002', 'c002'),
('sardine', 'none', '', 'p003', 'c001'),
('laptop', 'u r on a one right now', '', 'p004', 'c002'),
('sneakers', 'none', '', 'p005', 'c002');


insert into storagesites_sitetype (name)
values
('Public'),
('Private'),
('Hazmat'),
('Cold storage'),
('Smart'),
('Distribution Center');


insert into storagesites_site (id, addr, img, name, type_id, phone)
values
('s001', 'safi', '', 'marsa', 4, '0636363636'),
('s002', 'youssoufia', '', 'local', 2, '0636363637'),
('s003', 'rabat', '', 'center', 5, '0636363638'),
('s004', 'agadir', '', 'garage', 2, '0636363639');


insert into suppliers_supplier (id, is_active, addr, desc, email, img, name, site, phone)
values
('s001', true, 'youssoufia', 'what ever u want', 'tamaracurtis@example.com', 'http://nelson.com/', 'karim4business', '', '0636363640'),
('s002', true, 'agadir', 'none', 'hperez@example.net', '', 'cna3', 'https://peterson.com/', '0636363641'),
('s003', false, 'safi', 'none', 'joshuagross@example.net', '', 'ocp', 'https://www.smith-jackson.org/', '0636363642');


insert into items_item (id, img, desc, qty, ttl, site_id, suppl_id, prod_id, currency, price)
values
('i001', '', 'none', 10,	'chair',	's001', 's001', 'p001', 'MAD', 0),
('i002', '', 'none', 40,	'laptop',	's002', 's002', 'p002', 'MAD', 0),
('i003', '', 'none', 60,	'pc case',	's003', 's003', 'p003', 'MAD', 0),
('i004', '', 'none', 6,		'table',	's004', 's001', 'p004', 'MAD', 0),
('i005', '', 'none', 190,	'cable',	's002', 's002', 'p005', 'MAD', 0),
('i006', '', 'none', 300,	'book',		's002', 's003', 'p001', 'MAD', 0),
('i007', '', 'none', 200,	'notebook',	's003', 's001', 'p002', 'MAD', 0),
('i008', '', 'none', 1100,	'sardine',	's004', 's002', 'p003', 'MAD', 0),
('i009', '', 'none', 1000,	'indomi',	's001', 's003', 'p004', 'MAD', 0),
('i010', '', 'none', 150, 	'momo',		's002', 's001', 'p005', 'MAD', 0),
('i011', '', 'none', 120,	'mirindina','s002', 's002', 'p001', 'MAD', 0),
('i012', '', 'none', 10000,	'kabaila',	's003', 's003', 'p005', 'MAD', 0);

insert into users_user
values
(
	1,
	'pbkdf2_sha256$720000$Y9CmQU2sbpdnVEg6EUFwKU$SDUnK+lGhqwhl1yhQzP+6PUG9C9Iipv/1rg3i623w7Y=',
	NULL,
	1,
	'karim',
	1,
	1,
	'2024-08-24 03:35:09.233883',
	'staff',
	'karim@ims.org',
	NULL,NULL,'','','',
	'2024-08-24 03:35:09.233924'
);
