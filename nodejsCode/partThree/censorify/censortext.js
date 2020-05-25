var censoreWords = ["sad", "bad", "mad"];
var customCensoreWords = [];
function censor(inStr) {
  for (idx in censoreWords){
    inStr = inStr.replace(censoreWords[idx], "****");
  }
  for (idx in customCensoreWords){
    inStr = inStr.replace(customCensoreWords[idx], "****");
  }
  return inStr;
}
function addCensoredWord(word){
  customCensoreWords.push(word);
}
function getCensoredWords(){
  return censoreWords.concat(customCensoreWords);
}
exports.censor = censor;
exports.addCensoredWord = addCensoreWord;
exports.getCensoredWords = getCensoreWords;
