// async simply allows us to write promises based code as if it was synchronous and it checks that we are not breaking the execution thread. 
// Await function is used to wait for the promise. It could be used within the async block only. 
// It makes the code wait until the promise returns a result. 
async function getUsers() {
    await fetch("https://reqres.in/api/users")
    .then(res=>res.json())
    .then(data=>console.log(data))
    .catch(error=>console.log("Error"))
}

async function saveUsers() {
    await fetch("https://reqres.in/api/users")
    .then(res=>res.json())
    .then(data=> jsonData = JSON.stringify(data))
    .catch(error=>console.log("Error"))
    //creating an anchor element using jQuery/Javascript
    var element = document.createElement('a');
    // Encodes a text string as a valid component of a Uniform Resource Identifier 
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(jsonData));
    // The download attribute specifies that the target will be downloaded
    element.setAttribute('download', "savedUsers.json");
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
    console.log("the data is saved");
  }
getUsers();
  

