function toggleInfoInRow(infoRow) {
    [...infoRow.cells].forEach(function(cell, index) {
        if (cell.lastElementChild != null && cell.lastElementChild.className==="dop-info"){
            infoRow.cells[index].lastElementChild.style.display = 
            cell.lastElementChild.style.display === 'block' ? 'none' : 'block';
        }
    });
}

function toggleInfoInH1(infoH1) {
    if (infoH1.lastElementChild != null && infoH1.lastElementChild.className==="dop-info"){
        infoH1.lastElementChild.style.display = 
        infoH1.lastElementChild.style.display === 'block' ? 'none' : 'block';
    }
}

function sortTable(button) {
    let columnIndex = 1;
    table = button.parentElement.closest('table');
    
    let ascending = button.classList.contains('fa-arrow-down-a-z') ? false : true;

    [...document.getElementsByClassName('button-sort-table')].forEach(function(btn, i){
        let newClass = 'fa-arrows-up-down';
        if (btn == button){
            columnIndex = i+1;
            newClass = ascending ? 'fa-arrow-down-a-z' : 'fa-arrow-down-z-a';
        }
        btn.classList.remove('fa-arrow-down-z-a');
        btn.classList.remove('fa-arrow-down-a-z');
        btn.classList.remove('fa-arrows-up-down');
        btn.classList.add(newClass);
    });

    let rows = Array.from(table.rows).slice(1); // Exclude the header row

    rows.sort((rowA, rowB) => {
        let a = rowA.cells[columnIndex].textContent.trim();
        let b = rowB.cells[columnIndex].textContent.trim();

        if (ascending) {
            return a=='' || a.localeCompare(b);
        } else {
            return b=='' || b.localeCompare(a);
        }
    });
    
    // Append sorted rows back to the table
    for (let row of rows) {
        table.tBodies[0].appendChild(row);
    }
}