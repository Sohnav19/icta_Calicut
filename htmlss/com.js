function Submit1(){
    var n1=document.getElementById("getnumber1").value;
    console.log(n1)
    var n2=document.getElementById("getnumber2").value;
    console.log(n2)
    
    var n3=document.getElementById("getnumber3").value;
    console.log(n3)


    var x=parseInt(n1);
    var y=parseInt(n2);
    var z=parseInt(n3);

    var ans=n1>n2?(n1>n3?n1:n3):(n2>n3?n2:n3);
    console.log(ans)
    alert("largest is "+ans);
    document.getElementById("result").innerHTML="<table class='table'><tr><td>result is "+ans+"</td></tr></table>";

}
function Submit2(){
    var n1=document.getElementById("getnumber1").value;
    console.log(n1)
    var n2=document.getElementById("getnumber2").value;
    console.log(n2)
    
    var n3=document.getElementById("getnumber3").value;
    console.log(n3)


    var x=parseInt(n1);
    var y=parseInt(n2);
    var z=parseInt(n3);

    var an=n1<n2?(n1<n3?n1:n3):(n2<n3?n2:n3);
    console.log(an)
    alert("smallest is "+an);
    document.getElementById("result").innerHTML="<table class='table'><tr><td>result is "+an+"</td></tr></table>";

}