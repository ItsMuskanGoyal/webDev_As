function required()
{
var empt = document.form1.num1.value;
if (empt === "")
{
alert("Please input a Value");
return false;
}
else 
{
alert('Code has accepted : you can try another');
return true; 
}
}

document.write("Max is : ")

num1 = parseInt(prompt("Enter a number 1"))
num2 = parseInt(prompt("Enter a number 2"))
num3 = parseInt(prompt("Enter a number 3"))


if (num1>num2) {
    if (num1>mum3) {
        document.write(num1)
    } else {
        document.write(num3)
    }
} else {
    if (num2>num3) {
        document.write(num2)
    } else {
        document.write(num3)
    }
}


numx = parseInt(prompt("Enter a number"))




