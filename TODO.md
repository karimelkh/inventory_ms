# TODOs

## issues

*(empty)*

## fixes

- make hide/show columns menu adabtable between pages
- make some enhancements in `items.views.index` (and for other apps)
- fix tailwind problem (not compiling some the classes in `categories` app)
- fix `show_item` view: does not work when `save` button clicked (context problem)
- fix the `no` button when deleting
- the update operation not working, make the create of users easy
- use `DO_NOTHING` or `SET_NULL` instead of `CASCADE` in some FKs
- fix zoom using a jquery plugin
- fix update and remove buttons in specific pages for and item...

## feats

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

### user

- change the default home look
- display the number of selected items in tables
- give dropdown menu a good new look
- table sorting
- make a tree view for the product and its items
- file upload
- when a user created send an email if it was provided
- search
- when all the checkbox are unchecked, uncheck the select all one 
- show a floating menu at a time
- make short links like: `i` -> `items`
- Bar/QR code support
- Reporting and Analytics
- support mobile
- table pagination
- mv all/some items from one site to another
- recent updates like in the arch [home](archlinux.org)

### messages

- give notifications/messages a new look (+ timeout)
- add animations to messages
- send a message if an item,... was not found when
requesting it
- send a message when a form does not create a new thing
and the reason

### buttons

- make the update button besides the delete button
- add abort button when updating

### forms

- make the forms with separated html files and
use ajax to get them as popups

## others

- use 2-cols table with no header for displaying
specific items
- make errors in the bottom instead of above
- make different users types and permissions and
the ability for some users to manage other users
- make the `img` field fk referencing the table of imgs
- use django-phonenumber-field
- add rating attribute/column to some tables
- handle forms errors
- discover decorators that comes with django:
  - `user_passes_test`
  - `require_http_methods`
  - `cache_page`
  - `vary_on_headers`
- make `SITE_TYPES` a table instead of a var
- apply some jquery plugins:
  - [EasyZoom](i-like-robots.github.io/EasyZoom)
  - check the [repo](github.com/petk/awesome-jquery)
- add more to the messaging feature
- think about moving to bootstrap
or use it with tailwindcss

## Ideas for home page

- grid of items and products, ...
- notifications
- latest changes/actions
