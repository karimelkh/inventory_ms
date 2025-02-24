# Changelogs

## commit [b0a15ef](https://github.com/karimelkh/inventory_ms/commit/b0a15ef8e46b4365df371136a8f3bee9fc1319a2)

- make an appropriate id for the models
- enhance the update experience by
- fix all update issues in index pages
- make site types a model `SiteType`
- adding messages when the update succeeds or fails
- link items and products

## commit [cfb7f56](https://github.com/karimelkh/inventory_ms/commit/cfb7f56251d3895db34758425bd3c8012ae61f27):

- code enhancements:
- use `url` keyword instead of static urls
- database changes, renaming, ...
- delete items/users/categories/suppliers/sites in groups

## commit [b5d4f61](https://github.com/karimelkh/inventory_ms/commit/b5d4f610c8674930f508db9d3178f22239464422):

- code enhancements especially in `views.py`
- messages (just starting)
- migrations: some column alters (required fields)
- re-configure tailwindcss (no much diff between old one)

## commit [f4f7038](https://github.com/karimelkh/inventory_ms/commit/f4f70387f48bcea74e1325b7af356bdf61e21c80):

- **Date:**
- **Add Category app:**
  - setup the `category` app
  - mv `Category` model to `categories` app from `items` app

## commit [e54a03a](https://github.com/karimelkh/inventory_ms/commit/e54a03afc47c80abe4c513a2e17cf8928f238205):

- **Date:** Date: Thu Jul 11 23:24:23 2024 +0100
- **dropdown menu for fks**:
  - migrating from `forms.Form` to `forms.ModelForm`
  - using existing values of other tables referenced by fks

## commit [cc21ecd](https://github.com/karimelkh/inventory_ms/commit/cc21ecdef5ff5c676eebd91e2bd07cc8c89574f2):

- **Date:** Thu Jul 11 19:43:44 2024 +0100
- **Add support for images**:
  - support images (just for upload)
  - some cleanup for `urls.py` and `views.py` of the `items` app from tests

## commit [bff9678](https://github.com/karimelkh/inventory_ms/commit/bff96784b5050533d5ea96c2e97e846cd9d9ea4c):

- **Date:** Thu Jul 11 14:44:38 2024 +0100
- **Feats and Fixes**:
  - add `users` app for managing users, auth, permissions
  - moving `login`/`logout` feats to `users` app
  - add `users` app that manage items
  - reduce some tailwind classes in html by editing input.css
  - some cleaning

## commit [0787d5f](https://github.com/karimelkh/inventory_ms/commit/0787d5f321aebed32b8b0aab750bc3cf2898a314):

- **Date:** Tue Jul 9 21:47:40 2024 +0100
- **Miner changes**:
  - start reducing tailwind classes
  - separating JS files to: `theme.js`, `login.js` and `main.js`
  - add `create new` list
  - add some styles to the login page
