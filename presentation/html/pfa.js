function GetElementInsideContainer(containerID, childID) {
    var elm = {};
    var elms = document.getElementById(containerID).getElementsByTagName("*");
    for (var i = 0; i < elms.length; i++) {
        if (elms[i].id === childID) {
            elm = elms[i];
            break;
        }
    }
    return elm;
}

function openFig(evt, contID, figID) {
  // Declare all variables
  var i, tabcontent, tablinks, cont;
	
	// Elements of the container
	var elms = document.getElementById(contID).getElementsByTagName("*");

  // Get all elements with class="tabcontent" and hide them
  for (i = 0; i < elms.length; i++) {
		if(elms[i].className == "tabcontent") {
      elms[i].style.display = "none";
    }
  }

  // Get all elements with class="tablinks" and remove the class "active"
  for (i = 0; i < elms.length; i++) {
    if(elms[i].className == "tab") {
      tablinks = elms[i].getElementsByClassName("tablinks");
      for (j = 0; j < tablinks.length; j++) {
        tablinks[j].className = tablinks[j].className.replace(" active", "");
      }
    }
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(figID).style.display = "block";
  evt.currentTarget.className += " active";
}


