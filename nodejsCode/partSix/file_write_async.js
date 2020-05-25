var fs = require('fs');
var fruitBowl = ['apple', 'orange', 'banana', 'grapes'];
function writeFruit(fd){
  if(fruitBowl.length){
    var fruit = fruitBowl.pop() + " ";
    fs.write(fd, fruit, null, 'utf8', function(err, bytes){
      if(err){
        console.log("File Write Failed.");
      } else{
        console.log("Write: %s %dbytes", fruit, bytes); 
      }
    });
  } else{
    fs.close(fd);
  }
}
fs.open('fruit.txt', 'w', function(err, fd){
  for(var j = 0; j <= 3; j++){
    writeFruit(fd);
  }
});
