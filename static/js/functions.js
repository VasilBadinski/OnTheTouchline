function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.body.style.backgroundColor = "white";
}

window.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('nav.sidenav a');

  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });
});

function swapWithMain(clickedSidebar) {
    const mainArticle = document.getElementById('mainArticle');

    const mainTitle = mainArticle.querySelector('h2').textContent;
    const mainSummary = mainArticle.querySelector('p').textContent;
    const mainImageSrc = mainArticle.querySelector('img').src;
    const mainImageAlt = mainArticle.querySelector('img').alt;

    const sideTitle = clickedSidebar.querySelector('h2').textContent;
    const sideSummary = clickedSidebar.querySelector('p').textContent;
    const sideImage = clickedSidebar.querySelector('img');

    mainArticle.querySelector('h2').textContent = sideTitle;
    mainArticle.querySelector('p').textContent = sideSummary;
    const mainImage = mainArticle.querySelector('img');
    mainImage.src = sideImage.src;
    mainImage.alt = sideImage.alt;

    clickedSidebar.querySelector('h2').textContent = mainTitle;
    clickedSidebar.querySelector('p').textContent = mainSummary;
    sideImage.src = mainImageSrc;
    sideImage.alt = mainImageAlt;
}

