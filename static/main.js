let addNote = $("#addNote")
let stickyList = $("#stickyList")
function addStikyNote(){
    // let addNote = $("#addNote")
    // addNote.parent().parent().append("<li><a href='#' contenteditable><h2>Title #8</h2><p>Text Content #8</p></a></li>")
    // stickyList.append("<li><button id='addNote'><div><h1 id='plus'>+</h1><p id='subtitle'>add sticky note</p></div></button></li>")
    console.log(addNote.parent().parent())
    addNote.parent().before("<li><a href='#' contenteditable><h2>Title #8</h2><p>Text Content #8</p></a></li>")
}
addNote.on("click", addStikyNote)