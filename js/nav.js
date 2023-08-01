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
  