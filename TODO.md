# TODOs

## issues

- updating images not working
- The Category could not be changed because the data didn't validate
- The title of the Site can't be updated
    - solution: hide the id field

## fixes

- make some enhancements in `items.views.index` (and for other apps)
- fix tailwind problem (not compiling some the classes in `categories` app)
- fix `show_item` view: does not work when `save` button clicked (context problem)
- fix the `no` button when deleting
- the update operation not working, make the create of users easy
- use `DO_NOTHING` or `SET_NULL` instead of `CASCADE` in some FKs

## feats

- detaile error messages: errors reasons
- change the default home look
- make the update button besides the delete button
- display the number of selected items in tables
- give dropdown menu a good new look
- give notifications/messages a new look (+ timeout)
- table sorting
- make a tree view for the product and its items
- make the products app
- file uplaod
- send a message if an item,... was not found when
requesting it
- when a user created send an email if it was provided
- add abort button when updating
- send a message when a form does not create a new thing
and the reason
- class-based view
- search
- add animations to messages
- make the forms with separated html files and
use ajax to get them as popups
- when all the checkbox are unchecked, uncheck the select all one 
- form help messages
- make short links like: `i` -> `items`
- rename files/images after uploading them
- edit db schema: products/items can have multiple storage sites
- drag&drop images/attachments [yt](https://www.youtube.com/watch?v=9Xh_ZpFkROI)
- page 404
- create the following apps:
  - `orders`/`ship`: -
  - `notifications`: notify for low stock (...)
  - `settings`: stock settings
  - `partners` to transfare items to them
- show a floating menu at a time
- Bar/QR code support
- Reporting and Analytics
- support mobile
- history and system logs
- mv all/some items from one site to another
- recent updates like in the arch [home](archlinux.org)
- backup
- pagination

## others

- use 2-cols table with no header for displaying
specific items
- make errors in the bottom instead of above
- make different users types and permessions and
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
