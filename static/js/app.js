document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.querySelector(".hamburger");
  const nav = document.querySelector(".nav");
  const navLinks = document.querySelectorAll(".nav--link");

  // Toggle navigation menu when hamburger is clicked
  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("close");
    nav.classList.toggle("open");

    // Fix menu to stay in the nav area
    if (nav.classList.contains("open")) {
      nav.style.position = "fixed";
      nav.style.top = "60px"; // Adjust this value based on your header height
    } else {
      setTimeout(() => {
        nav.style.position = "";
        nav.style.top = "";
      }, 300); // Match this to your transition time
    }
  });

  // Close menu when a link is clicked
  navLinks.forEach(link => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("close");
      nav.classList.remove("open");

      // Reset positioning after transition
      setTimeout(() => {
        nav.style.position = "";
        nav.style.top = "";
      }, 300);
    });
  });
});