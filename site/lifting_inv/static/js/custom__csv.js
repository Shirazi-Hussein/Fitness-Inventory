
$(document).ready(function(){
	  console.log('Script running')
	var data;
	$.ajax({
	type : "GET",
	  url: "../static/js/combined_csv.csv",
	  dataType: "text",       
	  success: function(response)  
	  {
		var items = $.csv.toObjects(response);
		var data = JSON.parse(JSON.stringify(items));
		var total_html = "";
		console.log(data);

	    $.each( items , function(i, item) {
		   if (data[i].stock == "In stock" || data[i].stock == "In Stock" ) {
		   		total_html += '<div class="col-md-4 col-xs-6">'+
					            '<div class="product">'+
					                '<a href="'+ data[i].url +'" target="_blank">'+
						                '<div class="product-img">'+
						                    '<img src="'+ data[i].img_url +'" alt="'+ data[i].p_title  +'">'+
						                '</div>'+
					                '</a>'+
					                '<div class="product-body">'+
					                    '<p class="product-category">'+ data[i].company +'</p>'+
					                    '<h3 class="product-name"><a target="_blank" href="'+ data[i].url +'">'+ data[i].p_title +'</a></h3>'+
					                    '<h4 class="product-price">'+ data[i].price +'</h4>'+
					                '</div>'+
					            '</div>'+
					        '</div>';
		   }
			
		});
  		$('.load_csv').append(total_html);

	  } ,
	  fail : function(console){
		  console.log('Erro')
	  }
	});

  });