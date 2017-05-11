var Schedule = (function($) {

    "use strict";

    function Schedule(schedule_data) {


        this.schedule = schedule_data;
        this.table_body = $("#schedule_table>tbody");
        this.setup_table();
        this.fill_table();

    }

    Schedule.prototype.setup_table = function() {

        for (var i = 5; i <= 12; i++) {
            if (i ==12) {
                var id = i + "_pm";
                this.table_body.append($('<tr/>').attr('id', id));

                var row = $("tr[id=" + id + "]");
                row.append($('<td/>').html(i + ":00 PM"));
            }
            else {
                var id = i + "_am";
                this.table_body.append($('<tr/>').attr('id', id));

                var row = $("tr[id=" + id + "]");
                row.append($('<td/>').html(i + ":00 AM"));
            }
            for (var j = 0; j < 7; j++) {
                row.append($('<td/>').addClass("weekday_" + j));
            }

        }
        for (var i = 1; i < 12; i++) {
            var id = i + "_pm";
            this.table_body.append($('<tr/>').attr('id', id));

            var row = $("tr[id=" + id + "]");
            row.append($('<td/>').html(i + ":00 PM"));

            for (var j = 0; j < 7; j++) {
                row.append($('<td/>').addClass("weekday_" + j));
            }

        }
    };

    Schedule.prototype.fill_table = function() {
        $.each(this.schedule, function (i, shift) {
            $('tr .weekday_' + parseInt(i)).each(function(j, time_slot) {
                var start_parts = shift.start_time.split(":");
                var start = parseInt(start_parts[0]);
                if (start_parts[1].slice(-2) == "PM" && start != 12) {
                    start += 12
                }
                var end_parts = shift.end_time.split(":");
                var end = parseInt(end_parts[0]);
                if (end_parts[1].slice(-2) == "PM" && end != 12) {
                    end += 12
                }
                var row_parts = $(time_slot).parent('tr').attr('id').split("_");
                var row_time = parseInt(row_parts[0]);
                if (row_parts[1] == "pm" && row_time != 12) {
                    row_time += 12
                }
                if (row_time >= start && row_time <= end) {
                    if (shift.is_sub_shift) {
                        $(time_slot).addClass("working sub");
                    }
                    else if (shift.shift_taken) {
                        $(time_slot).addClass("working taken");
                    }
                    else if (shift.up_for_sub) {
                        $(time_slot).addClass("working up-for-sub");
                    }
                    else {
                        $(time_slot).addClass("working");
                    }

                }
            });
        });
    };
    return Schedule;

})(jQuery);