[...document.getElementsByClassName('boldButton')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('bold', false, null);});});

[...document.getElementsByClassName('orderedListButton')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('insertOrderedList', false, null);});});

[...document.getElementsByClassName('unorderedListButton')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('insertUnorderedList', false, null);});});

[...document.getElementsByClassName('header2Button')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('formatBlock', false, 'h2');});});

[...document.getElementsByClassName('header3Button')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('formatBlock', false, 'h3');});});
    
[...document.getElementsByClassName('header4Button')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('formatBlock', false, 'h4');});});
    
[...document.getElementsByClassName('divButton')].forEach(element => {
    element.addEventListener('click', function() {
    document.execCommand('formatBlock', false, 'div');});});



function postTextFromEditor(current_editor) {
    textarea = current_editor.parentNode.lastElementChild.lastElementChild;

    textarea.innerHTML = current_editor.innerHTML;
    
    let xhr = new XMLHttpRequest();
    xhr.open('POST', document.URL, true);
    
    // xhr.onload = function() {
    //     let comment_form = current_comment.parentNode.parentNode;
    //     if (xhr.status === 200) {
    //         animate(current_comment, 'comment-animation')
    //         if (current_comment.value == "")
    //             document.getElementById('all_comments').removeChild(comment_form);
    //     }
    // }
    xhr.send(new FormData(textarea.parentNode));
}