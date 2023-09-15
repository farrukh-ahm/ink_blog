document.addEventListener('DOMContentLoaded', ()=> {
    console.log("connected, hello")
    console.log("here")
    // NAVBAR INIT
    var navbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(navbar);

    // SELECT INIT
    let selectInt = document.querySelectorAll('select');
    M.FormSelect.init(selectInt);

    // MODAL TRIGGER
    // let elems = document.querySelectorAll('.modal');
    // M.Modal.init(elems);
    let popOp = document.querySelector('.modal');
    let modal = M.Modal.init(popOp);
    let modalTrigger = document.querySelector(".modal-trigger")
    let modalClose = document.querySelector(".modal-close")
    modalTrigger.addEventListener("click", ()=>{
      console.log("click")
      modal.open()
    })
    for(let close of modalClose){
     close.addEventListener("click", ()=>{
        modal.close()
    })
    }

  });