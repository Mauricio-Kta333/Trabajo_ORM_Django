google.charts.load('current', {'packages':['corechart']});


$(function() {
    google.charts.setOnLoadCallback(graficar);
    let option = {
        headers: {
            'X-CSRF-TOKEN':getCookie('csrf_token')
        }
    };
    fetch (url)
        .then(response => response.json())
        .then(data => console.log(data))
    
    // $.ajaxSetup({
    //     headers: {
    //         'X-CSRF-TOKEN':getCookie('csrf_token')
    //     }
    // })

})

function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0,name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
            
        }
    }
    return cookieValue;
}

function graficar() {

    $.ajax({
        url: '/grafica1Google/',
        dataType: 'json',
        type: 'post',
        cache: false,
        async: false,
        success: function (data) {
            console.log(data)
            var data = google.visualization.arrayToDataTable(data.datos)
            var options = {
                title: 'Ventas Por Producto',
                legend: None,
            
            };
            var grafica = document.getElementById('graficaGo')
            var chart = new google.visualization.ColumnChart(grafica);

            chart.draw(data, options)
        }
        
    })




    // var data = google.visualization.arrayToDataTable([
    //     ['Task', 'Hours per Day'],
    //     ['Work',     1],
    //     ['Eat',      5],
    //     ['Commute',  6],
    //     ['Watch TV', 2],
    //     ['Sleep',    10]
    //   ]);

    //   var options = {
    //     title: 'My Daily Activities'
    //   };

    //   var chart = new google.visualization.PieChart(grafica);

    //   chart.draw(data, options);
}