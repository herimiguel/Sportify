$(document).ready(function() {
    $('.login').slideDown(1000);
});

$(document).ready(function() {
    $('.main').slideDown(1000);
});

$(document).ready(function() {
    $('register').slideDown(1000);
});
    
console.log('NOW READY')

$('.loginbtn').click(function() {
    $('.main').fadeOut(750);
    $('.login').slideUp(750);
    console.log("LOGIN")

});



$('.group').click(function() {
    $('.grouplist').slideToggle(750);
});

$('.group1').click(function() {
    $('.grouplist1').slideToggle(750);
});

