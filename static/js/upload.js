$(function () {

  $(".js-upload-images").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,
    start: function (e) {
      $(".progress-bar").css({"width": "0%"});
      $("#modal-progress").removeClass('fade').modal("show");
    },
    stop: function (e) {
      $("#modal-progress").on('hide.bs.modal', function (e) {
        $(document.body).removeClass('modal-open');
        $('.modal-backdrop').remove();
      });
      $("#modal-progress").addClass('fade').modal("hide");
    },
    progressall: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },
    done: function (e, data) {
      if (data.result.is_valid) {
        let data_url = $("#fileupload").attr('data-url');
        let data_csrf = $("#fileupload").attr('data-csrf');

        $("#gallery").prepend(
          "<div class='row border'>" +
            "<div class='col-10'>" +
              "<a href='" + data.result.url + "'>" +
              "<img src='" + data.result.tmb_url + "'/>" +
              "<br>" +
              "<span>" + data.result.name + ", " +
                getWidthHeight(data) + ", " +
                getSize(data) + ", " +
                "uploaded: now" +
              "</span>" +
              "</a>" +
            "</div>" +
            "<div class='col-2'>" +
              "<button type='button' class='close' aria-label='Delete' " +
                "data-url='" + data_url +
                "' data-csrf='" + data_csrf +
                "' data-pk='" + data.result.pk +
               "'>" +
              "<span aria-hidden='true'>&times;</span>" +
              "</button>" +
            "</div>" +
          "</div>"
        );

        $(".close").click(deleteImage);
      }
    }
  });

  $(".close").click(deleteImage);

});

function deleteImage() {
  $.ajax({
    headers: { "X-CSRFToken": $(this).attr('data-csrf') },
    url: $(this).attr('data-url'),
    type: 'DELETE',
    contentType:'application/json',
    success: () => {$(this.parentElement.parentElement).remove();},
    data: {'pk': $(this).attr('data-pk')}
  });
}

function getWidthHeight(data) {
  return data.result.width + "x" + data.result.height;
}

function getSize(data) {
  return "size: " + data.result.size;
}