// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
    var i = 0;
    
    var resizeCarousel = function(carousel, scrollable, elems) {
        // Adjust height of the carousel to the max height of the elements.
        var base_height = Math.max.apply(null,
            $(elems).map(function() { return $(this).height() }).get()
        );
        //Commented out min height. Why do we need a min height of 200?
        //if(base_height < $(carousel).height()) {
        //    base_height = $(carousel).height() - $(".navi").outerHeight(true);
        //}
        $(elems).height(base_height);
        
        // Re-size .scrollable. Since all .tileItem lements have equal height 
        // by now, we can rely on the first element in the set.
        var scrollable_height = $(elems).eq(0).outerHeight(true);
        $(scrollable).height(scrollable_height);
        
        // Re-size .carousel.
        var outer_height = $(scrollable).outerHeight(true) + $(".navi").outerHeight(true);
        var $carousel = $(carousel);
        if ($carousel.height() < outer_height) {
            // 'resized.carousel' is a custom trigger that 3rd-party code can use for 
            // binding events to the moment when a carousel is resized. 'carousel' namespace 
            // minimizes chances of conflicting with any other custom trigger of the same 'resized'
            // name.
            // In your custom JS code to bind an event to the moment when a carousel has been 
            // completely loaded and resized use something like this:
            // $("#my-special-case .carousel").bind('resized.carousel', function(event, newheight) {
            //     your custom handler for resized.carousel' event
            // });
            // This is helpful if you need to have more than 1 carousel in the same row
            // and want all of them to be the same height - then you bind risizing function to this
            // 'resized.carousel' trigger.
            $carousel.height(outer_height).trigger('resized.carousel', [outer_height]);
        }
    };
    
    
    
    $(".toolBar").hide();
    var carousels = $(".carousel");
    
    carousels.each( function(i) {
        var carousel = this;
        
        var scrollable = $(this).find(".scrollable").eq(0);        
        var elems = $(scrollable).find('.tileItem');
        
        var setWidthCarousels = function() {
            // Set width of all carousel items so they wrap and have correct widths
            scrollable_width = $(scrollable).width();

            for (i=0; i<elems.length; i++) {   
                $(elems[i]).css( {width: scrollable_width } );
            };
        };
        
        $(scrollable).bind('onAllImagesReady', function() {
            setTimeout(function() {
                setWidthCarousels();
                resizeCarousel(carousel, scrollable, elems);
                
                var ap = (carousels.length == 1) ? true : false;  
        
                // initialize scrollable 
                var api = $(scrollable).scrollable({
                    size: 1,  
                    clickable: false,      
                    loop: true
                });
                if (!api.getNaviButtons) 
                    api.circular().autoscroll({autoplay: ap,steps:1,interval:25000}).navigator({api:true});            
            }, 200);
        });
        
        var images = $(scrollable).find("img");
        images.each(function(i) {
            var src = $(this).attr('src');
            $(this).attr('src', src + '?timestamp=' + (new Date()).getTime()).load(function(event) {
                if (i++ == images.length-1) $(scrollable).trigger('onAllImagesReady');                
            });
        });          
    });    
    
    // Show toolBar when hovering over a carousel
    $(".carousel").hover(
        function(){
            $(this).find(".toolBar").eq(0).slideToggle('fast').show();
        },
        function(){
            $(this).find(".toolBar").eq(0).slideToggle('fast').hide();
        }
    );
})
