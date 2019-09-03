//Tab Script
function openGuild(evt, guildName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(guildName).style.display = "block";
    evt.currentTarget.className += " active";
  }

// Post script
var data = {};

function addElement(elementTag, elementId, elementValue, html) {
    // Adds an element to the document
    var p = document.getElementById("queue");
    var newElement = document.createElement(elementTag);
    newElement.setAttribute('id', elementId);
    newElement.setAttribute('value', elementValue);
    newElement.innerHTML = html;
    p.appendChild(newElement);
}

function removeElement(elementId) {
    // Removes an element from the document
    var element = document.getElementById(elementId);
    element.parentNode.removeChild(element);
    delete data[elementId];
    console.log(`removed player`)
    console.log(data)
}
//need tp fix to allow multiples
i = 0;
function addPlayer(playerId, playerName, filename) {
    playerId = playerId + i;
    i++;
    var html = `<span id="${playerId}">${playerName}</span> <a href="" class="remove" onclick="javascript:removeElement('${playerId}'); return false;">Remove</a>`;
    addElement('p', playerId, filename, html);
    data[playerId] = filename;
    console.log(`added player`)
    console.log(data)
}

function postData() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/makePDF', true);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    xhr.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // Request finished. Do processing here.
            window.location.href = `/download/${xhr.response}`;
        }
    }
    if (Object.keys(data).length === 0 && data.constructor === Object){
        window.alert("Empty Queue")
    } else if (Object.keys(data).length > 20 && data.constructor === Object) {
        window.alert("Sorry, The Limit is 20.")
    } else {
        var element = document.getElementById('createPDF');
        element.disabled = true;
        element.innerHTML = "Please Wait"
        xhr.send(JSON.stringify(data));
    }
}