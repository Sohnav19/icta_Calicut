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