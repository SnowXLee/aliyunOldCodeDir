var http = require('http');
var url = require('url');
var querystring = require('querystring');
//var APIKEY = ""//place your own api key within the quotes.
function sendResponse(weatherData, res){
  var page = '<!DOCTYPE html>' +
    '<html lang="en">' +
    '<head>' +
    '<meta charset="UTF-8">' +
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">' +
    '<title>External Example</title>' +
    '</head>' +
    '<body>' +
    '<form method="post">City:' + 
    '<input name="city">' +
    '<br>' +
    '<input type="submit" value="Get Weather">' +
    '</from>';
    if(weatherData){
      page += '<h1>Weather Info</h1><p>' + weatherData + '</p>';
    }
    page += '</body></html>';
    console.log(page);
    res.end(page);
}
function parseWeather(weatherResponse, res){
  var weatherData = '';
  weatherResponse.on('data', function(chunk){
    weatherData += chunk;
  });
}
function getWeather(city, res){
  city = city.replace(' ', '-');
  console.log(city);
  var options = {
    //host: 'http://flash.weather.com.cn/wmaps/xml/china.xml',
    host: 'flash.weather.com.cn',
    path: 'wmaps/xml/china.xml'
  };
  http.request(options, function(weatherResponse){
    console.log(weatherResponse);
    parseWeather(weatherResponse, res);
  }).end();
}
http.createServer(function(req, res){
  console.log(req.method);
  if(req.method == "POST"){
    var reqData = '';
    req.on('data', function(chunk){
      reqData += chunk;
    });
    req.on('end', function(){
      var postParams = querystring.parse(reqData);
      console.log(postParams);
      //getWeather(postParams.city, res);
      getWeather(postParams.city, res);
    });
  } else{
    sendResponse(null, res);
  }
}).listen(8000);
