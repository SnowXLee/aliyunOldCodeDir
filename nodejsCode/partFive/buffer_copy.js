var alphabet = new Buffer('lasjfklasdjfklasjklfaklsfklasdjfkl');
var StringDecoder = require('string_decoder').StringDecoder;
var decoder = new StringDecoder('utf8');
console.log(decoder.write(alphabet));
//复制整个缓冲区
var blank = new Buffer(26);
blank.fill();
console.log("Blank: " + decoder.write(blank));
alphabet.copy(blank);
console.log("Blank: " + decoder.write(blank));
//复制缓冲区的一部分
var dashes = new Buffer(26);
dashes.fill('-');
console.log("Dashes: " + decoder.write(dashes));
alphabet.copy(dashes, 10, 10, 15);
console.log("Dashes: " + decoder.write(dashes));
//利用缓冲区索引直接复制
var dots = new Buffer('-------------------------');
dots.fill('.');
console.log("Dots: " + decoder.write(dots));
for (var i = 0; i < dots.length; i++){
  if (i % 2){
    dots[i] = alphabet[i];
  }
}
console.log("Dots: " + dots.toString());
