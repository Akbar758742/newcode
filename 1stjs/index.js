// var a=prompt("enter  first name"); 
// var b=prompt("enter last name"); 
// var c=a.concat(" "+b);
// document.write(c+"<br>");
// var d=c.length
// document.write("total lenth is "+d+"</br>");
// document.write("uppercase is "+ c.toUpperCase()+"<br>");
// document.write("lowercase is "+ c.toLowerCase());



var a=prompt("enter first number:");
var b=prompt("enere second number");
a=parseInt(a,10);
b=parseInt(b,10);
var sum,sub,mul,div;
sum=a+b;
sub=a-b;
mul=a*b;
div=a/b;
document.write(a+"+"+b+"="+sum+"<br>");
document.write(a+"-"+b+"="+sub+"<br>");
document.write(a+"*"+b+"="+mul+"<br>");
document.write(a+"/"+b+"="+div+"<br>");




var far=parseFloat(prompt("enter fahreinheit"));
var celseus= (far-32)*(5/9);
document.write("celcius is="+celseus);