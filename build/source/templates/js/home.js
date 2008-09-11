function HomeHandler(_$document) {
    this.$document = _$document;
    thisHH = this;
    this.$document.ready(function() {
        $(window).scroll(function() {
            thisHH.handleScroll();
        });
        $(window).resize(function() {
            thisHH.handleResize();
        })
        thisHH.handleResize();
        thisHH.handleScroll();
    });
}

HomeHandler.prototype.handleScroll = function() {
    $("body").css("background-position", "" + 
        "-" + (this.$document.scrollLeft() / this.xScrollDenom) + "px " +
        "-" + (this.$document.scrollTop() / this.yScrollDenom) + "px");
};

HomeHandler.prototype.handleResize = function() {
    $body = $("body")
    $win = $(window)
    this.xScrollDenom = $body.width() / (1823 - $win.width());
    this.yScrollDenom = $body.height() / (1200 - $win.height());
};

hh = new HomeHandler($(document));
