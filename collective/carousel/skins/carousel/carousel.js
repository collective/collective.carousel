// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {

    var resizeCarousel = function(carousel, scrollable, elems) {
        // Adjust height of the carousel to the max height of the elements.
        var base_height = Math.max.apply(null,
            $(elems).map(function() { return $(this).height() }).get()
        );
        $(elems).height(base_height);
        
        // Re-size .scrollable. Since all .tileItem lements have equal height 
        // by now, we can rely on the first element in the set.
        var scrollable_height = $(elems).eq(0).outerHeight(true);
        $(scrollable).height(scrollable_height);    
        
        // Re-size .carousel.
        var outer_height = $(scrollable).outerHeight(true) + $(".navi").outerHeight(true);
        $(carousel).height(outer_height);
    };
    $(".toolBar").hide();
    var carousels = $(".carousel");
    
    carousels.each( function(i) {
        var carousel = this;
        var scrollable = $(this).find(".scrollable").eq(0);        
        var elems = $(scrollable).find('.tileItem');
        
        // Set width of all carousel items so they wrap and have correct widths
        var cwidth = $(this).innerWidth();
        $(scrollable).width(cwidth);        
        scrollable_width = $(scrollable).innerWidth();        
        
        for (i=0; i<elems.length; i++) {   
            $(elems[i]).css( {width: scrollable_width } );
        };
        
        resizeCarousel(this, scrollable, elems);                         
        
        $(scrollable).find("img").load(function() {
            // If an image is loaded later we need to resize the whole carousel to fit it
            resizeCarousel(carousel, scrollable, elems);          
        });            
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