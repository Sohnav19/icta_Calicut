function Read(){
    
    var name=document.getElementById("getname").value;
    console.log(name)
    var rollno=document.getElementById("getrollno").value;
    console.log(rollno)
    
    var admission=document.getElementById("getadmissionno").value;
    console.log(admission)
    var age=document.getElementById("getage").value;
    if(age>=18)
    {
        alert(" you r eligible")
        console.log(" u r eligible")
    }
    else
    {
        alert(" u r not eligible")
        console.log(" u r not eligible") 
    }

}
function Ans(){
    var opt1=document.getElementById("getoperand1").value;
    var opt2=document.getElementById("getoperand2").value;
    var op=document.getElementById("operation");
    var opr=op.options[op.selectedIndex].value;
    
    var x=parseInt(opt1);
    var y=parseInt(opt2);
    


    console.log(opt1)
    console.log(opt2)

    if(opr=="add"){
        var opt3=x+y
        console.log(opt3)
    }
    else if(opr=="sub"){
        var opt3=x-y
        console.log(opt3)

    }
    
    else if(opr=="mul"){
        var opt3=x*y
        console.log(opt3)

    }
    else if(opr=="div"){
        var opt3=x/y
        console.log(opt3)

    }

    

}
