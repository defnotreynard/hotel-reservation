  function zoomImage(src) {
    const modal = document.getElementById("zoomModal");
    const image = document.getElementById("zoomedImg");
    image.src = src;
    modal.classList.remove("hidden");
    modal.classList.add("flex");
  }

  function closeZoom() {
    const modal = document.getElementById("zoomModal");
    modal.classList.remove("flex");
    modal.classList.add("hidden");
  }

  // Close when clicking on background (but not image)
  document.getElementById("zoomModal").addEventListener("click", function (e) {
    if (e.target.id === "zoomModal") closeZoom();
  });