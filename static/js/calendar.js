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
                var selectedOption = $("rect.selected").first()[0];
            console.log(selectedOption)
                switch (selectedOption.id) {
                    case "legende_L":
                        $(this).toggleClass('rect_L');
                        break;
                    case "legende_B":
                        $(this).toggleClass('rect_B');
                        break;
                    case "legende_C":
                        $(this).toggleClass('rect_C');
                        break;
                    case "legende_T":
                        $(this).toggleClass('rect_T');
                        break;
                    case "legende_O":
                        $(this).toggleClass('rect_O');
                        break;
                    case "legende_N":
                        $(this).toggleClass('rect_N');
                        break;
                    case "legende_M":
                        $(this).toggleClass('rect_M');
                        break;
                }
        });
        $(this).hover(function (e) {
            if(e.buttons == 1){
                var selectedOption = $("rect.selected").first()[0];
                switch (selectedOption.id) {
                    case "legende_L":
                        $(this).toggleClass('rect_L');
                        break;
                    case "legende_B":
                        $(this).toggleClass('rect_B');
                        break;
                    case "legende_C":
                        $(this).toggleClass('rect_C');
                        break;
                    case "legende_T":
                        $(this).toggleClass('rect_T');
                        break;
                    case "legende_O":
                        $(this).toggleClass('rect_O');
                        break;
                    case "legende_N":
                        $(this).toggleClass('rect_N');
                        break;
                    case "legende_M":
                        $(this).toggleClass('rect_M');
                        break;
                }
            }
        }, function (e) {

        });
    });
});