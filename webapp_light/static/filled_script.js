$(document).ready(function() {
    $('#info-wrapper').slideDown(500);
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#title-wrapper").offset().top + $("#title-wrapper").height()
    }, 1000);
});