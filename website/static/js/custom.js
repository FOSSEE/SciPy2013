$(document).ready(function(){
  $("#sponsors img").mouseover(function(){
    var source = $(this).attr("src");
    source = source.replace("-alt.png", "-logo.png");
    $(this).attr("src", source);
  });
  
  $("#sponsors img").mouseleave(function(){
    var source = $(this).attr("src");
    source = source.replace("-logo.png", "-alt.png");
    $(this).attr("src", source);
  });
});