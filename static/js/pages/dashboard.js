/*
 * Author: Abdullah A Almsaeed
 * Date: 4 Jan 2014
 * Description:
 *      This is a demo file used only for the main dashboard (index.html)
 **/

function submitFilter(id) {
    changeCategory(id);

   if(id === 0) {
       $("#id_category").val('').change();
   } else {
    $("#id_category").val(id).change();
   }


}

function changeCategory(id) {
  $(".categories").each(function (){
       $(this).removeClass('active');
   })


   $("a.category-"+ id).addClass('active');

}

$(function () {

  'use strict'
    var categoryId, startDate, endDate, keyword;

    $("#id_category").change(function () {
      categoryId = $(this).val();
      search(categoryId);
    });

    function search(categoryId, startDate, endDate, keyword) {
       var url = "search";
        changeCategory(categoryId);
        if(categoryId == 0 || categoryId == '0') categoryId = '';

      $.ajax({
        url: url,
        data: {
          'category': categoryId,
          'startDate': startDate,
          'endDate': endDate,
          'keyword': keyword
        },
        success: function (data) {
          $("#posts").html(data);
        }
      });
    }

  // Make the dashboard widgets sortable Using jquery UI
  $('.connectedSortable').sortable({
    placeholder: 'sort-highlight',
    connectWith: '.connectedSortable',
    handle: '.card-header, .nav-tabs',
    forcePlaceholderSize: true,
    zIndex: 999999
  })
  $('.connectedSortable .card-header, .connectedSortable .nav-tabs-custom').css('cursor', 'move')

  // jQuery UI sortable for the todo list
  $('.todo-list').sortable({
    placeholder: 'sort-highlight',
    handle: '.handle',
    forcePlaceholderSize: true,
    zIndex: 999999
  })

  // bootstrap WYSIHTML5 - text editor
  $('.textarea').summernote({
    height: 300
  });

  $('.daterange').daterangepicker({
    ranges: {
      'Today': [moment(), moment()],
      'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
      'Last 7 Days': [moment().subtract(6, 'days'), moment()],
      'Last 30 Days': [moment().subtract(29, 'days'), moment()],
      'This Month': [moment().startOf('month'), moment().endOf('month')],
      'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
    },
    startDate: moment().subtract(29, 'days'),
    endDate: moment()
  }, function (start, end) {
    startDate = start.format("YYYY-MM-DD HH:mm:ss");
    endDate = end.format("YYYY-MM-DD HH:mm:ss");
    search(categoryId, startDate, endDate, keyword);
  })

  /* jQueryKnob */
  $('.knob').knob()

  // The Calender
  $('#calendar').datetimepicker({
    format: 'L',
    inline: true
  })

  // SLIMSCROLL FOR CHAT WIDGET
  $('#chat-box').overlayScrollbars({
    height: '250px'
  })



})