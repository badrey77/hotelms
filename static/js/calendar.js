$(document).ready(function() {
    $.each($("rect[id^='legende_']"), function () {
        $(this).mousedown(function (e) {
            $.each($("rect[id^='legende_']"),function () {
                $(this).removeClass('selected');
            });
            $(this).addClass("selected");
        })
    });
    $.each($("rect[id^='rect']"), function () {
        $(this).mousedown(function (e) {
            $(this).toggleClass('rect_B');
        });
        $(this).hover(function (e) {
            if(e.buttons == 1){
                var selectedOption = $("rect.selected").first()[0];
                console.log(selectedOption.id)
                switch (selectedOption) {
                    case "rect_B":
                        $(this).addClass('rect_B');
                }
            }
        }, function (e) {

        });
    });
});