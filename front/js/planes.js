$(document).ready(function(){
    let planes = $('#div-movil')
    let html = '<div class="card col-12">'+
    '<img src="{image}" class="card-img-top" alt="...">'+
    '<div class="card-body">'+
      '<h5 class="card-title">{name}</h5>'+
      '<p class="card-text">{desc}</p>'+
      '<p class="card-text">${price}</p>'+
    '</div>'+
  '</div>'
    axios.get('http://localhost:8000/planes/?format=json')
    .then((resp) => {
        resp.data.map((plan) => {
            planes.append(html
                .replace('{image}', plan.image)
                .replace('{name}', plan.name)
                .replace('{desc}', plan.description)
                .replace('{price}', plan.price)
                );
        })

    }).catch((err) => {
        console.log(err)
        alert('Error al obtener planes')
    })
})