

function redirect(to){
    switch(to) {
        case "login":
          alert("omadam tosh")
          window.location = "./login.html"
          history.pushState({}, "", "/details");
          break;
        case "signup":
          // code block
          break;
        default:
          
      }
}