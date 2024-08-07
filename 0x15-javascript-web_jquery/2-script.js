// Updates the text color with jQuery when user clicks on `DIV#red_header`

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('header').css('color', '#FF0000');
  });
});
