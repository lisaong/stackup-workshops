// https://docs.microsoft.com/en-us/aspnet/core/blazor/call-javascript-from-dotnet?view=aspnetcore-3.1

// Blazor will automatically escape raw html.
// Run a client-side script to decode for readability in the browser.
// https://stackoverflow.com/questions/1912501/unescape-html-entities-in-javascript
function htmlDecode(input) {
    var doc = new DOMParser().parseFromString(input, "text/html");
    return doc.documentElement.textContent;
  } 

window.unescapeHtml = (rawHtml) => {
    return htmlDecode(rawHtml);
};