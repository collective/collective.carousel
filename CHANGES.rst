Changelog
=========

1.6.2 - August 28, 2013
-----------------------

- Allow configuring of image_scales in portlets.
  [thet]

- Added MANIFEST.in to prevent issues with packaging.
  [bogdangi]


1.6.1 - May 2, 2013
-------------------

- Remove stale pdb statement.
  [thet]


1.6 - April 11, 2013
--------------------

- Depend on plone.app.jquerytools and include the scrollable plugins. Include
  an Upgrade step for it (Upgrade 1 to 2).
  [thet]


1.5 - March 2, 2013
-------------------

- Support for new-style Collection type keeping backwards-compatibility
  support for the old-style Topic
  [mishunov, ableeb]

- Don't base the carousel portlet on the collection one since it brings quite
  some unnecessary fileds that don't make sense in this context.
  [mishunov]

- Reduced the default rotation time for a carousel to 10 seconds.
  [mishunov]

- Replace '$' with 'jQuery' in the javascript to avoid unnecessary integration
  conflicts.
  [mishunov]

- We use plain CSS instead of the images for the arrows.
  [mishunov]

- Updated bundled jQueryTools to 1.2.5 and removed 'scrollable' module from
  the local copy.
  [mishunov]

- Complete revert of djay's changes to the javascript.
  [mishunov]

- Add French translation.
  [toutpt]

1.4 - January 27, 2011
----------------------

- Spanish translation.
  [hvelarde]

- Czech translation.
  [lzdych]

- More settings for carousel portlet.
  [djay]

- Pause carousel on :hover.
  [djay]

- Leadimage tile.
  [djay]

- Danish translation
  [stonor]

- Portuguese translation
  [davilima6]

1.3 - July 6, 2010
------------------

- Fixed norwegian translation
  [sh]

- Actual russian translation missing in previous release
  [spliter]

1.2 - June 30, 2010
-------------------

- Russian translation
  [spliter]

1.1 - June 30, 2010
-------------------

- Norwegian translation
  [sh, ggozad]

- Brazilian-Portuguese translation
  [davilima6]

- Added i18n support
  [stonor]

- Fixed the height of the carousel for cases when items are shorter than the
  carousel's height declared in CSS.
  [spliter]

1.0 - April 15, 2010
--------------------

- Added information about 'resized.carousel' event to README.txt
  [spliter]

- Custom 'resized.carousel' event for being able to bind custom
  handlers to the moment when a carousel is re-sized.
  [spliter]

- Limit number of items returned by a carousel to 7.
  [spliter]

- Adjusted slightly to work on Plone 4.
  [hannosch]

- Initial release
  [spliter]

