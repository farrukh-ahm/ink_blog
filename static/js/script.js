document.addEventListener('DOMContentLoaded', ()=> {
    console.log("connected")
    // NAVBAR INIT
    var navbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(navbar);

    // SELECT INIT
    let selectInt = document.querySelectorAll('select');
    M.FormSelect.init(selectInt);

    // MODAL TRIGGER
    let popOp = document.querySelector('#modal1');
    let modal = M.Modal.init(popOp);
    let modalTrigger = document.querySelectorAll(".modal-trigger");
    let modalClose = document.querySelectorAll(".modal-close");
    let idHandler = document.querySelector(".comment-delete-form");
    if(modalTrigger){

      modalTrigger.forEach(open1 => {

        open1.addEventListener("click", (e)=>{
          let commentId = e.target.getAttribute("data-type");
          idHandler.setAttribute("action", `/comment_delete/${commentId}`);
          console.log(commentId);
          modal.open();
        })

      })

      // modalTrigger.addEventListener("click", (e)=>{
      //   let commentId = e.target.getAttribute("data-type")
      //   idHandler.setAttribute("action", `/comment_delete/${commentId}`)
      //   console.log(commentId)
      //   modal.open()
      // })

    }

    modalClose.forEach(close =>{
      close.addEventListener("click", ()=>{
        modal.close()
      })
    })

  });

    // POST DELETE MODAL
    let pdPopUp = document.querySelector("#modal2");
    let modal2 = M.Modal.init(pdPopUp);
    let modalTrigger2 = document.querySelectorAll(".modal-trigger-2");
    let modalClose2 = document.querySelector(".modal-close-2");
    let postDelForm = document.querySelector(".post-delete-form");

    if (modalTrigger2) {

      modalTrigger2.forEach(openM => {
        openM.addEventListener("click", (e)=>{
          let getSlug = e.target.getAttribute("data-slug")
          postDelForm.setAttribute("action", `/post_delete/${getSlug}`)
          console.log(getSlug)
          modal2.open()
        })
      })
      // modalTrigger2.addEventListener("click", (e)=>{
      //   console.log("click")
      //   modal2.open()
      // })

    }

    modalClose2.addEventListener("click", ()=>{
      console.log("click again");
      modal2.close()
  })