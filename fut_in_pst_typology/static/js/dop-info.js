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

function sortTable(button, columnIndex) {
    let table = document.getElementsByClassName('home')[0];
    let ascending = button.textContent!='↓' ? true : false;

    [...document.getElementsByClassName('button-sort-table')].forEach(function(btn, i){
        btn.textContent = "↕";
    })
    button.textContent = ascending ? '↓' : '↑';

    let rows = Array.from(table.rows).slice(1); // Exclude the header row

    rows.sort((rowA, rowB) => {
        let a = rowA.cells[columnIndex].textContent.trim();
        let b = rowB.cells[columnIndex].textContent.trim();

        if (ascending) {
            return a.localeCompare(b);
        } else {
            return b.localeCompare(a);
        }
    });
    
    // Append sorted rows back to the table
    for (let row of rows) {
        table.tBodies[0].appendChild(row);
    }
}