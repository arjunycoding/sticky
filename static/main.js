let addNote = $("#addNote")
let stickyList = $("#stickyList")
function addStikyNote(){
    stickyList.append("<li><a href='#' contenteditable><h2>Title #8</h2><p>Text Content #8</p></a></li>")
}
addNote.on("click", addStikyNote)