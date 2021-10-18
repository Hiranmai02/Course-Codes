function compute()
{
    var p = document.getElementById("principal").value;
    var n = document.getElementById("years").value;
    var r = document.getElementById("rate").value;
    document.getElementById("result").innerHTML = p*n*r/100
}  

function sliderChange(val) {
    var val = document.getElementById('rate').value;
    document.getElementById('output').innerHTML = val;
    console.log(val)
}