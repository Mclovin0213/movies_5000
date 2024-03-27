element = document.getElementById('content');
element.innerHTML = `
    <h2>Top 100</h2>
`;

let top100;

function getTop100() {
    fetch('/get_100')
        .then(response => response.json())
        .then(data => {
            top100 = data;
            console.log(top100);
        });
}

// Function to generate the top 100 elements
function generateTop100Elements() {

}

// Function to set the active button
function setActive(button) {
    const buttons = document.querySelectorAll('.radioButton');
    buttons.forEach(btn => {
      btn.classList.remove('active');
    });
  
    button.classList.add('active');

    changeContent(button.textContent)
}

function changeContent(title) {
    if (title == "Top 100") {
        element.innerHTML = `
            <h2>${title}</h2>
        `;
    } else if (title == "Budget vs Revenue") {
        element.innerHTML = `
            <h2>${title}</h2>
        `;
    } else if (title == "Popularity vs Rating") {
        element.innerHTML = `
            <h2>${title}</h2>
        `;
    } else if (title == "Production Company Stats") {
        element.innerHTML = `
            <h2>${title}</h2>
        `;
    }
}