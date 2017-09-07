/**
 * Created by Reinier on 26-6-2017.
 *
 */

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});
