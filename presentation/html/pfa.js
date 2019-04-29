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

// Tabbed figures
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

// Collapsible
function clickCollapsible(id) {
	var elm = document.getElementById(id);
	elm.classList.toggle("active");
	var content = elm.nextElementSibling;
	if (content.style.display === "block") {
		content.style.display = "none";
	} else {
		content.style.display = "block";
	}
}

// Once thebelab is ready, auto-run all the cells in a "thebeAuto" div
thebelab.on("status", function(evt, data) {
		if (data.status == "ready") {
      // Find my special "auto-run" divs
			var autos = document.getElementsByClassName("thebeAuto");
			for (i = 0; i < autos.length; i++) {
				// Get all the "thebelab-cell" elements
				var cells = autos[i].childNodes;
				for (j = 0; j < cells.length; j++) {
					if (cells[j].className == "thebelab-cell") {
            console.log("Auto-running thebeCell. Ignore the following error")
            console.log(cells[j])
            cells[j].children[1].click()
					}
				}
			}
		}
})


