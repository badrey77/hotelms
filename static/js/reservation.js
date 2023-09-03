$(document).ready(function() {
    const $ = django.jQuery;
    if($("div.js-inline-admin-formset, div.inline-group") != 'undefined') {
        var ul = $.parseHTML('<ul></ul>')[0];

        $("div.js-inline-admin-formset, div.inline-group").wrapAll("<div id='new-tabs' />")
        $.each($("div.js-inline-admin-formset, div.inline-group"), function () {
            var str = $(this).attr('id').substring(0, $(this).attr('id').length - 10);
            var sli = '<li><a href="#' + $(this).attr("id") + '">' + str + '</a></li>';
            var li = $.parseHTML(sli)[0];
            $(ul).append(li);
        })
        $(function () {
            $("#new-tabs").prepend(ul);
            $("#new-tabs").tabs({active: 0});
        });
    }
});

const get_more_info = function () {
    const $ = django.jQuery;
    const label = $("#id_label").val();
    const info = $("#id_more_info");

    $.ajax({
        url:'/main/search?q='+label
    }).done(function (data) {
        try {
            var arr = JSON.parse(data);
            ingr = arr[0].food.nutrients
            info.text(JSON.stringify(ingr))
        }
        catch (e)
        {
            console.log(e)
        }
    })
}