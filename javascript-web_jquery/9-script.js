// $(document).ready(function () {
//  $.ajax({
//    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
//    type: 'GET',
//    async: true,
//    dataType: 'jsonp',
//    crossDomain: true,
//    success: (data) => {
//      $('#hello').text(data.hello);
//    },
//    error: () => {
//      console.log('Error fetching translation.');
//    }
//  });
// });
$(document).ready(function () {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  const proxy = 'https://cors-anywhere.herokuapp.com/';
  $.get(proxy + url, function (data) {
    $('#hello').text(data.hello);
  });
});
