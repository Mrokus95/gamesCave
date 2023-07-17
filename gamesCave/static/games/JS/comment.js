// commentSection 
const commentButton = document.getElementById("comment-button");
const commentSection = document.getElementById("comment-section");

commentButton.addEventListener("click", () => {
  commentSection.classList.toggle("comment-section-hide");
});