const slider = document.querySelector('.slider');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

let scrollAmount = 0;
const scrollMax = slider.scrollWidth - slider.clientWidth;

prevBtn.addEventListener('click', () => {
  if (scrollAmount !== 0) {
    scrollAmount -= 320;
    slider.scrollTo({
      top: 0,
      left: scrollAmount,
      behavior: 'smooth'
    });
  }
});

nextBtn.addEventListener('click', () => {
  if (scrollAmount < scrollMax) {
    scrollAmount += 320;
    slider.scrollTo({
      top: 0,
      left: scrollAmount,
      behavior: 'smooth'
    });
  }
});
