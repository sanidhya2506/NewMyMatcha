// script.js
fetch('dramas.json')
  .then(response => {
    if (!response.ok) throw new Error("Failed to load dramas.json");
    return response.json();
  })
  .then(data => {
    const dramaList = document.getElementById('dramaList');

    for (const country in data) {
      // Country header
      const countryHeader = document.createElement('h3');
      countryHeader.textContent = country.charAt(0).toUpperCase() + country.slice(1) + " Dramas";
      dramaList.appendChild(countryHeader);

      // Grid container
      const countryGrid = document.createElement('div');
      countryGrid.style.display = "grid";
      countryGrid.style.gridTemplateColumns = "repeat(auto-fit, minmax(200px, 1fr))";
      countryGrid.style.gap = "20px";
      countryGrid.style.marginBottom = "30px";

      data[country].forEach(drama => {
        const card = document.createElement('a'); // Use <a> to wrap whole card
        card.href = drama.link;
        card.className = "card-result"; // matches your CSS

        card.innerHTML = `
          <img src="${drama.image}" alt="${drama.title}">
          <div class="card-info">
            <h4>${drama.title} (${drama.year})</h4>
            <p>${drama.genre.join(', ')}</p>
          </div>
        `;

        countryGrid.appendChild(card);
      });

      dramaList.appendChild(countryGrid);
    }
  })
  .catch(err => console.error('Error loading dramas:', err));
