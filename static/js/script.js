document.addEventListener('DOMContentLoaded', ()=> {
    console.log("connected")
    // NAVBAR INIT
    var navbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(navbar);

    // SELECT INIT
    let selectInt = document.querySelectorAll('select');
    M.FormSelect.init(selectInt);

    // MODAL TRIGGER
    let popOp = document.querySelector('.modal');
    let modal = M.Modal.init(popOp);
    let modalTrigger = document.querySelector(".modal-trigger");
    let modalClose = document.querySelectorAll(".modal-close");
    let idHandler = document.querySelector(".approval-delete-form")
    modalTrigger.addEventListener("click", (e)=>{
      let commentId = e.target.getAttribute("data-type")
      idHandler.setAttribute("action", `/comment_delete/${commentId}`)
      console.log(commentId)
      modal.open()
    })

    modalClose.forEach(close => ()=>{
      close.addEventListener("click", ()=>{
        modal.close()
      })
    })

  });