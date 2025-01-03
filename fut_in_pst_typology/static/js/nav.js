function toggleLeftNav() {
    const leftnav = document.getElementById('leftnav');
    const overlay = document.getElementById('overlay');
    leftnav.classList.toggle('active');
    overlay.classList.toggle('active');
}