// Простая микро-анимация: подсветка карточки по клику
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll("[data-card]");

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      card.classList.add("card--active");
      setTimeout(() => card.classList.remove("card--active"), 220);
    });
  });
});
