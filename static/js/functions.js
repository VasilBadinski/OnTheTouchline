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


function toggleLeagueMenu() {
    const menu = document.getElementById("league-submenu");
    menu.style.display = (menu.style.display === "flex") ? "none" : "flex";
}


document.addEventListener('DOMContentLoaded', function() {
  const leagueSelect = document.getElementById('id_league');
  const clubSelect = document.getElementById('id_club');

  leagueSelect.addEventListener('change', function() {
    const leagueId = this.value;

    fetch(`/ajax/get-clubs/?league_id=${leagueId}`)
      .then(response => response.json())
      .then(data => {
        clubSelect.innerHTML = '';

        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = '';
        clubSelect.appendChild(defaultOption);

        data.clubs.forEach(club => {
          const option = document.createElement('option');
          option.value = club.id;
          option.text = club.eng_name;
          clubSelect.appendChild(option);
        });
      });
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const clubSelect = document.getElementById('id_club');
  const playerSelect = document.getElementById('id_player');

  clubSelect.addEventListener('change', function() {
    const clubId = this.value;

    fetch(`/ajax/get-players/?club_id=${clubId}`)
      .then(response => response.json())
      .then(data => {
        playerSelect.innerHTML = '';

        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = '';
        playerSelect.appendChild(defaultOption);

        data.players.forEach(player => {
          const option = document.createElement('option');
          option.value = player.id;
          option.text = player.eng_name;
          playerSelect.appendChild(option);
        });
      });
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const leagueSelect = document.getElementById('id_league');
  const homeTeamSelect = document.getElementById('id_home_team');
  const awayTeamSelect = document.getElementById('id_away_team');

  leagueSelect.addEventListener('change', function() {
    const leagueId = this.value;

    fetch(`/ajax/get-clubs/?league_id=${leagueId}`)
      .then(response => response.json())
      .then(data => {
        // Clear existing options
        homeTeamSelect.innerHTML = '';
        awayTeamSelect.innerHTML = '';

        // Add default empty option
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = '';
        homeTeamSelect.appendChild(defaultOption.cloneNode(true));
        awayTeamSelect.appendChild(defaultOption.cloneNode(true));

        // Populate both selects with clubs
        data.clubs.forEach(club => {
          const option1 = document.createElement('option');
          option1.value = club.id;
          option1.text = club.eng_name;

          const option2 = option1.cloneNode(true);  // Clone for away team

          homeTeamSelect.appendChild(option1);
          awayTeamSelect.appendChild(option2);
        });
      });
  });
});

document.addEventListener("DOMContentLoaded", function () {
   const navLinks = document.querySelectorAll(".club-nav ul li a");
   const currentUrl = window.location.href;

   let activeFound = false;

   navLinks.forEach(link => {
      if (currentUrl === link.href) {
         link.parentElement.classList.add("active");
         activeFound = true;
      }
   });

   if (!activeFound) {
      const overviewLink = document.querySelector('.club-nav ul li a[href$="/overview/"]');
      if (overviewLink) {
         window.location.href = overviewLink.href;
      }
   }
});

