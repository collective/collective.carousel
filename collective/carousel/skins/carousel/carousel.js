// What is $(document).ready ? See: http://flowplayer.org/tools/using.html#document_ready
jQuery(function($) {
    var carousels = $(".carousel");

    var resizeCarousel = function(carousel, elems) {
        // adjust height of the carousel to the max height of the elements
        var base_height = Math.max.apply(null,
            elems.map(function() { return $(this).innerHeight() }).get()
        );
        elems.height(base_height);
        $(carousel).find(".scrollable").height(base_height);    
        $(carousel).height(elems.outerHeight(true) + $(".navi").outerHeight(true) + 10);
        // 35px in the following like is 20px (height of navi) + 15px (1/2 height of the button)
        $(carousel).find(".browse").css("margin-top", (($(carousel).height()/2) - 20 - 15));
    };
    
    // doesn't make sense to enable autoscrolling if more than one 
    // carousel is on a page - this just distracts and annoys
    var ap = (carousels.length == 1) ? true : false;
    
    // initialize scrollable 
    var api = $("div.scrollable").scrollable({
        size: 1,  
        clickable: false,      
        loop: true
    }).circular().autoscroll({autoplay: ap,steps:1,interval:25000}).navigator({api:true});
    
    carousels.each( function(i) {
        var elems = $(this).find('.scrollable .items .tileItem');
        resizeCarousel($(this), elems); 
        elems.find("img").load(function() {
            c = carousels[i];
            resizeCarousel(c, elems); 
        });
    })
    // $(".fullscreen-switcher:eq(0) a").prepOverlay(
    //     {
    //         subtype: 'ajax',
    //         filter: '#content > *',
    //         formtarget: 'form#content form',
    //         noform: 'reload'
    //     }
    // )
    
    // $("#carousel-fullscreen").overlay({
    //        api: true,
    //        target: "#kiosk-wrapper",
    //        top: "center",
    //        left: 0,
    //        closeOnClick: false,        
    //        speed: "slow",           
    //        expose: {
    //             color: "#fff",
    //             opacity: 1.0,
    //             loadSpeed: 'fast'
    //        },
    //        onBeforeLoad: function() {   
    //            // copy .scrollable to overlay
    //            this.getOverlay().height($(window).height());
    //            this.getOverlay().width($(window).width());
    //        },
    //        onLoad: function() {
    //            console.info(api.getIndex());              
    //            this.getOverlay().toggleClass("activeKiosk");
    //        },
    //        onClose: function() {
    //            api.begin();
    //            this.getOverlay().removeAttr("style");
    //            this.getOverlay().toggleClass("activeKiosk");               
    //        }
    // });    
})