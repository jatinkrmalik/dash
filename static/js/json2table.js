
    function json2table(myjson) {
       
        // for header
        var col = [];
        for (var i = 0; i < myjson.length; i++) {
            for (var key in myjson[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }

        // create dynamic table
        var table = document.createElement("table");

        // creating table raw

        var tr = table.insertRow(-1);                   

        for (var i = 0; i < col.length; i++) {
            // table header
            var th = document.createElement("th");      
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // adding json data into table raw
        for (var i = 0; i < myjson.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = myjson[i][col[j]];
            }
        }

        // container which hold the table
        var divContainer = document.getElementById("showData");
        divContainer.innerHTML = "";

        //appending table into container
        divContainer.appendChild(table);

    }