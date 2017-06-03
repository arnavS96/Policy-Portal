<script>
$(document).ready(function() {
    $('.add-member').click(function(ev) {
        ev.preventDefault();
        var count = $('#members-form-container').children().length;
        var tmplMarkup = $('#member-template').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#members-form-container').append(compiledTmpl);

        // update form count
        $('#id_member_members-TOTAL_FORMS').attr('value', count+1);

        // some animate to scroll to view our new form
        $('html, body').animate({
                scrollTop: $("#add-member-button").position().top-200
            }, 800);
    });
});
</script>