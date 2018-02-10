
<script>
   var url ="http://localhost:5000/all_user"

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "method": "GET",
    }

    $.ajax(settings).done(function (response) {
        $("#showData").hide();
        window.alert(response.data);
        if (response.success) {
            $("#showData").show(500);
            console.log(response.data);
 
        } else {
            $("#showData").hide(500);
        }
    }).fail(function (response) {
        $("#showData").show(500);
        $("#showData").html("<h5 class='center-align'>Network error, couldn't fetch routes.</h5>");
    });
    </script>
