function HomeHandler(_$document) {
    this.$document = _$document;
    thisHH = this;
    this.$document.ready(function() {
        $(window).scroll(function() {
            thisHH.handleScroll();
        });
    });
}

HomeHandler.prototype.handleScroll = function() {
    $("body").css("background-position", "" + 
        "-" + (this.$document.scrollLeft() / 20) + "px " +
        "-" + (this.$document.scrollTop() / 20) + "px");
};

hh = new HomeHandler($(document));
