var fs = require('fs');
fs.stat('file_stats.js', function(err, stats){
  if(!err){
    console.log('stats: ' + JSON.stringify(stats, null, '  '));
    console.log(stats.isFile() ? "Is a Folder" : "Is not a Folder");
    console.log(stats.isDirectory() ? "Is a Folder" : "Is not a Folder");
    stats.isDirectory();
    stats.isBlockDevice();
    stats.isCharacterDevice();
    stats.isFIFO();
    stats.isSocket();
  }
});
