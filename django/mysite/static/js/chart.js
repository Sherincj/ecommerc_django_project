
    function getproddata(){
     var xhttp = new XMLHttpRequest()
     xhttp.open('GET','/home/produ/'+document.getElementById('keyword').value,true)
     xhttp.onreadystatechange = function(){
         if(this.readyState == 4 && this.status == 200){
             var data = JSON.parse(this.responseText);
             console.log(data);
             str = '<table>'
                for(x of data.produ){
                    str = str + '<tr>'
                    str = str + '<td>' + (x.name) + '<td>'
                    
                }
                str = str + '</table>'
                document.getElementById('datass').innerHTML = str
         }
     };
     xhttp.send();
    
    } 
 

    function getallpro(){
        var xhttp = new XMLHttpRequest()
        xhttp.open('GET','/home/alldata')
        xhttp.onreadystatechange = function(){
            if(this.readyState == 4 && this.status == 200){
                var datax = JSON.parse(this.responseText);
                drawdata(datax)
            }
        };
        xhttp.send();
    }


 
    function drawdata(datax){

        const ctx = document.getElementById('myChart');

            new Chart(ctx, {
                type: 'bar',
                data: {
                labels: getname(datax),
                datasets: [{
                    label: '# of Votes',
                    data: getprice(datax),
                    borderWidth: 1
                }]
                },
                options: {
                scales: {
                    y: {
                    beginAtZero: true
                    }
                }
                }
            });
            }
function getname(datax){
    let labels=[]
    for(x of datax.new){
        labels.push(x.name)

    }
    return labels
}
function getprice(datax){
    let labels=[]
    for(x of datax.new){
        labels.push(x.price)

    }
    return labels
}
 
