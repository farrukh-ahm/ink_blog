document.addEventListener('DOMContentLoaded', ()=> {
    console.log("connected")
    
    // NAVBAR INIT
    var navbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(navbar);

    // SELECT INIT
    let selectInt = document.querySelectorAll('select');
    M.FormSelect.init(selectInt);

  });