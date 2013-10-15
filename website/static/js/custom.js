$(document).ready(function(){

var dadar = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=dadar+station&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FZMqIgEdYXRXBCkdh7S_3M7nOzHZNplA5uMmIw%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=&amp;sll=19.037454,72.908363&amp;sspn=0.188885,0.308647&amp;mra=ls&amp;ie=UTF8&amp;ll=19.037454,72.908363&amp;spn=0.112729,0.100371&amp;t=m&amp;output=embed"></iframe>'

var thane = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Thane+Railway+Station,+Station+Road+Kopri,+Thane,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FY7CJAEd_4BZBCkjQ1Rf37jnOzF9iI2abfvySQ%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=4&amp;oq=IIT&amp;sll=19.155222,72.944412&amp;sspn=0.094375,0.154324&amp;mra=pd&amp;ie=UTF8&amp;ll=19.155222,72.944412&amp;spn=0.06341,0.058068&amp;t=m&amp;output=embed"></iframe>' 

var bandra = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Bandra+Terminus,+Naupada,+Bandra+East,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FWLeIgEdQHdXBCm3sivHGcnnOzF9Gr08r3UTdQ%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=0&amp;oq=Bandra+ter&amp;sll=19.155709,72.945614&amp;sspn=0.094375,0.154324&amp;mra=ls&amp;ie=UTF8&amp;ll=19.155709,72.945614&amp;spn=0.079966,0.075124&amp;t=m&amp;output=embed"></iframe>'

var tilak = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Lokmanya+Tilak+Terminus,+Pipeline+Road,+Kurla,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FSb7IgEdST5YBCGh8y-GNk5pZinbn-jom8jnOzGh8y-GNk5pZg%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=0&amp;oq=Lokmany&amp;sll=19.101053,72.879009&amp;sspn=0.094406,0.154324&amp;mra=ls&amp;ie=UTF8&amp;ll=19.101053,72.879009&amp;spn=0.063015,0.045739&amp;t=m&amp;output=embed"></iframe>'

var central = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Mumbai+Central+station,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FVt4IQEd3SJXBCFssj0JqjsoWSmzxd6Nbs7nOzFssj0JqjsoWQ%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=&amp;sll=19.0472,72.879606&amp;sspn=0.188874,0.308647&amp;mra=ls&amp;ie=UTF8&amp;t=m&amp;ll=19.0472,72.879606&amp;spn=0.163085,0.117661&amp;output=embed"></iframe>'

var shivaji = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Chhatrapati+Shivaji+International+Airport,+Andheri+East,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FQFLIwEdg-NXBCGuqHTEYBrMHilHKb2ZUMjnOzGuqHTEYBrMHg%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=4&amp;oq=IIT&amp;sll=19.099667,72.883154&amp;sspn=0.094407,0.154324&amp;mra=pd&amp;ie=UTF8&amp;t=m&amp;ll=19.110379,72.895527&amp;spn=0.029763,0.042183&amp;output=embed"></iframe>'

var airport = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Chhatrapati+Shivaji+International+Airport,+Andheri+East,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FQFLIwEdg-NXBCGuqHTEYBrMHilHKb2ZUMjnOzGuqHTEYBrMHg%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=4&amp;oq=IIT&amp;sll=19.099667,72.883154&amp;sspn=0.094407,0.154324&amp;mra=pd&amp;ie=UTF8&amp;t=m&amp;ll=19.110379,72.895527&amp;spn=0.029763,0.042183&amp;output=embed"></iframe>'

  /* Load map on link click */
  $(".side-nav li a").click(function(){
    
    var clicked = $(this).attr("id");
    switch(clicked){
    	case "airport": clicked = airport; break;
    	case "dadar": clicked = dadar; break;
    	case "thane": clicked = thane; break;
    	case "bandra": clicked = bandra; break;
    	case "tilak": clicked = tilak; break;
    	case "central": clicked = central; break;
    	case "shivaji": clicked = shivaji; break;
    }
    $(".side-nav li").removeClass("active");
    $(this).closest('li').addClass("active");
    $("#mappy").html(clicked);

    /* Map loading display */

  });
});