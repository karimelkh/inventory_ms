# TODOs

## issues

*empty*

## fixes

- make hide/show columns menu adaptable between pages
- make some enhancements in `items.views.index` (and for other apps)
- fix all problems with adding new stuff
    - fix `show_item` view: does not work when `save` button clicked (context problem)
- fix the `no` button when deleting
- the update operation not working, make the create of users easy
- use `DO_NOTHING` or `SET_NULL` instead of `CASCADE` in some FKs
- follow the device timestamp

## feats

### main

- import/export data
- moving items from one site to another
- log system
- ui/ux

### technical

- class-based view
- rename files/images after uploading them
- page 404
- create the following apps:
    - `orders`/`ship`: -
    - `settings`: stock settings
    - `partners` to transfer items to them
- history and system logs
- backup
- find a way to use csrf token properly without using `csrf_exempt` decorator
- make different users types and permissions and
the ability for some users to manage other users
- make the `img` field fk referencing the table of imgs
- use django-phonenumber-field

### ui/ux

- for the recent changes page, use [this](https://getbootstrap.com/docs/5.3/components/card/#card-layout)
card layout
- add urls to logs: use the `reverse` function
- handle the case where the added thing has same values (id, title, category, ...)
as an existing record
    - maybe asking for merge is the best way
- upload data via a text/csv file
- add links to suppliers/categories/... in items and products show pages
- work on the html titles attributes (like in item currency, ...) **??**
- when requesting data using ajax, fill the divs with loading animation first
- display the number of selected items in tables
- table sorting
- make a tree view for the product and its items
- when a user created send an email if it was provided
- search
- when all the checkbox are unchecked, uncheck the select all one 
- make short links like: `i` -> `items`
- Bar/QR code support
- Reporting and Analytics
- support mobile
- table pagination
- mv all/some items from one site to another
- recent updates like in the arch [home](archlinux.org)
- discover decorators that comes with django:
    - `user_passes_test`
    - `require_http_methods`
    - `cache_page`
    - `vary_on_headers`

### messages

- give notifications/messages a new look (at the bottom) + timeout
- add animations to messages
- send a message if an item,... was not found when
requesting it (now, its just an 404 page)
- send a message when a form does not create a new thing
and the reason

### buttons

- make the update button besides the delete button (in the final step: functionality)
- add abort button when updating
