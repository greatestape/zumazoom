function BoxedUniverse(_$box) {
    this.$box = _$box;
    this.$mainBlock = $("#MainBlock");
    this.$contactBlock = $("#ContactBlock");
}

BoxedUniverse.prototype.dropBoxes = function() {
    this.$box.find("#MainBlock, #ContactBlock").moveBlock([0, 600]);
}

BoxedUniverse.prototype.dropMainBox = function() {
    this.$mainBlock.moveBlock([0, 600]);
}

$(document).ready(function() {
    bu = new BoxedUniverse($("#MainBox"));
})


$.fn.moveBlock = function(delta) {
    currentOffset = [parseInt(this.css('marginLeft').split('px')[0]),
                     parseInt(this.css('marginTop').split('px')[0])];
    targetOffset = [currentOffset[0] + delta[0],
                    currentOffset[1] + delta[1]];
    this.css({backgroundPosition: (0 - currentOffset[0]) + 'px ' + (0 - currentOffset[1]) + 'px'});
    console.log("animating ", this, " from ", currentOffset, " to ", targetOffset);
    this.animate({
        marginLeft: targetOffset[0] + "px",
        marginTop: targetOffset[1] + "px",
        backgroundPosition: '(' + (0 - targetOffset[0]) + 'px ' + (0 - targetOffset[1]) + 'px)'
        }, 5000);
};

/** 
 * @author Alexander Farkas 
 * Support for negative offsets added by Sam Bull
 */
(function($) { 
    $.extend($.fx.step,{ 
        backgroundPosition: function(fx) { 
            if (fx.state == 0 && typeof fx.end == 'string') { 
                var start = $.curCSS(fx.elem,'backgroundPosition'); 
                start = toArray(start); 
                fx.start = [start[0],start[2]]; 
                var end = toArray(fx.end); 
                fx.end = [end[0],end[2]]; 
                fx.unit = [end[1],end[3]]; 
            }
            var nowPosX = []; 
            nowPosX[0] = ((fx.end[0] - fx.start[0]) * fx.pos) + fx.start[0] + fx.unit[0]; 
            nowPosX[1] = ((fx.end[1] - fx.start[1]) * fx.pos) + fx.start[1] + fx.unit[1];            
            fx.elem.style.backgroundPosition = nowPosX[0]+' '+nowPosX[1]; 
            
           function toArray(strg){ 
               strg = strg.replace(/left|top/g,'0px'); 
               strg = strg.replace(/right|bottom/g,'100%'); 
               strg = strg.replace(/(\d+)(\s|\)|$)/g,"$1px$2"); 
               var res = strg.match(/(-?\d+)(px|\%|em|pt)\s(-?\d+)(px|\%|em|pt)/); 
               return [parseFloat(res[1]),res[2],parseFloat(res[3]),res[4]]; 
           } 
        } 
   }); 
    
})(jQuery);