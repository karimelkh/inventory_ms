# IMS

## TODOs

### fixes

- fix: change the default home look
- fix: make some enhancements in `items.views.index` (and for other apps)
- fix tailwind problem (not compiling some the classes in `categories` app)
- fix: delay/lag in loading styles after hiding columns (just in Firefox)
  - **possible solutions:**
    - return a json response and generate table in JS

### feats

- make the forms with separated html files and
use ajax to get them as popups
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
  - `partners`
- show a floating menu at a time
- Bar/QR code support
- Reporting and Analytics
- support mobile
- history and system logs
- mv all/some items from one site to another
- recent updates like in the arch [home](archlinux.org)

### others

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
