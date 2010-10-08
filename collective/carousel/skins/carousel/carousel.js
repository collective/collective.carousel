// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
	
	// The carousel was not loading properly in some browsers and the reason seemed to be that
	// even though the jQuery document.ready function is being triggered, the DOM elements inside
	// the carousel have not loaded in sufficiently for jQuery to correctly calculate widths and heights.
	// The solution is to wrap eveything in a timer, giving the browser a little bit of extra time to do
	// the layout calculations. Interestingly webkit browsers require more time (1250ms) then others browsers(500ms).
	setTimeout(function(){
		
		    var resizeCarousel = function(carousel, scrollable, elems) {
		        // Adjust height of the carousel to the max height of the elements.
		        var base_height = Math.max.apply(null,
		            $(elems).map(function() { return $(this).height() }).get()
		        );
		        if(base_height < $(carousel).height()) {
		            base_height = $(carousel).height() - $(".navi").outerHeight(true);
		        }
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
		    var interval = 3000; // default transition interval, overidable by rel=""
		    
		    carousels.each( function(i) {
		        var carousel = this;
		        var scrollable = $(this).find(".scrollable").eq(0);        
		        var elems = $(scrollable).find('.tileItem');
		        
		        // Set width of all carousel items so they wrap and have correct widths
		        scrollable_width = $(scrollable).width();         
		        for (i=0; i<elems.length; i++) {
		            $(elems[i]).css( {width: scrollable_width + 'px' } );
		        };
		        
		        // Use setTimeout here to give other code a chance to bind events.
		        // setTimeout 0 causes code to run right after the jQuery load event has finished.
		        // setTimeout(function() { resizeCarousel(carousel, scrollable, elems); }, 0);
		        setTimeout(function() { resizeCarousel(carousel, scrollable, elems) }, 0);        
		        
		        $(scrollable).find("img").load(function(event) {
		            // If an image is loaded later we need to resize the whole carousel to fit it          
		            resizeCarousel(carousel, scrollable, elems);          
		        });
		        
		        // if a interval rel is set, apply it here
		        if(parseInt($(scrollable).attr('rel')) > 0)
		        {
		        	interval = parseInt($(scrollable).attr('rel'));
		        }
		    });
		    
		    // doesn't make sense to enable autoscrolling if more than one 
		    // carousel is on a page - this just distracts and annoys
		    var ap = (carousels.length == 1) ? true : false;
		    
		    // initialize scrollable 
		    var api = $("div.scrollable").scrollable({
		        size: 1,  
		        clickable: false,      
		        loop: true
		    }).circular().autoscroll({autoplay: ap,steps:1,interval:interval}).navigator({api:true});
		      
		    // Show toolBar when hovering over a carousel
		    $(".carousel").hover(
		        function(){
		            $(this).find(".toolBar").eq(0).slideToggle('fast').show();
		        },
		        function(){
		            $(this).find(".toolBar").eq(0).slideToggle('fast').hide();
		        }
		    );
		    
		    // Pause on hover
		    //$(scrollable).hover(api.pause);
		    // Pause button
		    $(".carousel .pause").click(function (){api.pause();})
    
	}, (($.browser.safari||$.browser.webkit) ? 1250 : 500)); // this is the loading delay time to fix the DOM issue described at the top of this script
	;
	
})