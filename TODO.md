# TODOs

## issues

- issues with hiding forms and pop-ups

## fixes

- fix delete btn in index pages
- make hide/show columns menu adaptable between pages
- make some enhancements in `items.views.index` (and for other apps)
- fix tailwind problem (not compiling some the classes in `categories` app)
- fix all problems with adding new stuff
    - fix `show_item` view: does not work when `save` button clicked (context problem)
- fix the `no` button when deleting
- the update operation not working, make the create of users easy
- use `DO_NOTHING` or `SET_NULL` instead of `CASCADE` in some FKs
- fix delete btns

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
- find a way to use csrf token properly without using `csrf_exempt` decorator
- think about moving to bootstrap
or use it with tailwindcss
- make different users types and permissions and
the ability for some users to manage other users
- make the `img` field fk referencing the table of imgs
- use django-phonenumber-field

### user

- when requesting data using ajax, fill the divs with loading animation first
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
- discover decorators that comes with django:
  - `user_passes_test`
  - `require_http_methods`
  - `cache_page`
  - `vary_on_headers`
- apply some jquery plugins:
  - check the [repo](https://github.com/petk/awesome-jquery)

### messages

- give notifications/messages a new look (at the bottom) + timeout
- add animations to messages
- send a message if an item,... was not found when
requesting it (now, its just an 404 page)
- send a message when a form does not create a new thing
and the reason

### buttons

- make the update button besides the delete button
- add abort button when updating

### forms

- make the (new, delete, update) forms with separated html files and
use ajax to get them as popups

## Ideas for home page

- grid of items and products, ...
- notifications
- latest changes/actions
