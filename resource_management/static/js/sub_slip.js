var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function() {
    $('.take-sub-slip').on('click', function (e) {
        var slip_id = parseInt($(e.target).closest(".sub-slip")[0].id.split("_")[2]);
        $.ajax({
            url: take_slip_url,
            data: {'slip_id': slip_id},
            method: 'POST',
            success: function() {
                location.reload()
                alert("You have taken a sub slip");
            }
        })
    });
});