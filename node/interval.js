function printHello(){
   console.log( "Hello, World!");
}

function stopTimer(){
  clearInterval(inter);
}
// Now call above function after 2 seconds
setTimeout = (stopTimer, 2000);
var inter = setInterval(printHello, 500);
