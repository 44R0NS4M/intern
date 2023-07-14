
    // function scrollf() {
    //   var elements = document.querySelectorAll("li a");
      
    //   elements.forEach(function(element){
    //   element.scrollIntoView({ behavior: "smooth"});});
    //   //const element = document.getElementById(id);
    //   element.addEventListener("click", function(event){event.preventDefault();});
    //   element.addEventListener('mouseover', function() {
    //     element.classList.add('hovered');
    //   });
      
    //   // Remove the class on mouseout
    //   element.addEventListener('mouseout', function() {
    //     element.classList.remove('hovered');
    //   }); 
    // }
  
    
    function scrollf(id) {
      var links = document.querySelectorAll('#scrl');
      const element = document.getElementById(id);
links.forEach(function(link) {
  link.addEventListener('click', function(event) {
    element.scrollIntoView({ behavior: "smooth"});
    event.preventDefault();
  });

  link.addEventListener('mouseover', function() {
    this.classList.add('hovered');
  });

  link.addEventListener('mouseout', function() {
    this.classList.remove('hovered');
  });
});
    }
  