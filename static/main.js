let profileBtn = $("#profileBtn")
let profile = $("#profile")
profile.hide()
function displayProfile(){
    profile.show()
    $("body").css("opacity", 0.5)
    profile.css("opacity", 1.0)
}
profileBtn.on("click", displayProfile)