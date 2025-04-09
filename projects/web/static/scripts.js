const expandableItems = document.querySelectorAll('.expandable');

expandableItems.forEach(item => {
  item.addEventListener('click', function(event) {
    // Prevent the click from triggering any parent expandable items
    event.stopPropagation();

    // Find the nested UL within the clicked LI
    const nestedUl = this.querySelector('.nested-ul');

    if (nestedUl) {
      // Check both the computed style and inline style
      const isHidden = window.getComputedStyle(nestedUl).display === 'none';
      nestedUl.style.display = isHidden ? 'block' : 'none';
      this.classList.toggle('expanded');
    }
  });
});