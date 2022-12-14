const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const images = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg', 'pic5.jpg']
/* Declaring the alternative text for each image file */

/* Looping through images */
for (image of images) {
    const newImage = document.createElement('img');
    newImage.setAttribute('src', './images/' + image);
    newImage.setAttribute('alt', image);
    thumbBar.appendChild(newImage);
}
thumbBar.addEventListener('click', (e) => {
    src = e.target.src;
    displayedImage.src = src;
})
/* Wiring up the Darken/Lighten button */
btn.addEventListener('click', (e) => {
    let btn = e.target;
    if (btn.getAttribute('class') === 'dark') {
        btn.setAttribute('class', 'light');
        btn.textContent = 'Lighten';
        overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
    } else {
        btn.setAttribute('class', 'dark');
        btn.textContent = 'Darken';
        overlay.style.backgroundColor = 'rgba(0,0,0,0)';
    }
})