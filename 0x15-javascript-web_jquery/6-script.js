//script that updates the text of the <header> element
$(function () {
  $("DIV#update_header").click(function () {
    $("header").text("New Header!!!");
  });
});
