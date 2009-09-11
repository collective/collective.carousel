// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
    // initialize scrollable 
    $("div.scrollable").scrollable({
        size: 1,        
    }).circular().autoscroll(25000).navigator();
})