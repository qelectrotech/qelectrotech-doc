.. _doc_changelog:

=======================
Documentation Changelog
=======================

QET Documentation Changelog 0.9 (2025-12-18)
============================================

Adding Windows build instructions (Huge Thanks to  `ssweber`_` for the original Gist)

Doc
---
- Switched from using bootstap4 theme to furo sphinx theme. (Reason is that the former isn't updated anymore. The later is updated, is used for the python + pip doc and has built-in support for dark theme.)
- Use sphinx-design extension to simplify appearance of welcome page.

Feature
-------

- Added Dev docs on how to build the app
- Added GitHub CI to automatically build, publish and licence files on push/merge/ pull request to branch. Using Sphinx-note's page action
- Added app changelog in developer/app_changelog.rst + Documentation changelog
- Created doc hub on homepage instead of going directly in user doc
- Added automatic Doxygen doc support
- Add spellchecking system on deploy


Bugfix
------

- Update User docs
- Update low-res icons/images
- Create a (proprer) directory structure to switch from a messy structure to an organized one (especially for images)



QET Documentation Changelog 0.8 (2020-03-22)
============================================

Bugfix
------

- Documentation re-structured to minimize the size using common figures.
- Some grammatical corrections.


Doc
---

- Documentation ready for internationalization, file structure and new filename definition (``figure_languge_filename = "{path}{language}/{basename}{ext}"``) for the automatic selection of figures depending on the language.
- Official icons added in the images.
- test


Feature
-------

- Forum and Home page links added to the documentation menu.
- New theme used (sphinxbootstrap4theme).
- Some new information added
- pdf version created and download link added to index page.




https://github.com/ssweber
