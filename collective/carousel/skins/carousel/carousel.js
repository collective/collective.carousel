// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
    var elems = $('#flowpanes .items .tileItem');

    var resizeCarousel = function() {
        // adjust height of the carousel to the max height of the elements
        var base_height = Math.max.apply(null,
            elems.map(function() { return $(this).innerHeight() }).get()
        );
        elems.height(base_height);
        $("#flowpanes").height(base_height);    
        $("#carousel").height(elems.outerHeight(true) + $(".navi").outerHeight(true) + 10);
        // 35px in the following like is 20px (height of navi) + 15px (1/2 height of the button)
        $(".browse").css("margin-top", ($("#carousel").height()/2 - 35));
    };
    elems.find("img").load(function() {
        resizeCarousel(); 
    });

    // initialize scrollable 
    $("div.scrollable").scrollable({
        size: 1,  
        clickable: false,      
        loop: true,
    }).circular().autoscroll(25000).navigator();
 
})