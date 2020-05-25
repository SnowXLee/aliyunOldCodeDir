var censor = require("censorify");
console.log(censor.getCensoredWords());
console.log(censor.censor("Some very sad, bad and mad text."));
censor.addCensoreWord("gloomy");
console.log(censor.getCensoredWords());
console.log(censor.censor("A very gloomy day."));
