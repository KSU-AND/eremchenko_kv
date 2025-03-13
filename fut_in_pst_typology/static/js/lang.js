
function main() {
    registerTextareaInputListener();
    registerAddImageFormListener();
    registerKeysListener();    
}

function postMainComment(text_area) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            animate(text_area, 'comment-animation');
        }
    }
    xhr.send(new FormData(text_area.parentNode.parentNode));
};

function postIntableSelect(select) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            animate(select, 'select-in-table-animation');
        }
    }
    xhr.send(new FormData(select.parentNode.parentNode));
};

function postAddComment(button) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            let help_div = document.createElement('div');
            help_div.innerHTML = xhr.response;
            comment = help_div.firstChild;
            document.getElementById('all_comments').appendChild(comment);
            addTextareaInputListener(comment.querySelector(".commentForm .comment"));
            comment.querySelector(".commentForm .comment").focus();
        }
    }
    xhr.send(new FormData(button.parentNode.parentNode));
};

function postComment(current_comment) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    
    xhr.onload = function() {
        let comment_form = current_comment.parentNode.parentNode;
        if (xhr.status === 200) {
            animate(current_comment, 'comment-animation');
            if (current_comment.value == "")
                document.getElementById('all_comments').removeChild(comment_form);
        }
    }
    xhr.send(new FormData(current_comment.parentNode));
}

function postAddImage(button) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            button.parentNode.parentNode.parentNode.innerHTML = xhr.response;
            registerTextareaInputListener();
        }
    }
    xhr.send(new FormData(button.parentNode));
};


function addTextareaInputListener(textarea){
    textarea.style.overflowY = "hidden";
    textarea.addEventListener("input", function() {
        this.style.height = "auto";
        this.style.height = this.scrollHeight + "px";
        this.innerHTML = this.value;
    });
}
function registerTextareaInputListener() {
    document.querySelectorAll("textarea").forEach(function(textarea) {
        textarea.style.height = textarea.scrollHeight + "px";
        addTextareaInputListener(textarea);
    });
};

function addAddImageFormListener(fileInput){
    fileInput.addEventListener("change", function() {
        this.parentNode.lastElementChild.innerHTML = this.files[0].name;
    });
}
function registerAddImageFormListener() {
    document.querySelectorAll("input[type=file]").forEach(function(fileInput) {
        addAddImageFormListener(fileInput);
    });
};

function registerKeysListener() {
    document.body.addEventListener('keydown', function(e) {
        if (e.key == "Escape") {
            e.target.blur();
        }
        else if (e.ctrlKey && e.key == "Enter") {
            e.target.blur();
        }
        else if (e.shiftKey && e.key == "Enter") {
            e.target.blur();
            setTimeout(function() {
                document.getElementsByClassName('add-comment-button')[0].click();
            }, 100)
        }
      });
}


function animate(object, className){
    object.classList.remove(className);
    object.offsetWidth
    object.classList.add(className);
}

function toggleImageZoom(button) {
    [...document.getElementsByClassName('img-cmnt')].forEach(function(img) {
        img.classList.toggle('img-zoom');
    });
    button.textContent = button.textContent=='zoom ✅'? 'zoom ❎' : 'zoom ✅';
    button.classList.toggle('zoom');
}

function toggleTheoryBlocksOverlay(){
    theoryBlocksBack.classList.toggle("active");
    theoryBlocksDiv.classList.toggle("active");
}

function postAddSource(button) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            let help_div = document.createElement('div');
            help_div.innerHTML = xhr.response;
            source = help_div.firstElementChild;
            document.getElementById('sources').appendChild(source);
            source.querySelector(".source").focus();
        }
    }
    xhr.send(new FormData(button.parentNode.parentNode));
};
function postSource(current_source) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    
    xhr.onload = function() {
        let comment_form = current_source.parentNode;
        if (xhr.status === 200) {   
            animate(current_source, 'comment-animation');
            if (current_source.value == "")
                document.getElementById('sources').removeChild(comment_form);
        }
    }
    xhr.send(new FormData(current_source.parentNode));
}

function postTheoryBlocks(button) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);

    xhr.onload = function() {
        if (xhr.status === 200) {
            toggleTheoryBlocksOverlay();
            all_theory_blocks.innerHTML = xhr.response;
        }
    }
    xhr.send(new FormData(theoryBlocksForm));
};