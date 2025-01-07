function turnOnImageShow(img) {
    modalContainer = img.nextElementSibling
    modalContainer.classList.toggle('active');
}

function turnOffImageShow(modalContainer) {
    modalContainer.classList.toggle('active');
}

function deleteImage(button) {
    data = new FormData(button.nextElementSibling);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);

    xhr.onload = function() {
        if (xhr.status === 200) {
            document.getElementById("image_"+data.get("delete_image")).remove();
        }
    }
    xhr.send(data);
}