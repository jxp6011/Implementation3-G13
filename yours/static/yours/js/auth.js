console.log(isAuthenticated);

const elt = document.querySelector('a.link');

function handleClick(e) {
  if (!isAuthenticated) {     // (1)
    e.preventDefault();        // (2)
    alert('Login Required.');  // (3)
  }
}

elt.addEventListener('click', handleClick);
