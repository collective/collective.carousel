(function($) {

    $.fn.resizeCarousel = function () {
        return this.each(function () {
            // get the scrollable API for this carousel
            var imgHeight, baseHeight,
                $this = $(this),
                $carousel = $('.scrollable', $this),
                api = $carousel.data('scrollable'),
                $items = api.getItems(),
                $images = $('img', $items),
                carouselWidth = $carousel.width(),
                clonedClass = api.getConf().clonedClass;

            // We are resizing carousel after it has been initialized. Since it could have different default width, we need to make sure the carousel is focused on the correct item to avoid the carousel having 'sliced in half' position. In this case we position on the first item, that follows the first cloned item
            api.getItemWrap().attr('style', 'left: -' + carouselWidth + 'px');

            $.each($items, function () {
                //  Adjust the widths of the carousel items
                $(this).add($('.' + clonedClass, $carousel)).width(carouselWidth);
            });

            // Adjust the heights of the carousel items. We can not do
            // this in the same jQuery.each loop with tthe width, because we
            // need all of the items to re-flow after width's adjustments.
            baseHeight = Math.max.apply(Math,
                $items
                    .map(function () {
                        return $(this).height();
                    })
                    .get()
                );

            if ($images.length === 0) {
                // 'resized.carousel' is a custom trigger that 3rd-party
                // code can use for binding events to the moment when a
                // carousel is resized. 'carousel' namespace minimizes
                // chances of conflicting with any other custom trigger of
                // the same 'resized' name. In your custom JS code to bind
                // an event to the moment when a carousel has been
                // completely loaded and resized use something like this:
                // $("#my-special-case .carousel")
                //     .bind('resized.carousel',
                //           function (event, newheight) {
                //               the custom handler resized.carousel event
                //           });
                // This is helpful if you need to have more than 1
                // carousel in the same row and want all of them to be the
                // same height - then you bind resizing function to this
                // 'resized.carousel' trigger.

                $this.add($carousel)
                    .height(baseHeight)
                    .trigger('resized.carousel', [baseHeight]);
            } else {
                // If the carousel has images, then we need to wait for
                // all the images to be loaded before resizing the height
                // of the carousel.
                $images.load(function () {
                    var newHeight = Math.max.apply(Math,
                        $items
                            .map(function () {
                                return $(this).height();
                            })
                            .get()
                        );
                    if (newHeight >= baseHeight) {
                        $this.add($carousel)
                            .height(newHeight)
                            .trigger('resized.carousel', [newHeight]);
                    }
                });
            }
        });
    };

    $.fn.initializeCarousel = function () {
        return this.each(function () {
            var $this = $(this);
            var scrollable = $(this).find('div.scrollable');
            var api,
                ap = ($this.length > 1) ? false : true,
                timer = scrollable.attr('data-timer');

            // initialize scrollable
            if ( ! (($('html').hasClass('ie8')) || ($('html').hasClass('ie7'))) ) {
                api = scrollable
                    .scrollable({
                        size: 1,
                        clickable: false,
                        loop: true,
                        circular: true
                    })
                    .autoscroll({
                        autoplay: ap,
                        steps: 1,
                        interval: timer
                    })
                    .navigator({
                        api: true
                    });
            } else {
                // reduced for IE8/IE7
                api = scrollable.scrollable({
                    size: 1,
                    clickable: false,
                    loop: true,
                    circular: true
                });
            }

            $this.resizeCarousel();

            // Pause on hover
            if (api) {
                $this.mouseenter(api.pause);
                $this.mouseleave(api.play);
            }

            // Show toolBar when hovering over a carousel
            $this.hover(function () {
                $this.find('.toolBar').eq(0).slideToggle('fast');
            });

        });
    };

    $(document).ready(function() {
        $('html').addClass('hideTools');
        $('.collective.carousel').initializeCarousel();
    });

})(jQuery);
