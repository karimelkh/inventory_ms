insert into products_product (ttl, desc, img, id)
values
('chair', 'used to seat', 'imgs/chair_h6pQLPi.jpeg', 'p001'),
('table', 'used to eat on it', '', 'p002'),
('sardine', 'none', '', 'p003'),
('laptop', 'u r on a one right now', '', 'p004'),
('sneakers', 'none', '', 'p005');

insert into categories_category (id, clr, desc, name)
values
('c001', 'red', 'none', 'solid'),
('c002', 'green', 'none', 'food');

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


insert into items_item (id, img, desc, qty, ttl, cat_id, site_id, suppl_id, prod_id)
values
('i001', '', 'none', 10, 'chair', 'c001', 's001', 's001', 'p001'),
('i002', '', 'none', 40, 'laptop', 'c002', 's002', 's002', 'p002'),
('i003', '', 'none', 60, 'pc case', 'c001', 's003', 's003', 'p003'),
('i004', '', 'none', 6, 'table', 'c002', 's004', 's001', 'p004'),
('i005', '', 'none', 190, 'cable', 'c001', 's002', 's002', 'p005'),
('i006', '', 'none', 300, 'book', 'c002', 's002', 's003', 'p001'),
('i007', '', 'none', 200, 'notebook', 'c001', 's003', 's001', 'p002'),
('i008', '', 'none', 1100, 'sardine', 'c002', 's004', 's002', 'p003'),
('i009', '', 'none', 1000, 'indomi', 'c001', 's001', 's003', 'p004'),
('i010', '', 'none', 150, 'momo', 'c002', 's002', 's001', 'p005'),
('i011', '', 'none', 120, 'mirindina', 'c001', 's002', 's002', 'p001'),
('i012', '', 'none', 10000, 'kabaila', 'c002', 's003', 's003', 'p005');


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
