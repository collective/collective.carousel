// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
    // adjust height of the carousel to the max height of the elements
    base_height = Math.max.apply(null,
        $("#flowpanes .items .tileItem").map(function() { return $(this).innerHeight() }).get()
    );
    $("#flowpanes .items .tileItem").height(base_height);
    $("#flowpanes").height(base_height);    
    $("#carousel").height($("#flowpanes .items .tileItem").outerHeight(true) + $(".navi").outerHeight(true) + 10);
        
    // initialize scrollable 
    $("div.scrollable").scrollable({
        size: 1,        
    }).circular().autoscroll(25000).navigator();
})