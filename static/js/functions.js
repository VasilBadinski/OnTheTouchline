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

        homeTeamSelect.innerHTML = '';
        awayTeamSelect.innerHTML = '';


        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = '';
        homeTeamSelect.appendChild(defaultOption.cloneNode(true));
        awayTeamSelect.appendChild(defaultOption.cloneNode(true));


        data.clubs.forEach(club => {
          const option1 = document.createElement('option');
          option1.value = club.id;
          option1.text = club.eng_name;

          const option2 = option1.cloneNode(true);

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


document.addEventListener('DOMContentLoaded', () => {

    const questions = document.querySelectorAll('.question-block');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');

    if (questions.length === 0 || !prevBtn || !nextBtn || !submitBtn) {
        return;
    }

    let current = 0;

    function showStep(index) {
        questions.forEach((q, i) => {
            q.style.display = i === index ? 'block' : 'none';
        });

        prevBtn.style.display = index > 0 ? 'inline-block' : 'none';
        nextBtn.style.display = index < questions.length - 1 ? 'inline-block' : 'none';
        submitBtn.style.display = index === questions.length - 1 ? 'inline-block' : 'none';
    }

    prevBtn.addEventListener('click', () => {
        if (current > 0) current--;
        showStep(current);
    });

    nextBtn.addEventListener('click', () => {
        if (current < questions.length - 1) current++;
        showStep(current);
    });

    showStep(0);
});


document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search-input');
  const resultsDiv = document.getElementById('search-results');

  let controller = null;

  searchInput.addEventListener('input', async function () {
    const query = this.value.trim();

    if (controller) controller.abort();
    controller = new AbortController();
    const { signal } = controller;

    if (query.length === 0) {
      resultsDiv.innerHTML = '';
      resultsDiv.style.display = 'none';
      return;
    }

    try {
      const response = await fetch(`/api/search/?q=${encodeURIComponent(query)}`, { signal });
      if (!response.ok) throw new Error('Network error');
      const data = await response.json();

      renderResults(data);
    } catch (err) {
      if (err.name !== 'AbortError') {
        console.error(err);
        resultsDiv.innerHTML = '<p>Error loading results.</p>';
        resultsDiv.style.display = 'block';
      }
    }
  });

  function renderResults(data) {
      const players = data.players.map(p => `<a href="/players/${p.slug}/" class="result-item">👤 ${p.name}</a>`).join('');
      const leagues = data.leagues.map(l => `<a href="/leagues/${l.slug}/" class="result-item">🏆 ${l.name}</a>`).join('');
      const clubs = data.clubs.map(c => `<a href="/clubs/${c.slug}/" class="result-item">⚽ ${c.name}</a>`).join('');

      if (!players && !leagues && !clubs) {
        resultsDiv.innerHTML = '<p class="no-results">No results found.</p>';
      } else {
        resultsDiv.innerHTML = `
          ${players}
          ${leagues}
          ${clubs}
        `;
      }

      resultsDiv.style.display = 'block';
  }

  document.addEventListener('click', function (e) {
    if (!searchInput.contains(e.target) && !resultsDiv.contains(e.target)) {
      resultsDiv.style.display = 'none';
    }
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search-input');
  const clearIcon = document.getElementById('clear-icon');

  searchInput.addEventListener('input', function () {
    clearIcon.style.display = this.value ? 'block' : 'none';
  });

  clearIcon.addEventListener('click', function () {
    searchInput.value = '';
    searchInput.focus();
    clearIcon.style.display = 'none';
    document.getElementById('search-results').innerHTML = '';
  });
});
