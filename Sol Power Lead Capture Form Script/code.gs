// REQUIREMENTS
// submitted form data must be the last ROW - having any data below this will break the script:

// After saving this script, select "Triggers" => "Current script's triggers" => Click to add a script 
// Choose this script's name, select "From spreadsheet" and select "On form submit", and then save

function EmailFormConfirmation(e) {
  
  // sheets with form data in it
  var sheetName = "Sheet1"; 
  
  // column containing email address 1 = A, 2 = B etc
  var nameColumn = 2; 
  var emailColumn = 3;
  var phoneColumn = 4;
  var notesColumn = 5;
  
  // email subject and message to send to user
  var subject = "Sol Power Web Email";
  var message = "This is an automated form completion email.  Thanks for submitting!"; 
  
  
  // Main script follows       
  var s = SpreadsheetApp.getActiveSheet();
  var columns = s.getRange(1,1,1,s.getLastColumn()).getValues()[0];    
  var message = "A new lead was entered through the Sol Power Website Form. Info is below:\n\n";
  
  var i = 0;
  
  for ( var key in columns ) {
    var header = columns[key];
    i++;
    message += header + ' : '+ s.getRange(s.getLastRow(),i).getValue().toString() + "\n";   
  }
  

  // This is the MailApp service of Google Apps Script
  // that sends the email. You can also use GmailApp for HTML Mail.
    
  MailApp.sendEmail("ryanwright@solpowerllc.com,sam@awkwardengineer.com", subject, message); 
    
  
  

}