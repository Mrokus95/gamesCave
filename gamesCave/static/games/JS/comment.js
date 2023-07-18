// commentSection 
const commentButton = document.getElementById("comment-button");
const commentSection = document.getElementById("comment-section");

commentButton.addEventListener("click", () => {
  commentSection.classList.toggle("comment-section-hide");
});

$(document).ready(function() {
  const commentSection = $('#comment-section');

  // Obsługa kliknięcia linków paginacji
  $(document).on('click', '.pagination a', function(event) {
    event.preventDefault();
    const url = $(this).attr('href');

    // Ładowanie nowej strony paginacji przy użyciu AJAX
    $.ajax({
      url: url,
      type: 'GET',
      success: function(data) {
        const newComments = $(data).find('#comment-section').html();
        commentSection.html(newComments);

        // Przewinięcie strony do początku sekcji komentarzy
        $('html, body').animate({
          scrollTop: commentSection.offset().top
        }, 500);
      }
    });
  });
});