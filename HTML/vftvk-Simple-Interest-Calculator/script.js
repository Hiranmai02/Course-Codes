function isempty(){
    var p = document.getElementById("principal").value;
    if( (p == "") || (p == null)){
        alert("Please enter a positive number");
        p.focus();
        return false;
    }
}
function check()
{
    var p = document.getElementById("principal").value;
    if((p <= 0)){
        alert("Please enter a positive number");
        p.focus();
        return false;
    }
}

function compute()
{
    var p = document.getElementById("principal").value;
    var n = document.getElementById("years").value;
    var r = document.getElementById("rate").value;
    var c = document.getElementById("current").value;
    document.getElementById("result").innerHTML = p*n*r/100
    document.getElementById("p").innerHTML = p
    document.getElementById("r").innerHTML = r
    document.getElementById("c").innerHTML = parseInt(c)+parseInt(n)
}  

function sliderChange(val) {
    var val = document.getElementById('rate').value;
    document.getElementById('output').innerHTML = val;
    console.log(val)
}