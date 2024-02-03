const btnAbrirModal = document.querySelectorAll(".btn-abrir-modal");
const btnCerrarModal = document.querySelectorAll(".btn-cerrar-modal");

btnAbrirModal.forEach(btn=>{
    btn.addEventListener("click",()=>{
        let id = btn.getAttribute("data-id");
        let modal = document.querySelector("#modal-"+id);
        modal.showModal();
    })
})

btnCerrarModal.forEach(btn=>{
    btn.addEventListener("click", ()=>{
        let modal = btn.closest("dialog");
        modal.close();
    })
})