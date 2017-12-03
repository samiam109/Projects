function postEmail() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()[0];

  var lastRow = sheet.getLastRow();
  var lastColumn = sheet.getLastColumn();

  var type = sheet.getRange(lastRow, 2).getValue();
  var email = sheet.getRange(lastRow, 3).getValue();
  var isBeta = sheet.getRange(lastRow, 5).getValue();

  var url = (isBeta === "Beta") ? "http://ec2-34-209-188-172.us-west-2.compute.amazonaws.com:1313/beta/add" : "http://ec2-35-167-227-237.us-west-2.compute.amazonaws.com:1313/beta/add";

  var data = {
    "email": email,
    "type": type,
  };
  var options = {
    "method" : "post",
    "contentType": "application/json",
    "payload" : JSON.stringify(data),
    "muteHttpExceptions" : true,
  };

  var request = UrlFetchApp.fetch(url, options);

  var status = request.getResponseCode();
  var res = JSON.parse(request.getContentText());

  Logger.log(res);
  Logger.log(status);
  
  var msg = "";
  if (status === 200 || status === 201) {
    //if successful write token to spreadsheet
    msg = res.token ? res.token : "ERROR on 200";
    Logger.log(res.token ? res.token : "ERROR");
  } else {
    msg = res.errors.email ? res.errors.email : "ERROR not 200";
    Logger.log("An Error Occurred: " + msg);
  }

  sheet.getRange(lastRow, lastColumn).setValue(msg)
}
