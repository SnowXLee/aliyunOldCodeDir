var fs = require('fs');
var config = {
  maxFiles: 20,
  maxConnections:15,
  rootPath: "/webroot"
};
var configTxt = JSON.stringify(config);
fs.writeFile('config.txt', configTxt, {encoding: 'utf8', flag:'w'}, function(err){
  if(err){
    console.log("config Write Failed.");
  } else{
    console.log("Config Saved.");
  }
});
