---------
Overview.
---------

collective.carousel is the package that lets you add "carousels" of items in your Plone site. More than one carousels on one page are supported.

collective.carousel is based on `Scrollable`__ plugin of `JQuery Tools library`__.

  .. |---| unicode:: U+2014  .. em dash
  .. __: http://flowplayer.org/tools/scrollable.html
  .. __: http://flowplayer.org/tools/index.html

How to get a carousel?
======================

Work of carousel is based on one assumption |---| you already have a collection that returns results for showing in the carousel.
    
Carousel can be added in 2 ways:

    * as a viewlet above page's title;
    * as a portlet to any portlet manager in your site.
    
Carousel above page's title (Content carousel).
-----------------------------------------------

    * Go to ``Edit`` tab on a page where you want to add a carousel;
    * go to ``Settings``;
    * add a collection that will provide content for carousel to ``Carousel object`` field;
    * if you want to add more than one carousel, add more collections to the same field;
    * after saving your page, you should see the carousel(s) above your page's title,

Carousel in a portlet.
----------------------

    * On a page where you want to add a carousel click ``Manage portlets`` in one of the columns of your site;
    * choose ``Carousel portlet`` from ``Add portlet...`` menu;
    * collection portlet is a derivative from standard collection portlet in Plone, hence the same fields are available for this type of portlets as well;
    * fill out the fields in the form specifying a collection that will provide content for the carousel portlet.

Tips
====

What if I want to move carousel to another place?
-------------------------------------------------
Content carousel is defined with a regular viewlet. This lets you to move that viewlet to any place in your site the same way you would do with any other viewlet. Read `Moving a viewlet from a viewlet manager to another one`__ for more info on how to move viewlets from one viewlet manager to another.

  .. __: http://plone.org/documentation/tutorial/customizing-main-template-viewlets/moving-a-viewlet/
  
How do I customize carousel's view?
-----------------------------------
collective.carousel provides a flexible way of customizing the look of items, shown in a carousel based on a content type of the item. collective.carousel comes with 2 bundled views that are available for items, rendered in a carousel:
  * `browser/templates/news_item_tile.pt` |---| defines how News Items should be rendered in a carousel;
  * `browser/templates/dafault_tile.pt` |---| how all the rest content types should be rendered in a carousel.

If you need to either override one of the existing views or define a new view for any content type you can do this from your package using ZCML registartion. Please take a look at `browser/configure.zcml` and `testing.zcml` for examples of such registrations. Note that there are pages with 2 different names:
  * `carousel-view` |---| defines a view for a content type in content carousel;
  * `carousel-portlet-view` |---| the view for a content type when shown in a carousel portlet.

So if you need to override/register a view for any specific content type for content carousel, your `<browser:page />` has to have `carousel-view` name. In case you want to override/register a view for carousel portlet, name should be `carousel-portlet-view`.
  

Developed by **Jarn AS** |---| http://www.jarn.com

Development sponsored by the **Bergen Public Library** |---| http://www.nettbiblioteket.no


