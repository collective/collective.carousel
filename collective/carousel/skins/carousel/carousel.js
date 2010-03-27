// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
    var carousels = $(".carousel");

    var resizeCarousel = function(carousel, scrollable, elems) {
        // var scrollable = $(carousel).find(".scrollable").eq(0);
                
        // adjust height of the carousel to the max height of the elements
        var base_height = Math.max.apply(null,
            $(elems).map(function() { return $(this).innerHeight() }).get()
        );
        
        $(elems).height(base_height);
        
        $(scrollable).height(base_height);    
        $(carousel).height($(elems).outerHeight(true) + $(".carouselNavBar").outerHeight(true) + 10);
        // 35px in the following like is 20px (height of carouselNavBar) + 15px (1/2 height of the button)
        $(carousel).find(".browse").css("margin-top", (($(carousel).height()/2) - 20 - 15));
    };
    
    carousels.each( function(i) {
        var scrollable = $(this).find(".scrollable").eq(0);        
        var elems = $(scrollable).find('.tileItem');
        // set width of all elems so they wrap and have correct heights
        var cwidth = $(this).innerWidth();
        
        $(scrollable).width(cwidth);
        
        for (i=0; i<elems.length; i++) {   
            $(elems[i]).css( {width: cwidth } );
        };

        if($(scrollable).find("img").length == 0) {
            console.info("Carousel has NO images");
            // We resize right away
            resizeCarousel(this, scrollable, elems);             
        } 
        else if($(scrollable).find("img").length > 0) {
            console.info("Carousel HAS images");            
            resizeCarousel(this, scrollable, elems);          
            // We wait until all images are loaded and resize afterwards
            $(scrollable).find("img").load(function() {
                alert("Image");
                c = carousels[i];
                resizeCarousel(this, scrollable, elems);          
            });            
        }
    })    
    
    // doesn't make sense to enable autoscrolling if more than one 
    // carousel is on a page - this just distracts and annoys
    var ap = (carousels.length == 1) ? true : false;  
    
    // initialize scrollable 
    var api = $("div.scrollable").scrollable({
        size: 1,  
        clickable: false,      
        loop: true
    }).circular().autoscroll({autoplay: ap,steps:1,interval:25000}).navigator({api:true});
      
    // Show navigation arrows and toolBar when hovering over a carousel
})