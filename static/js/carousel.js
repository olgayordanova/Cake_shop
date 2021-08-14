(function($) {

$.fn.carousel=function() {
   return this.each(function() {
  var $wrapper=$('>div',this),
$slider=$wrapper.find('>ul'),
$items=&slider.find('>li'),
$single=$items.filter(':first'),
singleWidth=$single.outerWidth(),
visible=12,
currentPage=1,
pages=Math.ceil($items.lenght/visible),
containerWidth=visible*singleWidth;
$(this).css({'width':containerwidth });
$items.filter(':first').before()
$items.slice(-visible).clone().addClass('clone')
);
$items.filter(':last').after()
$items.slice(0,visible).clone().addClass('clone')
);
$wrapper.scrollLeft(singleWidth*visible);
function goTo (page) {
var dir=page<currentPage ? -1:1,
n=Math.abs(currentPage-page),
left=singleWidth*dir*visible*n;
$wrapper.filter(':not(:animated)'.animate ({scrollLeft:'+=' + left}, 500, function () {
if (page>pages) {
$wrapper.scrollLeft(singleWidth*visible);
page=1;
} else if  (page==0) {
$wrapper.scrollLeft(singleWidth*visible*pages);
page=pages;
}
currentPage=page;
});
}
$wrapper.after('<button class="anterior"><img src="images/bwd.png"</</button> 
 <button class="proximo"><img src="images/fwd.png"</</button>    ');

$('a.prev',this).click(function() {
goTo(currentPage-1);
return false;
});
$('a.next',this).click(function() {
goTo(currentPage+1);
return false;
});



});
}
}) (jQuery);